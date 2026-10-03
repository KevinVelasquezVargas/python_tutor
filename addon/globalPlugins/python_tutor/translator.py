# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/translator.py
# Propósito: Traductor de sintaxis Python a Lenguaje Humano para accesibilidad (Bilingüe).
# Autor: Kevin Andrés Velasquez Vargas
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import re
from .i18n import obtener_idioma_actual


def traducir_linea_codigo(linea, lang=None):
    """
    Recibe una línea de código de Python y devuelve una explicación pedagógica,
    clara y natural en español o inglés para personas usuarias de lectores de pantalla.
    Totalmente local, sin conexión a Internet y sin latencia.
    """
    if lang is None:
        lang = obtener_idioma_actual()

    raw_linea = linea.strip()
    is_en = (lang == "en")

    if not raw_linea:
        return "Empty line." if is_en else "Línea vacía."

    # Comentarios
    if raw_linea.startswith("#"):
        comentario = raw_linea.lstrip("#").strip()
        if is_en:
            return f"Comment: {comentario}. Computers ignore this line, it serves as an explanatory note."
        return f"Comentario: {comentario}. Las computadoras ignoran esta línea, sirve como nota explicativa."

    # Quitar comentario inline si existe
    codigo = raw_linea
    if " #" in codigo:
        codigo = codigo.split(" #")[0].strip()

    # 1. Instrucción print
    m_print = re.match(r"^print\s*\((.*)\)$", codigo)
    if m_print:
        contenido = m_print.group(1).strip()
        if not contenido:
            return "Print statement: Outputs a blank line to console." if is_en else "Instrucción print: Imprime una línea en blanco en la salida de consola."
        if (contenido.startswith("'") and contenido.endswith("'")) or (contenido.startswith('"') and contenido.endswith('"')):
            texto = contenido[1:-1]
            return f"Print statement: Displays on screen and speaks aloud: '{texto}'." if is_en else f"Instrucción print: Muestra en pantalla y lee con voz el mensaje: '{texto}'."
        elif "," in contenido:
            return f"Print statement: Displays multiple values separated by spaces: {contenido}." if is_en else f"Instrucción print: Muestra varios datos en pantalla separados por espacios: {contenido}."
        elif any(op in contenido for op in ["+", "-", "*", "/", "%"]):
            return f"Print statement: Calculates mathematical expression '{contenido}' and outputs the result." if is_en else f"Instrucción print: Calcula la operación matemática '{contenido}' y muestra el resultado."
        else:
            return f"Print statement: Displays the value stored in variable or expression: {contenido}." if is_en else f"Instrucción print: Muestra el valor contenido en la variable o expresión: {contenido}."

    # 2. Control de flujo: if
    m_if = re.match(r"^if\s+(.*):$", codigo)
    if m_if:
        cond = m_if.group(1).strip()
        return f"Conditional 'if': Checks whether '{cond}' evaluates to true. If so, executes the indented block." if is_en else f"Condicional 'si' (if): Comprueba si se cumple '{cond}'. Si es verdadera, ejecutará las instrucciones indentadas siguientes."

    # 3. Control de flujo: elif
    m_elif = re.match(r"^elif\s+(.*):$", codigo)
    if m_elif:
        cond = m_elif.group(1).strip()
        return f"Alternative condition 'elif': If previous condition was false and '{cond}' is true, executes this block." if is_en else f"Condición alternativa (elif): Si la condición anterior fue falsa pero '{cond}' es verdadera, ejecutará este bloque."

    # 4. Control de flujo: else
    if codigo == "else:":
        return "Default branch 'else': Executes when none of the preceding conditions were met." if is_en else "Caso alternativo 'de lo contrario' (else): Se ejecutará si ninguna de las condiciones anteriores resultó verdadera."

    # 5. Bucle for
    m_for = re.match(r"^for\s+([a-zA-Z0-9_,\s]+)\s+in\s+(.*):$", codigo)
    if m_for:
        var = m_for.group(1).strip()
        iterable = m_for.group(2).strip()
        return f"'For' loop: Iterates through each item in '{iterable}', assigning it to '{var}'." if is_en else f"Bucle 'para cada' (for): Recorrerá uno a uno los elementos de '{iterable}', asignando cada uno a la variable '{var}' en cada vuelta."

    # 6. Bucle while
    m_while = re.match(r"^while\s+(.*):$", codigo)
    if m_while:
        cond = m_while.group(1).strip()
        return f"'While' loop: Repeats indented instructions continuously while condition '{cond}' remains true." if is_en else f"Bucle 'mientras' (while): Repetirá las instrucciones siguientes de forma continua mientras la condición '{cond}' siga siendo verdadera."

    # 7. Definición de función: def
    m_def = re.match(r"^def\s+([a-zA-Z0-9_]+)\s*\((.*)\):$", codigo)
    if m_def:
        nombre = m_def.group(1).strip()
        params = m_def.group(2).strip()
        if is_en:
            p_desc = f"with parameters '{params}'" if params else "without parameters"
            return f"Function definition (def): Defines reusable function '{nombre}' {p_desc}."
        p_desc = f"con los parámetros '{params}'" if params else "sin recibir parámetros"
        return f"Definición de función: Crea una nueva función llamada '{nombre}' {p_desc}."

    # 8. Sentencia return
    m_ret = re.match(r"^return(\s+(.*))?$", codigo)
    if m_ret:
        val = m_ret.group(2)
        if val:
            return f"'Return' statement: Exits the function and returns result: {val.strip()}." if is_en else f"Retorno de función: Finaliza la ejecución de la función y devuelve el resultado: {val.strip()}."
        return "'Return' statement: Exits the function without returning a specific value." if is_en else "Retorno de función: Finaliza la ejecución de la función sin devolver ningún valor específico."

    # 9. Asignaciones acumulativas: +=, -=, *=, /=
    m_aug = re.match(r"^([a-zA-Z0-9_]+)\s*(\+=|-=|\*=|/=|//=)\s*(.*)$", codigo)
    if m_aug:
        var = m_aug.group(1)
        op = m_aug.group(2)
        val = m_aug.group(3)
        if is_en:
            op_names_en = {"+=": "adding", "-=": "subtracting", "*=": "multiplying by", "/=": "dividing by", "//=": "floor dividing by"}
            return f"Augmented assignment: Updates variable '{var}' by {op_names_en.get(op, 'applying')} {val}."
        op_nombres_es = {"+=": "sumándole", "-=": "restándole", "*=": "multiplicándolo por", "/=": "dividiéndolo entre", "//=": "haciendo división entera con"}
        return f"Actualización acumulativa: Modifica la variable '{var}' {op_nombres_es.get(op, 'aplicándole')} {val}."

    # 10. Asignación estándar: variable = valor
    m_assign = re.match(r"^([a-zA-Z0-9_]+)\s*=\s*(.*)$", codigo)
    if m_assign:
        var = m_assign.group(1)
        val = m_assign.group(2).strip()

        if "input(" in val:
            return f"User input assignment: Prompts user for input and stores it in variable '{var}'." if is_en else f"Asignación con entrada de usuario: Pide al usuario que escriba un dato y lo guarda en la variable '{var}'."
        elif (val.startswith("'") and val.endswith("'")) or (val.startswith('"') and val.endswith('"')):
            return f"Variable assignment: Stores string {val} in variable '{var}'." if is_en else f"Asignación de variable: Guarda en la variable '{var}' el texto {val}."
        elif val.isdigit() or (val.startswith("-") and val[1:].isdigit()):
            return f"Variable assignment: Stores integer {val} in variable '{var}'." if is_en else f"Asignación de variable: Guarda en la variable '{var}' el número entero {val}."
        elif val in ("True", "False"):
            return f"Variable assignment: Stores boolean {val} in variable '{var}'." if is_en else f"Asignación de variable: Guarda en la variable '{var}' el valor lógico {val}."
        elif val.startswith("[") and val.endswith("]"):
            return f"Variable assignment: Stores list in variable '{var}'." if is_en else f"Asignación de variable: Crea una lista de elementos y la almacena en '{var}'."
        else:
            return f"Variable assignment: Evaluates '{val}' and assigns the result to variable '{var}'." if is_en else f"Asignación de variable: Evalúa '{val}' y guarda el resultado en la variable '{var}'."

    # 11. Manejo de excepciones: try y except
    if codigo == "try:":
        return "'Try' block: Starts a protected block to safely attempt execution." if is_en else "Bloque vigilado (try): Inicia una sección donde intentará ejecutar código protegiéndolo de posibles errores."

    m_exc = re.match(r"^except(\s+([a-zA-Z0-9_]+))?:$", codigo)
    if m_exc:
        err = m_exc.group(2)
        if err:
            return f"'Except' block: Catches exception of type '{err}' to handle it safely." if is_en else f"Captura de error (except): Si en el bloque try ocurre un fallo de tipo '{err}', ejecutará estas instrucciones para solucionarlo."
        return "'Except' block: Catches any exception to execute fallback code." if is_en else "Captura de error (except): Si en el bloque anterior ocurre cualquier error, ejecutará este bloque de contingencia."

    # 12. Importaciones
    m_imp = re.match(r"^import\s+([a-zA-Z0-9_,\s]+)$", codigo)
    if m_imp:
        return f"'Import' statement: Loads library '{m_imp.group(1).strip()}' to access its features." if is_en else f"Importación de módulo: Carga la librería '{m_imp.group(1).strip()}' para utilizar sus funciones adicionales."

    m_from = re.match(r"^from\s+([a-zA-Z0-9_.]+)\s+import\s+(.*)$", codigo)
    if m_from:
        return f"'Import from' statement: Loads '{m_from.group(2).strip()}' from module '{m_from.group(1).strip()}'." if is_en else f"Importación específica: Carga '{m_from.group(2).strip()}' desde el módulo '{m_from.group(1).strip()}'."

    # 13. Métodos de listas
    if ".append(" in codigo:
        m_app = re.search(r"([a-zA-Z0-9_]+)\.append\((.*)\)", codigo)
        if m_app:
            return f"List append method: Appends item '{m_app.group(2)}' to end of list '{m_app.group(1)}'." if is_en else f"Método append: Agrega el elemento '{m_app.group(2)}' al final de la lista '{m_app.group(1)}'."

    if ".remove(" in codigo:
        m_rem = re.search(r"([a-zA-Z0-9_]+)\.remove\((.*)\)", codigo)
        if m_rem:
            return f"List remove method: Removes first occurrence of '{m_rem.group(2)}' from list '{m_rem.group(1)}'." if is_en else f"Método remove: Elimina la primera aparición de '{m_rem.group(2)}' en la lista '{m_rem.group(1)}'."

    # 14. Control directo: break, continue, pass
    if codigo == "break":
        return "'Break' statement: Immediately terminates the current loop." if is_en else "Sentencia break: Interrumpe y finaliza inmediatamente el bucle actual."
    if codigo == "continue":
        return "'Continue' statement: Skips to next iteration of the loop." if is_en else "Sentencia continue: Salta directamente a la siguiente vuelta del bucle ignorando el resto del bloque."
    if codigo == "pass":
        return "'Pass' statement: Null placeholder statement." if is_en else "Sentencia pass: Indicador de paso nulo (no realiza ninguna acción, reserva el espacio de un bloque)."

    return f"Code line: {codigo}." if is_en else f"Línea de código: {codigo}."
