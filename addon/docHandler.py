# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: docHandler.py
# Propósito: Localización y apertura accesible de la documentación HTML del complemento.
# Plantilla: Adaptado al estándar canónico oficial AddonTemplate de NVDA.
# Autor: Kevin Andrés Velasquez Vargas
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import os
import webbrowser

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

    # Obtener código de idioma activo
    lang = "es"
    try:
        from globalPlugins.python_tutor.i18n import obtener_idioma_actual
        lang = obtener_idioma_actual() or "es"
    except Exception:
        try:
            from .globalPlugins.python_tutor.i18n import obtener_idioma_actual
            lang = obtener_idioma_actual() or "es"
        except Exception:
            if languageHandler and hasattr(languageHandler, 'getLanguage'):
                try:
                    lang = languageHandler.getLanguage() or "es"
                except Exception:
                    lang = "es"

    candidatos_idioma = [lang]
    if "_" in lang:
        candidatos_idioma.append(lang.split("_")[0])
    if lang.startswith("en"):
        if "en" not in candidatos_idioma:
            candidatos_idioma.append("en")
        if "es" not in candidatos_idioma:
            candidatos_idioma.append("es")
    else:
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

    # 5. Probar archivos .md (fallback en entornos de desarrollo y pruebas)
    for l in candidatos_idioma:
        p = os.path.join(base_dir, "doc", l, "readme.md")
        if os.path.isfile(p):
            return p
    root_md = os.path.join(os.path.dirname(base_dir), "README.md")
    if os.path.isfile(root_md):
        return root_md

    return None


def openDoc(fileName="readme.html"):
    """
    Abre la documentación HTML en el navegador web predeterminado del sistema.
    """
    doc_path = getDocFilePath(fileName)
    is_en = False
    try:
        from globalPlugins.python_tutor.i18n import obtener_idioma_actual
        is_en = (obtener_idioma_actual() == "en")
    except Exception:
        pass

    msg_opening = "Opening documentation in web browser..." if is_en else "Abriendo documentación en el navegador web..."
    msg_not_found = "Documentation file not found." if is_en else "El archivo de documentación no fue encontrado."

    if doc_path and os.path.isfile(doc_path):
        try:
            os.startfile(doc_path)
            if ui:
                ui.message(msg_opening)
            return True
        except Exception:
            try:
                uri = f"file:///{os.path.abspath(doc_path).replace(os.sep, '/')}"
                webbrowser.open(uri)
                if ui:
                    ui.message(msg_opening)
                return True
            except Exception as e:
                if ui:
                    ui.message(f"Error: {e}")
                return False
    else:
        if ui:
            ui.message(msg_not_found)
        return False
