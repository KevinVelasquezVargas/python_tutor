# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/braille_helper.py
# Propósito: Optimizaciones y salida adaptada para líneas Braille en NVDA.
# Autor: Kevin Andrés Velasquez Vargas
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

try:
    import braille
except ImportError:
    braille = None


def anunciar_braille(texto):
    """Envía un mensaje directo y sin retardo a la línea Braille conectada."""
    if braille and hasattr(braille, "handler") and hasattr(braille.handler, "message"):
        try:
            braille.handler.message(texto)
            return True
        except Exception:
            pass
    return False


def formatear_linea_para_braille(linea):
    """
    Formatea una línea de código para lectura limpia en pantallas Braille.
    Utiliza texto estándar sin caracteres ni símbolos extraños que confundan la voz o el tacto.
    """
    espacios = len(linea) - len(linea.lstrip(" "))
    nivel = espacios // 4

    if nivel == 0:
        return linea.strip()

    from .i18n import obtener_idioma_actual
    lbl = "Level" if obtener_idioma_actual() == "en" else "Nivel"
    return f"[{lbl} {nivel}] {linea.strip()}"
