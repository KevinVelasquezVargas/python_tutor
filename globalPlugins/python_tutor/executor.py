# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/executor.py
# Propósito: Ejecución segura con watchdog y diagnóstico pedagógico de errores.
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import sys
import io
import threading
import traceback


class ExecutionResult:
    """Contenedor de los resultados de ejecución y análisis pedagógico."""
    def __init__(self, output="", success=True, error_line=None, error_type="", error_msg="", friendly_explanation="", timed_out=False, local_ns=None):
        self.output = output
        self.success = success
        self.error_line = error_line
        self.error_type = error_type
        self.error_msg = error_msg
        self.friendly_explanation = friendly_explanation
        self.timed_out = timed_out
        self.local_ns = local_ns or {}


def explain_error(error_type, error_msg, linea=1):
    """
    Traduce excepciones estándar de Python en explicaciones pedagógicas claras,
    respetuosas y orientadas al aprendizaje accesible.
    """
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
        return f"En la línea {linea}: Se produjo un error de tipo {error_type}: {error_msg}."


def ejecutar_codigo_seguro(src, timeout=3.0):
    """
    Ejecuta el código en un hilo secundario aislado, vigilado por un temporizador.
    Garantiza la captura limpia de sys.stdout y protege la estabilidad de NVDA.
    """
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
                local_ns=local_ns
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
            friendly = explain_error(err_type, err_msg, linea_error)

            result_holder['res'] = ExecutionResult(
                output=f"Error en línea {linea_error} ({err_type}): {err_msg}",
                success=False,
                error_line=linea_error,
                error_type=err_type,
                error_msg=err_msg,
                friendly_explanation=friendly,
                local_ns=local_ns
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

    # Restauración mandataria inmediata en el hilo principal
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    if hilo.is_alive():
        timeout_explanation = explain_error("TimeoutError", "Límite de tiempo excedido", 1)
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
