# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/translator.py
# Propósito: Traductor de sintaxis Python a Lenguaje Humano para accesibilidad.
# Autor: Kevin Andrés Velasquez Vargas
# Internacionalización (i18n): MisterK-Dev (desarrollado con Google Antigravity 2.0)
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import re

try:
    import addonHandler
    addonHandler.initTranslation()
except Exception:
    pass

try:
    _
except NameError:
    def _(msg):
        return msg


def traducir_linea_codigo(linea):
    """
    Recibe una línea de código de Python y devuelve una explicación pedagógica,
    clara y natural para personas usuarias de lectores de pantalla.
    """
    raw_linea = linea.strip()
    if not raw_linea:
        # Translators: Screen reader explanation for an empty line of code.
        return _("Empty line.")

    # Comentarios
    if raw_linea.startswith("#"):
        comentario = raw_linea.lstrip("#").strip()
        # Translators: Screen reader explanation for a Python comment line.
        return _("Comment: {comment}. Computers ignore this line; it serves as an explanatory note.").format(comment=comentario)

    # Quitar comentario inline si existe
    codigo = raw_linea
    if " #" in codigo:
        codigo = codigo.split(" #")[0].strip()

    # 1. Instrucción print
    m_print = re.match(r"^print\s*\((.*)\)$", codigo)
    if m_print:
        contenido = m_print.group(1).strip()
        if not contenido:
            # Translators: Screen reader explanation for print statement with no arguments.
            return _("print instruction: Prints a blank line to console output.")
        if (contenido.startswith("'") and contenido.endswith("'")) or (contenido.startswith('"') and contenido.endswith('"')):
            texto = contenido[1:-1]
            # Translators: Screen reader explanation for print statement with text literal.
            return _("print instruction: Displays on screen and speaks aloud the message: '{text}'.").format(text=texto)
        elif "," in contenido:
            # Translators: Screen reader explanation for print statement with multiple comma-separated items.
            return _("print instruction: Displays multiple items on screen separated by spaces: {items}.").format(items=contenido)
        elif any(op in contenido for op in ["+", "-", "*", "/", "%"]):
            # Translators: Screen reader explanation for print statement with arithmetic operation.
            return _("print instruction: Calculates the mathematical operation '{operation}' and displays the result.").format(operation=contenido)
        else:
            # Translators: Screen reader explanation for print statement with variable or expression.
            return _("print instruction: Displays the value stored in variable or expression: {expression}.").format(expression=contenido)

    # 2. Control de flujo: if
    m_if = re.match(r"^if\s+(.*):$", codigo)
    if m_if:
        cond = m_if.group(1).strip()
        # Translators: Screen reader explanation for an if conditional statement.
        return _("Conditional 'if': Checks if '{condition}' is met. If true, executes the following indented statements.").format(condition=cond)

    # 3. Control de flujo: elif
    m_elif = re.match(r"^elif\s+(.*):$", codigo)
    if m_elif:
        cond = m_elif.group(1).strip()
        # Translators: Screen reader explanation for an elif conditional statement.
        return _("Alternative condition 'elif': If the previous condition was false but '{condition}' is true, executes this block.").format(condition=cond)

    # 4. Control de flujo: else
    if codigo == "else:":
        # Translators: Screen reader explanation for an else statement.
        return _("Alternative case 'else': Executes if none of the preceding conditions were true.")

    # 5. Bucle for
    m_for = re.match(r"^for\s+([a-zA-Z0-9_,\s]+)\s+in\s+(.*):$", codigo)
    if m_for:
        var = m_for.group(1).strip()
        iterable = m_for.group(2).strip()
        # Translators: Screen reader explanation for a for loop.
        return _("For loop: Iterates item by item over '{iterable}', assigning each to variable '{variable}' on each pass.").format(iterable=iterable, variable=var)

    # 6. Bucle while
    m_while = re.match(r"^while\s+(.*):$", codigo)
    if m_while:
        cond = m_while.group(1).strip()
        # Translators: Screen reader explanation for a while loop.
        return _("While loop: Repeats following statements continuously as long as condition '{condition}' remains true.").format(condition=cond)

    # 7. Definición de función: def
    m_def = re.match(r"^def\s+([a-zA-Z0-9_]+)\s*\((.*)\):$", codigo)
    if m_def:
        nombre = m_def.group(1).strip()
        params = m_def.group(2).strip()
        # Translators: Part of function definition description when arguments are present.
        param_desc = _("with parameters '{params}'").format(params=params) if params else _("without receiving parameters")
        # Translators: Screen reader explanation for a function definition.
        return _("Function definition: Creates a new function named '{name}' {param_desc}.").format(name=nombre, param_desc=param_desc)

    # 8. Sentencia return
    m_ret = re.match(r"^return(\s+(.*))?$", codigo)
    if m_ret:
        val = m_ret.group(2)
        if val:
            # Translators: Screen reader explanation for return statement returning a value.
            return _("Function return: Ends function execution and returns result: {value}.").format(value=val.strip())
        # Translators: Screen reader explanation for bare return statement.
        return _("Function return: Ends function execution without returning a specific value.")

    # 9. Asignaciones acumulativas: +=, -=, *=, /=
    m_aug = re.match(r"^([a-zA-Z0-9_]+)\s*(\+=|-=|\*=|/=|//=)\s*(.*)$", codigo)
    if m_aug:
        var = m_aug.group(1)
        op = m_aug.group(2)
        val = m_aug.group(3)
        op_nombres = {
            # Translators: Augmented assignment description for +=.
            "+=": _("adding"),
            # Translators: Augmented assignment description for -=.
            "-=": _("subtracting"),
            # Translators: Augmented assignment description for *=.
            "*=": _("multiplying by"),
            # Translators: Augmented assignment description for /=.
            "/=": _("dividing by"),
            # Translators: Augmented assignment description for //=.
            "//=": _("floor dividing by")
        }
        # Translators: Fallback verb for unrecognized augmented assignment operators.
        op_label = op_nombres.get(op, _("applying"))
        # Translators: Screen reader explanation for augmented assignment operators (+-, -=, etc.).
        return _("Cumulative update: Modifies variable '{variable}' by {op} {value}.").format(variable=var, op=op_label, value=val)

    # 10. Asignación estándar: variable = valor
    m_assign = re.match(r"^([a-zA-Z0-9_]+)\s*=\s*(.*)$", codigo)
    if m_assign:
        var = m_assign.group(1)
        val = m_assign.group(2).strip()

        if "input(" in val:
            # Translators: Screen reader explanation for user input prompt assignment.
            return _("Assignment with user input: Prompts the user for input and stores it in variable '{variable}'.").format(variable=var)
        elif (val.startswith("'") and val.endswith("'")) or (val.startswith('"') and val.endswith('"')):
            # Translators: Screen reader explanation for string assignment.
            return _("Variable assignment: Stores text {value} in variable '{variable}'.").format(variable=var, value=val)
        elif val.isdigit() or (val.startswith("-") and val[1:].isdigit()):
            # Translators: Screen reader explanation for integer assignment.
            return _("Variable assignment: Stores integer number {value} in variable '{variable}'.").format(variable=var, value=val)
        elif val in ("True", "False"):
            # Translators: Screen reader explanation for boolean assignment.
            return _("Variable assignment: Stores boolean value {value} in variable '{variable}'.").format(variable=var, value=val)
        elif val.startswith("[") and val.endswith("]"):
            # Translators: Screen reader explanation for list assignment.
            return _("Variable assignment: Creates a list of elements and stores it in '{variable}'.").format(variable=var)
        else:
            # Translators: Screen reader explanation for generic expression assignment.
            return _("Variable assignment: Evaluates '{value}' and stores result in variable '{variable}'.").format(variable=var, value=val)

    # 11. Manejo de excepciones: try y except
    if codigo == "try:":
        # Translators: Screen reader explanation for try block.
        return _("Guarded block (try): Begins a protected section executing code safe from errors.")

    m_exc = re.match(r"^except(\s+([a-zA-Z0-9_]+))?:$", codigo)
    if m_exc:
        err = m_exc.group(2)
        if err:
            # Translators: Screen reader explanation for typed except block.
            return _("Error handler (except): If error '{error}' occurs in try block, executes these recovery statements.").format(error=err)
        # Translators: Screen reader explanation for general except block.
        return _("Error handler (except): If any error occurs in the preceding block, executes this fallback block.")

    # 12. Importaciones
    m_imp = re.match(r"^import\s+([a-zA-Z0-9_,\s]+)$", codigo)
    if m_imp:
        # Translators: Screen reader explanation for import statement.
        return _("Module import: Loads library '{module}' to use its functions.").format(module=m_imp.group(1).strip())

    m_from = re.match(r"^from\s+([a-zA-Z0-9_.]+)\s+import\s+(.*)$", codigo)
    if m_from:
        # Translators: Screen reader explanation for from-import statement.
        return _("Specific import: Loads '{item}' from module '{module}'.").format(item=m_from.group(2).strip(), module=m_from.group(1).strip())

    # 13. Métodos comunes de listas: append, remove, pop
    if ".append(" in codigo:
        m_app = re.search(r"([a-zA-Z0-9_]+)\.append\((.*)\)", codigo)
        if m_app:
            # Translators: Screen reader explanation for list.append method.
            return _("append method: Adds element '{item}' to the end of list '{list_name}'.").format(item=m_app.group(2), list_name=m_app.group(1))

    if ".remove(" in codigo:
        m_rem = re.search(r"([a-zA-Z0-9_]+)\.remove\((.*)\)", codigo)
        if m_rem:
            # Translators: Screen reader explanation for list.remove method.
            return _("remove method: Removes first occurrence of '{item}' from list '{list_name}'.").format(item=m_rem.group(2), list_name=m_rem.group(1))

    # 14. Control directo: break, continue, pass
    if codigo == "break":
        # Translators: Screen reader explanation for break statement.
        return _("break statement: Immediately terminates the current loop.")
    if codigo == "continue":
        # Translators: Screen reader explanation for continue statement.
        return _("continue statement: Skips directly to the next loop iteration.")
    if codigo == "pass":
        # Translators: Screen reader explanation for pass statement.
        return _("pass statement: Null operation placeholder reserving space for a block.")

    # Translators: Screen reader explanation for generic line of code.
    return _("Code line: {code}.").format(code=codigo)
