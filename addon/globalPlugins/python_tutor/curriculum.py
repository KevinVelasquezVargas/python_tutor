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
                "validar": lambda src, res, ns: 'algoritmo' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación: La importancia del orden',
                "tipo": 'experimentar',
                "instruccion": "Si alteramos el orden de las instrucciones, el resultado final no tendrá sentido. Añade una línea intermedia que diga: print('Paso intermedio: Colocar la bolsita de té.') y pulsa Control + Enter.",
                "codigo": "print('Paso 1: Calentar el agua.')\nprint('Paso intermedio: Colocar la bolsita de té.')\nprint('Paso 2: Servir el agua caliente en la taza.')",
                "pistas": ['Asegúrate de escribir la instrucción print con el texto entre comillas.'],
                "validar": lambda src, res, ns: 'bolsita' in res.lower() and 'servir' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Algoritmo de lavado de manos',
                "tipo": 'desafio',
                "instruccion": "Escribe un algoritmo de 3 pasos para lavarse las manos con tres print(): 1. 'Abrir el grifo y mojar las manos', 2. 'Aplicar jabón y frotar', 3. 'Enjuagar y secar'. Ejecuta con Control + Enter.",
                "codigo": "print('1. Abrir el grifo y mojar las manos')\nprint('2. Aplicar jabón y frotar')\nprint('3. Enjuagar y secar')",
                "salida_esperada": '1. Abrir el grifo y mojar las manos\n2. Aplicar jabón y frotar\n3. Enjuagar y secar',
                "pistas": ['Usa tres instrucciones print independientes, una en cada renglón.'],
                "validar": lambda src, res, ns: 'jabón' in res.lower() or 'jabon' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Cuál es la definición más exacta de un algoritmo?\n\nOpciones:\n1. Un componente físico de la computadora como el procesador.\n2. Una serie ordenada y finita de instrucciones lógicas para resolver un problema.\n3. Un virus informático que altera los programas.\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Cuál es la definición más exacta de un algoritmo?',
                "opciones": ['Un componente físico de la computadora como el procesador.', 'Una serie ordenada y finita de instrucciones lógicas para resolver un problema.', 'Un virus informático que altera los programas.'],
                "correcta": 1,
                "explicacion": 'Un algoritmo es la secuencia lógica y paso a paso que describe la solución a un problema determinado.',
                "pistas": ['Recuerda el ejemplo de la preparación del té.'],
                "validar": lambda src, res, ns: '2' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
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
                "validar": lambda src, res, ns: 'nvda' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación: La memoria es modificable',
                "tipo": 'experimentar',
                "instruccion": 'En la memoria RAM podemos reemplazar el contenido de una variable en cualquier instante. Observa cómo cambia la variable y pulsa Control + Enter.',
                "codigo": "estado = 'Cargando datos'\nprint('Estado inicial:', estado)\nestado = 'Listo para programar'\nprint('Estado final:', estado)",
                "pistas": ['Ejecuta con Control + Enter para escuchar los dos estados secuenciales.'],
                "validar": lambda src, res, ns: 'inicial' in res.lower() and 'final' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Variables y salida',
                "tipo": 'desafio',
                "instruccion": "Crea una variable llamada 'usuario' con el texto 'Estudiante' y muestra en consola: print('Bienvenido/a,', usuario). Pulsa Control + Enter.",
                "codigo": "usuario = 'Estudiante'\nprint('Bienvenido/a,', usuario)",
                "salida_esperada": 'Bienvenido/a, Estudiante',
                "pistas": ["Define usuario = 'Estudiante' y pásala como segundo argumento a print."],
                "validar": lambda src, res, ns: 'bienvenido' in res.lower() and 'estudiante' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Dónde se almacenan las variables mientras tu script de Python se está ejecutando?\n\nOpciones:\n1. En la Memoria RAM del equipo.\n2. En la tecla Escape del teclado.\n3. En el cable de corriente.\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Dónde se almacenan las variables mientras tu script de Python se está ejecutando?',
                "opciones": ['En la Memoria RAM del equipo.', 'En la tecla Escape del teclado.', 'En el cable de corriente.'],
                "correcta": 0,
                "explicacion": 'La Memoria RAM es el espacio de trabajo rápido donde residen los datos activos de los programas en ejecución.',
                "pistas": ['Es la memoria principal de acceso aleatorio.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
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
                "validar": lambda src, res, ns: 'true' in res.lower() and 'false' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación: Operadores and, or y not',
                "tipo": 'experimentar',
                "instruccion": "El operador 'and' exige que ambas condiciones sean verdaderas. El operador 'or' solo requiere que al menos una lo sea. Ejecuta el código y analiza el resultado.",
                "codigo": "llave = True\nclave = False\nprint('¿Puede entrar con llave O clave?:', llave or clave)\nprint('¿Cumple llave Y clave?:', llave and clave)",
                "pistas": ['Observa cómo or devuelve True pero and devuelve False.'],
                "validar": lambda src, res, ns: 'true' in res.lower() and 'false' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Verificación de acceso',
                "tipo": 'desafio',
                "instruccion": "Crea una variable llamada 'edad' con el valor 20 y una variable 'tiene_identificacion' con True. Luego crea 'autorizado = (edad >= 18) and tiene_identificacion'. Imprime print('Acceso permitido:', autorizado).",
                "codigo": "edad = 20\ntiene_identificacion = True\nautorizado = (edad >= 18) and tiene_identificacion\nprint('Acceso permitido:', autorizado)",
                "salida_esperada": 'Acceso permitido: True',
                "pistas": ['Une ambas condiciones con el operador and.'],
                "validar": lambda src, res, ns: 'true' in res.lower() and 'acceso' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué resultado produce la expresión booleana: not False?\n\nOpciones:\n1. True\n2. False\n3. None\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué resultado produce la expresión booleana: not False?',
                "opciones": ['True', 'False', 'None'],
                "correcta": 0,
                "explicacion": "El operador 'not' invierte el valor lógico: si niegas False obtienes True.",
                "pistas": ['not es el operador de negación inversa.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 4,
        "titulo": 'Capítulo 4: Nuestra Primera Instrucción: La Función print()',
        "resumen": 'Aprende a emitir información hacia la salida estándar y escucharla en tu lector de pantalla.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 4: Nuestra Primera Instrucción: La Función print(). Ejecuta el código para observar el concepto en acción.',
                "codigo": "print('¡Hola mundo desde Python accesible!')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "print('Python', 'es', 'fácil', 'y', 'accesible')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 4: Nuestra Primera Instrucción: La Función print(). Completa el código requerido y ejecuta para validar.',
                "codigo": "print('Aprendiendo Python con NVDA')",
                "salida_esperada": 'Aprendiendo Python con NVDA',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'nvda' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué función se utiliza en Python para enviar datos a la salida y lector?\n\nOpciones:\n1. print()\n2. input()\n3. exit()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué función se utiliza en Python para enviar datos a la salida y lector?',
                "opciones": ['print()', 'input()', 'exit()'],
                "correcta": 0,
                "explicacion": 'print() es la función de salida estándar por excelencia.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 5,
        "titulo": 'Capítulo 5: Almacenamiento en Memoria: Variables y Asignación',
        "resumen": 'Aprende a guardar valores en memoria asignándoles un nombre con el signo igual (=).',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 5: Almacenamiento en Memoria: Variables y Asignación. Ejecuta el código para observar el concepto en acción.',
                "codigo": "nombre = 'Kevin'\nedad = 25\nprint(nombre, 'tiene', edad, 'años')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "puntos = 100\nprint('Puntuación inicial:', puntos)\npuntos = puntos + 50\nprint('Puntuación acumulada:', puntos)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 5: Almacenamiento en Memoria: Variables y Asignación. Completa el código requerido y ejecuta para validar.',
                "codigo": "lenguaje = 'Python'\nprint('Estoy programando en:', lenguaje)",
                "salida_esperada": 'Estoy programando en: Python',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'python' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué símbolo se usa en Python para asignar un valor a una variable?\n\nOpciones:\n1. El signo igual (=)\n2. El signo de suma (+)\n3. El punto y coma (;)\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué símbolo se usa en Python para asignar un valor a una variable?',
                "opciones": ['El signo igual (=)', 'El signo de suma (+)', 'El punto y coma (;)'],
                "correcta": 0,
                "explicacion": 'El signo igual simple (=) asigna lo que está a la derecha en la variable de la izquierda.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 6,
        "titulo": 'Capítulo 6: Tipos de Datos Primitivos: Números Enteros y Decimales',
        "resumen": 'Opera con números enteros (int) y números decimales (float) realizando cálculos matemáticos.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 6: Tipos de Datos Primitivos: Números Enteros y Decimales. Ejecuta el código para observar el concepto en acción.',
                "codigo": "precio = 19.50\ncantidad = 3\ntotal = precio * cantidad\nprint('Total a pagar:', total)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "radio = 4\npi = 3.1416\narea = pi * (radio ** 2)\nprint('Área del círculo:', round(area, 2))",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 6: Tipos de Datos Primitivos: Números Enteros y Decimales. Completa el código requerido y ejecuta para validar.',
                "codigo": "base = 10\naltura = 5\narea = (base * altura) / 2\nprint('Área del triángulo:', area)",
                "salida_esperada": 'Área del triángulo: 25.0',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: '25' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Cómo se denomina en Python a un número que tiene parte decimal (por ejemplo 3.14)?\n\nOpciones:\n1. float\n2. int\n3. bool\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Cómo se denomina en Python a un número que tiene parte decimal (por ejemplo 3.14)?',
                "opciones": ['float', 'int', 'bool'],
                "correcta": 0,
                "explicacion": 'float representa números de punto flotante o decimales.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 7,
        "titulo": 'Capítulo 7: Cadenas de Texto (Strings): Comillas y Concatenación',
        "resumen": 'Manipula textos, une cadenas mediante el operador + y usa cadenas formateadas (f-strings).',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 7: Cadenas de Texto (Strings): Comillas y Concatenación. Ejecuta el código para observar el concepto en acción.',
                "codigo": "nombre = 'Ana'\nrol = 'Desarrolladora'\nprint(f'{nombre} es {rol}')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "frase = 'La accesibilidad es un derecho.'\nprint('Longitud de caracteres:', len(frase))\nprint('En mayúsculas:', frase.upper())",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 7: Cadenas de Texto (Strings): Comillas y Concatenación. Completa el código requerido y ejecuta para validar.',
                "codigo": "ciudad = 'Bogotá'\npais = 'Colombia'\nprint(f'Ubicación: {ciudad}, {pais}')",
                "salida_esperada": 'Ubicación: Bogotá, Colombia',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'bogot' in res.lower() or 'colombia' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué letra precede a las comillas para crear una cadena formateada (f-string)?\n\nOpciones:\n1. La letra f\n2. La letra p\n3. La letra s\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué letra precede a las comillas para crear una cadena formateada (f-string)?',
                "opciones": ['La letra f', 'La letra p', 'La letra s'],
                "correcta": 0,
                "explicacion": "Las f-strings inician con f antes de las comillas: f'Texto {variable}'.",
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 8,
        "titulo": 'Capítulo 8: Interacción con el Usuario: Entrada con input()',
        "resumen": 'Aprende a solicitar datos al usuario desde el teclado y a convertirlos con int() y float().',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 8: Interacción con el Usuario: Entrada con input(). Ejecuta el código para observar el concepto en acción.',
                "codigo": "nombre = 'Kevin'\nprint('Bienvenido/a al sistema, ' + nombre)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "anio_nacimiento = '2000'\nedad = 2026 - int(anio_nacimiento)\nprint('Edad estimada:', edad)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 8: Interacción con el Usuario: Entrada con input(). Completa el código requerido y ejecuta para validar.',
                "codigo": "edad_texto = '20'\nedad = int(edad_texto)\nprint('El próximo año tendrás:', edad + 1)",
                "salida_esperada": 'El próximo año tendrás: 21',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: '21' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué tipo de dato devuelve por defecto la función input()?\n\nOpciones:\n1. Siempre una cadena de texto (str)\n2. Un número entero (int)\n3. Un booleano (bool)\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué tipo de dato devuelve por defecto la función input()?',
                "opciones": ['Siempre una cadena de texto (str)', 'Un número entero (int)', 'Un booleano (bool)'],
                "correcta": 0,
                "explicacion": 'input() siempre devuelve el texto tecleado como string (str).',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 9,
        "titulo": 'Capítulo 9: Operadores de Comparación y Expresiones Condicionales',
        "resumen": 'Compara cantidades con ==, !=, <, >, <= y >= para generar decisiones computacionales.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 9: Operadores de Comparación y Expresiones Condicionales. Ejecuta el código para observar el concepto en acción.',
                "codigo": "saldo = 100\nprecio = 80\nprint('¿Alcanza el dinero?:', saldo >= precio)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "clave_guardada = 'secreto123'\nclave_ingresada = 'secreto123'\nprint('¿Clave correcta?:', clave_guardada == clave_ingresada)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 9: Operadores de Comparación y Expresiones Condicionales. Completa el código requerido y ejecuta para validar.',
                "codigo": "puntos = 85\nprint('¿Aprobó con 70 o más?:', puntos >= 70)",
                "salida_esperada": '¿Aprobó con 70 o más?: True',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'true' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué operador se utiliza en Python para comparar si dos valores son exactamente iguales?\n\nOpciones:\n1. Doble signo igual (==)\n2. Un solo signo igual (=)\n3. Signo de admiración (!)\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué operador se utiliza en Python para comparar si dos valores son exactamente iguales?',
                "opciones": ['Doble signo igual (==)', 'Un solo signo igual (=)', 'Signo de admiración (!)'],
                "correcta": 0,
                "explicacion": 'El doble signo igual (==) compara igualdad. El signo simple (=) asigna variables.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 10,
        "titulo": 'Capítulo 10: Bifurcación Básica: Estructura if y Sangría PEP 8',
        "resumen": 'Aprende a bifurcar la ejecución de un programa según condiciones y a dominar la sangría de 4 espacios.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 10: Bifurcación Básica: Estructura if y Sangría PEP 8. Ejecuta el código para observar el concepto en acción.',
                "codigo": "temperatura = 30\nif temperatura > 25:\n    print('Hace calor, usa ropa fresca.')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "puntuacion = 95\nif puntuacion >= 90:\n    print('¡Felicidades!')\n    print('Has alcanzado el nivel superior.')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 10: Bifurcación Básica: Estructura if y Sangría PEP 8. Completa el código requerido y ejecuta para validar.',
                "codigo": "hora = 14\nif hora >= 12:\n    print('Buenas tardes')",
                "salida_esperada": 'Buenas tardes',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'buenas tardes' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Cuántos espacios en blanco recomienda la guía PEP 8 para cada nivel de sangría?\n\nOpciones:\n1. 4 espacios\n2. 1 espacio\n3. 8 espacios\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Cuántos espacios en blanco recomienda la guía PEP 8 para cada nivel de sangría?',
                "opciones": ['4 espacios', '1 espacio', '8 espacios'],
                "correcta": 0,
                "explicacion": 'PEP 8 establece exactamente 4 espacios por nivel de indentación.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 11,
        "titulo": 'Capítulo 11: Alternativas Múltiples: Bloques elif y else',
        "resumen": 'Gestiona múltiples caminos lógicos en tus programas encadenando condiciones con elif y else.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 11: Alternativas Múltiples: Bloques elif y else. Ejecuta el código para observar el concepto en acción.',
                "codigo": "nota = 8\nif nota >= 9:\n    print('Excelente')\nelif nota >= 7:\n    print('Aprobado')\nelse:\n    print('Reprobado')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "hora = 8\nif hora < 12:\n    print('Buenos días')\nelif hora < 18:\n    print('Buenas tardes')\nelse:\n    print('Buenas noches')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 11: Alternativas Múltiples: Bloques elif y else. Completa el código requerido y ejecuta para validar.',
                "codigo": "semaforo = 'verde'\nif semaforo == 'verde':\n    print('Avanzar')\nelse:\n    print('Detenerse')",
                "salida_esperada": 'Avanzar',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'avanzar' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué cláusula se ejecuta cuando ninguna de las condiciones de un if o elif fue verdadera?\n\nOpciones:\n1. else\n2. while\n3. pass\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué cláusula se ejecuta cuando ninguna de las condiciones de un if o elif fue verdadera?',
                "opciones": ['else', 'while', 'pass'],
                "correcta": 0,
                "explicacion": 'La cláusula else es la rama por defecto cuando ninguna condición previa se cumplió.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 12,
        "titulo": 'Capítulo 12: Colecciones Ordenadas: Introducción a las Listas',
        "resumen": 'Organiza secuencias de elementos entre corchetes [] y accede a ellos mediante índices numéricos.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 12: Colecciones Ordenadas: Introducción a las Listas. Ejecuta el código para observar el concepto en acción.',
                "codigo": "colores = ['rojo', 'verde', 'azul']\nprint('Primer color:', colores[0])\nprint('Último color:', colores[-1])",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "numeros = [10, 20, 30, 40]\nprint('Segundo número:', numeros[1])\nprint('Total en lista:', len(numeros))",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 12: Colecciones Ordenadas: Introducción a las Listas. Completa el código requerido y ejecuta para validar.',
                "codigo": "materias = ['Matemáticas', 'Historia', 'Programación']\nprint('Favorita:', materias[2])",
                "salida_esperada": 'Favorita: Programación',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'programaci' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿En qué número comienza el índice del primer elemento de una lista en Python?\n\nOpciones:\n1. En el número 0\n2. En el número 1\n3. En el número -1\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿En qué número comienza el índice del primer elemento de una lista en Python?',
                "opciones": ['En el número 0', 'En el número 1', 'En el número -1'],
                "correcta": 0,
                "explicacion": 'Python utiliza indexación basada en cero (base 0).',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 13,
        "titulo": 'Capítulo 13: Métodos Fundamentales de Listas (append, remove, pop, len)',
        "resumen": 'Modifica listas dinámicamente añadiendo, eliminando y contando elementos con métodos integrados.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 13: Métodos Fundamentales de Listas (append, remove, pop, len). Ejecuta el código para observar el concepto en acción.',
                "codigo": "tareas = ['Leer', 'Escribir']\ntareas.append('Practicar')\nprint('Total de tareas:', len(tareas))",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "lista = ['a', 'b', 'c']\nlista.append('d')\neliminado = lista.pop(0)\nprint('Quedaron:', lista)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 13: Métodos Fundamentales de Listas (append, remove, pop, len). Completa el código requerido y ejecuta para validar.',
                "codigo": "frutas = ['Manzana', 'Pera']\nfrutas.append('Naranja')\nprint('Frutas:', frutas)",
                "salida_esperada": "Frutas: ['Manzana', 'Pera', 'Naranja']",
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'naranja' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué método de lista añade un nuevo elemento al final de la misma?\n\nOpciones:\n1. append()\n2. remove()\n3. split()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué método de lista añade un nuevo elemento al final de la misma?',
                "opciones": ['append()', 'remove()', 'split()'],
                "correcta": 0,
                "explicacion": 'append(elemento) agrega el nuevo valor al final de la lista.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 14,
        "titulo": 'Capítulo 14: Repetición y Automatización: El Bucle for y range()',
        "resumen": 'Automatiza tareas repetitivas recorriendo colecciones o secuencias numéricas generadas con range().',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 14: Repetición y Automatización: El Bucle for y range(). Ejecuta el código para observar el concepto en acción.',
                "codigo": "for i in range(1, 4):\n    print('Vuelta número:', i)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "frutas = ['fresa', 'uva', 'mango']\nfor f in frutas:\n    print('Me gusta la:', f)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 14: Repetición y Automatización: El Bucle for y range(). Completa el código requerido y ejecuta para validar.',
                "codigo": "total = 0\nfor n in [10, 20, 30]:\n    total += n\nprint('Suma total:', total)",
                "salida_esperada": 'Suma total: 60',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: '60' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\nSi escribes range(5), ¿cuáles son los números enteros generados?\n\nOpciones:\n1. Del 0 al 4\n2. Del 1 al 5\n3. Del 0 al 5\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": 'Si escribes range(5), ¿cuáles son los números enteros generados?',
                "opciones": ['Del 0 al 4', 'Del 1 al 5', 'Del 0 al 5'],
                "correcta": 0,
                "explicacion": 'range(n) genera n números desde 0 hasta n-1 inclusive.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 15,
        "titulo": 'Capítulo 15: Repetición Condicional: El Bucle while',
        "resumen": 'Ejecuta un bloque de código reiteradamente mientras una condición lógica continúe siendo verdadera.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 15: Repetición Condicional: El Bucle while. Ejecuta el código para observar el concepto en acción.',
                "codigo": "contador = 1\nwhile contador <= 3:\n    print('Conteo:', contador)\n    contador += 1",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "energia = 100\nwhile energia > 50:\n    energia -= 20\nprint('Energía final:', energia)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 15: Repetición Condicional: El Bucle while. Completa el código requerido y ejecuta para validar.',
                "codigo": "vidas = 3\nwhile vidas > 0:\n    print('Vida restante:', vidas)\n    vidas -= 1\nprint('Juego terminado')",
                "salida_esperada": 'Juego terminado',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'terminado' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué peligro ocurre si la condición de un bucle while nunca cambia a False?\n\nOpciones:\n1. Un bucle infinito que congela el programa\n2. Un error de sintaxis inmediato\n3. El equipo se formatea\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué peligro ocurre si la condición de un bucle while nunca cambia a False?',
                "opciones": ['Un bucle infinito que congela el programa', 'Un error de sintaxis inmediato', 'El equipo se formatea'],
                "correcta": 0,
                "explicacion": 'Si la condición nunca es falsa, el bucle se repite indefinidamente (bucle infinito).',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 16,
        "titulo": 'Capítulo 16: Colecciones Clave-Valor: Diccionarios en Python',
        "resumen": 'Almacena pares asociativos de información delimitados por llaves {} y busca datos por clave.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 16: Colecciones Clave-Valor: Diccionarios en Python. Ejecuta el código para observar el concepto en acción.',
                "codigo": "contacto = {'nombre': 'Carlos', 'telefono': '555-1234'}\nprint('Nombre:', contacto['nombre'])",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "precios = {'manzana': 2, 'pera': 3}\nprecios['platano'] = 1.5\nprint('Total de frutas:', len(precios))",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 16: Colecciones Clave-Valor: Diccionarios en Python. Completa el código requerido y ejecuta para validar.',
                "codigo": "alumno = {'nombre': 'Laura', 'curso': 'Python'}\nprint('Estudiante:', alumno['nombre'], 'en curso', alumno['curso'])",
                "salida_esperada": 'Estudiante: Laura en curso Python',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'laura' in res.lower() and 'python' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué delimitadores encierran los datos de un diccionario en Python?\n\nOpciones:\n1. Llaves { }\n2. Corchetes [ ]\n3. Paréntesis ( )\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué delimitadores encierran los datos de un diccionario en Python?',
                "opciones": ['Llaves { }', 'Corchetes [ ]', 'Paréntesis ( )'],
                "correcta": 0,
                "explicacion": "Los diccionarios se delimitan mediante llaves { 'clave': 'valor' }.",
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 17,
        "titulo": 'Capítulo 17: Tuplas y Conjuntos (Sets): Inmutabilidad y Únicos',
        "resumen": 'Conoce las tuplas () inmutables y los conjuntos set {} para operaciones con colecciones sin duplicados.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 17: Tuplas y Conjuntos (Sets): Inmutabilidad y Únicos. Ejecuta el código para observar el concepto en acción.',
                "codigo": "coordenadas = (10, 20)\nprint('Latitud:', coordenadas[0])\ncolores_unicos = set(['rojo', 'azul', 'rojo'])\nprint('Únicos:', colores_unicos)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "a = {1, 2, 3}\nb = {3, 4, 5}\nunion = a.union(b)\nprint('Unión de conjuntos:', sorted(list(union)))",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 17: Tuplas y Conjuntos (Sets): Inmutabilidad y Únicos. Completa el código requerido y ejecuta para validar.',
                "codigo": "numeros = set([1, 2, 2, 3, 3, 4])\nprint('Cantidad de números únicos:', len(numeros))",
                "salida_esperada": 'Cantidad de números únicos: 4',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: '4' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué diferencia esencial tiene una tupla con respecto a una lista convencional?\n\nOpciones:\n1. Las tuplas son inmutables (no se pueden modificar)\n2. Las tuplas solo aceptan números\n3. Las tuplas no tienen índice\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué diferencia esencial tiene una tupla con respecto a una lista convencional?',
                "opciones": ['Las tuplas son inmutables (no se pueden modificar)', 'Las tuplas solo aceptan números', 'Las tuplas no tienen índice'],
                "correcta": 0,
                "explicacion": 'Las tuplas no permiten alterar ni reasignar sus elementos tras su creación.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 18,
        "titulo": 'Capítulo 18: Funciones Propias: Declaración con def y Parámetros',
        "resumen": 'Escribe bloques de código modulares y reutilizables bautizados con nombre propio mediante def.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 18: Funciones Propias: Declaración con def y Parámetros. Ejecuta el código para observar el concepto en acción.',
                "codigo": "def saludar(nombre):\n    print(f'¡Hola, {nombre}! Bienvenido a la clase.')\nsaludar('Elena')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "def multiplicar_por_diez(n):\n    print('Resultado:', n * 10)\nmultiplicar_por_diez(5)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 18: Funciones Propias: Declaración con def y Parámetros. Completa el código requerido y ejecuta para validar.',
                "codigo": "def sumar(a, b):\n    print('Resultado:', a + b)\nsumar(15, 25)",
                "salida_esperada": 'Resultado: 40',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: '40' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué palabra reservada se utiliza en Python para definir una función propia?\n\nOpciones:\n1. def\n2. function\n3. create\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué palabra reservada se utiliza en Python para definir una función propia?',
                "opciones": ['def', 'function', 'create'],
                "correcta": 0,
                "explicacion": "def (abreviatura de 'define') inicia la definición de una función.",
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 19,
        "titulo": 'Capítulo 19: Retorno de Resultados: La Sentencia return y Ámbito',
        "resumen": 'Devuelve valores procesados desde tus funciones hacia quien las invocó mediante return.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 19: Retorno de Resultados: La Sentencia return y Ámbito. Ejecuta el código para observar el concepto en acción.',
                "codigo": "def calcular_doble(numero):\n    return numero * 2\nresultado = calcular_doble(12)\nprint('El doble es:', resultado)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "def calcular_iva(precio):\n    return precio * 0.19\niva = calcular_iva(100)\nprint('IVA calculado:', iva)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 19: Retorno de Resultados: La Sentencia return y Ámbito. Completa el código requerido y ejecuta para validar.',
                "codigo": "def cuadrado(n):\n    return n * n\nval = cuadrado(7)\nprint('Cuadrado de 7:', val)",
                "salida_esperada": 'Cuadrado de 7: 49',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: '49' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué instrucción finaliza una función y envía el resultado al exterior?\n\nOpciones:\n1. return\n2. print\n3. send\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué instrucción finaliza una función y envía el resultado al exterior?',
                "opciones": ['return', 'print', 'send'],
                "correcta": 0,
                "explicacion": 'return detiene la función y entrega el valor computado.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 20,
        "titulo": 'Capítulo 20: Manejo Profesional de Errores: try, except y finally',
        "resumen": 'Protege tus programas contra excepciones inesperadas para que nunca colapsen ni se cierren solos.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 20: Manejo Profesional de Errores: try, except y finally. Ejecuta el código para observar el concepto en acción.',
                "codigo": "try:\n    calc = 10 / 0\nexcept ZeroDivisionError:\n    print('Aviso: No es posible dividir entre cero.')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "try:\n    dicc = {'a': 1}\n    val = dicc['b']\nexcept KeyError:\n    print('Clave inexistente en diccionario.')\nfinally:\n    print('Bloque final ejecutado.')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 20: Manejo Profesional de Errores: try, except y finally. Completa el código requerido y ejecuta para validar.',
                "codigo": "try:\n    num = int('no_es_numero')\nexcept ValueError:\n    print('Entrada inválida capturada.')",
                "salida_esperada": 'Entrada inválida capturada.',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'inv' in res.lower() or 'capturada' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué bloque se ejecuta obligatoriamente en un try/except ocurra o no un fallo?\n\nOpciones:\n1. finally\n2. while\n3. import\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué bloque se ejecuta obligatoriamente en un try/except ocurra o no un fallo?',
                "opciones": ['finally', 'while', 'import'],
                "correcta": 0,
                "explicacion": 'El bloque finally se ejecuta de manera garantizada para tareas de limpieza.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 21,
        "titulo": 'Capítulo 21: Decodificación de Tracebacks y Diagnóstico de Fallos',
        "resumen": 'Aprende a leer trazas de error (Tracebacks) con calma para situar el archivo, la línea y el tipo de excepción.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 21: Decodificación de Tracebacks y Diagnóstico de Fallos. Ejecuta el código para observar el concepto en acción.',
                "codigo": "print('Línea 1 normal')\n# El Traceback indica el archivo, la línea exacta y el motivo\nprint('Diagnóstico comprendido.')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "linea_fallo = 4\nmotivo = 'IndexError: list index out of range'\nprint(f'Error en línea {linea_fallo}: {motivo}')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 21: Decodificación de Tracebacks y Diagnóstico de Fallos. Completa el código requerido y ejecuta para validar.',
                "codigo": "try:\n    x = 10\n    y = 0\n    res = x / y\nexcept ZeroDivisionError as e:\n    print('Tipo de error:', type(e).__name__)",
                "salida_esperada": 'Tipo de error: ZeroDivisionError',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'zerodivisionerror' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\nEn un Traceback de Python, ¿dónde se encuentra la explicación final del error?\n\nOpciones:\n1. En la última línea de la traza\n2. En el medio de la pantalla\n3. No se muestra\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": 'En un Traceback de Python, ¿dónde se encuentra la explicación final del error?',
                "opciones": ['En la última línea de la traza', 'En el medio de la pantalla', 'No se muestra'],
                "correcta": 0,
                "explicacion": 'La última línea del Traceback indica el nombre exacto de la excepción y el mensaje descriptivo.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 22,
        "titulo": 'Capítulo 22: Entrada y Salida de Archivos: with open() para Texto',
        "resumen": 'Lee y escribe archivos en disco de forma segura utilizando administradores de contexto.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 22: Entrada y Salida de Archivos: with open() para Texto. Ejecuta el código para observar el concepto en acción.',
                "codigo": "# Escritura y lectura limpia en memoria o archivo:\ndatos = 'Registro accesible 2026'\nprint('Contenido procesado:', datos)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "lineas = ['Reporte A', 'Reporte B']\nprint('Líneas preparadas:', len(lineas))",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 22: Entrada y Salida de Archivos: with open() para Texto. Completa el código requerido y ejecuta para validar.',
                "codigo": "archivo_lineas = ['Línea 1', 'Línea 2']\nprint('Total guardado:', len(archivo_lineas))",
                "salida_esperada": 'Total guardado: 2',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: '2' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué ventaja ofrece usar la estructura 'with open()' al manipular archivos?\n\nOpciones:\n1. Cierra automáticamente el archivo al finalizar\n2. Aumenta la memoria RAM\n3. Borra el disco\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": "¿Qué ventaja ofrece usar la estructura 'with open()' al manipular archivos?",
                "opciones": ['Cierra automáticamente el archivo al finalizar', 'Aumenta la memoria RAM', 'Borra el disco'],
                "correcta": 0,
                "explicacion": 'with open asegura que el archivo se cierre correctamente incluso si ocurren excepciones.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 23,
        "titulo": 'Capítulo 23: Paradigma de Objetos: Clases, Instancias y Atributos',
        "resumen": 'Iníciate en la Programación Orientada a Objetos modelando entidades del mundo real con clases.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 23: Paradigma de Objetos: Clases, Instancias y Atributos. Ejecuta el código para observar el concepto en acción.',
                "codigo": "class Mascota:\n    pass\nmi_perro = Mascota()\nmi_perro.nombre = 'Tobi'\nprint('Mascota creada:', mi_perro.nombre)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Coche:\n    marca = 'Genérica'\nauto = Coche()\nprint('Marca de auto:', auto.marca)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 23: Paradigma de Objetos: Clases, Instancias y Atributos. Completa el código requerido y ejecuta para validar.',
                "codigo": "class Libro:\n    pass\nmi_libro = Libro()\nmi_libro.titulo = 'Python Accesible'\nprint('Libro:', mi_libro.titulo)",
                "salida_esperada": 'Libro: Python Accesible',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'python accesible' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué analogía define mejor la relación entre una clase y un objeto?\n\nOpciones:\n1. La clase es el plano o molde, y el objeto es la casa construida\n2. Son exactamente lo mismo\n3. El objeto crea a la clase\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué analogía define mejor la relación entre una clase y un objeto?',
                "opciones": ['La clase es el plano o molde, y el objeto es la casa construida', 'Son exactamente lo mismo', 'El objeto crea a la clase'],
                "correcta": 0,
                "explicacion": 'La clase define la estructura (molde); los objetos o instancias son los ejemplares concretos.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 24,
        "titulo": 'Capítulo 24: El Constructor __init__ y el Parámetro self',
        "resumen": 'Inicializa el estado y atributos de tus objetos automáticamente al nacer con el método constructor.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 24: El Constructor __init__ y el Parámetro self. Ejecuta el código para observar el concepto en acción.',
                "codigo": "class Persona:\n    def __init__(self, nombre, ciudad):\n        self.nombre = nombre\n        self.ciudad = ciudad\np = Persona('Carlos', 'Madrid')\nprint(p.nombre, 'vive en', p.ciudad)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Rectangulo:\n    def __init__(self, ancho, alto):\n        self.ancho = ancho\n        self.alto = alto\nr = Rectangulo(5, 10)\nprint('Área:', r.ancho * r.alto)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 24: El Constructor __init__ y el Parámetro self. Completa el código requerido y ejecuta para validar.',
                "codigo": "class Alumno:\n    def __init__(self, nombre, nota):\n        self.nombre = nombre\n        self.nota = nota\na = Alumno('Sara', 10)\nprint(f'{a.nombre} obtuvo {a.nota}')",
                "salida_esperada": 'Sara obtuvo 10',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'sara' in res.lower() and '10' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué representa el primer parámetro 'self' dentro de los métodos de una clase?\n\nOpciones:\n1. Hace referencia a la instancia específica del objeto actual\n2. Es una función matemática\n3. Significa segundo\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": "¿Qué representa el primer parámetro 'self' dentro de los métodos de una clase?",
                "opciones": ['Hace referencia a la instancia específica del objeto actual', 'Es una función matemática', 'Significa segundo'],
                "correcta": 0,
                "explicacion": 'self representa al propio objeto concreto sobre el que se está operando.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 25,
        "titulo": 'Capítulo 25: Métodos de Instancia y Encapsulamiento',
        "resumen": 'Dota a tus objetos de comportamientos y acciones que interactúan con sus atributos internos.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 25: Métodos de Instancia y Encapsulamiento. Ejecuta el código para observar el concepto en acción.',
                "codigo": "class CuentaBancaria:\n    def __init__(self, titular, saldo):\n        self.titular = titular\n        self.saldo = saldo\n    def depositar(self, monto):\n        self.saldo += monto\nc = CuentaBancaria('Kevin', 100)\nc.depositar(50)\nprint('Saldo actual:', c.saldo)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Luz:\n    def __init__(self):\n        self.encendida = False\n    def conmutar(self):\n        self.encendida = not self.encendida\nl = Luz()\nl.conmutar()\nprint('Luz encendida:', l.encendida)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 25: Métodos de Instancia y Encapsulamiento. Completa el código requerido y ejecuta para validar.',
                "codigo": "class Termostato:\n    def __init__(self, temp):\n        self.temp = temp\n    def subir(self, grados):\n        self.temp += grados\nt = Termostato(20)\nt.subir(3)\nprint('Nueva temp:', t.temp)",
                "salida_esperada": 'Nueva temp: 23',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: '23' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Cómo se denomina una función definida dentro de una clase que opera sobre sus datos?\n\nOpciones:\n1. Método\n2. Variable global\n3. Bucle\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Cómo se denomina una función definida dentro de una clase que opera sobre sus datos?',
                "opciones": ['Método', 'Variable global', 'Bucle'],
                "correcta": 0,
                "explicacion": 'Las funciones declaradas en el cuerpo de una clase se denominan métodos.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 26,
        "titulo": 'Capítulo 26: Herencia de Clases: Reutilización con super()',
        "resumen": 'Hereda propiedades de clases existentes para crear jerarquías organizadas y no repetir código.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 26: Herencia de Clases: Reutilización con super(). Ejecuta el código para observar el concepto en acción.',
                "codigo": "class Animal:\n    def __init__(self, especie):\n        self.especie = especie\nclass Perro(Animal):\n    def __init__(self, nombre):\n        super().__init__('Canino')\n        self.nombre = nombre\np = Perro('Fido')\nprint(p.nombre, 'es de especie', p.especie)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Dispositivo:\n    def __init__(self, encendido=True):\n        self.encendido = encendido\nclass Celular(Dispositivo):\n    def __init__(self, modelo):\n        super().__init__()\n        self.modelo = modelo\nc = Celular('Accesible')\nprint(c.modelo, 'encendido:', c.encendido)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 26: Herencia de Clases: Reutilización con super(). Completa el código requerido y ejecuta para validar.',
                "codigo": "class Vehiculo:\n    def __init__(self, ruedas):\n        self.ruedas = ruedas\nclass Moto(Vehiculo):\n    def __init__(self):\n        super().__init__(2)\nm = Moto()\nprint('Ruedas de moto:', m.ruedas)",
                "salida_esperada": 'Ruedas de moto: 2',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: '2' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué función se utiliza en una clase hija para invocar al constructor de la clase padre?\n\nOpciones:\n1. super().__init__()\n2. parent()\n3. base()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué función se utiliza en una clase hija para invocar al constructor de la clase padre?',
                "opciones": ['super().__init__()', 'parent()', 'base()'],
                "correcta": 0,
                "explicacion": 'super() accede a los métodos heredados de la superclase padre.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 27,
        "titulo": 'Capítulo 27: Polimorfismo y Métodos Especiales (__str__)',
        "resumen": 'Personaliza cómo se representan tus objetos en texto legible para sintetizadores mediante __str__.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 27: Polimorfismo y Métodos Especiales (__str__). Ejecuta el código para observar el concepto en acción.',
                "codigo": "class Usuario:\n    def __init__(self, user):\n        self.user = user\n    def __str__(self):\n        return f'Perfil de Usuario: {self.user}'\nu = Usuario('Admin')\nprint(u)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Cancion:\n    def __init__(self, titulo, artista):\n        self.titulo = titulo\n        self.artista = artista\n    def __str__(self):\n        return f'{self.titulo} por {self.artista}'\nc = Cancion('Himno', 'Accesibilidad')\nprint(c)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 27: Polimorfismo y Métodos Especiales (__str__). Completa el código requerido y ejecuta para validar.',
                "codigo": "class Producto:\n    def __init__(self, nom, precio):\n        self.nom = nom\n        self.precio = precio\n    def __str__(self):\n        return f'{self.nom} a ${self.precio}'\nprod = Producto('Teclado', 45)\nprint(prod)",
                "salida_esperada": 'Teclado a $45',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'teclado' in res.lower() and '45' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué método mágico define la representación en cadena de texto cuando usamos print(objeto)?\n\nOpciones:\n1. __str__\n2. __init__\n3. __len__\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué método mágico define la representación en cadena de texto cuando usamos print(objeto)?',
                "opciones": ['__str__', '__init__', '__len__'],
                "correcta": 0,
                "explicacion": 'El método __str__ devuelve la cadena legible por humanos al imprimir el objeto.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 28,
        "titulo": 'Capítulo 28: Módulos de la Biblioteca Estándar (math, random, datetime)',
        "resumen": "Aprovecha las 'pilas incluidas' de Python importando módulos oficiales de matemáticas, azar y fechas.",
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 28: Módulos de la Biblioteca Estándar (math, random, datetime). Ejecuta el código para observar el concepto en acción.',
                "codigo": "import math\nprint('Raíz cuadrada de 64:', math.sqrt(64))",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "import math\nprint('Factorial de 5:', math.factorial(5))",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 28: Módulos de la Biblioteca Estándar (math, random, datetime). Completa el código requerido y ejecuta para validar.',
                "codigo": "import math\nradio = 5\ncircunferencia = 2 * math.pi * radio\nprint('Circunferencia aproximada:', round(circunferencia, 2))",
                "salida_esperada": 'Circunferencia aproximada: 31.42',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: '31.42' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué instrucción se usa para traer un módulo externo o estándar a nuestro programa?\n\nOpciones:\n1. import\n2. include\n3. require\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué instrucción se usa para traer un módulo externo o estándar a nuestro programa?',
                "opciones": ['import', 'include', 'require'],
                "correcta": 0,
                "explicacion": 'La palabra clave import incorpora bibliotecas y módulos.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 29,
        "titulo": 'Capítulo 29: Persistencia Estructurada: Formato JSON y Serialización',
        "resumen": 'Aprende a transformar estructuras de datos complejas en formato JSON para guardar configuraciones e intercambiar datos.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 29: Persistencia Estructurada: Formato JSON y Serialización. Ejecuta el código para observar el concepto en acción.',
                "codigo": "import json\ndatos = {'usuario': 'David', 'activo': True}\ntexto_json = json.dumps(datos)\nprint('JSON generado:', texto_json)",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": 'import json\ns = \'{"version": 2.0, "lenguaje": "Python"}\'\nd = json.loads(s)\nprint(\'Versión recuperada:\', d[\'version\'])',
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 29: Persistencia Estructurada: Formato JSON y Serialización. Completa el código requerido y ejecuta para validar.',
                "codigo": "import json\ninfo = {'curso': 'Python 2026', 'alumnos': 150}\ns = json.dumps(info)\nrecuperado = json.loads(s)\nprint('Curso recuperado:', recuperado['curso'])",
                "salida_esperada": 'Curso recuperado: Python 2026',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'python 2026' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué función del módulo json convierte un diccionario de Python en texto JSON?\n\nOpciones:\n1. json.dumps()\n2. json.loads()\n3. json.parse()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué función del módulo json convierte un diccionario de Python en texto JSON?',
                "opciones": ['json.dumps()', 'json.loads()', 'json.parse()'],
                "correcta": 0,
                "explicacion": 'dumps (dump string) serializa objetos Python a texto en formato JSON.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 30,
        "titulo": 'Capítulo 30: Bases de Datos Relacionales con SQLite: Tablas y Consultas',
        "resumen": 'Almacena datos relacionales persistentes con el motor nativo SQLite3 mediante tablas, inserciones y consultas SELECT.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 30: Bases de Datos Relacionales con SQLite: Tablas y Consultas. Ejecuta el código para observar el concepto en acción.',
                "codigo": 'import sqlite3\ncon = sqlite3.connect(\':memory:\')\ncur = con.cursor()\ncur.execute(\'CREATE TABLE notas (materia TEXT, calificacion INT)\')\ncur.execute(\'INSERT INTO notas VALUES ("Python", 10)\')\ncur.execute(\'SELECT * FROM notas\')\nprint(\'Registro encontrado:\', cur.fetchone())\ncon.close()',
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": 'import sqlite3\ncon = sqlite3.connect(\':memory:\')\ncur = con.cursor()\ncur.execute(\'CREATE TABLE tareas (id INT, item TEXT)\')\ncur.execute(\'INSERT INTO tareas VALUES (1, "Estudiar")\')\ncur.execute(\'SELECT COUNT(*) FROM tareas\')\nprint(\'Total tareas:\', cur.fetchone()[0])\ncon.close()',
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 30: Bases de Datos Relacionales con SQLite: Tablas y Consultas. Completa el código requerido y ejecuta para validar.',
                "codigo": 'import sqlite3\ncon = sqlite3.connect(\':memory:\')\ncur = con.cursor()\ncur.execute(\'CREATE TABLE usuarios (id INT, nombre TEXT)\')\ncur.execute(\'INSERT INTO usuarios VALUES (1, "Laura")\')\ncur.execute(\'SELECT nombre FROM usuarios WHERE id = 1\')\nfila = cur.fetchone()\nprint(\'Usuario consultado:\', fila[0])\ncon.close()',
                "salida_esperada": 'Usuario consultado: Laura',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'laura' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué instrucción SQL se utiliza para recuperar y consultar registros de una tabla?\n\nOpciones:\n1. SELECT\n2. INSERT\n3. DELETE\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué instrucción SQL se utiliza para recuperar y consultar registros de una tabla?',
                "opciones": ['SELECT', 'INSERT', 'DELETE'],
                "correcta": 0,
                "explicacion": 'SELECT es la instrucción universal para consultar datos en bases de datos relacionales.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 31,
        "titulo": 'Capítulo 31: Consumo de Servicios Web: Peticiones HTTP y Respuestas JSON',
        "resumen": 'Comprende cómo los programas solicitan información a servidores web remotos e interpretan respuestas en JSON.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 31: Consumo de Servicios Web: Peticiones HTTP y Respuestas JSON. Ejecuta el código para observar el concepto en acción.',
                "codigo": 'import json\n# Simulación de respuesta de API REST:\nrespuesta_api = \'{"estado": 200, "mensaje": "Servidor en línea"}\'\nobj = json.loads(respuesta_api)\nprint(\'Respuesta recibida:\', obj[\'mensaje\'])',
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": 'import json\nresp = \'{"usuarios": ["Carlos", "Ana", "Marcos"]}\'\ndata = json.loads(resp)\nprint(\'Primer usuario recibido:\', data[\'usuarios\'][0])',
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 31: Consumo de Servicios Web: Peticiones HTTP y Respuestas JSON. Completa el código requerido y ejecuta para validar.',
                "codigo": 'import json\napi_data = \'{"precio_dolar": 4100, "moneda": "COP"}\'\nd = json.loads(api_data)\nprint(\'Valor en COP:\', d[\'precio_dolar\'])',
                "salida_esperada": 'Valor en COP: 4100',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: '4100' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Qué código de estado HTTP representa tradicionalmente una petición exitosa?\n\nOpciones:\n1. 200 (OK)\n2. 404 (No encontrado)\n3. 500 (Error del servidor)\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Qué código de estado HTTP representa tradicionalmente una petición exitosa?',
                "opciones": ['200 (OK)', '404 (No encontrado)', '500 (Error del servidor)'],
                "correcta": 0,
                "explicacion": 'El código HTTP 200 OK indica que el servidor procesó y respondió la solicitud correctamente.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
            },
        ]
    },
    {
        "id": 32,
        "titulo": 'Capítulo 32: Calidad de Software: Pruebas Unitarias con unittest',
        "resumen": 'Asegura la estabilidad de tu código construyendo pruebas unitarias automatizadas con la biblioteca estándar unittest.',
        "pasos": [
            {
                "titulo": 'Paso 1: Fundamento Conceptual',
                "tipo": 'observar',
                "instruccion": 'En este paso aprenderemos sobre Capítulo 32: Calidad de Software: Pruebas Unitarias con unittest. Ejecuta el código para observar el concepto en acción.',
                "codigo": "import unittest\ndef multiplicar(a, b):\n    return a * b\n# Verificación manual assert:\nassert multiplicar(3, 4) == 12\nprint('Prueba unitaria superada: 3 * 4 = 12')",
                "pistas": ['Pulsa Control + Enter para ejecutar.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "def restar(a, b):\n    return a - b\nassert restar(10, 4) == 6\nprint('Prueba de resta exitosa.')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: len(res.strip()) > 0
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": 'Desafío práctico del Capítulo 32: Calidad de Software: Pruebas Unitarias con unittest. Completa el código requerido y ejecuta para validar.',
                "codigo": "def es_par(numero):\n    return numero % 2 == 0\nassert es_par(4) == True\nassert es_par(5) == False\nprint('Todas las pruebas unitarias pasaron con éxito.')",
                "salida_esperada": 'Todas las pruebas unitarias pasaron con éxito.',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'todas las pruebas' in res.lower() or 'éxito' in res.lower() or 'exito' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n¿Cuál es el propósito primordial de escribir pruebas unitarias?\n\nOpciones:\n1. Verificar de forma automática que cada pequeña parte del código funciona como se espera\n2. Hacer que el programa corra más rápido\n3. Cambiar el color del editor\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pregunta": '¿Cuál es el propósito primordial de escribir pruebas unitarias?',
                "opciones": ['Verificar de forma automática que cada pequeña parte del código funciona como se espera', 'Hacer que el programa corra más rápido', 'Cambiar el color del editor'],
                "correcta": 0,
                "explicacion": 'Las pruebas unitarias garantizan que el código cumpla sus requisitos y previenen regresiones en el software.',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "validar": lambda src, res, ns: '1' in ''.join([l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith('#')])
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
