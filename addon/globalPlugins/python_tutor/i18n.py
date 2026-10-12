# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/i18n.py
# Propósito: Sistema central de internacionalización. Interfaz ES/EN con
#            detección generalizada a cualquier catálogo lessons/<idioma>.json.
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
        "language_menu": "Cambiar idioma...",
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
        "language_menu": "Switch Language...",
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
    },
    "pt": {
        "app_title": "Aprendizagem de Python com NVDA",
        "app_subtitle": "Ambiente formativo e editor acessível de Python",
        "menu_file": "&Ficheiro",
        "menu_edit": "&Editar",
        "menu_tools": "Ferramen&tas",
        "menu_settings": "&Configuração",
        "menu_glossary": "&Glossário",
        "menu_help": "&Ajuda",
        "btn_run": "Executar (F5)",
        "btn_explain": "Explicar linha (F1)",
        "btn_ask_ai": "Consultar a IA (Ctrl+Shift+I)",
        "mode_learning": "Modo Aprendizagem",
        "mode_editor": "Modo Editor Autónomo",
        "switched_to_editor": "Modo Editor Autónomo ativado.",
        "switched_to_learning": "Modo Aprendizagem ativado.",
        "syntax_ok": "Sintaxe verificada com sucesso.",
        "syntax_error": "Erro de sintaxe detetado.",
        "new_script": "Novo script iniciado.",
        "file_opened": "Ficheiro carregado com sucesso: {name}",
        "file_saved": "Guardado com sucesso em: {name}",
        "shortcuts_title": "Guia de Atalhos de Teclado",
        "about_title": "Acerca de Aprendizagem de Python com NVDA",
        "ai_assistant_title": "Assistente de Inteligência Artificial",
        "ai_config_title": "Configuração do Assistente de IA...",
        "ai_consult_menu": "Consultar o Assistente de IA...\tCtrl+Shift+I",
        "pip_manager_title": "Gestor acessível de pacotes (pip)...",
        "project_manager_title": "Explorador de projetos multificheiro...\tCtrl+Shift+E",
        "language_menu": "Mudar idioma...",
        "settings_lang_label": "Idioma da interface e lições:",
        "settings_lang_auto": "Automático (segundo o NVDA)",
        "settings_lang_es": "Espanhol (Español)",
        "settings_lang_en": "Inglês (English)",
        "settings_ai_f1_label": "Ativar Assistente de IA para F1 (opcional, requer chave API)",
        "settings_ai_key_label": "Chave API do Google Gemini (opcional):",
        "settings_ai_note": "Por predefinição, a tecla F1 funciona de forma local e privada, sem ligação.",
        "settings_open_pip": "Abrir Gestor de Pacotes pip...",
        "settings_open_projects": "Abrir Explorador de Projetos...",
        "line_empty": "Linha vazia.",
        "comment_line": "Comentário: {comment}. Os computadores ignoram esta linha; serve como nota explicativa.",
        "print_empty": "Instrução print: Imprime uma linha em branco na saída da consola.",
        "print_text": "Instrução print: Mostra no ecrã e lê em voz alta a mensagem: '{text}'.",
        "if_cond": "Condicional 'se' (if): Verifica se '{cond}' se cumpre. Se for verdadeira, executa as instruções indentadas seguintes.",
        "elif_cond": "Condição alternativa (elif): Se a condição anterior foi falsa mas '{cond}' for verdadeira, executa este bloco.",
        "else_cond": "Bloco alternativo final (else): Executa-se se nenhuma das condições anteriores se cumpriu.",
        "for_loop": "Ciclo for: Itera e repete o bloco de código percorrendo '{target}'.",
        "while_loop": "Ciclo while: Repete as instruções indentadas enquanto a condição '{cond}' continuar verdadeira.",
        "def_func": "Definição de função (def): Declara uma função chamada '{name}' com os parâmetros '{params}'.",
        "class_def": "Definição de classe (class): Cria um modelo de objetos chamado '{name}'.",
        "return_stmt": "Instrução return: Termina a função e devolve o valor '{val}'.",
        "import_stmt": "Importação (import): Carrega o módulo ou biblioteca '{mod}' para usar as suas funções.",
        "try_block": "Bloco de controlo try: Tenta executar as instruções seguintes de forma segura.",
        "except_block": "Captura de erro (except): Trata a exceção '{exc}' se ocorreu um erro no bloco try."
    }
}


def _normalizar_idioma_soportado(lang):
    """Mapea un código bruto ('pt_PT', 'en-US') al idioma soportado más cercano.

    Prioriza los catálogos de lecciones (lessons_loader.normalizar_idioma)
    y aplica como respaldo los prefijos de la interfaz (DICCIONARIO).
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
    if prefijo in DICCIONARIO:
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
    """Devuelve el código del idioma activo (p. ej. 'es', 'en', 'pt')."""
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
