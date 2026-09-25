# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/curriculum.py
# Propósito: Temario pedagógico no visual de 32 capítulos progresivos con
#            fundamentos conceptuales previos, retos prácticos y quizzes formativos.
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

CURRICULUM = [
    {
        "id": 1,
        "titulo": 'Capítulo 1: Pensamiento Computacional y Algoritmos Cotidianos',
        "resumen": '¿Qué es pensar como un programador? Descubre qué es un algoritmo a través de secuencias de pasos de la vida cotidiana.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento: ¿Qué es un algoritmo?',
                "tipo": 'observar',
                "instruccion": 'Un algoritmo es una serie ordenada y finita de pasos lógicos para resolver un problema o lograr una meta. En la vida diaria seguimos algoritmos al cocinar o cruzar la calle. En programación, la computadora no improvisa: ejecuta estrictamente la secuencia que le ordenas. Pulsa Control + Enter para escuchar este primer algoritmo.',
                "codigo": "print('Paso 1: Llenar la tetera con agua.')\nprint('Paso 2: Calentar el agua hasta hervir.')\nprint('Paso 3: Servir en una taza con infusión.')\nprint('¡Algoritmo completado!')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación: La importancia del orden',
                "tipo": 'experimentar',
                "instruccion": "Si alteramos el orden de las instrucciones, el resultado final no tendrá sentido. Añade entre el paso 1 y el paso 2 la línea: print('Paso intermedio: Colocar la bolsita de té.') y pulsa Control + Enter.",
                "codigo": "print('Paso 1: Calentar el agua.')\n# Escribe aquí la línea intermedia con print:\n\nprint('Paso 2: Servir el agua caliente en la taza.')",
                "pistas": ["Escribe print('Paso intermedio: Colocar la bolsita de té.') entre las dos líneas existentes."],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Algoritmo de lavado de manos',
                "tipo": 'desafio',
                "instruccion": "Escribe un algoritmo de 3 pasos para lavarse las manos usando tres instrucciones print(): 1. 'Abrir el grifo y mojar las manos', 2. 'Aplicar jabón y frotar', 3. 'Enjuagar y secar'. Ejecuta con Control + Enter para comprobar.",
                "codigo": '# Escribe aquí las 3 instrucciones print() para cada paso:\n# 1. Abrir el grifo y mojar las manos\n# 2. Aplicar jabón y frotar\n# 3. Enjuagar y secar\n\n',
                "salida_esperada": '1. Abrir el grifo y mojar las manos\n2. Aplicar jabón y frotar\n3. Enjuagar y secar',
                "pistas": ['Usa tres instrucciones print independientes, cada una con el texto entre comillas.', "Ejemplo: print('1. Abrir el grifo y mojar las manos')"],
                "validar": lambda src, res, ns: ("jabón" in res.lower() or "jabon" in res.lower()) and "grifo" in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Cuál es la definición más exacta de un algoritmo?\n\nOpciones:\n1. Un componente físico de la computadora como el procesador.\n2. Una serie ordenada y finita de instrucciones lógicas para resolver un problema.\n3. Un virus informático que altera los programas.\n\nEscribe el número de tu opción (1, 2 o 3) en el editor y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Recuerda el ejemplo de la preparación del té.'],
                "pregunta": '¿Cuál es la definición más exacta de un algoritmo?',
                "opciones": ['Un componente físico de la computadora como el procesador.', 'Una serie ordenada y finita de instrucciones lógicas para resolver un problema.', 'Un virus informático que altera los programas.'],
                "correcta": 1,
                "explicacion": 'Un algoritmo es la secuencia lógica y paso a paso que describe la solución a un problema determinado.',
                "validar": lambda src, res, ns: '2' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 2,
        "titulo": 'Capítulo 2: Arquitectura Básica: Entrada, Proceso, Memoria y Salida',
        "resumen": 'Comprende cómo viaja la información dentro de un computador: periféricos de entrada, memoria RAM, procesador y canales de salida.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento: El ciclo Entrada-Proceso-Salida',
                "tipo": 'observar',
                "instruccion": 'Todo programa informático sigue este ciclo: Entrada (teclado), Memoria RAM (donde residen variables temporales), Procesador CPU (donde se hacen cálculos) y Salida (pantalla y lector de voz). Ejecuta el código para observar este flujo en acción.',
                "codigo": "# Entrada y Memoria:\nherramienta = 'NVDA'\n# Procesamiento:\nmensaje = 'Entorno accesible asistido por: ' + herramienta\n# Salida:\nprint(mensaje)",
                "pistas": ['Pulsa Control + Enter para ver la salida.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación: La memoria es modificable',
                "tipo": 'experimentar',
                "instruccion": "En la memoria RAM podemos reemplazar el contenido de una variable en cualquier instante. Observa cómo cambia la variable 'estado' y ejecuta con Control + Enter.",
                "codigo": "estado = 'Cargando datos'\nprint('Estado inicial:', estado)\n# Cambia aquí el valor de estado a 'Listo para programar':\nestado = 'Listo para programar'\nprint('Estado final:', estado)",
                "pistas": ['Ejecuta con Control + Enter para escuchar los dos estados secuenciales.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Variables y salida',
                "tipo": 'desafio',
                "instruccion": "Crea una variable llamada 'usuario' con el texto 'Estudiante' y muestra en consola usando print: Bienvenido/a, Estudiante. Ejecuta con Control + Enter.",
                "codigo": "# 1. Crea la variable usuario con el valor 'Estudiante'\n# 2. Usa print('Bienvenido/a,', usuario) para mostrar el saludo\n\n",
                "salida_esperada": 'Bienvenido/a, Estudiante',
                "pistas": ["Escribe usuario = 'Estudiante' en el primer renglón y luego print('Bienvenido/a,', usuario)."],
                "validar": lambda src, res, ns: "bienvenido" in res.lower() and "estudiante" in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Dónde se almacenan las variables mientras tu script de Python se está ejecutando?\n\nOpciones:\n1. En la Memoria RAM del equipo.\n2. En la tecla Escape del teclado.\n3. En el cable de corriente.\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Es la memoria principal de acceso aleatorio.'],
                "pregunta": '¿Dónde se almacenan las variables mientras tu script de Python se está ejecutando?',
                "opciones": ['En la Memoria RAM del equipo.', 'En la tecla Escape del teclado.', 'En el cable de corriente.'],
                "correcta": 0,
                "explicacion": 'La Memoria RAM es el espacio de trabajo rápido donde residen los datos activos de los programas en ejecución.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 3,
        "titulo": 'Capítulo 3: Lógica Booleana: Verdadero, Falso y Decisiones',
        "resumen": 'Aprende el fundamento binario de toda decisión digital: los valores True y False y los operadores lógicos and, or y not.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento: Proposiciones booleanas',
                "tipo": 'observar',
                "instruccion": 'Una proposición booleana solo puede evaluarse como Verdadera (True) o Falsa (False). Por ejemplo: 10 > 5 es True, mientras que 2 > 8 es False. Ejecuta el código para escuchar estas evaluaciones.',
                "codigo": "print('¿10 es mayor que 5?:', 10 > 5)\nprint('¿2 es mayor que 8?:', 2 > 8)",
                "pistas": ['Pulsa Control + Enter para escuchar True y False.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación: Operadores and, or y not',
                "tipo": 'experimentar',
                "instruccion": "El operador 'and' exige que ambas condiciones sean verdaderas. El operador 'or' solo requiere que al menos una lo sea. Ejecuta el código y analiza el resultado.",
                "codigo": "llave = True\nclave = False\nprint('¿Puede entrar con llave O clave?:', llave or clave)\nprint('¿Cumple llave Y clave?:', llave and clave)",
                "pistas": ['Observa cómo or devuelve True pero and devuelve False.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Verificación de acceso',
                "tipo": 'desafio',
                "instruccion": "Crea una variable llamada 'edad' con el valor 20 y una variable 'tiene_identificacion' con True. Luego crea 'autorizado = (edad >= 18) and tiene_identificacion'. Imprime print('Acceso permitido:', autorizado).",
                "codigo": "# 1. Crea la variable edad con 20\n# 2. Crea tiene_identificacion con True\n# 3. Crea autorizado = (edad >= 18) and tiene_identificacion\n# 4. Muestra: print('Acceso permitido:', autorizado)\n\n",
                "salida_esperada": 'Acceso permitido: True',
                "pistas": ['Une ambas condiciones con el operador and.'],
                "validar": lambda src, res, ns: "true" in res.lower() and "acceso" in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué resultado produce la expresión booleana: not False?\n\nOpciones:\n1. True\n2. False\n3. None\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['not es el operador de negación inversa.'],
                "pregunta": '¿Qué resultado produce la expresión booleana: not False?',
                "opciones": ['True', 'False', 'None'],
                "correcta": 0,
                "explicacion": "El operador 'not' invierte el valor lógico: si niegas False obtienes True.",
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 4,
        "titulo": 'Capítulo 4: Nuestra Primera Instrucción: La Función print()',
        "resumen": 'Aprende a emitir información hacia la salida estándar y escucharla en tu lector de pantalla.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento: La función print()',
                "tipo": 'observar',
                "instruccion": 'La función print() envía mensajes a la salida para que el lector de pantalla los verbalice. El texto siempre debe ir rodeado por comillas simples o dobles. Pulsa Control + Enter para escuchar este saludo inicial.',
                "codigo": "print('¡Hola mundo desde Python accesible!')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación: Varios argumentos separados por coma',
                "tipo": 'experimentar',
                "instruccion": 'print() puede recibir varios textos separados por comas. Python insertará automáticamente un espacio entre cada uno. Cambia algún texto o añade uno nuevo y pulsa Control + Enter.',
                "codigo": "print('Python', 'es', 'fácil', 'y', 'accesible')",
                "pistas": ['Modifica o agrega un argumento entre comillas.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Tu propio saludo',
                "tipo": 'desafio',
                "instruccion": "Escribe una instrucción print() que muestre exactamente el mensaje: 'Aprendiendo Python con NVDA'. Pulsa Control + Enter para validar.",
                "codigo": '# Escribe aquí tu instrucción print() con el mensaje indicado:\n\n',
                "salida_esperada": 'Aprendiendo Python con NVDA',
                "pistas": ["Escribe: print('Aprendiendo Python con NVDA') respetando las comillas y los paréntesis."],
                "validar": lambda src, res, ns: "aprendiendo python con nvda" in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué función se utiliza en Python para enviar datos a la salida y lector de pantalla?\n\nOpciones:\n1. print()\n2. input()\n3. exit()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué función se utiliza en Python para enviar datos a la salida y lector?',
                "opciones": ['print()', 'input()', 'exit()'],
                "correcta": 0,
                "explicacion": 'print() es la función de salida estándar por excelencia.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 5,
        "titulo": 'Capítulo 5: Almacenamiento en Memoria: Variables y Asignación',
        "resumen": 'Aprende a guardar valores en memoria asignándoles un nombre con el signo igual (=).',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento: Crear y asignar variables',
                "tipo": 'observar',
                "instruccion": 'Una variable es un nombre que apunta a un dato guardado en la memoria. Se usa el signo igual (=) para asignar. Ejecuta el código para observar cómo se combinan texto y números.',
                "codigo": "nombre = 'Kevin'\nedad = 25\nprint(nombre, 'tiene', edad, 'años')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación: Actualizar el valor de una variable',
                "tipo": 'experimentar',
                "instruccion": 'Podemos sumar puntos a una variable existente y reasignarla. Cambia el valor que se suma (50) por otro número y pulsa Control + Enter.',
                "codigo": "puntos = 100\nprint('Puntuación inicial:', puntos)\npuntos = puntos + 50\nprint('Puntuación acumulada:', puntos)",
                "pistas": ['Modifica el número 50 por el valor que prefieras y ejecuta.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Variable de lenguaje',
                "tipo": 'desafio',
                "instruccion": "Crea una variable llamada 'lenguaje' con el texto 'Python' y luego muestra en consola: print('Estoy programando en:', lenguaje). Pulsa Control + Enter.",
                "codigo": "# 1. Crea la variable lenguaje = 'Python'\n# 2. Imprime: print('Estoy programando en:', lenguaje)\n\n",
                "salida_esperada": 'Estoy programando en: Python',
                "pistas": ["Asigna lenguaje = 'Python' y luego pásala a print."],
                "validar": lambda src, res, ns: "programando en" in res.lower() and "python" in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué símbolo se usa en Python para asignar un valor a una variable?\n\nOpciones:\n1. El signo igual (=)\n2. El signo de suma (+)\n3. El punto y coma (;)\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['El operador de asignación es =.'],
                "pregunta": '¿Qué símbolo se usa en Python para asignar un valor a una variable?',
                "opciones": ['El signo igual (=)', 'El signo de suma (+)', 'El punto y coma (;)'],
                "correcta": 0,
                "explicacion": 'El signo igual simple (=) asigna lo que está a la derecha en la variable de la izquierda.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 6,
        "titulo": 'Capítulo 6: Tipos de Datos Primitivos: Números Enteros y Decimales',
        "resumen": 'Opera con números enteros (int) y números decimales (float) realizando cálculos matemáticos.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento: Enteros (int) y Decimales (float)',
                "tipo": 'observar',
                "instruccion": 'En Python, los números sin punto son enteros (int) y los que tienen punto decimal son flotantes (float). Ejecuta el código para observar cómo se multiplican.',
                "codigo": "precio = 19.50\ncantidad = 3\ntotal = precio * cantidad\nprint('Total a pagar:', total)",
                "pistas": ['Pulsa Control + Enter para ver la multiplicación.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación: Operaciones con decimales',
                "tipo": 'experimentar',
                "instruccion": 'El operador ** calcula potencias (radio al cuadrado). Cambia el valor del radio a 5 y pulsa Control + Enter para ver cómo cambia el área.',
                "codigo": "radio = 4\npi = 3.1416\narea = pi * (radio ** 2)\nprint('Área del círculo:', round(area, 2))",
                "pistas": ['Cambia radio = 4 por radio = 5.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Cálculo de área de triángulo',
                "tipo": 'desafio',
                "instruccion": "Crea las variables base = 10 y altura = 5. Calcula area = (base * altura) / 2 e imprime: print('Área del triángulo:', area). Ejecuta con Control + Enter.",
                "codigo": "# 1. Define base = 10 y altura = 5\n# 2. Calcula area = (base * altura) / 2\n# 3. Imprime: print('Área del triángulo:', area)\n\n",
                "salida_esperada": 'Área del triángulo: 25.0',
                "pistas": ['Recuerda usar la barra inclinada / para la división.'],
                "validar": lambda src, res, ns: "25" in res and ("triángulo" in res.lower() or "triangulo" in res.lower())
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Cómo se denomina en Python al tipo de dato numérico que tiene parte decimal?\n\nOpciones:\n1. float\n2. int\n3. bool\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ["Viene del inglés 'floating point'."],
                "pregunta": '¿Cómo se denomina en Python a un número con parte decimal?',
                "opciones": ['float', 'int', 'bool'],
                "correcta": 0,
                "explicacion": 'float representa números de coma flotante (decimales).',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 7,
        "titulo": 'Capítulo 7: Cadenas de Texto (Strings): Comillas y Concatenación',
        "resumen": 'Manipula texto en Python usando comillas simples, dobles y cadenas formateadas modernas (f-strings).',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento: Concatenación con + y f-strings',
                "tipo": 'observar',
                "instruccion": "Las cadenas de texto (str) pueden unirse con el operador + o usando f-strings colocando una 'f' antes de las comillas e insertando variables entre llaves {}. Ejecuta para ver ambos métodos.",
                "codigo": "nombre = 'Laura'\nsaludo = f'Hola {nombre}, bienvenida a Python.'\nprint(saludo)",
                "pistas": ['Pulsa Control + Enter para ver la interpolación de texto.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación: Repetición de texto con *',
                "tipo": 'experimentar',
                "instruccion": 'Al multiplicar un texto por un número, Python lo repite. Cambia el multiplicador 3 por 5 y pulsa Control + Enter.',
                "codigo": "aplauso = '¡Bravo! '\nprint(aplauso * 3)",
                "pistas": ['Cambia * 3 por * 5.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Crear una f-string',
                "tipo": 'desafio',
                "instruccion": "Crea una variable ciudad = 'Bogotá' y pais = 'Colombia'. Usa una f-string para imprimir exactamente: print(f'Ubicación: {ciudad}, {pais}').",
                "codigo": "# 1. Define ciudad = 'Bogotá' y pais = 'Colombia'\n# 2. Imprime usando f-string: print(f'Ubicación: {ciudad}, {pais}')\n\n",
                "salida_esperada": 'Ubicación: Bogotá, Colombia',
                "pistas": ['Coloca f antes de las comillas y las variables dentro de {ciudad} y {pais}.'],
                "validar": lambda src, res, ns: "bogot" in res.lower() and "colombia" in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué letra precede a las comillas para crear una cadena formateada moderna en Python?\n\nOpciones:\n1. La letra f\n2. La letra p\n3. La letra s\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ["f viene de 'format'."],
                "pregunta": '¿Qué letra precede a las comillas para crear una f-string?',
                "opciones": ['La letra f', 'La letra p', 'La letra s'],
                "correcta": 0,
                "explicacion": 'La letra f convierte una cadena en una f-string (cadena formateada).',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 8,
        "titulo": 'Capítulo 8: Interacción con el Usuario: Entrada con input()',
        "resumen": 'Aprende a capturar datos que el usuario escribe por teclado y a transformarlos con int() o float().',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento: La función input()',
                "tipo": 'observar',
                "instruccion": 'input() permite recibir datos del usuario. Recuerda que input() SIEMPRE devuelve una cadena de texto (str). Si necesitas hacer cálculos matemáticos, debes convertirlo con int(). Ejecuta para observar la conversión.',
                "codigo": "edad_texto = '25'\nedad_numero = int(edad_texto)\nprint('Edad numérica convertida:', edad_numero)\nprint('El doble de tu edad es:', edad_numero * 2)",
                "pistas": ['Pulsa Control + Enter para ver la conversión.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación: input con mensaje',
                "tipo": 'experimentar',
                "instruccion": 'Observa cómo se le pasa un texto informativo a input(). Modifica el mensaje dentro de input y pulsa Control + Enter.',
                "codigo": "nombre = 'Ana'\nprint(f'¡Hola {nombre}! Bienvenido/a al aprendizaje interactivo.')",
                "pistas": ["Cambia 'Ana' por tu propio nombre."],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Conversión y cálculo',
                "tipo": 'desafio',
                "instruccion": "Tienes la variable edad_texto = '20'. Conviértela a entero usando int(edad_texto) y guarda el resultado en 'edad'. Luego muestra: print('El próximo año tendrás:', edad + 1).",
                "codigo": "edad_texto = '20'\n# 1. Convierte edad_texto a entero: edad = int(edad_texto)\n# 2. Imprime: print('El próximo año tendrás:', edad + 1)\n\n",
                "salida_esperada": 'El próximo año tendrás: 21',
                "pistas": ['Usa int(edad_texto) para la conversión.'],
                "validar": lambda src, res, ns: "21" in res and ("tendrás" in res.lower() or "tendras" in res.lower())
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué tipo de dato devuelve por defecto la función input() de Python?\n\nOpciones:\n1. Siempre una cadena de texto (str)\n2. Un número entero (int)\n3. Un booleano (bool)\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Todo lo que entra por teclado se lee inicialmente como texto.'],
                "pregunta": '¿Qué tipo de dato devuelve por defecto input()?',
                "opciones": ['Siempre una cadena de texto (str)', 'Un número entero (int)', 'Un booleano (bool)'],
                "correcta": 0,
                "explicacion": 'input() siempre retorna una cadena (str), por eso se requiere int() o float() para operar numéricamente.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 9,
        "titulo": 'Capítulo 9: Operadores de Comparación y Expresiones Condicionales',
        "resumen": 'Compara valores usando >, <, >=, <=, == y != para tomar decisiones en tus programas.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento: Operadores relacionales',
                "tipo": 'observar',
                "instruccion": 'Los operadores relacionales comparan dos valores: > (mayor), < (menor), >= (mayor o igual), <= (menor o igual), == (igual) y != (distinto). Ejecuta para observar sus resultados booleanos.',
                "codigo": "x = 15\ny = 20\nprint('¿x es menor que y?:', x < y)\nprint('¿x es igual a y?:', x == y)\nprint('¿x es distinto de y?:', x != y)",
                "pistas": ['Pulsa Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación: Comparar textos',
                "tipo": 'experimentar',
                "instruccion": 'También puedes comparar textos con ==. Si cambias el texto para que coincidan exactamente, el resultado cambiará a True. Modifica y ejecuta.',
                "codigo": "clave_ingresada = 'secreta'\nclave_real = 'secreta'\nprint('¿Clave correcta?:', clave_ingresada == clave_real)",
                "pistas": ['Cambia una de las cadenas para que no coincidan o mantenlas iguales.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Nota de aprobación',
                "tipo": 'desafio',
                "instruccion": "Crea una variable puntos = 85. Imprime en consola: print('¿Aprobó con 70 o más?:', puntos >= 70). Pulsa Control + Enter.",
                "codigo": "# 1. Define puntos = 85\n# 2. Imprime: print('¿Aprobó con 70 o más?:', puntos >= 70)\n\n",
                "salida_esperada": '¿Aprobó con 70 o más?: True',
                "pistas": ['Usa el operador >= (mayor o igual).'],
                "validar": lambda src, res, ns: "70" in res and "true" in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué operador se utiliza en Python para comparar si dos valores son exactamente iguales?\n\nOpciones:\n1. Doble signo igual (==)\n2. Un solo signo igual (=)\n3. Signo de admiración (!)\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['No confundir asignación (=) con comparación.'],
                "pregunta": '¿Qué operador compara si dos valores son iguales?',
                "opciones": ['Doble signo igual (==)', 'Un solo signo igual (=)', 'Signo de admiración (!)'],
                "correcta": 0,
                "explicacion": 'El doble signo igual (==) compara igualdad. El signo simple (=) asigna valores.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 10,
        "titulo": 'Capítulo 10: Bifurcación Básica: Estructura if y Sangría PEP 8',
        "resumen": 'Ejecuta bloques de código bajo condición usando if y 4 espacios de sangría obligatoria.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento: La sentencia if y los 4 espacios',
                "tipo": 'observar',
                "instruccion": 'La sentencia if evalúa una condición terminando con dos puntos (:). Las líneas subordinadas deben llevar 4 espacios de sangría (tecla Tab). Ejecuta el código para observar cómo se cumple la condición.',
                "codigo": "temperatura = 30\nif temperatura > 25:\n    print('Hace calor, enciende el ventilador.')\nprint('Fin del análisis.')",
                "pistas": ['Pulsa Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación: Cuando la condición no se cumple',
                "tipo": 'experimentar',
                "instruccion": 'Si la condición es False, el bloque indentado no se ejecuta. Cambia temperatura a 15 y ejecuta con Control + Enter para escuchar cómo se salta el bloque.',
                "codigo": "temperatura = 15\nif temperatura > 25:\n    print('Hace calor.')\nprint('Fin del análisis de temperatura.')",
                "pistas": ['Cambia temperatura = 15 y ejecuta.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Saludo horario con if',
                "tipo": 'desafio',
                "instruccion": "Crea una variable hora = 14. Escribe un bloque if que compruebe si hora >= 12, y dentro imprima con 4 espacios de sangría: print('Buenas tardes').",
                "codigo": "# 1. Define hora = 14\n# 2. Escribe if hora >= 12:\n# 3. Con 4 espacios: print('Buenas tardes')\n\n",
                "salida_esperada": 'Buenas tardes',
                "pistas": ['No olvides los dos puntos (:) al final de la línea if.', 'Usa 4 espacios o pulsa Tab para la indentación.'],
                "validar": lambda src, res, ns: "buenas tardes" in res.lower() and "if " in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Cuántos espacios en blanco recomienda el estándar oficial PEP 8 para cada nivel de sangría en Python?\n\nOpciones:\n1. 4 espacios\n2. 1 espacio\n3. 10 espacios\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Es el estándar universal de Python.'],
                "pregunta": '¿Cuántos espacios recomienda PEP 8 para la sangría?',
                "opciones": ['4 espacios', '1 espacio', '10 espacios'],
                "correcta": 0,
                "explicacion": 'PEP 8 establece un estándar de 4 espacios por cada nivel de sangría.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 11,
        "titulo": 'Capítulo 11: Alternativas Múltiples: Bloques elif y else',
        "resumen": 'Maneja múltiples caminos posibles encadenando condiciones con elif y un caso por defecto con else.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Alternativas Múltiples: Bloques elif y else. Ejecuta el código para observar el concepto en acción.',
                "codigo": "nota = 7\nif nota >= 9:\n    print('Excelente')\nelif nota >= 5:\n    print('Aprobado')\nelse:\n    print('Reprobado')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "nota = 4\nif nota >= 9:\n    print('Excelente')\nelif nota >= 5:\n    print('Aprobado')\nelse:\n    print('Reprobado')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una variable nota = 8. Escribe if nota >= 9 imprima 'Excelente', elif nota >= 5 imprima 'Aprobado', y else imprima 'Reprobado'.",
                "codigo": '# 1. Define nota = 8\n# 2. Escribe la estructura if, elif y else:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "aprobado" in res.lower() and "elif" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué bloque condicional se ejecuta si ninguna condición anterior fue verdadera?\n\nOpciones:\n1. El bloque else\n2. El bloque if\n3. El bloque while\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué bloque condicional se ejecuta si ninguna condición anterior fue verdadera?',
                "opciones": ['El bloque else', 'El bloque if', 'El bloque while'],
                "correcta": 0,
                "explicacion": 'else se ejecuta como camino por defecto cuando todo lo anterior fue falso.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 12,
        "titulo": 'Capítulo 12: Colecciones Ordenadas: Introducción a las Listas',
        "resumen": 'Guarda múltiples elementos en una secuencia ordenada usando corchetes [] y accede mediante índices.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Colecciones Ordenadas: Introducción a las Listas. Ejecuta el código para observar el concepto en acción.',
                "codigo": "frutas = ['manzana', 'pera', 'plátano']\nprint('Primera fruta:', frutas[0])\nprint('Segunda fruta:', frutas[1])",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "frutas = ['manzana', 'pera', 'plátano']\n# Modifica el elemento en la posición 0:\nfrutas[0] = 'fresa'\nprint('Lista actualizada:', frutas)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una lista llamada 'compras' con 'pan', 'leche' y 'huevos'. Imprime el primer elemento usando compras[0].",
                "codigo": "# 1. Crea la lista compras con 'pan', 'leche' y 'huevos'\n# 2. Imprime el primer elemento con print(compras[0])\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "pan" in res.lower() and "compras" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Cuál es el índice del primer elemento de una lista en Python?\n\nOpciones:\n1. El índice 0\n2. El índice 1\n3. El índice -1\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Cuál es el índice del primer elemento de una lista en Python?',
                "opciones": ['El índice 0', 'El índice 1', 'El índice -1'],
                "correcta": 0,
                "explicacion": 'En Python la indexación empieza siempre en base cero (0).',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 13,
        "titulo": 'Capítulo 13: Métodos Fundamentales de Listas (append, remove, pop, len)',
        "resumen": 'Añade, elimina y cuenta elementos en listas dinámicas de Python.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Métodos Fundamentales de Listas (append, remove, pop, len). Ejecuta el código para observar el concepto en acción.',
                "codigo": "tareas = ['leer', 'programar']\ntareas.append('descansar')\nprint('Tareas totales:', len(tareas))\nprint('Lista:', tareas)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "tareas = ['leer', 'programar', 'descansar']\ntareas.remove('leer')\nprint('Después de borrar leer:', tareas)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una lista colores = ['rojo', 'verde']. Agrega 'azul' con append() y muestra la cantidad total con print('Total colores:', len(colores)).",
                "codigo": "colores = ['rojo', 'verde']\n# 1. Usa colores.append('azul')\n# 2. Imprime: print('Total colores:', len(colores))\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "3" in res and "colores" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué método agrega un nuevo elemento al final de una lista?\n\nOpciones:\n1. append()\n2. delete()\n3. add()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué método agrega un nuevo elemento al final de una lista?',
                "opciones": ['append()', 'delete()', 'add()'],
                "correcta": 0,
                "explicacion": 'append() añade un nuevo elemento al final de la lista.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 14,
        "titulo": 'Capítulo 14: Repetición y Automatización: El Bucle for y range()',
        "resumen": 'Automatiza tareas repetitivas recorriendo secuencias numéricas y listas con for.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Repetición y Automatización: El Bucle for y range(). Ejecuta el código para observar el concepto en acción.',
                "codigo": "for i in range(1, 4):\n    print('Número:', i)\nprint('Fin del bucle')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "animales = ['perro', 'gato', 'loro']\nfor animal in animales:\n    print('Mascota:', animal)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Escribe un bucle for que recorra range(1, 6) e imprima cada número: print('Contando:', numero).",
                "codigo": '# Escribe aquí el bucle for sobre range(1, 6):\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "5" in res and "for " in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué produce la función range(1, 5) en un bucle for?\n\nOpciones:\n1. Los números del 1 al 4\n2. Los números del 1 al 5\n3. Una lista vacía\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué produce la función range(1, 5) en un bucle for?',
                "opciones": ['Los números del 1 al 4', 'Los números del 1 al 5', 'Una lista vacía'],
                "correcta": 0,
                "explicacion": 'range(inicio, fin) llega hasta fin - 1.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 15,
        "titulo": 'Capítulo 15: Repetición Condicional: El Bucle while',
        "resumen": 'Ejecuta bloques repetidamente mientras se mantenga una condición booleana.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Repetición Condicional: El Bucle while. Ejecuta el código para observar el concepto en acción.',
                "codigo": "contador = 1\nwhile contador <= 3:\n    print('Vuelta:', contador)\n    contador = contador + 1\nprint('Bucle finalizado')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "energia = 3\nwhile energia > 0:\n    print('Energía restante:', energia)\n    energia = energia - 1",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una variable contador = 1. Escribe un bucle while que mientras contador <= 3 imprima print('Paso:', contador) y sume 1 a contador.",
                "codigo": 'contador = 1\n# Escribe el bucle while aquí con contador <= 3:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "3" in res and "while " in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué precaución crucial se debe tomar al programar un bucle while?\n\nOpciones:\n1. Asegurar que la condición cambie para evitar un bucle infinito\n2. Poner punto y coma al final\n3. Usar comillas triples\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué precaución crucial se debe tomar al programar un bucle while?',
                "opciones": ['Asegurar que la condición cambie para evitar un bucle infinito', 'Poner punto y coma al final', 'Usar comillas triples'],
                "correcta": 0,
                "explicacion": 'Si la condición nunca se vuelve falsa, el bucle se ejecuta infinitamente bloqueando el programa.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 16,
        "titulo": 'Capítulo 16: Colecciones Clave-Valor: Diccionarios en Python',
        "resumen": 'Asocia pares de información mediante llaves {} con claves y valores.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Colecciones Clave-Valor: Diccionarios en Python. Ejecuta el código para observar el concepto en acción.',
                "codigo": "contacto = {'nombre': 'Carlos', 'telefono': '555-1234'}\nprint('Nombre:', contacto['nombre'])\nprint('Teléfono:', contacto['telefono'])",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "contacto = {'nombre': 'Carlos', 'telefono': '555-1234'}\ncontacto['ciudad'] = 'Madrid'\nprint('Diccionario ampliado:', contacto)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea un diccionario llamado 'precios' con 'manzana': 2 y 'pera': 3. Imprime: print('Precio manzana:', precios['manzana']).",
                "codigo": "# 1. Crea el diccionario precios con 'manzana': 2 y 'pera': 3\n# 2. Imprime: print('Precio manzana:', precios['manzana'])\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "2" in res and "precios" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué delimitador se utiliza para declarar diccionarios en Python?\n\nOpciones:\n1. Llaves {}\n2. Corchetes []\n3. Paréntesis ()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué delimitador se utiliza para declarar diccionarios en Python?',
                "opciones": ['Llaves {}', 'Corchetes []', 'Paréntesis ()'],
                "correcta": 0,
                "explicacion": 'Los diccionarios se declaran entre llaves {} con pares clave: valor.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 17,
        "titulo": 'Capítulo 17: Tuplas y Conjuntos (Sets): Inmutabilidad y Únicos',
        "resumen": 'Usa tuplas para datos fijos que no cambian y conjuntos para colecciones sin duplicados.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Tuplas y Conjuntos (Sets): Inmutabilidad y Únicos. Ejecuta el código para observar el concepto en acción.',
                "codigo": "punto = (10, 20)\nprint('Coordenada X:', punto[0])\nprint('Coordenada Y:', punto[1])",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "numeros = {1, 2, 2, 3, 3, 4}\nprint('Conjunto sin duplicados:', numeros)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una tupla llamada 'coordenadas' con los valores (50, 100). Imprime: print('Coordenadas:', coordenadas).",
                "codigo": "# 1. Crea la tupla coordenadas = (50, 100)\n# 2. Imprime: print('Coordenadas:', coordenadas)\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "50" in res and "100" in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Cuál es la principal diferencia entre una tupla y una lista?\n\nOpciones:\n1. Las tuplas son inmutables (no se pueden modificar)\n2. Las tuplas no aceptan números\n3. Las tuplas solo tienen un elemento\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Cuál es la principal diferencia entre una tupla y una lista?',
                "opciones": ['Las tuplas son inmutables (no se pueden modificar)', 'Las tuplas no aceptan números', 'Las tuplas solo tienen un elemento'],
                "correcta": 0,
                "explicacion": 'Las tuplas son inmutables una vez creadas, lo que garantiza la integridad de los datos.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 18,
        "titulo": 'Capítulo 18: Funciones Propias: Declaración con def y Parámetros',
        "resumen": 'Empaqueta instrucciones reutilizables asignándoles un nombre propio con def.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Funciones Propias: Declaración con def y Parámetros. Ejecuta el código para observar el concepto en acción.',
                "codigo": "def saludar(nombre):\n    print(f'¡Hola, {nombre}! Bienvenido a las funciones.')\n\nsaludar('Elena')\nsaludar('Marcos')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "def calcular_doble(num):\n    print('El doble es:', num * 2)\n\ncalcular_doble(8)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Define una función llamada 'sumar(a, b)' que imprima: print('Resultado:', a + b). Luego invócala con sumar(5, 7).",
                "codigo": "# 1. Define def sumar(a, b):\n# 2. Dentro imprime: print('Resultado:', a + b)\n# 3. Invoca sumar(5, 7)\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "12" in res and "def sumar" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué palabra clave se usa para definir una nueva función en Python?\n\nOpciones:\n1. def\n2. function\n3. fn\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué palabra clave se usa para definir una nueva función en Python?',
                "opciones": ['def', 'function', 'fn'],
                "correcta": 0,
                "explicacion": "La palabra clave 'def' (de define) declara una función.",
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 19,
        "titulo": 'Capítulo 19: Retorno de Resultados: La Sentencia return y Ámbito',
        "resumen": 'Devuelve valores calculados al código que llamó a la función y entiende el alcance local de las variables.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Retorno de Resultados: La Sentencia return y Ámbito. Ejecuta el código para observar el concepto en acción.',
                "codigo": "def multiplicar(a, b):\n    return a * b\n\nresultado = multiplicar(4, 5)\nprint('Resultado obtenido con return:', resultado)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "def es_mayor_de_edad(edad):\n    return edad >= 18\n\nprint('¿Puede votar?:', es_mayor_de_edad(20))",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Define una función 'cuadrado(n)' que retorne n * n usando return. Guarda cuadrado(6) en la variable 'res' e imprime: print('El cuadrado es:', res).",
                "codigo": "# 1. Define def cuadrado(n): con return n * n\n# 2. Guarda res = cuadrado(6)\n# 3. Imprime: print('El cuadrado es:', res)\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "36" in res and "return" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué sucede cuando una función ejecuta la instrucción return?\n\nOpciones:\n1. Finaliza la función y devuelve el valor procesado\n2. Imprime el valor en pantalla\n3. Reinicia la computadora\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué sucede cuando una función ejecuta la instrucción return?',
                "opciones": ['Finaliza la función y devuelve el valor procesado', 'Imprime el valor en pantalla', 'Reinicia la computadora'],
                "correcta": 0,
                "explicacion": 'return concluye la ejecución de la función y entrega el resultado a quien la llamó.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 20,
        "titulo": 'Capítulo 20: Manejo Profesional de Errores: try, except y finally',
        "resumen": 'Evita que tu programa se detenga ante errores inesperados capturando excepciones.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Manejo Profesional de Errores: try, except y finally. Ejecuta el código para observar el concepto en acción.',
                "codigo": "try:\n    divisor = 0\n    resultado = 10 / divisor\n    print(resultado)\nexcept ZeroDivisionError:\n    print('Aviso: No se puede dividir entre cero.')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "try:\n    numero = int('no_es_un_numero')\nexcept ValueError:\n    print('Aviso: El texto no pudo convertirse a número.')\nfinally:\n    print('Bloque finally completado.')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Escribe un bloque try donde dividas 20 entre 0, y en el except ZeroDivisionError imprime: print('Error capturado con éxito').",
                "codigo": '# Escribe aquí el bloque try y except ZeroDivisionError:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "error capturado" in res.lower() and "except" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Para qué sirve la cláusula except en Python?\n\nOpciones:\n1. Para capturar errores específicos y evitar que el programa se cierre\n2. Para crear bucles\n3. Para borrar archivos\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Para qué sirve la cláusula except en Python?',
                "opciones": ['Para capturar errores específicos y evitar que el programa se cierre', 'Para crear bucles', 'Para borrar archivos'],
                "correcta": 0,
                "explicacion": 'except intercepta la excepción permitiendo que el programa maneje la situación con elegancia.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 21,
        "titulo": 'Capítulo 21: Decodificación de Tracebacks y Diagnóstico de Fallos',
        "resumen": 'Aprende a leer el informe de error de Python para ubicar la línea y causa exacta del fallo.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Decodificación de Tracebacks y Diagnóstico de Fallos. Ejecuta el código para observar el concepto en acción.',
                "codigo": "# Un Traceback muestra el archivo, línea y tipo de error:\nprint('Analizando Traceback...')\n# TypeError ocurre al sumar tipos incompatibles:\ntipo_error = 'TypeError: unsupported operand type(s)'\nprint('Diagnóstico:', tipo_error)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "try:\n    lista = [1, 2]\n    print(lista[10])\nexcept IndexError as err:\n    print('Índice fuera de rango:', err)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Corrige el error en el código: convierte '5' a número con int() antes de sumar para que imprima: print('Suma correcta:', 10 + int('5')).",
                "codigo": "# Corrige la suma convirtiendo '5' a int:\nnumero = 10\ntexto = '5'\n# Imprime: print('Suma correcta:', numero + int(texto))\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "15" in res and "suma correcta" in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué tecla rápida de Aprendizaje de Python con NVDA sitúa el cursor directamente en la línea del error del Traceback?\n\nOpciones:\n1. F4\n2. F1\n3. F12\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué tecla rápida de Aprendizaje de Python con NVDA sitúa el cursor directamente en la línea del error del Traceback?',
                "opciones": ['F4', 'F1', 'F12'],
                "correcta": 0,
                "explicacion": 'F4 salta inmediatamente a la línea del error en el editor y lee el diagnóstico.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 22,
        "titulo": 'Capítulo 22: Entrada y Salida de Archivos: with open() para Texto',
        "resumen": 'Guarda y lee información en ficheros del disco duro de forma segura con with open().',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Entrada y Salida de Archivos: with open() para Texto. Ejecuta el código para observar el concepto en acción.',
                "codigo": "# with open garantiza que el archivo se cierre al salir del bloque:\nwith open('saludo.txt', 'w', encoding='utf-8') as f:\n    f.write('¡Hola desde archivo persistente!')\nprint('Archivo escrito con éxito.')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "with open('saludo.txt', 'r', encoding='utf-8') as f:\n    contenido = f.read()\nprint('Contenido leído:', contenido)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Usa with open('mensaje.txt', 'w', encoding='utf-8') as f: y escribe f.write('Python accesible'). Luego imprime: print('Guardado listo').",
                "codigo": "# Escribe el bloque with open('mensaje.txt', 'w', encoding='utf-8') as f:\n# Dentro escribe f.write('Python accesible')\n# Luego imprime: print('Guardado listo')\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "guardado listo" in res.lower() and "with open" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": "Pregunta de verificación conceptual:\n¿Por qué es recomendable usar 'with open()' al trabajar con archivos?\n\nOpciones:\n1. Porque cierra automáticamente el archivo incluso si ocurre un error\n2. Porque encripta los datos\n3. Porque no usa memoria\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": "¿Por qué es recomendable usar 'with open()' al trabajar con archivos?",
                "opciones": ['Porque cierra automáticamente el archivo incluso si ocurre un error', 'Porque encripta los datos', 'Porque no usa memoria'],
                "correcta": 0,
                "explicacion": 'with actúa como administrador de contexto asegurando la liberación de recursos.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 23,
        "titulo": 'Capítulo 23: Paradigma de Objetos: Clases, Instancias y Atributos',
        "resumen": 'Crea moldes del mundo real agrupando datos y comportamientos en clases.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Paradigma de Objetos: Clases, Instancias y Atributos. Ejecuta el código para observar el concepto en acción.',
                "codigo": "class Libro:\n    titulo = 'Aprendizaje de Python'\n    paginas = 200\n\nmi_libro = Libro()\nprint('Título del libro:', mi_libro.titulo)\nprint('Páginas:', mi_libro.paginas)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Dispositivo:\n    tipo = 'Lector de pantalla'\n\nlector = Dispositivo()\nlector.nombre = 'NVDA'\nprint('Dispositivo:', lector.nombre, 'Tipo:', lector.tipo)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una clase llamada 'Mascota' con un atributo de clase especie = 'Perro'. Crea un objeto perro = Mascota() e imprime: print('Especie:', perro.especie).",
                "codigo": "# 1. Declara class Mascota: con especie = 'Perro'\n# 2. Crea perro = Mascota()\n# 3. Imprime: print('Especie:', perro.especie)\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "perro" in res.lower() and "class Mascota" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué es una clase en programación orientada a objetos?\n\nOpciones:\n1. Un molde o plantilla para crear objetos con datos y funciones\n2. Una variable numérica\n3. Un bucle de repetición\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué es una clase en programación orientada a objetos?',
                "opciones": ['Un molde o plantilla para crear objetos con datos y funciones', 'Una variable numérica', 'Un bucle de repetición'],
                "correcta": 0,
                "explicacion": 'Una clase es el plano estructural a partir del cual se instancian los objetos.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 24,
        "titulo": 'Capítulo 24: El Constructor __init__ y el Parámetro self',
        "resumen": 'Inicializa objetos con valores específicos en el momento exacto de su creación.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre El Constructor __init__ y el Parámetro self. Ejecuta el código para observar el concepto en acción.',
                "codigo": "class Persona:\n    def __init__(self, nombre, edad):\n        self.nombre = nombre\n        self.edad = edad\n\np1 = Persona('Sofía', 28)\nprint(f'{p1.nombre} tiene {p1.edad} años.')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Cuenta:\n    def __init__(self, titular, saldo):\n        self.titular = titular\n        self.saldo = saldo\n\nc = Cuenta('Kevin', 500)\nprint('Titular:', c.titular, 'Saldo:', c.saldo)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una clase Usuario con def __init__(self, apodo): que asigne self.apodo = apodo. Crea u = Usuario('Programador') e imprime: print('Apodo:', u.apodo).",
                "codigo": "# 1. Crea class Usuario con __init__(self, apodo)\n# 2. Crea u = Usuario('Programador')\n# 3. Imprime: print('Apodo:', u.apodo)\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "programador" in res.lower() and "__init__" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Cuál es la función del método especial __init__?\n\nOpciones:\n1. Es el constructor que inicializa los atributos del objeto al crearlo\n2. Es una función para borrar el objeto\n3. Es un bucle for\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Cuál es la función del método especial __init__?',
                "opciones": ['Es el constructor que inicializa los atributos del objeto al crearlo', 'Es una función para borrar el objeto', 'Es un bucle for'],
                "correcta": 0,
                "explicacion": '__init__ se ejecuta automáticamente al instanciar un nuevo objeto.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 25,
        "titulo": 'Capítulo 25: Métodos de Instancia y Encapsulamiento',
        "resumen": 'Define acciones que cada objeto sabe realizar de forma autónoma.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Métodos de Instancia y Encapsulamiento. Ejecuta el código para observar el concepto en acción.',
                "codigo": "class Reproductor:\n    def __init__(self, cancion):\n        self.cancion = cancion\n    def reproducir(self):\n        print(f'Reproduciendo la pista: {self.cancion}')\n\nrep = Reproductor('Sinfonía Accesible')\nrep.reproducir()",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Termostato:\n    def __init__(self, temp):\n        self.temp = temp\n    def subir(self, grados):\n        self.temp += grados\n        print('Nueva temperatura:', self.temp)\n\nt = Termostato(20)\nt.subir(3)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una clase Saludo con def __init__(self, nombre): y un método saludar(self) que imprima: print(f'Hola, {self.nombre}'). Crea s = Saludo('Amigo') e invoca s.saludar().",
                "codigo": "# 1. Crea class Saludo con __init__(self, nombre) y método saludar(self)\n# 2. Crea s = Saludo('Amigo')\n# 3. Invoca s.saludar()\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "amigo" in res.lower() and "saludar" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué representa el primer parámetro 'self' en los métodos de una clase?\n\nOpciones:\n1. La referencia a la instancia específica del objeto que invocó el método\n2. Una palabra reservada de Windows\n3. Un número entero\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": "¿Qué representa el primer parámetro 'self' en los métodos de una clase?",
                "opciones": ['La referencia a la instancia específica del objeto que invocó el método', 'Una palabra reservada de Windows', 'Un número entero'],
                "correcta": 0,
                "explicacion": 'self permite que el método acceda y modifique los atributos de ese objeto en particular.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 26,
        "titulo": 'Capítulo 26: Herencia de Clases: Reutilización con super()',
        "resumen": 'Crea clases hijas especializadas que heredan propiedades de una clase padre.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Herencia de Clases: Reutilización con super(). Ejecuta el código para observar el concepto en acción.',
                "codigo": "class Animal:\n    def __init__(self, nombre):\n        self.nombre = nombre\n\nclass Perro(Animal):\n    def ladrar(self):\n        print(f'{self.nombre} dice: ¡Guau guau!')\n\nmi_perro = Perro('Toby')\nmi_perro.ladrar()",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Empleado:\n    def __init__(self, nombre, sueldo):\n        self.nombre = nombre\n        self.sueldo = sueldo\n\nclass Gerente(Empleado):\n    def __init__(self, nombre, sueldo, bono):\n        super().__init__(nombre, sueldo)\n        self.bono = bono\n\ng = Gerente('Marta', 3000, 500)\nprint('Gerente:', g.nombre, 'Total:', g.sueldo + g.bono)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una clase Vehiculo con __init__(self, marca). Crea una clase Coche(Vehiculo) que en su __init__(self, marca, modelo) use super().__init__(marca) y self.modelo = modelo. Crea c = Coche('Toyota', 'Corolla') e imprime: print(c.marca, c.modelo).",
                "codigo": "# 1. Crea class Vehiculo con __init__(self, marca)\n# 2. Crea class Coche(Vehiculo) usando super().__init__(marca)\n# 3. Crea c = Coche('Toyota', 'Corolla') e imprime print(c.marca, c.modelo)\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "toyota" in res.lower() and "corolla" in res.lower() and "super()" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué función permite invocar el constructor o métodos de la clase padre en la clase hija?\n\nOpciones:\n1. super()\n2. parent()\n3. base()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué función permite invocar el constructor o métodos de la clase padre en la clase hija?',
                "opciones": ['super()', 'parent()', 'base()'],
                "correcta": 0,
                "explicacion": 'super() otorga acceso directo a la clase base facilitando la extensión de código.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 27,
        "titulo": 'Capítulo 27: Polimorfismo y Métodos Especiales (__str__)',
        "resumen": 'Personaliza cómo el lector de pantalla y print leen tus objetos implementando __str__.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Polimorfismo y Métodos Especiales (__str__). Ejecuta el código para observar el concepto en acción.',
                "codigo": "class Alumno:\n    def __init__(self, nombre, curso):\n        self.nombre = nombre\n        self.curso = curso\n    def __str__(self):\n        return f'Alumno: {self.nombre}, Curso: {self.curso}'\n\nalumno = Alumno('David', 'Python')\nprint(alumno)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Producto:\n    def __init__(self, item, precio):\n        self.item = item\n        self.precio = precio\n    def __str__(self):\n        return f'Producto: {self.item} (${self.precio})'\n\nprint(Producto('Teclado accesible', 45))",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una clase Punto con __init__(self, x, y) y un método especial __str__(self) que devuelva f'Punto({self.x}, {self.y})'. Crea p = Punto(3, 7) e imprímelo con print(p).",
                "codigo": "# 1. Crea class Punto con __init__(self, x, y)\n# 2. Implementa def __str__(self): return f'Punto({self.x}, {self.y})'\n# 3. Imprime print(Punto(3, 7))\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: ("3" in res and "7" in res and "__str__" in src)
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Para qué sirve implementar el método especial __str__ en una clase?\n\nOpciones:\n1. Para definir la representación textual legible al imprimir el objeto con print()\n2. Para borrar el objeto de la memoria\n3. Para convertirlo en lista\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Para qué sirve implementar el método especial __str__ en una clase?',
                "opciones": ['Para definir la representación textual legible al imprimir el objeto con print()', 'Para borrar el objeto de la memoria', 'Para convertirlo en lista'],
                "correcta": 0,
                "explicacion": '__str__ devuelve una cadena amigable y comprensible para el lector de pantalla.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 28,
        "titulo": 'Capítulo 28: Módulos de la Biblioteca Estándar (math, random, datetime)',
        "resumen": 'Aprovecha librerías integradas de Python para matemáticas, azar y fechas sin instalar nada.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Módulos de la Biblioteca Estándar (math, random, datetime). Ejecuta el código para observar el concepto en acción.',
                "codigo": "import math\nprint('Raíz cuadrada de 64:', math.isqrt(64))\nprint('Valor de Pi redondeado:', round(math.pi, 4))",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "import random\nazar = random.randint(1, 10)\nprint('Número aleatorio entre 1 y 10:', azar)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Importa el módulo math y calcula la raíz cuadrada entera de 144 con math.isqrt(144). Imprime: print('Raíz de 144:', math.isqrt(144)).",
                "codigo": "# 1. import math\n# 2. Imprime: print('Raíz de 144:', math.isqrt(144))\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "12" in res and "math" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué palabra clave se usa para cargar módulos de la biblioteca estándar de Python?\n\nOpciones:\n1. import\n2. load\n3. include\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué palabra clave se usa para cargar módulos de la biblioteca estándar de Python?',
                "opciones": ['import', 'load', 'include'],
                "correcta": 0,
                "explicacion": 'import enlaza cualquier biblioteca estándar o archivo externo en tu código.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 29,
        "titulo": 'Capítulo 29: Persistencia Estructurada: Formato JSON y Serialización',
        "resumen": 'Guarda y lee diccionarios estructurados en formato de texto estándar JSON.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Persistencia Estructurada: Formato JSON y Serialización. Ejecuta el código para observar el concepto en acción.',
                "codigo": "import json\ndatos = {'usuario': 'Elena', 'nivel': 3, 'activo': True}\ntexto_json = json.dumps(datos)\nprint('Texto en formato JSON:', texto_json)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": 'import json\ntexto = \'{"curso": "Python", "duracion_horas": 40}\'\nobjeto = json.loads(texto)\nprint(\'Curso decodificado:\', objeto[\'curso\'])',
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Importa json. Crea un diccionario config = {'tema': 'oscuro', 'fuente': 14}. Conviértelo a texto JSON con json.dumps(config) e imprime: print('JSON:', json.dumps(config)).",
                "codigo": "import json\n# 1. Crea config = {'tema': 'oscuro', 'fuente': 14}\n# 2. Imprime: print('JSON:', json.dumps(config))\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "oscuro" in res.lower() and "json.dumps" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué función del módulo json convierte un diccionario de Python en una cadena de texto JSON?\n\nOpciones:\n1. json.dumps()\n2. json.loads()\n3. json.parse()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué función del módulo json convierte un diccionario de Python en una cadena de texto JSON?',
                "opciones": ['json.dumps()', 'json.loads()', 'json.parse()'],
                "correcta": 0,
                "explicacion": 'json.dumps() (dump string) serializa objetos de Python a texto JSON.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 30,
        "titulo": 'Capítulo 30: Bases de Datos Relacionales con SQLite: Tablas y Consultas',
        "resumen": 'Gestiona datos organizados en tablas usando SQL integrado y el módulo sqlite3.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Bases de Datos Relacionales con SQLite: Tablas y Consultas. Ejecuta el código para observar el concepto en acción.',
                "codigo": 'import sqlite3\ncon = sqlite3.connect(\':memory:\')\ncur = con.cursor()\ncur.execute(\'CREATE TABLE notas (id INTEGER, titulo TEXT)\')\ncur.execute("INSERT INTO notas VALUES (1, \'Mi primera nota en SQLite\')")\ncon.commit()\ncur.execute(\'SELECT titulo FROM notas\')\nprint(\'Nota en base de datos:\', cur.fetchone()[0])\ncon.close()',
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": 'import sqlite3\ncon = sqlite3.connect(\':memory:\')\ncur = con.cursor()\ncur.execute(\'CREATE TABLE usuarios (nombre TEXT, edad INT)\')\ncur.execute("INSERT INTO usuarios VALUES (\'Carlos\', 30)")\ncur.execute(\'SELECT COUNT(*) FROM usuarios\')\nprint(\'Total usuarios en BD:\', cur.fetchone()[0])\ncon.close()',
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una base de datos SQLite en memoria con con = sqlite3.connect(':memory:'), crea una tabla productos (nombre TEXT) e inserta 'Teclado'. Luego consulta con SELECT y muestra el producto.",
                "codigo": 'import sqlite3\ncon = sqlite3.connect(\':memory:\')\ncur = con.cursor()\n# 1. cur.execute(\'CREATE TABLE productos (nombre TEXT)\')\n# 2. cur.execute("INSERT INTO productos VALUES (\'Teclado\')")\n# 3. cur.execute(\'SELECT nombre FROM productos\')\n# 4. Imprime: print(\'Producto:\', cur.fetchone()[0])\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "teclado" in res.lower() and "sqlite3" in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué instrucción SQL se utiliza para consultar y extraer registros de una tabla?\n\nOpciones:\n1. SELECT\n2. INSERT\n3. DELETE\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué instrucción SQL se utiliza para consultar y extraer registros de una tabla?',
                "opciones": ['SELECT', 'INSERT', 'DELETE'],
                "correcta": 0,
                "explicacion": 'SELECT es la sentencia fundamental de consulta en SQL.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 31,
        "titulo": 'Capítulo 31: Consumo de Servicios Web: Peticiones HTTP y Respuestas JSON',
        "resumen": 'Comunícate con servidores en internet para obtener datos actualizados.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Consumo de Servicios Web: Peticiones HTTP y Respuestas JSON. Ejecuta el código para observar el concepto en acción.',
                "codigo": "# Simulación estructurada de consumo de API REST:\nrespuesta_api = {\n    'status': 200,\n    'datos': {'temperatura': 22, 'clima': 'Despejado'}\n}\nif respuesta_api['status'] == 200:\n    clima = respuesta_api['datos']['clima']\n    print(f'Reporte meteorológico de la API: {clima}')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "respuesta = {\n    'codigo': 200,\n    'usuarios': ['Andrea', 'Pablo', 'Lucía']\n}\nprint('Usuarios recibidos del servidor:', len(respuesta['usuarios']))",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Dada la respuesta simulada resp = {'estado': 'OK', 'mensaje': 'Servicio disponible'}, comprueba si resp['estado'] == 'OK' e imprime: print('API:', resp['mensaje']).",
                "codigo": "resp = {'estado': 'OK', 'mensaje': 'Servicio disponible'}\n# Comprueba si resp['estado'] == 'OK' e imprime print('API:', resp['mensaje'])\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "servicio disponible" in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué código de estado HTTP estándar indica que una petición web se resolvió con éxito?\n\nOpciones:\n1. 200 (OK)\n2. 404 (Not Found)\n3. 500 (Internal Error)\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué código de estado HTTP estándar indica que una petición web se resolvió con éxito?',
                "opciones": ['200 (OK)', '404 (Not Found)', '500 (Internal Error)'],
                "correcta": 0,
                "explicacion": 'El código 200 indica éxito en peticiones HTTP.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },
    {
        "id": 32,
        "titulo": 'Capítulo 32: Calidad de Software: Pruebas Unitarias con unittest',
        "resumen": 'Verifica automáticamente que cada parte de tu código funcione como se espera sin errores.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Calidad de Software: Pruebas Unitarias con unittest. Ejecuta el código para observar el concepto en acción.',
                "codigo": "def multiplicar(a, b):\n    return a * b\n\n# Verificación manual con assert:\nassert multiplicar(3, 4) == 12\nprint('Prueba unitaria superada: 3 * 4 = 12')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "def restar(a, b):\n    return a - b\n\nassert restar(10, 4) == 6\nprint('Prueba de resta exitosa.')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Define una función es_par(numero) que retorne numero % 2 == 0. Escribe assert es_par(4) == True y luego imprime: print('Todas las pruebas pasaron con éxito').",
                "codigo": "# 1. Define def es_par(numero): return numero % 2 == 0\n# 2. assert es_par(4) == True\n# 3. Imprime: print('Todas las pruebas pasaron con éxito')\n\n",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: "todas las pruebas" in res.lower() or "éxito" in res.lower() or "exito" in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Cuál es el propósito primordial de escribir pruebas unitarias?\n\nOpciones:\n1. Verificar de forma automática que cada pequeña parte del código funciona como se espera\n2. Hacer que el programa corra más rápido\n3. Cambiar el color del editor\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Cuál es el propósito primordial de escribir pruebas unitarias?',
                "opciones": ['Verificar de forma automática que cada pequeña parte del código funciona como se espera', 'Hacer que el programa corra más rápido', 'Cambiar el color del editor'],
                "correcta": 0,
                "explicacion": 'Las pruebas unitarias garantizan que el código cumpla sus requisitos y previenen regresiones en el software.',
                "validar": lambda src, res, ns: '1' in "".join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")])
            },
        ]
    },

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
