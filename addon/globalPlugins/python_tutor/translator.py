# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/translator.py
# Propósito: Traductor de sintaxis Python a Lenguaje Humano para accesibilidad.
#            Las explicaciones se traducen mediante gettext (i18n._t).
# Autor: Kevin Andrés Velasquez Vargas
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import re
from .i18n import _t


def traducir_linea_codigo(linea):
    """
    Recibe una línea de código de Python y devuelve una explicación pedagógica,
    clara y natural en el idioma activo para personas usuarias de lectores de pantalla.
    Totalmente local, sin conexión a Internet y sin latencia.
    """
    raw_linea = linea.strip()

    if not raw_linea:
        return _t("Línea vacía.")

    # Comentarios
    if raw_linea.startswith("#"):
        comentario = raw_linea.lstrip("#").strip()
        return _t(
            "Comentario: {comentario}. Las computadoras ignoran esta línea, sirve como nota explicativa.",
            comentario=comentario,
        )

    # Quitar comentario inline si existe
    codigo = raw_linea
    if " #" in codigo:
        codigo = codigo.split(" #")[0].strip()

    # 1. Instrucción print
    m_print = re.match(r"^print\s*\((.*)\)$", codigo)
    if m_print:
        contenido = m_print.group(1).strip()
        if not contenido:
            return _t("Instrucción print: Imprime una línea en blanco en la salida de consola.")
        if (contenido.startswith("'") and contenido.endswith("'")) or (contenido.startswith('"') and contenido.endswith('"')):
            texto = contenido[1:-1]
            return _t("Instrucción print: Muestra en pantalla y lee con voz el mensaje: '{texto}'.", texto=texto)
        elif "," in contenido:
            return _t("Instrucción print: Muestra varios datos en pantalla separados por espacios: {contenido}.", contenido=contenido)
        elif any(op in contenido for op in ["+", "-", "*", "/", "%"]):
            return _t("Instrucción print: Calcula la operación matemática '{contenido}' y muestra el resultado.", contenido=contenido)
        else:
            return _t("Instrucción print: Muestra el valor contenido en la variable o expresión: {contenido}.", contenido=contenido)

    # 2. Control de flujo: if
    m_if = re.match(r"^if\s+(.*):$", codigo)
    if m_if:
        cond = m_if.group(1).strip()
        return _t("Condicional 'si' (if): Comprueba si se cumple '{cond}'. Si es verdadera, ejecutará las instrucciones indentadas siguientes.", cond=cond)

    # 3. Control de flujo: elif
    m_elif = re.match(r"^elif\s+(.*):$", codigo)
    if m_elif:
        cond = m_elif.group(1).strip()
        return _t("Condición alternativa (elif): Si la condición anterior fue falsa pero '{cond}' es verdadera, ejecutará este bloque.", cond=cond)

    # 4. Control de flujo: else
    if codigo == "else:":
        return _t("Caso alternativo 'de lo contrario' (else): Se ejecutará si ninguna de las condiciones anteriores resultó verdadera.")

    # 5. Bucle for
    m_for = re.match(r"^for\s+([a-zA-Z0-9_,\s]+)\s+in\s+(.*):$", codigo)
    if m_for:
        var = m_for.group(1).strip()
        iterable = m_for.group(2).strip()
        return _t("Bucle 'para cada' (for): Recorrerá uno a uno los elementos de '{iterable}', asignando cada uno a la variable '{var}' en cada vuelta.", iterable=iterable, var=var)

    # 6. Bucle while
    m_while = re.match(r"^while\s+(.*):$", codigo)
    if m_while:
        cond = m_while.group(1).strip()
        return _t("Bucle 'mientras' (while): Repetirá las instrucciones siguientes de forma continua mientras la condición '{cond}' siga siendo verdadera.", cond=cond)

    # 7. Definición de función: def
    m_def = re.match(r"^def\s+([a-zA-Z0-9_]+)\s*\((.*)\):$", codigo)
    if m_def:
        nombre = m_def.group(1).strip()
        params = m_def.group(2).strip()
        if params:
            p_desc = _t("con los parámetros '{params}'", params=params)
        else:
            p_desc = _t("sin recibir parámetros")
        return _t("Definición de función: Crea una nueva función llamada '{nombre}' {p_desc}.", nombre=nombre, p_desc=p_desc)

    # 8. Sentencia return
    m_ret = re.match(r"^return(\s+(.*))?$", codigo)
    if m_ret:
        val = m_ret.group(2)
        if val:
            return _t("Retorno de función: Finaliza la ejecución de la función y devuelve el resultado: {val}.", val=val.strip())
        return _t("Retorno de función: Finaliza la ejecución de la función sin devolver ningún valor específico.")

    # 9. Asignaciones acumulativas: +=, -=, *=, /=
    m_aug = re.match(r"^([a-zA-Z0-9_]+)\s*(\+=|-=|\*=|/=|//=)\s*(.*)$", codigo)
    if m_aug:
        var = m_aug.group(1)
        op = m_aug.group(2)
        val = m_aug.group(3)
        op_nombres = {
            "+=": _t("sumándole"), "-=": _t("restándole"), "*=": _t("multiplicándolo por"),
            "/=": _t("dividiéndolo entre"), "//=": _t("haciendo división entera con"),
        }
        return _t(
            "Actualización acumulativa: Modifica la variable '{var}' {operacion} {val}.",
            var=var, operacion=op_nombres.get(op, _t("aplicándole")), val=val,
        )

    # 10. Asignación estándar: variable = valor
    m_assign = re.match(r"^([a-zA-Z0-9_]+)\s*=\s*(.*)$", codigo)
    if m_assign:
        var = m_assign.group(1)
        val = m_assign.group(2).strip()

        if "input(" in val:
            return _t("Asignación con entrada de usuario: Pide al usuario que escriba un dato y lo guarda en la variable '{var}'.", var=var)
        elif (val.startswith("'") and val.endswith("'")) or (val.startswith('"') and val.endswith('"')):
            return _t("Asignación de variable: Guarda en la variable '{var}' el texto {val}.", var=var, val=val)
        elif val.isdigit() or (val.startswith("-") and val[1:].isdigit()):
            return _t("Asignación de variable: Guarda en la variable '{var}' el número entero {val}.", var=var, val=val)
        elif val in ("True", "False"):
            return _t("Asignación de variable: Guarda en la variable '{var}' el valor lógico {val}.", var=var, val=val)
        elif val.startswith("[") and val.endswith("]"):
            return _t("Asignación de variable: Crea una lista de elementos y la almacena en '{var}'.", var=var)
        else:
            return _t("Asignación de variable: Evalúa '{val}' y guarda el resultado en la variable '{var}'.", var=var, val=val)

    # 11. Manejo de excepciones: try y except
    if codigo == "try:":
        return _t("Bloque vigilado (try): Inicia una sección donde intentará ejecutar código protegiéndolo de posibles errores.")

    m_exc = re.match(r"^except(\s+([a-zA-Z0-9_]+))?:$", codigo)
    if m_exc:
        err = m_exc.group(2)
        if err:
            return _t("Captura de error (except): Si en el bloque try ocurre un fallo de tipo '{err}', ejecutará estas instrucciones para solucionarlo.", err=err)
        return _t("Captura de error (except): Si en el bloque anterior ocurre cualquier error, ejecutará este bloque de contingencia.")

    # 12. Importaciones
    m_imp = re.match(r"^import\s+([a-zA-Z0-9_,\s]+)$", codigo)
    if m_imp:
        modulo = m_imp.group(1).strip()
        return _t("Importación de módulo: Carga la librería '{modulo}' para utilizar sus funciones adicionales.", modulo=modulo)

    m_from = re.match(r"^from\s+([a-zA-Z0-9_.]+)\s+import\s+(.*)$", codigo)
    if m_from:
        origen = m_from.group(1).strip()
        nombres = m_from.group(2).strip()
        return _t("Importación específica: Carga '{nombres}' desde el módulo '{origen}'.", nombres=nombres, origen=origen)

    # 13. Métodos de listas
    if ".append(" in codigo:
        m_app = re.search(r"([a-zA-Z0-9_]+)\.append\((.*)\)", codigo)
        if m_app:
            return _t(
                "Método append: Agrega el elemento '{item}' al final de la lista '{lista}'.",
                item=m_app.group(2), lista=m_app.group(1),
            )

    if ".remove(" in codigo:
        m_rem = re.search(r"([a-zA-Z0-9_]+)\.remove\((.*)\)", codigo)
        if m_rem:
            return _t(
                "Método remove: Elimina la primera aparición de '{item}' en la lista '{lista}'.",
                item=m_rem.group(2), lista=m_rem.group(1),
            )

    # 14. Control directo: break, continue, pass
    if codigo == "break":
        return _t("Sentencia break: Interrumpe y finaliza inmediatamente el bucle actual.")
    if codigo == "continue":
        return _t("Sentencia continue: Salta directamente a la siguiente vuelta del bucle ignorando el resto del bloque.")
    if codigo == "pass":
        return _t("Sentencia pass: Indicador de paso nulo (no realiza ninguna acción, reserva el espacio de un bloque).")

    return _t("Línea de código: {codigo}.", codigo=codigo)
