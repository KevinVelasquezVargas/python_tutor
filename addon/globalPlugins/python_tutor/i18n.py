# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/i18n.py
# Propósito: Sistema central de internacionalización basado en gettext.
#            Las cadenas de la interfaz viven en locale/<idioma>/LC_MESSAGES/
#            nvda.po (msgids en español, idioma base) y se compilan a .mo
#            con scons. Los catálogos de lecciones
#            (locale/<idioma>/lessons.json) comparten la misma detección
#            de idioma y conmutación en caliente.
# Autor: Kevin Andrés Velasquez Vargas
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import os
import gettext as _gettext

try:
    import languageHandler
except ImportError:
    languageHandler = None

_IDIOMA_ACTUAL = "es"
_TRADUCCIONES = {}
_TRADUCCION_BASE = _gettext.NullTranslations()


def _ruta_locale():
    """Devuelve la ruta del directorio addon/locale del complemento."""
    # addon/globalPlugins/python_tutor -> addon/locale
    return os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "locale")
    )


def _obtener_traduccion(lang):
    """Devuelve el objeto gettext del idioma, con caché y respaldo al msgid.

    El idioma base ('es') devuelve el propio msgid, de modo que no
    requiere catálogo compilado.
    """
    if lang == "es":
        return _TRADUCCION_BASE
    if lang not in _TRADUCCIONES:
        try:
            _TRADUCCIONES[lang] = _gettext.translation(
                "nvda", localedir=_ruta_locale(), languages=[lang]
            )
        except (OSError, IOError):
            _TRADUCCIONES[lang] = _gettext.NullTranslations()
    return _TRADUCCIONES[lang]


def _normalizar_idioma_soportado(lang):
    """Mapea un código bruto ('pt_PT', 'en-US') al idioma soportado más cercano.

    Prioriza los catálogos de lecciones (lessons_loader.normalizar_idioma)
    y aplica como respaldo cualquier idioma con carpeta en locale/.
    Devuelve None si no hay idioma adecuado.
    """
    if not lang:
        return None
    normalizar = None
    try:
        from .lessons_loader import normalizar_idioma as normalizar
    except ImportError:
        try:
            from lessons_loader import normalizar_idioma as normalizar
        except ImportError:
            normalizar = None
    if normalizar is not None:
        try:
            codigo = normalizar(lang)
            if codigo:
                return codigo
        except Exception:
            pass
    prefijo = str(lang).strip().lower().replace("-", "_").split("_")[0]
    if os.path.isdir(os.path.join(_ruta_locale(), prefijo)):
        return prefijo
    return None


def detectar_idioma_preferido():
    """Detecta el idioma activo basándose en la configuración del usuario o en NVDA."""
    global _IDIOMA_ACTUAL

    try:
        from .progress import ProgressManager
        saved = ProgressManager.get_setting("language", "auto")
        if saved and saved != "auto":
            codigo = _normalizar_idioma_soportado(saved)
            if codigo:
                _IDIOMA_ACTUAL = codigo
                return codigo
    except Exception:
        pass

    if languageHandler:
        try:
            codigo = _normalizar_idioma_soportado(languageHandler.getLanguage())
            if codigo:
                _IDIOMA_ACTUAL = codigo
                return codigo
        except Exception:
            pass

    import locale
    try:
        codigo = _normalizar_idioma_soportado(locale.getlocale()[0])
        if codigo:
            _IDIOMA_ACTUAL = codigo
            return codigo
    except Exception:
        pass

    _IDIOMA_ACTUAL = "es"
    return "es"


def obtener_idioma_actual():
    """Devuelve el código del idioma activo (p. ej. 'es', 'en', 'pt')."""
    return _IDIOMA_ACTUAL


def _t(texto, **kwargs):
    """Traduce un msgid (español base) al idioma activo mediante gettext.

    Si se pasan argumentos con nombre, se aplican como reemplazo
    ``str.format`` sobre el resultado ya traducido.
    """
    texto = _obtener_traduccion(_IDIOMA_ACTUAL).gettext(texto)
    if kwargs:
        try:
            return texto.format(**kwargs)
        except Exception:
            return texto
    return texto


# Alias para compatibilidad con llamadas gettext estándar
_ = _t


def establecer_idioma(lang_code):
    """Establece manualmente el idioma del complemento (código de catálogo disponible)."""
    global _IDIOMA_ACTUAL
    _IDIOMA_ACTUAL = _normalizar_idioma_soportado(lang_code) or "es"

    try:
        import sys
        for mod_name, mod in list(sys.modules.items()):
            if mod_name.endswith('.i18n') or mod_name == 'i18n':
                if hasattr(mod, '_IDIOMA_ACTUAL'):
                    mod._IDIOMA_ACTUAL = _IDIOMA_ACTUAL
    except Exception:
        pass

    try:
        from .progress import ProgressManager
        ProgressManager.set_setting("language", _IDIOMA_ACTUAL)
    except Exception:
        pass

    try:
        import sys
        titulo = _t("Aprendizaje de Python con NVDA")
        for mod_name in ('globalPlugins.python_tutor', 'addon.globalPlugins.python_tutor', 'python_tutor'):
            mod = sys.modules.get(mod_name)
            if mod:
                panel = getattr(mod, 'PythonTutorSettingsPanel', None)
                if panel:
                    panel.title = titulo
                plugin = getattr(mod, 'GlobalPlugin', None)
                if plugin:
                    plugin.scriptCategory = titulo
    except Exception:
        pass


# Inicializar detección automática al cargar
detectar_idioma_preferido()
