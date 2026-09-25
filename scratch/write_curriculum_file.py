# -*- coding: utf-8 -*-
import sys
import os

from build_curriculum import generate

chapters = generate()

output_path = os.path.abspath('globalPlugins/python_tutor/curriculum.py')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/curriculum.py
# Propósito: Temario pedagógico no visual de 32 capítulos progresivos con
#            fundamentos conceptuales previos, retos prácticos y quizzes formativos.
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

CURRICULUM = [
''')

    for c in chapters:
        f.write('    {\n')
        f.write(f'        "id": {c["id"]},\n')
        f.write(f'        "titulo": {repr(c["titulo"])},\n')
        f.write(f'        "resumen": {repr(c["resumen"])},\n')
        f.write('        "pasos": [\n')
        for p in c["pasos"]:
            f.write('            {\n')
            f.write(f'                "titulo": {repr(p["titulo"])},\n')
            f.write(f'                "tipo": {repr(p["tipo"])},\n')
            f.write(f'                "instruccion": {repr(p["instruccion"])},\n')
            f.write(f'                "codigo": {repr(p["codigo"])},\n')
            if "salida_esperada" in p and p["salida_esperada"]:
                f.write(f'                "salida_esperada": {repr(p["salida_esperada"])},\n')
            if "pistas" in p:
                f.write(f'                "pistas": {repr(p["pistas"])},\n')
            if "pregunta" in p:
                f.write(f'                "pregunta": {repr(p["pregunta"])},\n')
                f.write(f'                "opciones": {repr(p["opciones"])},\n')
                f.write(f'                "correcta": {p["correcta"]},\n')
                f.write(f'                "explicacion": {repr(p["explicacion"])},\n')

            # Write appropriate validator
            if p["tipo"] == "quiz":
                corr_str = str(p.get("correcta", 0) + 1)
                f.write(f'                "validar": lambda src, res, ns: {repr(corr_str)} in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])\n')
            elif p["tipo"] == "observar":
                f.write('                "validar": lambda src, res, ns: len(res.strip()) > 0\n')
            elif p["tipo"] == "experimentar":
                f.write('                "validar": lambda src, res, ns: len(res.strip()) > 0\n')
            else: # desafio
                cid = c["id"]
                if cid == 1:
                    f.write('                "validar": lambda src, res, ns: ("jabón" in res.lower() or "jabon" in res.lower()) and "grifo" in res.lower()\n')
                elif cid == 2:
                    f.write('                "validar": lambda src, res, ns: "bienvenido" in res.lower() and "estudiante" in res.lower()\n')
                elif cid == 3:
                    f.write('                "validar": lambda src, res, ns: "true" in res.lower() and "acceso" in res.lower()\n')
                elif cid == 4:
                    f.write('                "validar": lambda src, res, ns: "aprendiendo python con nvda" in res.lower()\n')
                elif cid == 5:
                    f.write('                "validar": lambda src, res, ns: "programando en" in res.lower() and "python" in res.lower()\n')
                elif cid == 6:
                    f.write('                "validar": lambda src, res, ns: "25" in res and ("triángulo" in res.lower() or "triangulo" in res.lower())\n')
                elif cid == 7:
                    f.write('                "validar": lambda src, res, ns: "bogot" in res.lower() and "colombia" in res.lower()\n')
                elif cid == 8:
                    f.write('                "validar": lambda src, res, ns: "21" in res and ("tendrás" in res.lower() or "tendras" in res.lower())\n')
                elif cid == 9:
                    f.write('                "validar": lambda src, res, ns: "70" in res and "true" in res.lower()\n')
                elif cid == 10:
                    f.write('                "validar": lambda src, res, ns: "buenas tardes" in res.lower() and "if " in src\n')
                elif cid == 11:
                    f.write('                "validar": lambda src, res, ns: "aprobado" in res.lower() and "elif" in src\n')
                elif cid == 12:
                    f.write('                "validar": lambda src, res, ns: "pan" in res.lower() and "compras" in src\n')
                elif cid == 13:
                    f.write('                "validar": lambda src, res, ns: "3" in res and "colores" in src\n')
                elif cid == 14:
                    f.write('                "validar": lambda src, res, ns: "5" in res and "for " in src\n')
                elif cid == 15:
                    f.write('                "validar": lambda src, res, ns: "3" in res and "while " in src\n')
                elif cid == 16:
                    f.write('                "validar": lambda src, res, ns: "2" in res and "precios" in src\n')
                elif cid == 17:
                    f.write('                "validar": lambda src, res, ns: "50" in res and "100" in res\n')
                elif cid == 18:
                    f.write('                "validar": lambda src, res, ns: "12" in res and "def sumar" in src\n')
                elif cid == 19:
                    f.write('                "validar": lambda src, res, ns: "36" in res and "return" in src\n')
                elif cid == 20:
                    f.write('                "validar": lambda src, res, ns: "error capturado" in res.lower() and "except" in src\n')
                elif cid == 21:
                    f.write('                "validar": lambda src, res, ns: "15" in res and "suma correcta" in res.lower()\n')
                elif cid == 22:
                    f.write('                "validar": lambda src, res, ns: "guardado listo" in res.lower() and "with open" in src\n')
                elif cid == 23:
                    f.write('                "validar": lambda src, res, ns: "perro" in res.lower() and "class Mascota" in src\n')
                elif cid == 24:
                    f.write('                "validar": lambda src, res, ns: "programador" in res.lower() and "__init__" in src\n')
                elif cid == 25:
                    f.write('                "validar": lambda src, res, ns: "amigo" in res.lower() and "saludar" in src\n')
                elif cid == 26:
                    f.write('                "validar": lambda src, res, ns: "toyota" in res.lower() and "corolla" in res.lower() and "super()" in src\n')
                elif cid == 27:
                    f.write('                "validar": lambda src, res, ns: ("3" in res and "7" in res and "__str__" in src)\n')
                elif cid == 28:
                    f.write('                "validar": lambda src, res, ns: "12" in res and "math" in src\n')
                elif cid == 29:
                    f.write('                "validar": lambda src, res, ns: "oscuro" in res.lower() and "json.dumps" in src\n')
                elif cid == 30:
                    f.write('                "validar": lambda src, res, ns: "teclado" in res.lower() and "sqlite3" in src\n')
                elif cid == 31:
                    f.write('                "validar": lambda src, res, ns: "servicio disponible" in res.lower()\n')
                elif cid == 32:
                    f.write('                "validar": lambda src, res, ns: "todas las pruebas" in res.lower() or "éxito" in res.lower() or "exito" in res.lower()\n')

            f.write('            },\n')
        f.write('        ]\n')
        f.write('    },\n')

    f.write('''
]

GLOSARIO = {
    'None': 'None: Objeto constante que representa formalmente la ausencia de valor o valor nulo.',
    'Traceback': 'Traceback: Informe diagnóstico de la pila de llamadas que detalla el camino de ejecución hasta el error.',
    '__init__': '__init__: Método constructor especial invocado automáticamente al instanciar una nueva clase.',
    '__str__': '__str__: Método especial que define la representación legible en cadena de texto devuelta por print(objeto).',
    'and': 'and: Operador lógico que retorna True si y solo si ambas expresiones son verdaderas.',
    'assert': 'assert: Sentencia de aserción que genera un AssertionError si la expresión booleana asociada es falsa.',
    'bool': 'bool: Tipo de dato booleano que solo admite dos estados: True (Verdadero) o False (Falso).',
    'break': 'break: Interrumpe de forma inmediata la ejecución del bucle (for o while) activo.',
    'class': 'class: Molde estructural para la definición de objetos bajo el paradigma de programación orientada a objetos.',
    'continue': 'continue: Salta el resto de la iteración actual y pasa a la siguiente vuelta del bucle.',
    'def': 'def: Palabra clave para declarar e inicializar funciones reutilizables con nombre propio.',
    'dict': 'dict: Colección asociativa de parejas clave-valor delimitada por llaves {}.',
    'elif': "elif: Abreviatura de 'else if'. Permite encadenar múltiples condiciones excluyentes de forma ordenada.",
    'else': 'else: Bloque condicional alternativo ejecutado cuando ninguna de las condiciones previas fue verdadera.',
    'except': 'except: Captura y gestiona un error específico dentro de un bloque protector try sin colapsar el programa.',
    'finally': 'finally: Bloque que se ejecuta de forma mandataria al concluir un bloque try/except.',
    'float': 'float: Tipo de dato primitivo para números decimales de coma flotante.',
    'for': 'for: Bucle de control utilizado para recorrer secuencialmente elementos de una lista, tupla o rango.',
    'if': 'if: Estructura condicional que ejecuta su bloque subordinado únicamente si su condición se evalúa como verdadera (True).',
    'import': 'import: Carga y enlaza bibliotecas y módulos del sistema en el espacio de nombres de tu script.',
    'in': 'in: Operador de pertenencia que verifica si un elemento está presente dentro de una colección.',
    'input': 'input(): Función que detiene la ejecución para leer texto ingresado por el usuario desde el teclado.',
    'int': 'int: Tipo de dato primitivo que representa números enteros sin parte fraccionaria.',
    'is': 'is: Operador de identidad que evalúa si dos variables apuntan al mismo objeto en memoria física.',
    'json': 'json: Módulo de la biblioteca estándar para serializar y deserializar datos en notación JavaScript Object Notation.',
    'len': 'len(): Retorna la cantidad total de elementos contenidos en una lista, texto, tupla o diccionario.',
    'list': 'list: Estructura de datos ordenada, indexada y mutable delimitada por corchetes [].',
    'not': 'not: Operador de negación que invierte el valor lógico de una condición.',
    'or': 'or: Operador lógico que retorna True si al menos una de las expresiones es verdadera.',
    'pass': 'pass: Instrucción nula utilizada como marcador de posición sintáctico en bloques vacíos.',
    'print': 'print(): Función incorporada para enviar mensajes y datos hacia la salida estándar y el lector de pantalla.',
    'range': 'range(): Genera una secuencia ordenada e inmutable de números enteros.',
    'return': 'return: Finaliza la ejecución de una función y devuelve un valor procesado al código que la invocó.',
    'self': 'self: Parámetro explícito en métodos de clase que referencia a la instancia viva sobre la cual se opera.',
    'set': 'set: Colección de datos desordenada y compuesta estrictamente por elementos únicos sin repeticiones.',
    'sqlite3': 'sqlite3: Módulo estándar de Python que implementa un motor de base de datos SQL embebido en disco o memoria.',
    'str': 'str: Tipo de dato para secuencias de texto alfanumérico delimitadas por comillas.',
    'super': 'super(): Función de conveniencia que permite acceder e invocar métodos delegados de la clase base padre.',
    'try': 'try: Delimita un bloque de código vigilado donde se anticipa la posibilidad de una excepción.',
    'tuple': 'tuple: Estructura de datos ordenada e inmutable delimitada por paréntesis ().',
    'unittest': 'unittest: Marco de pruebas automatizadas estándar para verificar unitariamente la validez del software.',
    'while': 'while: Bucle que repite un bloque de código continuamente mientras su condición lógica permanezca verdadera.',
    'with': 'with: Estructura para gestión segura de recursos del sistema mediante administradores de contexto.',
}
''')

print("Curriculum written successfully to", output_path)
