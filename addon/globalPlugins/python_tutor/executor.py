# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/executor.py
# Propósito: Ejecución segura con watchdog y diagnóstico pedagógico accesible.
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import os
import sys
import io
import threading
import traceback
import re

try:
    import addonHandler
    addonHandler.initTranslation()
except Exception:
    pass

try:
    _
except NameError:
    import gettext
    _loc = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "locale")
    try:
        _t = gettext.translation("nvda", localedir=_loc, languages=["es"])
        _ = _t.gettext
    except Exception:
        def _(msg):
            return msg


class ExecutionResult:
    """Contenedor de los resultados de ejecución y análisis pedagógico."""
    def __init__(self, output="", success=True, error_line=None, error_type="", error_msg="", friendly_explanation="", timed_out=False, local_ns=None, keyboard_warning=""):
        self.output = output
        self.success = success
        self.error_line = error_line
        self.error_type = error_type
        self.error_msg = error_msg
        self.friendly_explanation = friendly_explanation
        self.timed_out = timed_out
        self.local_ns = local_ns or {}
        self.keyboard_warning = keyboard_warning


def detectar_errores_teclado_comunes(src):
    """
    Detecta confusiones mecánicas frecuentes en teclados en español
    para orientar al estudiante antes de que se frustre con SyntaxError.
    """
    # 1. Comillas curvas / acentos tipográficos
    if "´" in src or "`" in src:
        return _("Keyboard notice: An accent (´) or backtick (`) was detected instead of a single quote ('). In Python, strings are enclosed in single quotes (') or double quotes (\").")

    if any(q in src for q in ["“", "”", "‘", "’"]):
        return _("Typography notice: The code contains curly or stylized quotes (“ ”). Python requires straight programming quotes (' or \").")

    # 2. Punto y coma al final de declaraciones de bloques
    for linea in src.splitlines():
        limpia = linea.strip()
        palabras_bloque = ("def ", "if ", "elif ", "while ", "for ", "class ", "try:", "except")
        if any(limpia.startswith(p) for p in palabras_bloque) and limpia.endswith(";"):
            return _("Syntax notice: You have placed a semicolon (;) at the end of a structure. In Python, functions, conditions, and loops must end with a colon (:).")

    # 3. Guion tipográfico largo en lugar del signo menos
    if "–" in src or "—" in src:
        return _("Character notice: An em dash or en dash (– or —) was detected. For mathematical subtraction and negative numbers, you must use a standard hyphen (-).")

    return ""


def generar_comparacion_salida(esperado, obtenido):
    """
    Genera una explicación comparativa accesible entre la salida esperada y la real.
    """
    esp_clean = esperado.strip()
    obt_clean = obtenido.strip()
    no_salida = _("(no output printed)")

    lineas = [
        _("Output comparison:"),
        # Translators: Output comparison expected output. {expected} is the expected output text.
        _("Expected output: {expected}").format(expected=esp_clean),
        # Translators: Output comparison actual output. {actual} is the program's output text.
        _("Your program's output: {actual}").format(actual=obt_clean if obt_clean else no_salida)
    ]

    if esp_clean.lower() == obt_clean.lower() and esp_clean != obt_clean:
        lineas.append(_("Pedagogical hint: Your output matches in words, but differs in uppercase or lowercase letters. Remember that Python is case-sensitive."))
    elif esp_clean.replace(" ", "") == obt_clean.replace(" ", ""):
        lineas.append(_("Pedagogical hint: The words match, but the spacing is not exactly the same as expected."))
    elif esp_clean.replace(",", "").replace(".", "") == obt_clean.replace(",", "").replace(".", ""):
        lineas.append(_("Pedagogical hint: Check the punctuation marks (commas or periods); some are missing or extra compared to the exercise."))
    else:
        lineas.append(_("Pedagogical hint: Check the text and variables requested in the mission instructions."))

    return "\n".join(lineas)


def explain_error(error_type, error_msg, linea=1, src=""):
    """
    Traduce excepciones estándar de Python en explicaciones pedagógicas claras,
    respetuosas y orientadas al aprendizaje accesible.
    """
    # Verificación previa de confusiones de teclado
    aviso_teclado = detectar_errores_teclado_comunes(src)
    if aviso_teclado:
        # Translators: Prefix with line number for keyboard warning. {line} is line number, {notice} is warning message.
        return _("On line {line}: {notice}").format(line=linea, notice=aviso_teclado)

    if error_type == "NameError":
        # Translators: Friendly explanation for NameError. {line} is the line number.
        return _("On line {line}: You have used a name or function that Python does not recognize yet. Check if it is spelled correctly or if you forgot to define the variable beforehand.").format(line=linea)
    elif error_type == "TypeError":
        # Translators: Friendly explanation for TypeError. {line} is the line number.
        return _("On line {line}: Type incompatibility. An operation was attempted between data types that do not directly combine (for example, adding text to a number without converting it first).").format(line=linea)
    elif error_type == "SyntaxError":
        # Translators: Friendly explanation for SyntaxError. {line} is the line number.
        return _("On line {line}: There is a detail in the code structure that the interpreter does not understand. Check for missing closing quotes, parentheses, or a colon at the end of the line.").format(line=linea)
    elif error_type == "IndentationError":
        # Translators: Friendly explanation for IndentationError. {line} is the line number.
        return _("On line {line}: Indentation error (spaces at line start). In Python, each indented block must be aligned exactly with 4 physical spaces.").format(line=linea)
    elif error_type == "IndexError":
        # Translators: Friendly explanation for IndexError. {line} is the line number.
        return _("On line {line}: Position out of range. You tried to access an element in a list or string that does not exist. Remember that indices start at 0.").format(line=linea)
    elif error_type == "KeyError":
        # Translators: Friendly explanation for KeyError. {line} is the line number.
        return _("On line {line}: Key not found in dictionary. Verify that the key name matches the stored data.").format(line=linea)
    elif error_type == "ZeroDivisionError":
        # Translators: Friendly explanation for ZeroDivisionError. {line} is the line number.
        return _("On line {line}: Division by zero. The calculation attempted to divide a quantity by 0, which is mathematically undefined.").format(line=linea)
    elif error_type == "ValueError":
        # Translators: Friendly explanation for ValueError. {line} is the line number.
        return _("On line {line}: Inappropriate value. The data type is correct, but the content cannot be processed (for example, trying to convert a word to an integer).").format(line=linea)
    elif error_type == "TimeoutError":
        return _("Active safety: Execution took more than 3 seconds and was stopped to protect your screen reader. A 'while' or 'for' loop might be missing an exit condition.")
    else:
        # Translators: Generic error explanation. {line} is line number, {error_type} is exception class name, {error_msg} is exception message.
        return _("On line {line}: An alert of type {error_type} occurred: {error_msg}.").format(line=linea, error_type=error_type, error_msg=error_msg)


def ejecutar_codigo_seguro(src, timeout=3.0):
    """
    Ejecuta el código en un hilo secundario aislado, vigilado por un temporizador.
    Garantiza la captura limpia de sys.stdout y protege la estabilidad de NVDA.
    """
    # 1. Comprobación temprana de caracteres de teclado incompatibles
    teclado_aviso = detectar_errores_teclado_comunes(src)

    result_holder = {}
    buf = io.StringIO()
    old_stdout = sys.stdout
    old_stderr = sys.stderr

    def worker():
        local_ns = {}
        try:
            sys.stdout = buf
            sys.stderr = buf
            compiled = compile(src, "<string>", "exec")
            exec(compiled, {"__builtins__": __builtins__}, local_ns)
            output = buf.getvalue()
            if not output:
                output = _("Code executed (no output printed to console).")
            result_holder['res'] = ExecutionResult(
                output=output,
                success=True,
                local_ns=local_ns,
                keyboard_warning=teclado_aviso
            )
        except Exception as e:
            tb = traceback.extract_tb(sys.exc_info()[2])
            linea_error = None
            for frame in reversed(tb):
                if frame.filename == "<string>":
                    linea_error = frame.lineno
                    break
            if not linea_error:
                linea_error = 1

            err_type = type(e).__name__
            err_msg = str(e)
            friendly = explain_error(err_type, err_msg, linea_error, src)

            # Translators: Error output during code execution. {line} is line number, {error_type} is exception name, {error_msg} is error description.
            err_output = _("Error on line {line} ({error_type}): {error_msg}").format(
                line=linea_error, error_type=err_type, error_msg=err_msg
            )
            result_holder['res'] = ExecutionResult(
                output=err_output,
                success=False,
                error_line=linea_error,
                error_type=err_type,
                error_msg=err_msg,
                friendly_explanation=friendly,
                local_ns=local_ns,
                keyboard_warning=teclado_aviso
            )
        finally:
            try:
                sys.stdout = old_stdout
                sys.stderr = old_stderr
            except Exception:
                pass

    hilo = threading.Thread(target=worker, name="PyTutorSandboxWorker", daemon=True)
    hilo.start()
    hilo.join(timeout=timeout)

    sys.stdout = old_stdout
    sys.stderr = old_stderr

    if hilo.is_alive():
        timeout_explanation = explain_error("TimeoutError", _("Execution time limit exceeded"), 1, src)
        return ExecutionResult(
            output=_("Security Error: Execution exceeded the limit of 3.0 seconds.\nPossible infinite loop detected."),
            success=False,
            error_line=1,
            error_type="TimeoutError",
            error_msg=_("Execution time limit exceeded."),
            friendly_explanation=timeout_explanation,
            timed_out=True
        )

    return result_holder.get(
        'res',
        ExecutionResult(
            output=_("Unknown error during process execution."),
            success=False,
            friendly_explanation=_("Could not complete script execution.")
        )
    )


def comprobar_balanceo_delimitadores(src):
    """
    Analiza el código en busca de paréntesis, corchetes, llaves y comillas desbalanceadas.
    Devuelve un mensaje accesible si encuentra una discrepancia, o None si está equilibrado.
    """
    pila = []
    mapa_cierre = {')': '(', ']': '[', '}': '{'}
    nombres_delimitadores = {
        '(': _('parenthesis'),
        '[': _('bracket'),
        '{': _('brace')
    }

    en_cadena = None  # "'" o '"'
    es_triple = False
    escape = False

    lineas = src.splitlines()
    for num_linea, linea in enumerate(lineas, start=1):
        idx = 0
        longitud = len(linea)
        while idx < longitud:
            c = linea[idx]

            # Manejo de caracteres escapados dentro de cadenas
            if escape:
                escape = False
                idx += 1
                continue

            if c == '\\' and en_cadena:
                escape = True
                idx += 1
                continue

            # Verificación de comillas
            if c in ("'", '"'):
                # Comprobar comillas triples
                if idx + 2 < longitud and linea[idx:idx+3] == c * 3:
                    if en_cadena == c and es_triple:
                        en_cadena = None
                        es_triple = False
                        idx += 3
                        continue
                    elif not en_cadena:
                        en_cadena = c
                        es_triple = True
                        idx += 3
                        continue

                # Comillas simples / normales
                if not es_triple:
                    if en_cadena == c:
                        en_cadena = None
                    elif not en_cadena:
                        en_cadena = c
                idx += 1
                continue

            # Si estamos dentro de una cadena de texto, ignoramos los delimitadores de sintaxis
            if en_cadena:
                idx += 1
                continue

            # Comentario: ignorar el resto de la línea
            if c == '#':
                break

            # Delimitadores de apertura
            if c in ('(', '[', '{'):
                pila.append((c, num_linea, idx + 1))
            # Delimitadores de cierre
            elif c in (')', ']', '}'):
                esperado = mapa_cierre[c]
                if not pila:
                    nombre = nombres_delimitadores.get(esperado, _("delimiter"))
                    # Translators: Delimiter mismatch error when closing delimiter has no corresponding opener.
                    # {line} is line number, {col} is column, {char} is closing character, {delimiter} is delimiter name.
                    return _("Line {line}, col {col}: Found closing '{char}' without a corresponding opening {delimiter}.").format(
                        line=num_linea, col=idx + 1, char=c, delimiter=nombre
                    )
                ultimo, lin_apertura, col_apertura = pila.pop()
                if ultimo != esperado:
                    nom_esp = nombres_delimitadores.get(ultimo, ultimo)
                    # Translators: Delimiter mismatch error when closing delimiter does not match opener.
                    # {line} is line number, {col} is column, {char} is closing char, {expected_name} is expected delimiter name, {expected_char} is expected char, {open_line} is line where opener was found.
                    return _("Line {line}, col {col}: Closed with '{char}', but expected closing {expected_name} '{expected_char}' opened on line {open_line}.").format(
                        line=num_linea, col=idx + 1, char=c, expected_name=nom_esp, expected_char=ultimo, open_line=lin_apertura
                    )

            idx += 1

        # Si había una cadena simple no cerrada al final de la línea
        if en_cadena and not es_triple:
            # Translators: Unclosed quote error at end of line. {line} is line number, {quote} is quote character.
            return _("Line {line}: Unclosed string quote {quote} at end of line.").format(
                line=num_linea, quote=en_cadena
            )

    if en_cadena and es_triple:
        # Translators: Unclosed triple quote block at end of file. {quotes} is triple quote string.
        return _("Syntax notice: Triple quote block {quotes} open without being closed at the end of the file.").format(
            quotes=en_cadena * 3
        )

    if pila:
        ultimo, lin_apertura, col_apertura = pila[-1]
        nom = nombres_delimitadores.get(ultimo, ultimo)
        # Translators: Unclosed delimiter error at end of code. {line} is line number, {col} is column, {delimiter} is delimiter name, {char} is delimiter char.
        return _("Line {line}, col {col}: The {delimiter} '{char}' remained open and was not closed.").format(
            line=lin_apertura, col=col_apertura, delimiter=nom, char=ultimo
        )

    return None
