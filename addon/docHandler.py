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
                ui.message("Abriendo el manual de usuario en el navegador...")
            return True
        except Exception:
            try:
                uri = f"file:///{os.path.abspath(doc_path).replace(os.sep, '/')}"
                webbrowser.open(uri)
                if ui:
                    ui.message("Abriendo el manual de usuario en el navegador...")
                return True
            except Exception as e:
                if ui:
                    ui.message(f"No fue posible abrir la documentación: {e}")
                return False
    else:
        if ui:
            ui.message("El archivo del manual de usuario no fue encontrado.")
        return False
