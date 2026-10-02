# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: docHandler.py
# Propósito: Localización y apertura accesible de la documentación HTML del complemento.
# Plantilla: Adaptado al estándar canónico oficial AddonTemplate de NVDA.
# Autor: Kevin Andrés Velasquez Vargas
# Internacionalización (i18n): MisterK-Dev (desarrollado con Google Antigravity 2.0)
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import os
import webbrowser

try:
    import addonHandler
    addonHandler.initTranslation()
except Exception:
    pass

try:
    _
except NameError:
    import gettext
    _base = os.path.dirname(os.path.abspath(__file__))
    _loc = os.path.join(_base, "locale")
    if not os.path.isdir(_loc):
        _loc = os.path.join(_base, "addon", "locale")
    try:
        _t = gettext.translation("nvda", localedir=_loc, languages=["es"])
        _ = _t.gettext
    except Exception:
        def _(msg):
            return msg

try:
    import languageHandler
except ImportError:
    languageHandler = None

try:
    import ui
except ImportError:
    ui = None



def getDocFilePath(fileName="readme.html"):
    """
    Retorna la ruta absoluta del archivo de documentación HTML localizado.
    Sigue las directrices de AddonTemplate buscando en doc/{idioma}/ y fallbacks.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Obtener código de idioma de NVDA
    lang = "es"
    if languageHandler and hasattr(languageHandler, 'getLanguage'):
        try:
            lang = languageHandler.getLanguage() or "es"
        except Exception:
            lang = "es"

    candidatos_idioma = [lang]
    if "_" in lang:
        candidatos_idioma.append(lang.split("_")[0])
    if "es" not in candidatos_idioma:
        candidatos_idioma.append("es")
    if "en" not in candidatos_idioma:
        candidatos_idioma.append("en")

    # 1. Probar en doc/<lang>/<fileName>
    for l in candidatos_idioma:
        p = os.path.join(base_dir, "doc", l, fileName)
        if os.path.isfile(p):
            return p

    # 2. Probar en doc/<fileName>
    p = os.path.join(base_dir, "doc", fileName)
    if os.path.isfile(p):
        return p

    # 3. Probar en raíz <base_dir>/<fileName>
    p = os.path.join(base_dir, fileName)
    if os.path.isfile(p):
        return p

    # 4. Probar variantes .html o .htm
    for l in candidatos_idioma:
        for f in ["readme.html", "README.html", "readme.htm"]:
            p = os.path.join(base_dir, "doc", l, f)
            if os.path.isfile(p):
                return p

    return None


def openDoc(fileName="readme.html"):
    """
    Abre la documentación HTML en el navegador web predeterminado del sistema.
    """
    doc_path = getDocFilePath(fileName)
    if doc_path and os.path.isfile(doc_path):
        try:
            os.startfile(doc_path)
            if ui:
                ui.message(_("Opening user guide in browser..."))
            return True
        except Exception:
            try:
                uri = f"file:///{os.path.abspath(doc_path).replace(os.sep, '/')}"
                webbrowser.open(uri)
                if ui:
                    ui.message(_("Opening user guide in browser..."))
                return True
            except Exception as e:
                if ui:
                    # Translators: Error message when documentation cannot be opened. {error} is the error details.
                    ui.message(_("Could not open documentation: {error}").format(error=e))
                return False
    else:
        if ui:
            ui.message(_("User guide file was not found."))
        return False
