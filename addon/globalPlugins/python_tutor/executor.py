# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/executor.py
# Propósito: Ejecución segura con watchdog y diagnóstico pedagógico accesible.
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import sys
import io
import threading
import traceback
import re


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
        return "Aviso de teclado: Se detectó el uso de un acento (´) o tilde invertida en lugar de una comilla simple ('). En Python los textos se encierran con comillas simples (') o dobles (\")."
    
    if any(q in src for q in ["“", "”", "‘", "’"]):
        return "Aviso de tipografía: El código contiene comillas curvas o estilizadas (“ ”). Python requiere comillas rectas de programación (' o \")."

    # 2. Punto y coma al final de declaraciones de bloques
    for linea in src.splitlines():
        limpia = linea.strip()
        palabras_bloque = ("def ", "if ", "elif ", "while ", "for ", "class ", "try:", "except")
        if any(limpia.startswith(p) for p in palabras_bloque) and limpia.endswith(";"):
            return "Aviso de sintaxis: Has colocado punto y coma (;) al final de una estructura. En Python, las funciones, condiciones y bucles deben finalizar con dos puntos (:)."

    # 3. Guion tipográfico largo en lugar del signo menos
    if "–" in src or "—" in src:
        return "Aviso de caracteres: Se detectó un guion largo (– o —). Para restas matemáticas y números negativos debes utilizar el guion simple (-)."

    return ""


def generar_comparacion_salida(esperado, obtenido):
    """
    Genera una explicación comparativa accesible entre la salida esperada y la real.
    """
    esp_clean = esperado.strip()
    obt_clean = obtenido.strip()

    lineas = [
        "=== COMPARACIÓN DE SALIDA ===",
        f"Salida esperada: {esp_clean}",
        f"Salida de tu programa: {obt_clean if obt_clean else '(sin salida impresa)'}"
    ]

    if esp_clean.lower() == obt_clean.lower() and esp_clean != obt_clean:
        lineas.append("Pista pedagógica: Tu salida coincide en las palabras, pero difiere en mayúsculas o minúsculas. Recuerda que Python distingue mayúsculas con exactitud.")
    elif esp_clean.replace(" ", "") == obt_clean.replace(" ", ""):
        lineas.append("Pista pedagógica: Las palabras coinciden, pero la separación de espacios no es exactamente igual a la esperada.")
    elif esp_clean.replace(",", "").replace(".", "") == obt_clean.replace(",", "").replace(".", ""):
        lineas.append("Pista pedagógica: Revisa los signos de puntuación (comas o puntos); faltan o sobran algunos respecto al ejercicio.")
    else:
        lineas.append("Pista pedagógica: Revisa el texto y variables solicitadas en la consigna de la misión.")

    return "\n".join(lineas)


def explain_error(error_type, error_msg, linea=1, src=""):
    """
    Traduce excepciones estándar de Python en explicaciones pedagógicas claras,
    respetuosas y orientadas al aprendizaje accesible.
    """
    # Verificación previa de confusiones de teclado
    aviso_teclado = detectar_errores_teclado_comunes(src)
    if aviso_teclado:
        return f"En la línea {linea}: {aviso_teclado}"

    if error_type == "NameError":
        return f"En la línea {linea}: Has utilizado un nombre o función que Python no reconoce todavía. Comprueba si está bien escrito o si olvidaste definir la variable previamente."
    elif error_type == "TypeError":
        return f"En la línea {linea}: Incompatibilidad de tipos. Se intentó realizar una operación entre datos que no combinan directamente (por ejemplo, sumar texto con un número sin convertirlo antes)."
    elif error_type == "SyntaxError":
        return f"En la línea {linea}: Hay un detalle en la estructura del código que el intérprete no comprende. Revisa si faltan comillas de cierre, paréntesis o los dos puntos al final de la línea."
    elif error_type == "IndentationError":
        return f"En la línea {linea}: Error de sangría (espacios al inicio). En Python, cada bloque subordinado debe alinearse de forma exacta con 4 espacios físicos."
    elif error_type == "IndexError":
        return f"En la línea {linea}: Posición fuera de rango. Intentaste acceder a un elemento en una lista o texto que no existe. Recuerda que las posiciones empiezan en 0."
    elif error_type == "KeyError":
        return f"En la línea {linea}: Clave no encontrada en el diccionario. Verifica que el nombre de la clave coincida con los datos registrados."
    elif error_type == "ZeroDivisionError":
        return f"En la línea {linea}: División entre cero. El cálculo intentó dividir una cantidad entre 0, lo cual es matemáticamente indefinido."
    elif error_type == "ValueError":
        return f"En la línea {linea}: Valor inapropiado. El tipo de dato es correcto, pero el contenido no se puede procesar (por ejemplo, intentar convertir una palabra a número entero)."
    elif error_type == "TimeoutError":
        return f"Seguridad activa: La ejecución tardó más de 3 segundos y se detuvo para proteger tu lector de pantalla. Es posible que un bucle 'while' o 'for' no tenga una condición de salida."
    else:
        return f"En la línea {linea}: Se produjo un aviso de tipo {error_type}: {error_msg}."


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
                output = "Código ejecutado (sin salidas impresas en consola)."
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

            result_holder['res'] = ExecutionResult(
                output=f"Error en línea {linea_error} ({err_type}): {err_msg}",
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
        timeout_explanation = explain_error("TimeoutError", "Límite de tiempo excedido", 1, src)
        return ExecutionResult(
            output="Error de Seguridad: La ejecución excedió el límite de 3.0 segundos.\nPosible bucle infinito detectado.",
            success=False,
            error_line=1,
            error_type="TimeoutError",
            error_msg="Tiempo de ejecución excedido.",
            friendly_explanation=timeout_explanation,
            timed_out=True
        )

    return result_holder.get(
        'res',
        ExecutionResult(
            output="Error desconocido durante la ejecución del proceso.",
            success=False,
            friendly_explanation="No fue posible completar la ejecución del script."
        )
    )


def comprobar_balanceo_delimitadores(src):
    """
    Analiza el código en busca de paréntesis, corchetes, llaves y comillas desbalanceadas.
    Devuelve un mensaje accesible si encuentra una discrepancia, o None si está equilibrado.
    """
    pila = []
    mapa_cierre = {')': '(', ']': '[', '}': '{'}
    nombres_delimitadores = {'(': 'paréntesis', '[': 'corchete', '{': 'llave'}

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
                    nombre = nombres_delimitadores.get(esperado, "delimitador")
                    return f"Línea {num_linea}, col {idx + 1}: Se encontró '{c}' de cierre sin un {nombre} de apertura correspondiente."
                ultimo, lin_apertura, col_apertura = pila.pop()
                if ultimo != esperado:
                    nom_esp = nombres_delimitadores.get(ultimo, ultimo)
                    return f"Línea {num_linea}, col {idx + 1}: Se cerró con '{c}', pero se esperaba cerrar el {nom_esp} '{ultimo}' abierto en la línea {lin_apertura}."

            idx += 1

        # Si había una cadena simple no cerrada al final de la línea
        if en_cadena and not es_triple:
            return f"Línea {num_linea}: Comilla {en_cadena} de texto sin cerrar al final de la línea."

    if en_cadena and es_triple:
        return f"Aviso de sintaxis: Bloque de comillas triples {en_cadena * 3} abierto sin cerrar al final del archivo."

    if pila:
        ultimo, lin_apertura, col_apertura = pila[-1]
        nom = nombres_delimitadores.get(ultimo, ultimo)
        return f"Línea {lin_apertura}, col {col_apertura}: El {nom} '{ultimo}' quedó abierto y no fue cerrado."

    return None

