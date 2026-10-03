# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/i18n.py
# Propósito: Sistema central de internacionalización bilingüe (Español / Inglés).
# Autor: Kevin Andrés Velasquez Vargas
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import os
import json

try:
    import languageHandler
except ImportError:
    languageHandler = None

_IDIOMA_ACTUAL = "es"

DICCIONARIO = {
    "es": {
        "app_title": "Aprendizaje de Python con NVDA",
        "app_subtitle": "Entorno formativo y editor accesible de Python",
        "menu_file": "&Archivo",
        "menu_edit": "&Edición",
        "menu_tools": "&Herramientas",
        "menu_settings": "&Configuración",
        "menu_glossary": "&Glosario",
        "menu_help": "&Ayuda",
        "btn_run": "Ejecutar (F5)",
        "btn_explain": "Explicar línea (F1)",
        "btn_ask_ai": "Consultar a la IA (Ctrl+Shift+I)",
        "mode_learning": "Modo Aprendizaje",
        "mode_editor": "Modo Solo Editor",
        "switched_to_editor": "Modo Solo Editor activado.",
        "switched_to_learning": "Modo Aprendizaje activado.",
        "syntax_ok": "Sintaxis verificada correctamente.",
        "syntax_error": "Error de sintaxis detectado.",
        "new_script": "Nuevo script iniciado.",
        "file_opened": "Archivo cargado correctamente: {name}",
        "file_saved": "Guardado correctamente en: {name}",
        "shortcuts_title": "Guía de Atajos de Teclado",
        "about_title": "Acerca de Aprendizaje de Python con NVDA",
        "ai_assistant_title": "Asistente de Inteligencia Artificial",
        "ai_config_title": "Configuración del Asistente de IA...",
        "ai_consult_menu": "Consultar al Asistente de IA...\tCtrl+Shift+I",
        "pip_manager_title": "Gestor accesible de paquetes (pip)...",
        "project_manager_title": "Explorador de proyectos multi-archivo...\tCtrl+Shift+E",
        "language_menu": "Cambiar idioma (Español / English)...",
        "settings_lang_label": "Idioma de la interfaz y lecciones:",
        "settings_lang_auto": "Automático (según NVDA)",
        "settings_lang_es": "Español",
        "settings_lang_en": "English",
        "settings_ai_f1_label": "Habilitar Asistente de IA para F1 (opcional, requiere clave API)",
        "settings_ai_key_label": "Clave API de Google Gemini (opcional):",
        "settings_ai_note": "Por defecto, la tecla F1 funciona de forma local y privada sin conexión.",
        "settings_open_pip": "Abrir Gestor de Paquetes pip...",
        "settings_open_projects": "Abrir Explorador de Proyectos...",
        "line_empty": "Línea vacía.",
        "comment_line": "Comentario: {comment}. Las computadoras ignoran esta línea, sirve como nota explicativa.",
        "print_empty": "Instrucción print: Imprime una línea en blanco en la salida de consola.",
        "print_text": "Instrucción print: Muestra en pantalla y lee con voz el mensaje: '{text}'.",
        "if_cond": "Condicional 'si' (if): Comprueba si se cumple '{cond}'. Si es verdadera, ejecutará las instrucciones indentadas siguientes.",
        "elif_cond": "Condición alternativa (elif): Si la condición anterior fue falsa pero '{cond}' es verdadera, ejecutará este bloque.",
        "else_cond": "Bloque alternativo final (else): Se ejecuta si ninguna de las condiciones anteriores se cumplió.",
        "for_loop": "Bucle for: Itera y repite el bloque de código recorriendo '{target}'.",
        "while_loop": "Bucle while: Repite las instrucciones indentadas mientras la condición '{cond}' siga siendo verdadera.",
        "def_func": "Definición de función (def): Declara una función llamada '{name}' con los parámetros '{params}'.",
        "class_def": "Definición de clase (class): Crea una plantilla de objetos llamada '{name}'.",
        "return_stmt": "Sentencia return: Finaliza la función y devuelve el valor '{val}'.",
        "import_stmt": "Importación (import): Carga el módulo o librería '{mod}' para usar sus funciones.",
        "try_block": "Bloque de control try: Intenta ejecutar las instrucciones siguientes de forma segura.",
        "except_block": "Captura de error (except): Maneja la excepción '{exc}' si ocurrió un error en el bloque try."
    },
    "en": {
        "app_title": "Learning Python with NVDA",
        "app_subtitle": "Accessible Python educational environment and professional code editor",
        "menu_file": "&File",
        "menu_edit": "&Edit",
        "menu_tools": "&Tools",
        "menu_settings": "&Settings",
        "menu_glossary": "&Glossary",
        "menu_help": "&Help",
        "btn_run": "Run script (F5)",
        "btn_explain": "Explain line (F1)",
        "btn_ask_ai": "Ask AI Tutor (Ctrl+Shift+I)",
        "mode_learning": "Learning Mode",
        "mode_editor": "Standalone Editor Mode",
        "switched_to_editor": "Standalone Editor Mode activated.",
        "switched_to_learning": "Learning Mode activated.",
        "syntax_ok": "Syntax verified successfully.",
        "syntax_error": "Syntax error detected.",
        "new_script": "New script started.",
        "file_opened": "File opened successfully: {name}",
        "file_saved": "Saved successfully to: {name}",
        "shortcuts_title": "Keyboard Shortcuts Guide",
        "about_title": "About Learning Python with NVDA",
        "ai_assistant_title": "AI Assistant",
        "ai_config_title": "AI Assistant Settings...",
        "ai_consult_menu": "Ask AI Assistant...\tCtrl+Shift+I",
        "pip_manager_title": "Accessible Package Manager (pip)...",
        "project_manager_title": "Multi-file Project Explorer...\tCtrl+Shift+E",
        "language_menu": "Switch Language (English / Español)...",
        "settings_lang_label": "Interface and curriculum language:",
        "settings_lang_auto": "Automatic (follow NVDA)",
        "settings_lang_es": "Español (Spanish)",
        "settings_lang_en": "English",
        "settings_ai_f1_label": "Enable AI Assistant for F1 (optional, requires API Key)",
        "settings_ai_key_label": "Google Gemini API Key (optional):",
        "settings_ai_note": "By default, F1 provides 100% offline, private local explanations.",
        "settings_open_pip": "Open Package Manager (pip)...",
        "settings_open_projects": "Open Project Explorer...",
        "line_empty": "Empty line.",
        "comment_line": "Comment: {comment}. Computers ignore this line, it serves as an explanatory note.",
        "print_empty": "Print statement: Outputs a blank line to the console.",
        "print_text": "Print statement: Displays on screen and speaks aloud: '{text}'.",
        "if_cond": "'If' condition: Checks whether '{cond}' evaluates to true. If so, executes the indented block.",
        "elif_cond": "'Elif' condition: If previous checks were false and '{cond}' is true, executes this block.",
        "else_cond": "'Else' block: Executes when none of the preceding conditions were met.",
        "for_loop": "'For' loop: Iterates through elements in '{target}'.",
        "while_loop": "'While' loop: Repeats the indented instructions while '{cond}' remains true.",
        "def_func": "Function definition (def): Declares a reusable function named '{name}' with parameters '{params}'.",
        "class_def": "Class definition: Defines an object template named '{name}'.",
        "return_stmt": "'Return' statement: Exits the function and returns the value '{val}'.",
        "import_stmt": "'Import' statement: Loads module or library '{mod}' to utilize its features.",
        "try_block": "'Try' block: Attempts to execute the following code safely.",
        "except_block": "'Except' block: Catches and handles exception '{exc}' if an error occurred in try block."
    }
}


def detectar_idioma_preferido():
    """Detecta el idioma activo basándose en la configuración del usuario o en NVDA."""
    global _IDIOMA_ACTUAL

    try:
        from .progress import ProgressManager
        saved = ProgressManager.get_setting("language", "auto")
        if saved in ("es", "en"):
            _IDIOMA_ACTUAL = saved
            return saved
    except Exception:
        pass

    if languageHandler:
        try:
            lang = languageHandler.getLanguage()
            if lang and (lang.lower().startswith("en") or "english" in lang.lower()):
                _IDIOMA_ACTUAL = "en"
                return "en"
            elif lang and (lang.lower().startswith("es") or "spanish" in lang.lower()):
                _IDIOMA_ACTUAL = "es"
                return "es"
        except Exception:
            pass

    import locale
    try:
        loc = locale.getlocale()[0]
        if loc and loc.lower().startswith("en"):
            _IDIOMA_ACTUAL = "en"
            return "en"
    except Exception:
        pass

    _IDIOMA_ACTUAL = "es"
    return "es"


def establecer_idioma(lang_code):
    """Establece manualmente el idioma del complemento ('es' o 'en')."""
    global _IDIOMA_ACTUAL
    if lang_code in DICCIONARIO:
        _IDIOMA_ACTUAL = lang_code
    else:
        _IDIOMA_ACTUAL = "es"

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
        for mod_name in ('globalPlugins.python_tutor', 'addon.globalPlugins.python_tutor', 'python_tutor'):
            mod = sys.modules.get(mod_name)
            if mod:
                panel = getattr(mod, 'PythonTutorSettingsPanel', None)
                if panel:
                    panel.title = "Learning Python with NVDA" if _IDIOMA_ACTUAL == "en" else "Aprendizaje de Python con NVDA"
                plugin = getattr(mod, 'GlobalPlugin', None)
                if plugin:
                    plugin.scriptCategory = "Learning Python with NVDA" if _IDIOMA_ACTUAL == "en" else "Aprendizaje de Python con NVDA"
    except Exception:
        pass


def obtener_idioma_actual():
    """Devuelve el código del idioma activo ('es' o 'en')."""
    return _IDIOMA_ACTUAL


def _t(clave, **kwargs):
    """Obtiene la cadena traducida para el idioma activo con reemplazo de variables."""
    lang = _IDIOMA_ACTUAL
    text = DICCIONARIO.get(lang, {}).get(clave)
    if text is None:
        if clave == "Aprendizaje de Python con NVDA":
            return "Learning Python with NVDA" if lang == "en" else "Aprendizaje de Python con NVDA"
        text = DICCIONARIO.get("es", {}).get(clave, clave)
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text

# Alias para compatibilidad con llamadas gettext estándar
_ = _t

# Inicializar detección automática al cargar
detectar_idioma_preferido()
