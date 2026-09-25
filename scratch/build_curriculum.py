# -*- coding: utf-8 -*-
"""
Script generador del currículo de 32 capítulos para Aprendizaje de Python con NVDA.
Garantiza que el paso 3 (desafío) no tenga la respuesta escrita en el editor, sino un área de trabajo
con comentarios guía donde el estudiante realmente debe escribir la solución para superar el reto.
"""

def generate():
    chapters = []

    # 1
    chapters.append({
        "id": 1,
        "titulo": "Capítulo 1: Pensamiento Computacional y Algoritmos Cotidianos",
        "resumen": "¿Qué es pensar como un programador? Descubre qué es un algoritmo a través de secuencias de pasos de la vida cotidiana.",
        "pasos": [
            {
                "titulo": "Paso 1: Fundamento: ¿Qué es un algoritmo?",
                "tipo": "observar",
                "instruccion": "Un algoritmo es una serie ordenada y finita de pasos lógicos para resolver un problema o lograr una meta. En la vida diaria seguimos algoritmos al cocinar o cruzar la calle. En programación, la computadora no improvisa: ejecuta estrictamente la secuencia que le ordenas. Pulsa Control + Enter para escuchar este primer algoritmo.",
                "codigo": "print('Paso 1: Llenar la tetera con agua.')\nprint('Paso 2: Calentar el agua hasta hervir.')\nprint('Paso 3: Servir en una taza con infusión.')\nprint('¡Algoritmo completado!')",
                "pistas": ["Pulsa Control + Enter para ejecutar."],
                "validar": lambda src, res, ns: 'algoritmo' in res.lower()
            },
            {
                "titulo": "Paso 2: Observación: La importancia del orden",
                "tipo": "experimentar",
                "instruccion": "Si alteramos el orden de las instrucciones, el resultado final no tendrá sentido. Añade entre el paso 1 y el paso 2 la línea: print('Paso intermedio: Colocar la bolsita de té.') y pulsa Control + Enter.",
                "codigo": "print('Paso 1: Calentar el agua.')\n# Escribe aquí la línea intermedia con print:\n\nprint('Paso 2: Servir el agua caliente en la taza.')",
                "pistas": ["Escribe print('Paso intermedio: Colocar la bolsita de té.') entre las dos líneas existentes."],
                "validar": lambda src, res, ns: 'bolsita' in res.lower() and 'servir' in res.lower()
            },
            {
                "titulo": "Paso 3: Reto Práctico: Algoritmo de lavado de manos",
                "tipo": "desafio",
                "instruccion": "Escribe un algoritmo de 3 pasos para lavarse las manos usando tres instrucciones print(): 1. 'Abrir el grifo y mojar las manos', 2. 'Aplicar jabón y frotar', 3. 'Enjuagar y secar'. Ejecuta con Control + Enter para comprobar.",
                "codigo": "# Escribe aquí las 3 instrucciones print() para cada paso:\n# 1. Abrir el grifo y mojar las manos\n# 2. Aplicar jabón y frotar\n# 3. Enjuagar y secar\n\n",
                "salida_esperada": "1. Abrir el grifo y mojar las manos\n2. Aplicar jabón y frotar\n3. Enjuagar y secar",
                "pistas": ["Usa tres instrucciones print independientes, cada una con el texto entre comillas.", "Ejemplo: print('1. Abrir el grifo y mojar las manos')"],
                "validar": lambda src, res, ns: ('jabón' in res.lower() or 'jabon' in res.lower()) and 'grifo' in res.lower()
            },
            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Cuál es la definición más exacta de un algoritmo?\n\nOpciones:\n1. Un componente físico de la computadora como el procesador.\n2. Una serie ordenada y finita de instrucciones lógicas para resolver un problema.\n3. Un virus informático que altera los programas.\n\nEscribe el número de tu opción (1, 2 o 3) en el editor y pulsa Control + Enter.",
                "codigo": "# Escribe aquí tu respuesta (1, 2 o 3):\n",
                "pregunta": "¿Cuál es la definición más exacta de un algoritmo?",
                "opciones": [
                    "Un componente físico de la computadora como el procesador.",
                    "Una serie ordenada y finita de instrucciones lógicas para resolver un problema.",
                    "Un virus informático que altera los programas."
                ],
                "correcta": 1,
                "explicacion": "Un algoritmo es la secuencia lógica y paso a paso que describe la solución a un problema determinado.",
                "pistas": ["Recuerda el ejemplo de la preparación del té."],
                "validar": lambda src, res, ns: '2' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            }
        ]
    })

    # 2
    chapters.append({
        "id": 2,
        "titulo": "Capítulo 2: Arquitectura Básica: Entrada, Proceso, Memoria y Salida",
        "resumen": "Comprende cómo viaja la información dentro de un computador: periféricos de entrada, memoria RAM, procesador y canales de salida.",
        "pasos": [
            {
                "titulo": "Paso 1: Fundamento: El ciclo Entrada-Proceso-Salida",
                "tipo": "observar",
                "instruccion": "Todo programa informático sigue este ciclo: Entrada (teclado), Memoria RAM (donde residen variables temporales), Procesador CPU (donde se hacen cálculos) y Salida (pantalla y lector de voz). Ejecuta el código para observar este flujo en acción.",
                "codigo": "# Entrada y Memoria:\nherramienta = 'NVDA'\n# Procesamiento:\nmensaje = 'Entorno accesible asistido por: ' + herramienta\n# Salida:\nprint(mensaje)",
                "pistas": ["Pulsa Control + Enter para ver la salida."],
                "validar": lambda src, res, ns: 'nvda' in res.lower()
            },
            {
                "titulo": "Paso 2: Observación: La memoria es modificable",
                "tipo": "experimentar",
                "instruccion": "En la memoria RAM podemos reemplazar el contenido de una variable en cualquier instante. Observa cómo cambia la variable 'estado' y ejecuta con Control + Enter.",
                "codigo": "estado = 'Cargando datos'\nprint('Estado inicial:', estado)\n# Cambia aquí el valor de estado a 'Listo para programar':\nestado = 'Listo para programar'\nprint('Estado final:', estado)",
                "pistas": ["Ejecuta con Control + Enter para escuchar los dos estados secuenciales."],
                "validar": lambda src, res, ns: 'inicial' in res.lower() and 'final' in res.lower()
            },
            {
                "titulo": "Paso 3: Reto Práctico: Variables y salida",
                "tipo": "desafio",
                "instruccion": "Crea una variable llamada 'usuario' con el texto 'Estudiante' y muestra en consola usando print: Bienvenido/a, Estudiante. Ejecuta con Control + Enter.",
                "codigo": "# 1. Crea la variable usuario con el valor 'Estudiante'\n# 2. Usa print('Bienvenido/a,', usuario) para mostrar el saludo\n\n",
                "salida_esperada": "Bienvenido/a, Estudiante",
                "pistas": ["Escribe usuario = 'Estudiante' en el primer renglón y luego print('Bienvenido/a,', usuario)."],
                "validar": lambda src, res, ns: 'bienvenido' in res.lower() and 'estudiante' in res.lower()
            },
            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Dónde se almacenan las variables mientras tu script de Python se está ejecutando?\n\nOpciones:\n1. En la Memoria RAM del equipo.\n2. En la tecla Escape del teclado.\n3. En el cable de corriente.\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí tu respuesta (1, 2 o 3):\n",
                "pregunta": "¿Dónde se almacenan las variables mientras tu script de Python se está ejecutando?",
                "opciones": ["En la Memoria RAM del equipo.", "En la tecla Escape del teclado.", "En el cable de corriente."],
                "correcta": 0,
                "explicacion": "La Memoria RAM es el espacio de trabajo rápido donde residen los datos activos de los programas en ejecución.",
                "pistas": ["Es la memoria principal de acceso aleatorio."],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            }
        ]
    })

    # 3
    chapters.append({
        "id": 3,
        "titulo": "Capítulo 3: Lógica Booleana: Verdadero, Falso y Decisiones",
        "resumen": "Aprende el fundamento binario de toda decisión digital: los valores True y False y los operadores lógicos and, or y not.",
        "pasos": [
            {
                "titulo": "Paso 1: Fundamento: Proposiciones booleanas",
                "tipo": "observar",
                "instruccion": "Una proposición booleana solo puede evaluarse como Verdadera (True) o Falsa (False). Por ejemplo: 10 > 5 es True, mientras que 2 > 8 es False. Ejecuta el código para escuchar estas evaluaciones.",
                "codigo": "print('¿10 es mayor que 5?:', 10 > 5)\nprint('¿2 es mayor que 8?:', 2 > 8)",
                "pistas": ["Pulsa Control + Enter para escuchar True y False."],
                "validar": lambda src, res, ns: 'true' in res.lower() and 'false' in res.lower()
            },
            {
                "titulo": "Paso 2: Observación: Operadores and, or y not",
                "tipo": "experimentar",
                "instruccion": "El operador 'and' exige que ambas condiciones sean verdaderas. El operador 'or' solo requiere que al menos una lo sea. Ejecuta el código y analiza el resultado.",
                "codigo": "llave = True\nclave = False\nprint('¿Puede entrar con llave O clave?:', llave or clave)\nprint('¿Cumple llave Y clave?:', llave and clave)",
                "pistas": ["Observa cómo or devuelve True pero and devuelve False."],
                "validar": lambda src, res, ns: 'true' in res.lower() and 'false' in res.lower()
            },
            {
                "titulo": "Paso 3: Reto Práctico: Verificación de acceso",
                "tipo": "desafio",
                "instruccion": "Crea una variable llamada 'edad' con el valor 20 y una variable 'tiene_identificacion' con True. Luego crea 'autorizado = (edad >= 18) and tiene_identificacion'. Imprime print('Acceso permitido:', autorizado).",
                "codigo": "# 1. Crea la variable edad con 20\n# 2. Crea tiene_identificacion con True\n# 3. Crea autorizado = (edad >= 18) and tiene_identificacion\n# 4. Muestra: print('Acceso permitido:', autorizado)\n\n",
                "salida_esperada": "Acceso permitido: True",
                "pistas": ["Une ambas condiciones con el operador and."],
                "validar": lambda src, res, ns: 'true' in res.lower() and 'acceso' in res.lower()
            },
            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué resultado produce la expresión booleana: not False?\n\nOpciones:\n1. True\n2. False\n3. None\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí tu respuesta (1, 2 o 3):\n",
                "pregunta": "¿Qué resultado produce la expresión booleana: not False?",
                "opciones": ["True", "False", "None"],
                "correcta": 0,
                "explicacion": "El operador 'not' invierte el valor lógico: si niegas False obtienes True.",
                "pistas": ["not es el operador de negación inversa."],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            }
        ]
    })

    # 4
    chapters.append({
        "id": 4,
        "titulo": "Capítulo 4: Nuestra Primera Instrucción: La Función print()",
        "resumen": "Aprende a emitir información hacia la salida estándar y escucharla en tu lector de pantalla.",
        "pasos": [
            {
                "titulo": "Paso 1: Fundamento: La función print()",
                "tipo": "observar",
                "instruccion": "La función print() envía mensajes a la salida para que el lector de pantalla los verbalice. El texto siempre debe ir rodeado por comillas simples o dobles. Pulsa Control + Enter para escuchar este saludo inicial.",
                "codigo": "print('¡Hola mundo desde Python accesible!')",
                "pistas": ["Pulsa Control + Enter para ejecutar."],
                "validar": lambda src, res, ns: 'hola mundo' in res.lower()
            },
            {
                "titulo": "Paso 2: Observación: Varios argumentos separados por coma",
                "tipo": "experimentar",
                "instruccion": "print() puede recibir varios textos separados por comas. Python insertará automáticamente un espacio entre cada uno. Cambia algún texto o añade uno nuevo y pulsa Control + Enter.",
                "codigo": "print('Python', 'es', 'fácil', 'y', 'accesible')",
                "pistas": ["Modifica o agrega un argumento entre comillas."],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": "Paso 3: Reto Práctico: Tu propio saludo",
                "tipo": "desafio",
                "instruccion": "Escribe una instrucción print() que muestre exactamente el mensaje: 'Aprendiendo Python con NVDA'. Pulsa Control + Enter para validar.",
                "codigo": "# Escribe aquí tu instrucción print() con el mensaje indicado:\n\n",
                "salida_esperada": "Aprendiendo Python con NVDA",
                "pistas": ["Escribe: print('Aprendiendo Python con NVDA') respetando las comillas y los paréntesis."],
                "validar": lambda src, res, ns: 'aprendiendo python con nvda' in res.lower()
            },
            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué función se utiliza en Python para enviar datos a la salida y lector de pantalla?\n\nOpciones:\n1. print()\n2. input()\n3. exit()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí tu respuesta (1, 2 o 3):\n",
                "pregunta": "¿Qué función se utiliza en Python para enviar datos a la salida y lector?",
                "opciones": ["print()", "input()", "exit()"],
                "correcta": 0,
                "explicacion": "print() es la función de salida estándar por excelencia.",
                "pistas": ["Lee detenidamente las 3 opciones."],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            }
        ]
    })

    # 5
    chapters.append({
        "id": 5,
        "titulo": "Capítulo 5: Almacenamiento en Memoria: Variables y Asignación",
        "resumen": "Aprende a guardar valores en memoria asignándoles un nombre con el signo igual (=).",
        "pasos": [
            {
                "titulo": "Paso 1: Fundamento: Crear y asignar variables",
                "tipo": "observar",
                "instruccion": "Una variable es un nombre que apunta a un dato guardado en la memoria. Se usa el signo igual (=) para asignar. Ejecuta el código para observar cómo se combinan texto y números.",
                "codigo": "nombre = 'Kevin'\nedad = 25\nprint(nombre, 'tiene', edad, 'años')",
                "pistas": ["Pulsa Control + Enter para ejecutar."],
                "validar": lambda src, res, ns: 'años' in res.lower() or 'anos' in res.lower()
            },
            {
                "titulo": "Paso 2: Observación: Actualizar el valor de una variable",
                "tipo": "experimentar",
                "instruccion": "Podemos sumar puntos a una variable existente y reasignarla. Cambia el valor que se suma (50) por otro número y pulsa Control + Enter.",
                "codigo": "puntos = 100\nprint('Puntuación inicial:', puntos)\npuntos = puntos + 50\nprint('Puntuación acumulada:', puntos)",
                "pistas": ["Modifica el número 50 por el valor que prefieras y ejecuta."],
                "validar": lambda src, res, ns: 'acumulada' in res.lower()
            },
            {
                "titulo": "Paso 3: Reto Práctico: Variable de lenguaje",
                "tipo": "desafio",
                "instruccion": "Crea una variable llamada 'lenguaje' con el texto 'Python' y luego muestra en consola: print('Estoy programando en:', lenguaje). Pulsa Control + Enter.",
                "codigo": "# 1. Crea la variable lenguaje = 'Python'\n# 2. Imprime: print('Estoy programando en:', lenguaje)\n\n",
                "salida_esperada": "Estoy programando en: Python",
                "pistas": ["Asigna lenguaje = 'Python' y luego pásala a print."],
                "validar": lambda src, res, ns: 'programando en' in res.lower() and 'python' in res.lower()
            },
            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué símbolo se usa en Python para asignar un valor a una variable?\n\nOpciones:\n1. El signo igual (=)\n2. El signo de suma (+)\n3. El punto y coma (;)\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí tu respuesta (1, 2 o 3):\n",
                "pregunta": "¿Qué símbolo se usa en Python para asignar un valor a una variable?",
                "opciones": ["El signo igual (=)", "El signo de suma (+)", "El punto y coma (;)"],
                "correcta": 0,
                "explicacion": "El signo igual simple (=) asigna lo que está a la derecha en la variable de la izquierda.",
                "pistas": ["El operador de asignación es =."],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            }
        ]
    })

    # 6
    chapters.append({
        "id": 6,
        "titulo": "Capítulo 6: Tipos de Datos Primitivos: Números Enteros y Decimales",
        "resumen": "Opera con números enteros (int) y números decimales (float) realizando cálculos matemáticos.",
        "pasos": [
            {
                "titulo": "Paso 1: Fundamento: Enteros (int) y Decimales (float)",
                "tipo": "observar",
                "instruccion": "En Python, los números sin punto son enteros (int) y los que tienen punto decimal son flotantes (float). Ejecuta el código para observar cómo se multiplican.",
                "codigo": "precio = 19.50\ncantidad = 3\ntotal = precio * cantidad\nprint('Total a pagar:', total)",
                "pistas": ["Pulsa Control + Enter para ver la multiplicación."],
                "validar": lambda src, res, ns: 'total a pagar' in res.lower()
            },
            {
                "titulo": "Paso 2: Observación: Operaciones con decimales",
                "tipo": "experimentar",
                "instruccion": "El operador ** calcula potencias (radio al cuadrado). Cambia el valor del radio a 5 y pulsa Control + Enter para ver cómo cambia el área.",
                "codigo": "radio = 4\npi = 3.1416\narea = pi * (radio ** 2)\nprint('Área del círculo:', round(area, 2))",
                "pistas": ["Cambia radio = 4 por radio = 5."],
                "validar": lambda src, res, ns: 'círculo' in res.lower() or 'circulo' in res.lower()
            },
            {
                "titulo": "Paso 3: Reto Práctico: Cálculo de área de triángulo",
                "tipo": "desafio",
                "instruccion": "Crea las variables base = 10 y altura = 5. Calcula area = (base * altura) / 2 e imprime: print('Área del triángulo:', area). Ejecuta con Control + Enter.",
                "codigo": "# 1. Define base = 10 y altura = 5\n# 2. Calcula area = (base * altura) / 2\n# 3. Imprime: print('Área del triángulo:', area)\n\n",
                "salida_esperada": "Área del triángulo: 25.0",
                "pistas": ["Recuerda usar la barra inclinada / para la división."],
                "validar": lambda src, res, ns: '25' in res and ('triángulo' in res.lower() or 'triangulo' in res.lower())
            },
            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Cómo se denomina en Python al tipo de dato numérico que tiene parte decimal?\n\nOpciones:\n1. float\n2. int\n3. bool\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí tu respuesta (1, 2 o 3):\n",
                "pregunta": "¿Cómo se denomina en Python a un número con parte decimal?",
                "opciones": ["float", "int", "bool"],
                "correcta": 0,
                "explicacion": "float representa números de coma flotante (decimales).",
                "pistas": ["Viene del inglés 'floating point'."],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            }
        ]
    })

    # 7
    chapters.append({
        "id": 7,
        "titulo": "Capítulo 7: Cadenas de Texto (Strings): Comillas y Concatenación",
        "resumen": "Manipula texto en Python usando comillas simples, dobles y cadenas formateadas modernas (f-strings).",
        "pasos": [
            {
                "titulo": "Paso 1: Fundamento: Concatenación con + y f-strings",
                "tipo": "observar",
                "instruccion": "Las cadenas de texto (str) pueden unirse con el operador + o usando f-strings colocando una 'f' antes de las comillas e insertando variables entre llaves {}. Ejecuta para ver ambos métodos.",
                "codigo": "nombre = 'Laura'\nsaludo = f'Hola {nombre}, bienvenida a Python.'\nprint(saludo)",
                "pistas": ["Pulsa Control + Enter para ver la interpolación de texto."],
                "validar": lambda src, res, ns: 'laura' in res.lower()
            },
            {
                "titulo": "Paso 2: Observación: Repetición de texto con *",
                "tipo": "experimentar",
                "instruccion": "Al multiplicar un texto por un número, Python lo repite. Cambia el multiplicador 3 por 5 y pulsa Control + Enter.",
                "codigo": "aplauso = '¡Bravo! '\nprint(aplauso * 3)",
                "pistas": ["Cambia * 3 por * 5."],
                "validar": lambda src, res, ns: 'bravo' in res.lower()
            },
            {
                "titulo": "Paso 3: Reto Práctico: Crear una f-string",
                "tipo": "desafio",
                "instruccion": "Crea una variable ciudad = 'Bogotá' y pais = 'Colombia'. Usa una f-string para imprimir exactamente: print(f'Ubicación: {ciudad}, {pais}').",
                "codigo": "# 1. Define ciudad = 'Bogotá' y pais = 'Colombia'\n# 2. Imprime usando f-string: print(f'Ubicación: {ciudad}, {pais}')\n\n",
                "salida_esperada": "Ubicación: Bogotá, Colombia",
                "pistas": ["Coloca f antes de las comillas y las variables dentro de {ciudad} y {pais}."],
                "validar": lambda src, res, ns: 'bogot' in res.lower() and 'colombia' in res.lower()
            },
            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué letra precede a las comillas para crear una cadena formateada moderna en Python?\n\nOpciones:\n1. La letra f\n2. La letra p\n3. La letra s\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí tu respuesta (1, 2 o 3):\n",
                "pregunta": "¿Qué letra precede a las comillas para crear una f-string?",
                "opciones": ["La letra f", "La letra p", "La letra s"],
                "correcta": 0,
                "explicacion": "La letra f convierte una cadena en una f-string (cadena formateada).",
                "pistas": ["f viene de 'format'."],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            }
        ]
    })

    # 8
    chapters.append({
        "id": 8,
        "titulo": "Capítulo 8: Interacción con el Usuario: Entrada con input()",
        "resumen": "Aprende a capturar datos que el usuario escribe por teclado y a transformarlos con int() o float().",
        "pasos": [
            {
                "titulo": "Paso 1: Fundamento: La función input()",
                "tipo": "observar",
                "instruccion": "input() permite recibir datos del usuario. Recuerda que input() SIEMPRE devuelve una cadena de texto (str). Si necesitas hacer cálculos matemáticos, debes convertirlo con int(). Ejecuta para observar la conversión.",
                "codigo": "edad_texto = '25'\nedad_numero = int(edad_texto)\nprint('Edad numérica convertida:', edad_numero)\nprint('El doble de tu edad es:', edad_numero * 2)",
                "pistas": ["Pulsa Control + Enter para ver la conversión."],
                "validar": lambda src, res, ns: '50' in res
            },
            {
                "titulo": "Paso 2: Observación: input con mensaje",
                "tipo": "experimentar",
                "instruccion": "Observa cómo se le pasa un texto informativo a input(). Modifica el mensaje dentro de input y pulsa Control + Enter.",
                "codigo": "nombre = 'Ana'\nprint(f'¡Hola {nombre}! Bienvenido/a al aprendizaje interactivo.')",
                "pistas": ["Cambia 'Ana' por tu propio nombre."],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": "Paso 3: Reto Práctico: Conversión y cálculo",
                "tipo": "desafio",
                "instruccion": "Tienes la variable edad_texto = '20'. Conviértela a entero usando int(edad_texto) y guarda el resultado en 'edad'. Luego muestra: print('El próximo año tendrás:', edad + 1).",
                "codigo": "edad_texto = '20'\n# 1. Convierte edad_texto a entero: edad = int(edad_texto)\n# 2. Imprime: print('El próximo año tendrás:', edad + 1)\n\n",
                "salida_esperada": "El próximo año tendrás: 21",
                "pistas": ["Usa int(edad_texto) para la conversión."],
                "validar": lambda src, res, ns: '21' in res and 'tendrás' in res.lower() or 'tendras' in res.lower()
            },
            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué tipo de dato devuelve por defecto la función input() de Python?\n\nOpciones:\n1. Siempre una cadena de texto (str)\n2. Un número entero (int)\n3. Un booleano (bool)\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí tu respuesta (1, 2 o 3):\n",
                "pregunta": "¿Qué tipo de dato devuelve por defecto input()?",
                "opciones": ["Siempre una cadena de texto (str)", "Un número entero (int)", "Un booleano (bool)"],
                "correcta": 0,
                "explicacion": "input() siempre retorna una cadena (str), por eso se requiere int() o float() para operar numéricamente.",
                "pistas": ["Todo lo que entra por teclado se lee inicialmente como texto."],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            }
        ]
    })

    # For chapters 9 to 32, we create tailored, high quality definitions
    # Let's add them cleanly:
    # 9: Operadores de Comparación
    chapters.append({
        "id": 9,
        "titulo": "Capítulo 9: Operadores de Comparación y Expresiones Condicionales",
        "resumen": "Compara valores usando >, <, >=, <=, == y != para tomar decisiones en tus programas.",
        "pasos": [
            {
                "titulo": "Paso 1: Fundamento: Operadores relacionales",
                "tipo": "observar",
                "instruccion": "Los operadores relacionales comparan dos valores: > (mayor), < (menor), >= (mayor o igual), <= (menor o igual), == (igual) y != (distinto). Ejecuta para observar sus resultados booleanos.",
                "codigo": "x = 15\ny = 20\nprint('¿x es menor que y?:', x < y)\nprint('¿x es igual a y?:', x == y)\nprint('¿x es distinto de y?:', x != y)",
                "pistas": ["Pulsa Control + Enter."],
                "validar": lambda src, res, ns: 'true' in res.lower() and 'false' in res.lower()
            },
            {
                "titulo": "Paso 2: Observación: Comparar textos",
                "tipo": "experimentar",
                "instruccion": "También puedes comparar textos con ==. Si cambias el texto para que coincidan exactamente, el resultado cambiará a True. Modifica y ejecuta.",
                "codigo": "clave_ingresada = 'secreta'\nclave_real = 'secreta'\nprint('¿Clave correcta?:', clave_ingresada == clave_real)",
                "pistas": ["Cambia una de las cadenas para que no coincidan o mantenlas iguales."],
                "validar": lambda src, res, ns: 'clave correcta' in res.lower()
            },
            {
                "titulo": "Paso 3: Reto Práctico: Nota de aprobación",
                "tipo": "desafio",
                "instruccion": "Crea una variable puntos = 85. Imprime en consola: print('¿Aprobó con 70 o más?:', puntos >= 70). Pulsa Control + Enter.",
                "codigo": "# 1. Define puntos = 85\n# 2. Imprime: print('¿Aprobó con 70 o más?:', puntos >= 70)\n\n",
                "salida_esperada": "¿Aprobó con 70 o más?: True",
                "pistas": ["Usa el operador >= (mayor o igual)."],
                "validar": lambda src, res, ns: '70' in res and 'true' in res.lower()
            },
            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué operador se utiliza en Python para comparar si dos valores son exactamente iguales?\n\nOpciones:\n1. Doble signo igual (==)\n2. Un solo signo igual (=)\n3. Signo de admiración (!)\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí tu respuesta (1, 2 o 3):\n",
                "pregunta": "¿Qué operador compara si dos valores son iguales?",
                "opciones": ["Doble signo igual (==)", "Un solo signo igual (=)", "Signo de admiración (!)"],
                "correcta": 0,
                "explicacion": "El doble signo igual (==) compara igualdad. El signo simple (=) asigna valores.",
                "pistas": ["No confundir asignación (=) con comparación."],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            }
        ]
    })

    # 10: Bifurcación Básica: Estructura if y Sangría PEP 8
    chapters.append({
        "id": 10,
        "titulo": "Capítulo 10: Bifurcación Básica: Estructura if y Sangría PEP 8",
        "resumen": "Ejecuta bloques de código bajo condición usando if y 4 espacios de sangría obligatoria.",
        "pasos": [
            {
                "titulo": "Paso 1: Fundamento: La sentencia if y los 4 espacios",
                "tipo": "observar",
                "instruccion": "La sentencia if evalúa una condición terminando con dos puntos (:). Las líneas subordinadas deben llevar 4 espacios de sangría (tecla Tab). Ejecuta el código para observar cómo se cumple la condición.",
                "codigo": "temperatura = 30\nif temperatura > 25:\n    print('Hace calor, enciende el ventilador.')\nprint('Fin del análisis.')",
                "pistas": ["Pulsa Control + Enter."],
                "validar": lambda src, res, ns: 'hace calor' in res.lower()
            },
            {
                "titulo": "Paso 2: Observación: Cuando la condición no se cumple",
                "tipo": "experimentar",
                "instruccion": "Si la condición es False, el bloque indentado no se ejecuta. Cambia temperatura a 15 y ejecuta con Control + Enter para escuchar cómo se salta el bloque.",
                "codigo": "temperatura = 15\nif temperatura > 25:\n    print('Hace calor.')\nprint('Fin del análisis de temperatura.')",
                "pistas": ["Cambia temperatura = 15 y ejecuta."],
                "validar": lambda src, res, ns: 'fin del análisis' in res.lower() or 'fin del analisis' in res.lower()
            },
            {
                "titulo": "Paso 3: Reto Práctico: Saludo horario con if",
                "tipo": "desafio",
                "instruccion": "Crea una variable hora = 14. Escribe un bloque if que compruebe si hora >= 12, y dentro imprima con 4 espacios de sangría: print('Buenas tardes').",
                "codigo": "# 1. Define hora = 14\n# 2. Escribe if hora >= 12:\n# 3. Con 4 espacios: print('Buenas tardes')\n\n",
                "salida_esperada": "Buenas tardes",
                "pistas": ["No olvides los dos puntos (:) al final de la línea if.", "Usa 4 espacios o pulsa Tab para la indentación."],
                "validar": lambda src, res, ns: 'buenas tardes' in res.lower() and 'if ' in src
            },
            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Cuántos espacios en blanco recomienda el estándar oficial PEP 8 para cada nivel de sangría en Python?\n\nOpciones:\n1. 4 espacios\n2. 1 espacio\n3. 10 espacios\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí tu respuesta (1, 2 o 3):\n",
                "pregunta": "¿Cuántos espacios recomienda PEP 8 para la sangría?",
                "opciones": ["4 espacios", "1 espacio", "10 espacios"],
                "correcta": 0,
                "explicacion": "PEP 8 establece un estándar de 4 espacios por cada nivel de sangría.",
                "pistas": ["Es el estándar universal de Python."],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            }
        ]
    })

    # Write all 32 chapters into a structured py file
    # We will build chapters 11 to 32 programmatically with exact pedagogical content
    titles_11_32 = [
        (11, "Alternativas Múltiples: Bloques elif y else", "Maneja múltiples caminos posibles encadenando condiciones con elif y un caso por defecto con else."),
        (12, "Colecciones Ordenadas: Introducción a las Listas", "Guarda múltiples elementos en una secuencia ordenada usando corchetes [] y accede mediante índices."),
        (13, "Métodos Fundamentales de Listas (append, remove, pop, len)", "Añade, elimina y cuenta elementos en listas dinámicas de Python."),
        (14, "Repetición y Automatización: El Bucle for y range()", "Automatiza tareas repetitivas recorriendo secuencias numéricas y listas con for."),
        (15, "Repetición Condicional: El Bucle while", "Ejecuta bloques repetidamente mientras se mantenga una condición booleana."),
        (16, "Colecciones Clave-Valor: Diccionarios en Python", "Asocia pares de información mediante llaves {} con claves y valores."),
        (17, "Tuplas y Conjuntos (Sets): Inmutabilidad y Únicos", "Usa tuplas para datos fijos que no cambian y conjuntos para colecciones sin duplicados."),
        (18, "Funciones Propias: Declaración con def y Parámetros", "Empaqueta instrucciones reutilizables asignándoles un nombre propio con def."),
        (19, "Retorno de Resultados: La Sentencia return y Ámbito", "Devuelve valores calculados al código que llamó a la función y entiende el alcance local de las variables."),
        (20, "Manejo Profesional de Errores: try, except y finally", "Evita que tu programa se detenga ante errores inesperados capturando excepciones."),
        (21, "Decodificación de Tracebacks y Diagnóstico de Fallos", "Aprende a leer el informe de error de Python para ubicar la línea y causa exacta del fallo."),
        (22, "Entrada y Salida de Archivos: with open() para Texto", "Guarda y lee información en ficheros del disco duro de forma segura con with open()."),
        (23, "Paradigma de Objetos: Clases, Instancias y Atributos", "Crea moldes del mundo real agrupando datos y comportamientos en clases."),
        (24, "El Constructor __init__ y el Parámetro self", "Inicializa objetos con valores específicos en el momento exacto de su creación."),
        (25, "Métodos de Instancia y Encapsulamiento", "Define acciones que cada objeto sabe realizar de forma autónoma."),
        (26, "Herencia de Clases: Reutilización con super()", "Crea clases hijas especializadas que heredan propiedades de una clase padre."),
        (27, "Polimorfismo y Métodos Especiales (__str__)", "Personaliza cómo el lector de pantalla y print leen tus objetos implementando __str__."),
        (28, "Módulos de la Biblioteca Estándar (math, random, datetime)", "Aprovecha librerías integradas de Python para matemáticas, azar y fechas sin instalar nada."),
        (29, "Persistencia Estructurada: Formato JSON y Serialización", "Guarda y lee diccionarios estructurados en formato de texto estándar JSON."),
        (30, "Bases de Datos Relacionales con SQLite: Tablas y Consultas", "Gestiona datos organizados en tablas usando SQL integrado y el módulo sqlite3."),
        (31, "Consumo de Servicios Web: Peticiones HTTP y Respuestas JSON", "Comunícate con servidores en internet para obtener datos actualizados."),
        (32, "Calidad de Software: Pruebas Unitarias con unittest", "Verifica automáticamente que cada parte de tu código funcione como se espera sin errores.")
    ]

    # Specific challenges and validation for chapters 11 to 32
    details = {
        11: {
            "p1_code": "nota = 7\nif nota >= 9:\n    print('Excelente')\nelif nota >= 5:\n    print('Aprobado')\nelse:\n    print('Reprobado')",
            "p2_code": "nota = 4\nif nota >= 9:\n    print('Excelente')\nelif nota >= 5:\n    print('Aprobado')\nelse:\n    print('Reprobado')",
            "p3_instr": "Crea una variable nota = 8. Escribe if nota >= 9 imprima 'Excelente', elif nota >= 5 imprima 'Aprobado', y else imprima 'Reprobado'.",
            "p3_start": "# 1. Define nota = 8\n# 2. Escribe la estructura if, elif y else:\n\n",
            "p3_val": lambda src, res, ns: 'aprobado' in res.lower() and 'elif' in src,
            "q_preg": "¿Qué bloque condicional se ejecuta si ninguna condición anterior fue verdadera?",
            "q_ops": ["El bloque else", "El bloque if", "El bloque while"],
            "q_corr": 0,
            "q_exp": "else se ejecuta como camino por defecto cuando todo lo anterior fue falso."
        },
        12: {
            "p1_code": "frutas = ['manzana', 'pera', 'plátano']\nprint('Primera fruta:', frutas[0])\nprint('Segunda fruta:', frutas[1])",
            "p2_code": "frutas = ['manzana', 'pera', 'plátano']\n# Modifica el elemento en la posición 0:\nfrutas[0] = 'fresa'\nprint('Lista actualizada:', frutas)",
            "p3_instr": "Crea una lista llamada 'compras' con 'pan', 'leche' y 'huevos'. Imprime el primer elemento usando compras[0].",
            "p3_start": "# 1. Crea la lista compras con 'pan', 'leche' y 'huevos'\n# 2. Imprime el primer elemento con print(compras[0])\n\n",
            "p3_val": lambda src, res, ns: 'pan' in res.lower() and 'compras' in src,
            "q_preg": "¿Cuál es el índice del primer elemento de una lista en Python?",
            "q_ops": ["El índice 0", "El índice 1", "El índice -1"],
            "q_corr": 0,
            "q_exp": "En Python la indexación empieza siempre en base cero (0)."
        },
        13: {
            "p1_code": "tareas = ['leer', 'programar']\ntareas.append('descansar')\nprint('Tareas totales:', len(tareas))\nprint('Lista:', tareas)",
            "p2_code": "tareas = ['leer', 'programar', 'descansar']\ntareas.remove('leer')\nprint('Después de borrar leer:', tareas)",
            "p3_instr": "Crea una lista colores = ['rojo', 'verde']. Agrega 'azul' con append() y muestra la cantidad total con print('Total colores:', len(colores)).",
            "p3_start": "colores = ['rojo', 'verde']\n# 1. Usa colores.append('azul')\n# 2. Imprime: print('Total colores:', len(colores))\n\n",
            "p3_val": lambda src, res, ns: '3' in res and 'colores' in src,
            "q_preg": "¿Qué método agrega un nuevo elemento al final de una lista?",
            "q_ops": ["append()", "delete()", "add()"],
            "q_corr": 0,
            "q_exp": "append() añade un nuevo elemento al final de la lista."
        },
        14: {
            "p1_code": "for i in range(1, 4):\n    print('Número:', i)\nprint('Fin del bucle')",
            "p2_code": "animales = ['perro', 'gato', 'loro']\nfor animal in animales:\n    print('Mascota:', animal)",
            "p3_instr": "Escribe un bucle for que recorra range(1, 6) e imprima cada número: print('Contando:', numero).",
            "p3_start": "# Escribe aquí el bucle for sobre range(1, 6):\n\n",
            "p3_val": lambda src, res, ns: '5' in res and 'for ' in src,
            "q_preg": "¿Qué produce la función range(1, 5) en un bucle for?",
            "q_ops": ["Los números del 1 al 4", "Los números del 1 al 5", "Una lista vacía"],
            "q_corr": 0,
            "q_exp": "range(inicio, fin) llega hasta fin - 1."
        },
        15: {
            "p1_code": "contador = 1\nwhile contador <= 3:\n    print('Vuelta:', contador)\n    contador = contador + 1\nprint('Bucle finalizado')",
            "p2_code": "energia = 3\nwhile energia > 0:\n    print('Energía restante:', energia)\n    energia = energia - 1",
            "p3_instr": "Crea una variable contador = 1. Escribe un bucle while que mientras contador <= 3 imprima print('Paso:', contador) y sume 1 a contador.",
            "p3_start": "contador = 1\n# Escribe el bucle while aquí con contador <= 3:\n\n",
            "p3_val": lambda src, res, ns: '3' in res and 'while ' in src,
            "q_preg": "¿Qué precaución crucial se debe tomar al programar un bucle while?",
            "q_ops": ["Asegurar que la condición cambie para evitar un bucle infinito", "Poner punto y coma al final", "Usar comillas triples"],
            "q_corr": 0,
            "q_exp": "Si la condición nunca se vuelve falsa, el bucle se ejecuta infinitamente bloqueando el programa."
        },
        16: {
            "p1_code": "contacto = {'nombre': 'Carlos', 'telefono': '555-1234'}\nprint('Nombre:', contacto['nombre'])\nprint('Teléfono:', contacto['telefono'])",
            "p2_code": "contacto = {'nombre': 'Carlos', 'telefono': '555-1234'}\ncontacto['ciudad'] = 'Madrid'\nprint('Diccionario ampliado:', contacto)",
            "p3_instr": "Crea un diccionario llamado 'precios' con 'manzana': 2 y 'pera': 3. Imprime: print('Precio manzana:', precios['manzana']).",
            "p3_start": "# 1. Crea el diccionario precios con 'manzana': 2 y 'pera': 3\n# 2. Imprime: print('Precio manzana:', precios['manzana'])\n\n",
            "p3_val": lambda src, res, ns: '2' in res and 'precios' in src,
            "q_preg": "¿Qué delimitador se utiliza para declarar diccionarios en Python?",
            "q_ops": ["Llaves {}", "Corchetes []", "Paréntesis ()"],
            "q_corr": 0,
            "q_exp": "Los diccionarios se declaran entre llaves {} con pares clave: valor."
        },
        17: {
            "p1_code": "punto = (10, 20)\nprint('Coordenada X:', punto[0])\nprint('Coordenada Y:', punto[1])",
            "p2_code": "numeros = {1, 2, 2, 3, 3, 4}\nprint('Conjunto sin duplicados:', numeros)",
            "p3_instr": "Crea una tupla llamada 'coordenadas' con los valores (50, 100). Imprime: print('Coordenadas:', coordenadas).",
            "p3_start": "# 1. Crea la tupla coordenadas = (50, 100)\n# 2. Imprime: print('Coordenadas:', coordenadas)\n\n",
            "p3_val": lambda src, res, ns: '50' in res and '100' in res,
            "q_preg": "¿Cuál es la principal diferencia entre una tupla y una lista?",
            "q_ops": ["Las tuplas son inmutables (no se pueden modificar)", "Las tuplas no aceptan números", "Las tuplas solo tienen un elemento"],
            "q_corr": 0,
            "q_exp": "Las tuplas son inmutables una vez creadas, lo que garantiza la integridad de los datos."
        },
        18: {
            "p1_code": "def saludar(nombre):\n    print(f'¡Hola, {nombre}! Bienvenido a las funciones.')\n\nsaludar('Elena')\nsaludar('Marcos')",
            "p2_code": "def calcular_doble(num):\n    print('El doble es:', num * 2)\n\ncalcular_doble(8)",
            "p3_instr": "Define una función llamada 'sumar(a, b)' que imprima: print('Resultado:', a + b). Luego invócala con sumar(5, 7).",
            "p3_start": "# 1. Define def sumar(a, b):\n# 2. Dentro imprime: print('Resultado:', a + b)\n# 3. Invoca sumar(5, 7)\n\n",
            "p3_val": lambda src, res, ns: '12' in res and 'def sumar' in src,
            "q_preg": "¿Qué palabra clave se usa para definir una nueva función en Python?",
            "q_ops": ["def", "function", "fn"],
            "q_corr": 0,
            "q_exp": "La palabra clave 'def' (de define) declara una función."
        },
        19: {
            "p1_code": "def multiplicar(a, b):\n    return a * b\n\nresultado = multiplicar(4, 5)\nprint('Resultado obtenido con return:', resultado)",
            "p2_code": "def es_mayor_de_edad(edad):\n    return edad >= 18\n\nprint('¿Puede votar?:', es_mayor_de_edad(20))",
            "p3_instr": "Define una función 'cuadrado(n)' que retorne n * n usando return. Guarda cuadrado(6) en la variable 'res' e imprime: print('El cuadrado es:', res).",
            "p3_start": "# 1. Define def cuadrado(n): con return n * n\n# 2. Guarda res = cuadrado(6)\n# 3. Imprime: print('El cuadrado es:', res)\n\n",
            "p3_val": lambda src, res, ns: '36' in res and 'return' in src,
            "q_preg": "¿Qué sucede cuando una función ejecuta la instrucción return?",
            "q_ops": ["Finaliza la función y devuelve el valor procesado", "Imprime el valor en pantalla", "Reinicia la computadora"],
            "q_corr": 0,
            "q_exp": "return concluye la ejecución de la función y entrega el resultado a quien la llamó."
        },
        20: {
            "p1_code": "try:\n    divisor = 0\n    resultado = 10 / divisor\n    print(resultado)\nexcept ZeroDivisionError:\n    print('Aviso: No se puede dividir entre cero.')",
            "p2_code": "try:\n    numero = int('no_es_un_numero')\nexcept ValueError:\n    print('Aviso: El texto no pudo convertirse a número.')\nfinally:\n    print('Bloque finally completado.')",
            "p3_instr": "Escribe un bloque try donde dividas 20 entre 0, y en el except ZeroDivisionError imprime: print('Error capturado con éxito').",
            "p3_start": "# Escribe aquí el bloque try y except ZeroDivisionError:\n\n",
            "p3_val": lambda src, res, ns: 'error capturado' in res.lower() and 'except' in src,
            "q_preg": "¿Para qué sirve la cláusula except en Python?",
            "q_ops": ["Para capturar errores específicos y evitar que el programa se cierre", "Para crear bucles", "Para borrar archivos"],
            "q_corr": 0,
            "q_exp": "except intercepta la excepción permitiendo que el programa maneje la situación con elegancia."
        },
        21: {
            "p1_code": "# Un Traceback muestra el archivo, línea y tipo de error:\nprint('Analizando Traceback...')\n# TypeError ocurre al sumar tipos incompatibles:\ntipo_error = 'TypeError: unsupported operand type(s)'\nprint('Diagnóstico:', tipo_error)",
            "p2_code": "try:\n    lista = [1, 2]\n    print(lista[10])\nexcept IndexError as err:\n    print('Índice fuera de rango:', err)",
            "p3_instr": "Corrige el error en el código: convierte '5' a número con int() antes de sumar para que imprima: print('Suma correcta:', 10 + int('5')).",
            "p3_start": "# Corrige la suma convirtiendo '5' a int:\nnumero = 10\ntexto = '5'\n# Imprime: print('Suma correcta:', numero + int(texto))\n\n",
            "p3_val": lambda src, res, ns: '15' in res and 'suma correcta' in res.lower(),
            "q_preg": "¿Qué tecla rápida de Aprendizaje de Python con NVDA sitúa el cursor directamente en la línea del error del Traceback?",
            "q_ops": ["F4", "F1", "F12"],
            "q_corr": 0,
            "q_exp": "F4 salta inmediatamente a la línea del error en el editor y lee el diagnóstico."
        },
        22: {
            "p1_code": "# with open garantiza que el archivo se cierre al salir del bloque:\nwith open('saludo.txt', 'w', encoding='utf-8') as f:\n    f.write('¡Hola desde archivo persistente!')\nprint('Archivo escrito con éxito.')",
            "p2_code": "with open('saludo.txt', 'r', encoding='utf-8') as f:\n    contenido = f.read()\nprint('Contenido leído:', contenido)",
            "p3_instr": "Usa with open('mensaje.txt', 'w', encoding='utf-8') as f: y escribe f.write('Python accesible'). Luego imprime: print('Guardado listo').",
            "p3_start": "# Escribe el bloque with open('mensaje.txt', 'w', encoding='utf-8') as f:\n# Dentro escribe f.write('Python accesible')\n# Luego imprime: print('Guardado listo')\n\n",
            "p3_val": lambda src, res, ns: 'guardado listo' in res.lower() and 'with open' in src,
            "q_preg": "¿Por qué es recomendable usar 'with open()' al trabajar con archivos?",
            "q_ops": ["Porque cierra automáticamente el archivo incluso si ocurre un error", "Porque encripta los datos", "Porque no usa memoria"],
            "q_corr": 0,
            "q_exp": "with actúa como administrador de contexto asegurando la liberación de recursos."
        },
        23: {
            "p1_code": "class Libro:\n    titulo = 'Aprendizaje de Python'\n    paginas = 200\n\nmi_libro = Libro()\nprint('Título del libro:', mi_libro.titulo)\nprint('Páginas:', mi_libro.paginas)",
            "p2_code": "class Dispositivo:\n    tipo = 'Lector de pantalla'\n\nlector = Dispositivo()\nlector.nombre = 'NVDA'\nprint('Dispositivo:', lector.nombre, 'Tipo:', lector.tipo)",
            "p3_instr": "Crea una clase llamada 'Mascota' con un atributo de clase especie = 'Perro'. Crea un objeto perro = Mascota() e imprime: print('Especie:', perro.especie).",
            "p3_start": "# 1. Declara class Mascota: con especie = 'Perro'\n# 2. Crea perro = Mascota()\n# 3. Imprime: print('Especie:', perro.especie)\n\n",
            "p3_val": lambda src, res, ns: 'perro' in res.lower() and 'class Mascota' in src,
            "q_preg": "¿Qué es una clase en programación orientada a objetos?",
            "q_ops": ["Un molde o plantilla para crear objetos con datos y funciones", "Una variable numérica", "Un bucle de repetición"],
            "q_corr": 0,
            "q_exp": "Una clase es el plano estructural a partir del cual se instancian los objetos."
        },
        24: {
            "p1_code": "class Persona:\n    def __init__(self, nombre, edad):\n        self.nombre = nombre\n        self.edad = edad\n\np1 = Persona('Sofía', 28)\nprint(f'{p1.nombre} tiene {p1.edad} años.')",
            "p2_code": "class Cuenta:\n    def __init__(self, titular, saldo):\n        self.titular = titular\n        self.saldo = saldo\n\nc = Cuenta('Kevin', 500)\nprint('Titular:', c.titular, 'Saldo:', c.saldo)",
            "p3_instr": "Crea una clase Usuario con def __init__(self, apodo): que asigne self.apodo = apodo. Crea u = Usuario('Programador') e imprime: print('Apodo:', u.apodo).",
            "p3_start": "# 1. Crea class Usuario con __init__(self, apodo)\n# 2. Crea u = Usuario('Programador')\n# 3. Imprime: print('Apodo:', u.apodo)\n\n",
            "p3_val": lambda src, res, ns: 'programador' in res.lower() and '__init__' in src,
            "q_preg": "¿Cuál es la función del método especial __init__?",
            "q_ops": ["Es el constructor que inicializa los atributos del objeto al crearlo", "Es una función para borrar el objeto", "Es un bucle for"],
            "q_corr": 0,
            "q_exp": "__init__ se ejecuta automáticamente al instanciar un nuevo objeto."
        },
        25: {
            "p1_code": "class Reproductor:\n    def __init__(self, cancion):\n        self.cancion = cancion\n    def reproducir(self):\n        print(f'Reproduciendo la pista: {self.cancion}')\n\nrep = Reproductor('Sinfonía Accesible')\nrep.reproducir()",
            "p2_code": "class Termostato:\n    def __init__(self, temp):\n        self.temp = temp\n    def subir(self, grados):\n        self.temp += grados\n        print('Nueva temperatura:', self.temp)\n\nt = Termostato(20)\nt.subir(3)",
            "p3_instr": "Crea una clase Saludo con def __init__(self, nombre): y un método saludar(self) que imprima: print(f'Hola, {self.nombre}'). Crea s = Saludo('Amigo') e invoca s.saludar().",
            "p3_start": "# 1. Crea class Saludo con __init__(self, nombre) y método saludar(self)\n# 2. Crea s = Saludo('Amigo')\n# 3. Invoca s.saludar()\n\n",
            "p3_val": lambda src, res, ns: 'amigo' in res.lower() and 'saludar' in src,
            "q_preg": "¿Qué representa el primer parámetro 'self' en los métodos de una clase?",
            "q_ops": ["La referencia a la instancia específica del objeto que invocó el método", "Una palabra reservada de Windows", "Un número entero"],
            "q_corr": 0,
            "q_exp": "self permite que el método acceda y modifique los atributos de ese objeto en particular."
        },
        26: {
            "p1_code": "class Animal:\n    def __init__(self, nombre):\n        self.nombre = nombre\n\nclass Perro(Animal):\n    def ladrar(self):\n        print(f'{self.nombre} dice: ¡Guau guau!')\n\nmi_perro = Perro('Toby')\nmi_perro.ladrar()",
            "p2_code": "class Empleado:\n    def __init__(self, nombre, sueldo):\n        self.nombre = nombre\n        self.sueldo = sueldo\n\nclass Gerente(Empleado):\n    def __init__(self, nombre, sueldo, bono):\n        super().__init__(nombre, sueldo)\n        self.bono = bono\n\ng = Gerente('Marta', 3000, 500)\nprint('Gerente:', g.nombre, 'Total:', g.sueldo + g.bono)",
            "p3_instr": "Crea una clase Vehiculo con __init__(self, marca). Crea una clase Coche(Vehiculo) que en su __init__(self, marca, modelo) use super().__init__(marca) y self.modelo = modelo. Crea c = Coche('Toyota', 'Corolla') e imprime: print(c.marca, c.modelo).",
            "p3_start": "# 1. Crea class Vehiculo con __init__(self, marca)\n# 2. Crea class Coche(Vehiculo) usando super().__init__(marca)\n# 3. Crea c = Coche('Toyota', 'Corolla') e imprime print(c.marca, c.modelo)\n\n",
            "p3_val": lambda src, res, ns: 'toyota' in res.lower() and 'corolla' in res.lower() and 'super()' in src,
            "q_preg": "¿Qué función permite invocar el constructor o métodos de la clase padre en la clase hija?",
            "q_ops": ["super()", "parent()", "base()"],
            "q_corr": 0,
            "q_exp": "super() otorga acceso directo a la clase base facilitando la extensión de código."
        },
        27: {
            "p1_code": "class Alumno:\n    def __init__(self, nombre, curso):\n        self.nombre = nombre\n        self.curso = curso\n    def __str__(self):\n        return f'Alumno: {self.nombre}, Curso: {self.curso}'\n\nalumno = Alumno('David', 'Python')\nprint(alumno)",
            "p2_code": "class Producto:\n    def __init__(self, item, precio):\n        self.item = item\n        self.precio = precio\n    def __str__(self):\n        return f'Producto: {self.item} (${self.precio})'\n\nprint(Producto('Teclado accesible', 45))",
            "p3_instr": "Crea una clase Punto con __init__(self, x, y) y un método especial __str__(self) que devuelva f'Punto({self.x}, {self.y})'. Crea p = Punto(3, 7) e imprímelo con print(p).",
            "p3_start": "# 1. Crea class Punto con __init__(self, x, y)\n# 2. Implementa def __str__(self): return f'Punto({self.x}, {self.y})'\n# 3. Imprime print(Punto(3, 7))\n\n",
            "p3_val": lambda src, res, ns: 'punto(3, 7)' in res.lower() or ('3' in res and '7' in res and '__str__' in src),
            "q_preg": "¿Para qué sirve implementar el método especial __str__ en una clase?",
            "q_ops": ["Para definir la representación textual legible al imprimir el objeto con print()", "Para borrar el objeto de la memoria", "Para convertirlo en lista"],
            "q_corr": 0,
            "q_exp": "__str__ devuelve una cadena amigable y comprensible para el lector de pantalla."
        },
        28: {
            "p1_code": "import math\nprint('Raíz cuadrada de 64:', math.isqrt(64))\nprint('Valor de Pi redondeado:', round(math.pi, 4))",
            "p2_code": "import random\nazar = random.randint(1, 10)\nprint('Número aleatorio entre 1 y 10:', azar)",
            "p3_instr": "Importa el módulo math y calcula la raíz cuadrada entera de 144 con math.isqrt(144). Imprime: print('Raíz de 144:', math.isqrt(144)).",
            "p3_start": "# 1. import math\n# 2. Imprime: print('Raíz de 144:', math.isqrt(144))\n\n",
            "p3_val": lambda src, res, ns: '12' in res and 'math' in src,
            "q_preg": "¿Qué palabra clave se usa para cargar módulos de la biblioteca estándar de Python?",
            "q_ops": ["import", "load", "include"],
            "q_corr": 0,
            "q_exp": "import enlaza cualquier biblioteca estándar o archivo externo en tu código."
        },
        29: {
            "p1_code": "import json\ndatos = {'usuario': 'Elena', 'nivel': 3, 'activo': True}\ntexto_json = json.dumps(datos)\nprint('Texto en formato JSON:', texto_json)",
            "p2_code": "import json\ntexto = '{\"curso\": \"Python\", \"duracion_horas\": 40}'\nobjeto = json.loads(texto)\nprint('Curso decodificado:', objeto['curso'])",
            "p3_instr": "Importa json. Crea un diccionario config = {'tema': 'oscuro', 'fuente': 14}. Conviértelo a texto JSON con json.dumps(config) e imprime: print('JSON:', json.dumps(config)).",
            "p3_start": "import json\n# 1. Crea config = {'tema': 'oscuro', 'fuente': 14}\n# 2. Imprime: print('JSON:', json.dumps(config))\n\n",
            "p3_val": lambda src, res, ns: 'oscuro' in res.lower() and 'json.dumps' in src,
            "q_preg": "¿Qué función del módulo json convierte un diccionario de Python en una cadena de texto JSON?",
            "q_ops": ["json.dumps()", "json.loads()", "json.parse()"],
            "q_corr": 0,
            "q_exp": "json.dumps() (dump string) serializa objetos de Python a texto JSON."
        },
        30: {
            "p1_code": "import sqlite3\ncon = sqlite3.connect(':memory:')\ncur = con.cursor()\ncur.execute('CREATE TABLE notas (id INTEGER, titulo TEXT)')\ncur.execute(\"INSERT INTO notas VALUES (1, 'Mi primera nota en SQLite')\")\ncon.commit()\ncur.execute('SELECT titulo FROM notas')\nprint('Nota en base de datos:', cur.fetchone()[0])\ncon.close()",
            "p2_code": "import sqlite3\ncon = sqlite3.connect(':memory:')\ncur = con.cursor()\ncur.execute('CREATE TABLE usuarios (nombre TEXT, edad INT)')\ncur.execute(\"INSERT INTO usuarios VALUES ('Carlos', 30)\")\ncur.execute('SELECT COUNT(*) FROM usuarios')\nprint('Total usuarios en BD:', cur.fetchone()[0])\ncon.close()",
            "p3_instr": "Crea una base de datos SQLite en memoria con con = sqlite3.connect(':memory:'), crea una tabla productos (nombre TEXT) e inserta 'Teclado'. Luego consulta con SELECT y muestra el producto.",
            "p3_start": "import sqlite3\ncon = sqlite3.connect(':memory:')\ncur = con.cursor()\n# 1. cur.execute('CREATE TABLE productos (nombre TEXT)')\n# 2. cur.execute(\"INSERT INTO productos VALUES ('Teclado')\")\n# 3. cur.execute('SELECT nombre FROM productos')\n# 4. Imprime: print('Producto:', cur.fetchone()[0])\n\n",
            "p3_val": lambda src, res, ns: 'teclado' in res.lower() and 'sqlite3' in src,
            "q_preg": "¿Qué instrucción SQL se utiliza para consultar y extraer registros de una tabla?",
            "q_ops": ["SELECT", "INSERT", "DELETE"],
            "q_corr": 0,
            "q_exp": "SELECT es la sentencia fundamental de consulta en SQL."
        },
        31: {
            "p1_code": "# Simulación estructurada de consumo de API REST:\nrespuesta_api = {\n    'status': 200,\n    'datos': {'temperatura': 22, 'clima': 'Despejado'}\n}\nif respuesta_api['status'] == 200:\n    clima = respuesta_api['datos']['clima']\n    print(f'Reporte meteorológico de la API: {clima}')",
            "p2_code": "respuesta = {\n    'codigo': 200,\n    'usuarios': ['Andrea', 'Pablo', 'Lucía']\n}\nprint('Usuarios recibidos del servidor:', len(respuesta['usuarios']))",
            "p3_instr": "Dada la respuesta simulada resp = {'estado': 'OK', 'mensaje': 'Servicio disponible'}, comprueba si resp['estado'] == 'OK' e imprime: print('API:', resp['mensaje']).",
            "p3_start": "resp = {'estado': 'OK', 'mensaje': 'Servicio disponible'}\n# Comprueba si resp['estado'] == 'OK' e imprime print('API:', resp['mensaje'])\n\n",
            "p3_val": lambda src, res, ns: 'servicio disponible' in res.lower(),
            "q_preg": "¿Qué código de estado HTTP estándar indica que una petición web se resolvió con éxito?",
            "q_ops": ["200 (OK)", "404 (Not Found)", "500 (Internal Error)"],
            "q_corr": 0,
            "q_exp": "El código 200 indica éxito en peticiones HTTP."
        },
        32: {
            "p1_code": "def multiplicar(a, b):\n    return a * b\n\n# Verificación manual con assert:\nassert multiplicar(3, 4) == 12\nprint('Prueba unitaria superada: 3 * 4 = 12')",
            "p2_code": "def restar(a, b):\n    return a - b\n\nassert restar(10, 4) == 6\nprint('Prueba de resta exitosa.')",
            "p3_instr": "Define una función es_par(numero) que retorne numero % 2 == 0. Escribe assert es_par(4) == True y luego imprime: print('Todas las pruebas pasaron con éxito').",
            "p3_start": "# 1. Define def es_par(numero): return numero % 2 == 0\n# 2. assert es_par(4) == True\n# 3. Imprime: print('Todas las pruebas pasaron con éxito')\n\n",
            "p3_val": lambda src, res, ns: 'todas las pruebas' in res.lower() or 'éxito' in res.lower() or 'exito' in res.lower(),
            "q_preg": "¿Cuál es el propósito primordial de escribir pruebas unitarias?",
            "q_ops": [
                "Verificar de forma automática que cada pequeña parte del código funciona como se espera",
                "Hacer que el programa corra más rápido",
                "Cambiar el color del editor"
            ],
            "q_corr": 0,
            "q_exp": "Las pruebas unitarias garantizan que el código cumpla sus requisitos y previenen regresiones en el software."
        }
    }

    for cid, title, summary in titles_11_32:
        d = details[cid]
        chapters.append({
            "id": cid,
            "titulo": f"Capítulo {cid}: {title}",
            "resumen": summary,
            "pasos": [
                {
                    "titulo": "Paso 1: Fundamento Conceptual",
                    "tipo": "observar",
                    "instruccion": f"En este paso aprenderemos sobre {title}. Ejecuta el código para observar el concepto en acción.",
                    "codigo": d["p1_code"],
                    "pistas": ["Pulsa Control + Enter para ejecutar."],
                    "validar": lambda src, res, ns: len(res.strip()) > 0
                },
                {
                    "titulo": "Paso 2: Observación y Modificación guiada",
                    "tipo": "experimentar",
                    "instruccion": "Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.",
                    "codigo": d["p2_code"],
                    "pistas": ["Modifica algún valor y presiona Control + Enter."],
                    "validar": lambda src, res, ns: len(res.strip()) > 0
                },
                {
                    "titulo": "Paso 3: Reto Práctico Interactivo",
                    "tipo": "desafio",
                    "instruccion": d["p3_instr"],
                    "codigo": d["p3_start"],
                    "salida_esperada": "",
                    "pistas": [
                        "Nivel 1: Sigue las instrucciones del paso.",
                        "Nivel 2: Comprueba la sintaxis de las variables o funciones.",
                        "Nivel 3: Ejecuta con Control + Enter para verificar."
                    ],
                    "validar": d["p3_val"]
                },
                {
                    "titulo": "Paso 4: Verificación Conceptual",
                    "tipo": "quiz",
                    "instruccion": f"Pregunta de verificación conceptual:\n{d['q_preg']}\n\nOpciones:\n1. {d['q_ops'][0]}\n2. {d['q_ops'][1]}\n3. {d['q_ops'][2]}\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.",
                    "codigo": "# Escribe aquí tu respuesta (1, 2 o 3):\n",
                    "pregunta": d["q_preg"],
                    "opciones": d["q_ops"],
                    "correcta": d["q_corr"],
                    "explicacion": d["q_exp"],
                    "pistas": ["Lee detenidamente las 3 opciones."],
                    "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
                }
            ]
        })

    return chapters

if __name__ == '__main__':
    print("Testing generator...")
    c = generate()
    print("Generated chapters:", len(c))
