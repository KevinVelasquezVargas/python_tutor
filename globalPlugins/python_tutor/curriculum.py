# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/curriculum.py
# Propósito: Temario pedagógico de 32 capítulos accesibles con fundamentos previos,
#            retos prácticos con código limpio y validaciones estrictas.
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
                "validar": lambda src, res, ns: 'completado' in res.lower() and 'tetera' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación: La importancia del orden',
                "tipo": 'experimentar',
                "instruccion": "Si alteramos el orden de las instrucciones, el resultado final no tendrá sentido. Añade entre el paso 1 y el paso 2 la línea: print('Paso intermedio: Colocar la bolsita de té.') y pulsa Control + Enter.",
                "codigo": "print('Paso 1: Calentar el agua.')\n# Modifica aquí: Agrega entre ambos pasos la línea:\n# print('Paso intermedio: Colocar la bolsita de té.')\n\nprint('Paso 2: Servir el agua caliente en la taza.')",
                "pistas": ["Escribe print('Paso intermedio: Colocar la bolsita de té.') entre las dos líneas existentes."],
                "validar": lambda src, res, ns: 'bolsita' in res.lower() and 'taza' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Algoritmo de lavado de manos',
                "tipo": 'desafio',
                "instruccion": "Escribe un algoritmo de 3 pasos para lavarse las manos usando tres instrucciones print(): 1. 'Abrir el grifo y mojar las manos', 2. 'Aplicar jabón y frotar', 3. 'Enjuagar y secar'. Ejecuta con Control + Enter para comprobar.",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "salida_esperada": '1. Abrir el grifo y mojar las manos\n2. Aplicar jabón y frotar\n3. Enjuagar y secar',
                "pistas": ['Usa tres instrucciones print independientes, cada una con el texto entre comillas.', "Ejemplo: print('1. Abrir el grifo y mojar las manos')"],
                "validar": lambda src, res, ns: ('jabón' in res.lower() or 'jabon' in res.lower()) and 'grifo' in res.lower() and ('secar' in res.lower() or 'enjuagar' in res.lower())
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Cuál es la definición más exacta de un algoritmo?\n\nOpciones:\n\n1. Un componente físico de la computadora como el procesador.\n\n2. Una serie ordenada y finita de instrucciones lógicas para resolver un problema.\n\n3. Un virus informático que altera los programas.\n\nEscribe el número de tu opción (1, 2 o 3) en el editor y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Recuerda el ejemplo de la preparación del té.'],
                "pregunta": '¿Cuál es la definición más exacta de un algoritmo?',
                "opciones": ['Un componente físico de la computadora como el procesador.', 'Una serie ordenada y finita de instrucciones lógicas para resolver un problema.', 'Un virus informático que altera los programas.'],
                "correcta": 1,
                "explicacion": 'Un algoritmo es la secuencia lógica y paso a paso que describe la solución a un problema determinado.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['2']
            }
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
                "validar": lambda src, res, ns: 'nvda' in res.lower() and 'mensaje' in ns
            },
            {
                "titulo": 'Paso 2: Observación: La memoria es modificable',
                "tipo": 'experimentar',
                "instruccion": "En la memoria RAM podemos reemplazar el contenido de una variable en cualquier instante. Observa cómo cambia la variable 'estado' y ejecuta con Control + Enter.",
                "codigo": "estado = 'Cargando datos'\nprint('Estado inicial:', estado)\n# Modifica aquí el valor asignado para que sea 'Completado':\nestado = 'Listo para programar'\nprint('Estado final:', estado)",
                "pistas": ['Ejecuta con Control + Enter para escuchar los dos estados secuenciales.'],
                "validar": lambda src, res, ns: 'completado' in res.lower() and ns.get('estado') == 'Completado'
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Variables y salida',
                "tipo": 'desafio',
                "instruccion": "Crea una variable llamada 'usuario' con el texto 'Estudiante' y muestra en consola usando print: Bienvenido/a, Estudiante. Ejecuta con Control + Enter.",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "salida_esperada": 'Bienvenido/a, Estudiante',
                "pistas": ["Escribe usuario = 'Estudiante' en el primer renglón y luego print('Bienvenido/a,', usuario)."],
                "validar": lambda src, res, ns: ns.get('usuario') == 'Estudiante' and 'estudiante' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Dónde se almacenan las variables mientras tu script de Python se está ejecutando?\n\nOpciones:\n\n1. En la Memoria RAM del equipo.\n\n2. En la tecla Escape del teclado.\n\n3. En el cable de corriente.\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Es la memoria principal de acceso aleatorio.'],
                "pregunta": '¿Dónde se almacenan las variables mientras tu script de Python se está ejecutando?',
                "opciones": ['En la Memoria RAM del equipo.', 'En la tecla Escape del teclado.', 'En el cable de corriente.'],
                "correcta": 0,
                "explicacion": 'La Memoria RAM es el espacio de trabajo rápido donde residen los datos activos de los programas en ejecución.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "codigo": "llave = True\nclave = False\n# Modifica clave a True para que ambas condiciones se cumplan:\nprint('¿Puede entrar con llave Y clave?:', llave and clave)",
                "pistas": ['Observa cómo or devuelve True pero and devuelve False.'],
                "validar": lambda src, res, ns: ns.get('clave') is True and 'true' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Verificación de acceso',
                "tipo": 'desafio',
                "instruccion": "Crea una variable llamada 'edad' con el valor 20 y una variable 'tiene_identificacion' con True. Luego crea 'autorizado = (edad >= 18) and tiene_identificacion'. Imprime print('Acceso permitido:', autorizado).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "salida_esperada": 'Acceso permitido: True',
                "pistas": ['Une ambas condiciones con el operador and.'],
                "validar": lambda src, res, ns: ns.get('edad') == 20 and ns.get('autorizado') is True and 'true' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué resultado produce la expresión booleana: not False?\n\nOpciones:\n\n1. True\n\n2. False\n\n3. None\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['not es el operador de negación inversa.'],
                "pregunta": '¿Qué resultado produce la expresión booleana: not False?',
                "opciones": ['True', 'False', 'None'],
                "correcta": 0,
                "explicacion": "El operador 'not' invierte el valor lógico: si niegas False obtienes True.",
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'hola mundo' in res.lower() and 'accesible' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación: Varios argumentos separados por coma',
                "tipo": 'experimentar',
                "instruccion": 'print() puede recibir varios textos separados por comas. Python insertará automáticamente un espacio entre cada uno. Cambia algún texto o añade uno nuevo y pulsa Control + Enter.',
                "codigo": "print('Python', 'es', 'fácil', 'y', 'accesible')\n# Modifica 'accesible' por 'potente' y ejecuta:",
                "pistas": ['Modifica o agrega un argumento entre comillas.'],
                "validar": lambda src, res, ns: 'potente' in res.lower() and 'fácil' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Tu propio saludo',
                "tipo": 'desafio',
                "instruccion": "Escribe una instrucción print() que muestre exactamente el mensaje: 'Aprendiendo Python con NVDA'. Pulsa Control + Enter para validar.",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "salida_esperada": 'Aprendiendo Python con NVDA',
                "pistas": ["Escribe: print('Aprendiendo Python con NVDA') respetando las comillas y los paréntesis."],
                "validar": lambda src, res, ns: 'aprendiendo python con nvda' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué función se utiliza en Python para enviar datos a la salida y lector de pantalla?\n\nOpciones:\n\n1. print()\n\n2. input()\n\n3. exit()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué función se utiliza en Python para enviar datos a la salida y lector?',
                "opciones": ['print()', 'input()', 'exit()'],
                "correcta": 0,
                "explicacion": 'print() es la función de salida estándar por excelencia.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: ns.get('edad') == 25 and 'kevin' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación: Actualizar el valor de una variable',
                "tipo": 'experimentar',
                "instruccion": 'Podemos sumar puntos a una variable existente y reasignarla. Cambia el valor que se suma (50) por otro número y pulsa Control + Enter.',
                "codigo": "puntos = 100\nprint('Puntuación inicial:', puntos)\n# Modifica aquí: suma 100 en lugar de 50 para llegar a 200 puntos:\npuntos = puntos + 50\nprint('Puntuación final:', puntos)",
                "pistas": ['Modifica el número 50 por el valor que prefieras y ejecuta.'],
                "validar": lambda src, res, ns: ns.get('puntos') == 200 and '200' in res
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Variable de lenguaje',
                "tipo": 'desafio',
                "instruccion": "Crea una variable llamada 'lenguaje' con el texto 'Python' y luego muestra en consola: print('Estoy programando en:', lenguaje). Pulsa Control + Enter.",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "salida_esperada": 'Estoy programando en: Python',
                "pistas": ["Asigna lenguaje = 'Python' y luego pásala a print."],
                "validar": lambda src, res, ns: ns.get('lenguaje') == 'Python' and 'python' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué símbolo se usa en Python para asignar un valor a una variable?\n\nOpciones:\n\n1. El signo igual (=)\n\n2. El signo de suma (+)\n\n3. El punto y coma (;)\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['El operador de asignación es =.'],
                "pregunta": '¿Qué símbolo se usa en Python para asignar un valor a una variable?',
                "opciones": ['El signo igual (=)', 'El signo de suma (+)', 'El punto y coma (;)'],
                "correcta": 0,
                "explicacion": 'El signo igual simple (=) asigna lo que está a la derecha en la variable de la izquierda.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: ns.get('total') == 58.5 and '58.5' in res
            },
            {
                "titulo": 'Paso 2: Observación: Operaciones con decimales',
                "tipo": 'experimentar',
                "instruccion": 'El operador ** calcula potencias (radio al cuadrado). Cambia el valor del radio a 5 y pulsa Control + Enter para ver cómo cambia el área.',
                "codigo": "# Modifica el radio a 5 en lugar de 4:\nradio = 4\npi = 3.1416\narea = pi * (radio ** 2)\nprint('Área del círculo:', round(area, 2))",
                "pistas": ['Cambia radio = 4 por radio = 5.'],
                "validar": lambda src, res, ns: ns.get('radio') == 5 and '78.54' in res
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Cálculo de área de triángulo',
                "tipo": 'desafio',
                "instruccion": "Crea las variables base = 10 y altura = 5. Calcula area = (base * altura) / 2 e imprime: print('Área del triángulo:', area). Ejecuta con Control + Enter.",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "salida_esperada": 'Área del triángulo: 25.0',
                "pistas": ['Recuerda usar la barra inclinada / para la división.'],
                "validar": lambda src, res, ns: ns.get('base') == 10 and ns.get('altura') == 5 and ns.get('area') == 25.0 and '25' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Cómo se denomina en Python al tipo de dato numérico que tiene parte decimal?\n\nOpciones:\n\n1. float\n\n2. int\n\n3. bool\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ["Viene del inglés 'floating point'."],
                "pregunta": '¿Cómo se denomina en Python a un número con parte decimal?',
                "opciones": ['float', 'int', 'bool'],
                "correcta": 0,
                "explicacion": 'float representa números de coma flotante (decimales).',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'laura' in res.lower() and 'bienvenida' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación: Repetición de texto con *',
                "tipo": 'experimentar',
                "instruccion": 'Al multiplicar un texto por un número, Python lo repite. Cambia el multiplicador 3 por 5 y pulsa Control + Enter.',
                "codigo": "aplauso = '¡Bravo! '\n# Modifica el multiplicador 3 por 5:\nprint(aplauso * 3)",
                "pistas": ['Cambia * 3 por * 5.'],
                "validar": lambda src, res, ns: res.count('¡Bravo!') >= 5
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Crear una f-string',
                "tipo": 'desafio',
                "instruccion": "Crea una variable ciudad = 'Bogotá' y pais = 'Colombia'. Usa una f-string para imprimir exactamente: print(f'Ubicación: {ciudad}, {pais}').",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "salida_esperada": 'Ubicación: Bogotá, Colombia',
                "pistas": ['Coloca f antes de las comillas y las variables dentro de {ciudad} y {pais}.'],
                "validar": lambda src, res, ns: ('bogotá' in res.lower() or 'bogota' in res.lower()) and 'colombia' in res.lower() and 'ubicación' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué letra precede a las comillas para crear una cadena formateada moderna en Python?\n\nOpciones:\n\n1. La letra f\n\n2. La letra p\n\n3. La letra s\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ["f viene de 'format'."],
                "pregunta": '¿Qué letra precede a las comillas para crear una f-string?',
                "opciones": ['La letra f', 'La letra p', 'La letra s'],
                "correcta": 0,
                "explicacion": 'La letra f convierte una cadena en una f-string (cadena formateada).',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: ns.get('edad_numero') == 25 and '25' in res
            },
            {
                "titulo": 'Paso 2: Observación: input con mensaje',
                "tipo": 'experimentar',
                "instruccion": 'Observa cómo se le pasa un texto informativo a input(). Modifica el mensaje dentro de input y pulsa Control + Enter.',
                "codigo": "nombre = 'Ana'\n# Modifica el saludo para que diga '¡Bienvenida, Ana!':\nprint(f'¡Hola {nombre}! Bienvenido/a al aprendizaje interactivo.')",
                "pistas": ["Cambia 'Ana' por tu propio nombre."],
                "validar": lambda src, res, ns: 'bienvenida, ana' in res.lower() or 'bienvenida ana' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Conversión y cálculo',
                "tipo": 'desafio',
                "instruccion": "Tienes la variable edad_texto = '20'. Conviértela a entero usando int(edad_texto) y guarda el resultado en 'edad'. Luego muestra: print('El próximo año tendrás:', edad + 1).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "salida_esperada": 'El próximo año tendrás: 21',
                "pistas": ['Usa int(edad_texto) para la conversión.'],
                "validar": lambda src, res, ns: ns.get('edad') == 20 and ('21' in res or ns.get('proximo') == 21 or ns.get('edad_siguiente') == 21)
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué tipo de dato devuelve por defecto la función input() de Python?\n\nOpciones:\n\n1. Siempre una cadena de texto (str)\n\n2. Un número entero (int)\n\n3. Un booleano (bool)\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Todo lo que entra por teclado se lee inicialmente como texto.'],
                "pregunta": '¿Qué tipo de dato devuelve por defecto input()?',
                "opciones": ['Siempre una cadena de texto (str)', 'Un número entero (int)', 'Un booleano (bool)'],
                "correcta": 0,
                "explicacion": 'input() siempre retorna una cadena (str), por eso se requiere int() o float() para operar numéricamente.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'true' in res.lower() and 'false' in res.lower() and ns.get('x') == 15
            },
            {
                "titulo": 'Paso 2: Observación: Comparar textos',
                "tipo": 'experimentar',
                "instruccion": 'También puedes comparar textos con ==. Si cambias el texto para que coincidan exactamente, el resultado cambiará a True. Modifica y ejecuta.',
                "codigo": "clave_ingresada = 'prueba'\nclave_real = 'secreta'\n# Modifica clave_ingresada para que coincida exactamente con clave_real:\nprint('¿Clave correcta?:', clave_ingresada == clave_real)",
                "pistas": ['Cambia una de las cadenas para que no coincidan o mantenlas iguales.'],
                "validar": lambda src, res, ns: ns.get('clave_ingresada') == 'secreta' and 'true' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Nota de aprobación',
                "tipo": 'desafio',
                "instruccion": "Crea una variable puntos = 85. Imprime en consola: print('¿Aprobó con 70 o más?:', puntos >= 70). Pulsa Control + Enter.",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "salida_esperada": '¿Aprobó con 70 o más?: True',
                "pistas": ['Usa el operador >= (mayor o igual).'],
                "validar": lambda src, res, ns: ns.get('puntos') == 85 and 'true' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué operador se utiliza en Python para comparar si dos valores son exactamente iguales?\n\nOpciones:\n\n1. Doble signo igual (==)\n\n2. Un solo signo igual (=)\n\n3. Signo de admiración (!)\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['No confundir asignación (=) con comparación.'],
                "pregunta": '¿Qué operador compara si dos valores son iguales?',
                "opciones": ['Doble signo igual (==)', 'Un solo signo igual (=)', 'Signo de admiración (!)'],
                "correcta": 0,
                "explicacion": 'El doble signo igual (==) compara igualdad. El signo simple (=) asigna valores.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'ventilador' in res.lower() and ns.get('temperatura') == 30
            },
            {
                "titulo": 'Paso 2: Observación: Cuando la condición no se cumple',
                "tipo": 'experimentar',
                "instruccion": 'Si la condición es False, el bloque indentado no se ejecuta. Cambia temperatura a 15 y ejecuta con Control + Enter para escuchar cómo se salta el bloque.',
                "codigo": "# Modifica la temperatura a 15 para comprobar que el bloque if no se ejecuta:\ntemperatura = 30\nif temperatura > 25:\n    print('Hace calor.')\nprint('Fin del programa.')",
                "pistas": ['Cambia temperatura = 15 y ejecuta.'],
                "validar": lambda src, res, ns: ns.get('temperatura') == 15 and 'hace calor' not in res.lower() and 'fin' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico: Saludo horario con if',
                "tipo": 'desafio',
                "instruccion": "Crea una variable hora = 14. Escribe un bloque if que compruebe si hora >= 12, y dentro imprima con 4 espacios de sangría: print('Buenas tardes').",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "salida_esperada": 'Buenas tardes',
                "pistas": ['No olvides los dos puntos (:) al final de la línea if.', 'Usa 4 espacios o pulsa Tab para la indentación.'],
                "validar": lambda src, res, ns: ns.get('hora') == 14 and 'buenas tardes' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Cuántos espacios en blanco recomienda el estándar oficial PEP 8 para cada nivel de sangría en Python?\n\nOpciones:\n\n1. 4 espacios\n\n2. 1 espacio\n\n3. 10 espacios\n\nEscribe tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Es el estándar universal de Python.'],
                "pregunta": '¿Cuántos espacios recomienda PEP 8 para la sangría?',
                "opciones": ['4 espacios', '1 espacio', '10 espacios'],
                "correcta": 0,
                "explicacion": 'PEP 8 establece un estándar de 4 espacios por cada nivel de sangría.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'aprobado' in res.lower() and ns.get('nota') == 7
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "# Modifica la nota a 10 para que se active la condición de 'Excelente':\nnota = 4\nif nota >= 9:\n    print('Excelente')\nelif nota >= 5:\n    print('Aprobado')\nelse:\n    print('Necesita reforzar')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: ns.get('nota') >= 9 and 'excelente' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una variable nota = 8. Escribe if nota >= 9 imprima 'Excelente', elif nota >= 5 imprima 'Aprobado', y else imprima 'Reprobado'.",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: ns.get('nota') == 8 and 'aprobado' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué bloque condicional se ejecuta si ninguna condición anterior fue verdadera?\n\nOpciones:\n\n1. El bloque else\n\n2. El bloque if\n\n3. El bloque while\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué bloque condicional se ejecuta si ninguna condición anterior fue verdadera?',
                "opciones": ['El bloque else', 'El bloque if', 'El bloque while'],
                "correcta": 0,
                "explicacion": 'else se ejecuta como camino por defecto cuando todo lo anterior fue falso.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'manzana' in res.lower() and 'pera' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "frutas = ['manzana', 'pera', 'plátano']\n# Modifica el elemento en la posición 0 asignando 'fresa':\nfrutas[0] = 'manzana'\nprint('Fruta modificada:', frutas[0])",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: ns.get('frutas') and ns.get('frutas')[0] == 'fresa' and 'fresa' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una lista llamada 'compras' con 'pan', 'leche' y 'huevos'. Imprime el primer elemento usando compras[0].",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: isinstance(ns.get('compras'), list) and len(ns.get('compras')) >= 3 and 'pan' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Cuál es el índice del primer elemento de una lista en Python?\n\nOpciones:\n\n1. El índice 0\n\n2. El índice 1\n\n3. El índice -1\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Cuál es el índice del primer elemento de una lista en Python?',
                "opciones": ['El índice 0', 'El índice 1', 'El índice -1'],
                "correcta": 0,
                "explicacion": 'En Python la indexación empieza siempre en base cero (0).',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'descansar' in res.lower() and len(ns.get('tareas', [])) == 3
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "tareas = ['leer', 'programar', 'descansar']\n# Modifica para eliminar 'descansar' en vez de 'leer':\ntareas.remove('leer')\nprint('Tareas restantes:', tareas)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: 'descansar' not in ns.get('tareas', []) and 'leer' in ns.get('tareas', [])
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una lista colores = ['rojo', 'verde']. Agrega 'azul' con append() y muestra la cantidad total con print('Total colores:', len(colores)).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: isinstance(ns.get('colores'), list) and 'azul' in ns.get('colores') and ('3' in res or len(ns.get('colores')) == 3)
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué método agrega un nuevo elemento al final de una lista?\n\nOpciones:\n\n1. append()\n\n2. delete()\n\n3. add()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué método agrega un nuevo elemento al final de una lista?',
                "opciones": ['append()', 'delete()', 'add()'],
                "correcta": 0,
                "explicacion": 'append() añade un nuevo elemento al final de la lista.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: all(str(i) in res for i in (1, 2, 3)) and 'fin del bucle' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "animales = ['perro', 'gato', 'loro']\n# Modifica agregando 'canario' a la lista para iterar 4 veces:\nfor animal in animales:\n    print('Mascota:', animal)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: 'canario' in res.lower() and len(ns.get('animales', [])) >= 4
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Escribe un bucle for que recorra range(1, 6) e imprima cada número: print('Contando:', numero).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: all(str(i) in res for i in range(1, 6))
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué produce la función range(1, 5) en un bucle for?\n\nOpciones:\n\n1. Los números del 1 al 4\n\n2. Los números del 1 al 5\n\n3. Una lista vacía\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué produce la función range(1, 5) en un bucle for?',
                "opciones": ['Los números del 1 al 4', 'Los números del 1 al 5', 'Una lista vacía'],
                "correcta": 0,
                "explicacion": 'range(inicio, fin) llega hasta fin - 1.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: all(str(i) in res for i in (1, 2, 3)) and ns.get('contador') == 4
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "# Modifica la energía inicial a 5 en lugar de 3:\nenergia = 3\nwhile energia > 0:\n    print('Energía restante:', energia)\n    energia = energia - 1\nprint('Sin energía')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: '5' in res and 'sin energía' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una variable contador = 1. Escribe un bucle while que mientras contador <= 3 imprima print('Paso:', contador) y sume 1 a contador.",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: all(str(i) in res for i in (1, 2, 3)) and ns.get('contador', 0) > 3
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué precaución crucial se debe tomar al programar un bucle while?\n\nOpciones:\n\n1. Asegurar que la condición cambie para evitar un bucle infinito\n\n2. Poner punto y coma al final\n\n3. Usar comillas triples\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué precaución crucial se debe tomar al programar un bucle while?',
                "opciones": ['Asegurar que la condición cambie para evitar un bucle infinito', 'Poner punto y coma al final', 'Usar comillas triples'],
                "correcta": 0,
                "explicacion": 'Si la condición nunca se vuelve falsa, el bucle se ejecuta infinitamente bloqueando el programa.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'carlos' in res.lower() and '555-1234' in res
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "contacto = {'nombre': 'Carlos', 'telefono': '555-1234'}\n# Modifica aquí la ciudad a 'Valencia':\ncontacto['ciudad'] = 'Madrid'\nprint('Contacto completo:', contacto)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: ns.get('contacto', {}).get('ciudad') == 'Valencia' and 'valencia' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea un diccionario llamado 'precios' con 'manzana': 2 y 'pera': 3. Imprime: print('Precio manzana:', precios['manzana']).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: isinstance(ns.get('precios'), dict) and ns.get('precios').get('manzana') == 2 and '2' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué delimitador se utiliza para declarar diccionarios en Python?\n\nOpciones:\n\n1. Llaves {}\n\n2. Corchetes []\n\n3. Paréntesis ()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué delimitador se utiliza para declarar diccionarios en Python?',
                "opciones": ['Llaves {}', 'Corchetes []', 'Paréntesis ()'],
                "correcta": 0,
                "explicacion": 'Los diccionarios se declaran entre llaves {} con pares clave: valor.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: '10' in res and '20' in res and isinstance(ns.get('punto'), tuple)
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "# Modifica el conjunto agregando el número 5:\nnumeros = {1, 2, 2, 3, 3, 4}\nprint('Conjunto sin duplicados:', numeros)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: isinstance(ns.get('numeros'), set) and 5 in ns.get('numeros')
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una tupla llamada 'coordenadas' con los valores (50, 100). Imprime: print('Coordenadas:', coordenadas).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: isinstance(ns.get('coordenadas'), tuple) and ns.get('coordenadas') == (50, 100) and '50' in res and '100' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Cuál es la principal diferencia entre una tupla y una lista?\n\nOpciones:\n\n1. Las tuplas son inmutables (no se pueden modificar)\n\n2. Las tuplas no aceptan números\n\n3. Las tuplas solo tienen un elemento\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Cuál es la principal diferencia entre una tupla y una lista?',
                "opciones": ['Las tuplas son inmutables (no se pueden modificar)', 'Las tuplas no aceptan números', 'Las tuplas solo tienen un elemento'],
                "correcta": 0,
                "explicacion": 'Las tuplas son inmutables una vez creadas, lo que garantiza la integridad de los datos.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: callable(ns.get('saludar')) and 'lucía' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "def calcular_doble(num):\n    print('El doble es:', num * 2)\n\n# Modifica la llamada para calcular el doble de 15:\ncalcular_doble(8)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: '30' in res or 'el doble es: 30' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Define una función llamada 'sumar(a, b)' que imprima: print('Resultado:', a + b). Luego invócala con sumar(5, 7).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: callable(ns.get('sumar')) and ('12' in res or 'resultado: 12' in res.lower())
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué palabra clave se usa para definir una nueva función en Python?\n\nOpciones:\n\n1. def\n\n2. function\n\n3. fn\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué palabra clave se usa para definir una nueva función en Python?',
                "opciones": ['def', 'function', 'fn'],
                "correcta": 0,
                "explicacion": "La palabra clave 'def' (de define) declara una función.",
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: ns.get('resultado') == 20 and callable(ns.get('multiplicar'))
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "def es_mayor_de_edad(edad):\n    return edad >= 18\n\n# Modifica la edad probada a 16:\nprint('¿Puede votar?:', es_mayor_de_edad(20))",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: 'false' in res.lower() and callable(ns.get('es_mayor_de_edad'))
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Define una función 'cuadrado(n)' que retorne n * n usando return. Guarda cuadrado(6) en la variable 'res' e imprime: print('El cuadrado es:', res).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: callable(ns.get('cuadrado')) and ns.get('cuadrado')(6) == 36 and '36' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué sucede cuando una función ejecuta la instrucción return?\n\nOpciones:\n\n1. Finaliza la función y devuelve el valor procesado\n\n2. Imprime el valor en pantalla\n\n3. Reinicia la computadora\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué sucede cuando una función ejecuta la instrucción return?',
                "opciones": ['Finaliza la función y devuelve el valor procesado', 'Imprime el valor en pantalla', 'Reinicia la computadora'],
                "correcta": 0,
                "explicacion": 'return concluye la ejecución de la función y entrega el resultado a quien la llamó.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'no es posible dividir por cero' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "try:\n    numero = int('123')\n    print('Número convertido:', numero)\nexcept ValueError:\n    print('Aviso: el texto no contiene dígitos válidos.')\n# Modifica el texto '123' por 'abc' para que salte la excepción ValueError:",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: 'aviso: el texto no contiene dígitos válidos' in res.lower() or 'aviso' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Escribe un bloque try donde dividas 20 entre 0, y en el except ZeroDivisionError imprime: print('Error capturado con éxito').",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'capturado con éxito' in res.lower() or 'capturado con exito' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Para qué sirve la cláusula except en Python?\n\nOpciones:\n\n1. Para capturar errores específicos y evitar que el programa se cierre\n\n2. Para crear bucles\n\n3. Para borrar archivos\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Para qué sirve la cláusula except en Python?',
                "opciones": ['Para capturar errores específicos y evitar que el programa se cierre', 'Para crear bucles', 'Para borrar archivos'],
                "correcta": 0,
                "explicacion": 'except intercepta la excepción permitiendo que el programa maneje la situación con elegancia.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'traceback' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "try:\n    lista = [1, 2]\n    # Modifica el índice a 1 para acceder correctamente al elemento sin error:\n    print('Elemento:', lista[10])\nexcept IndexError as err:\n    print('Error capturado: índice fuera de rango.')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: 'elemento: 2' in res.lower() and 'error capturado' not in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Corrige el error en el código: convierte '5' a número con int() antes de sumar para que imprima: print('Suma correcta:', 10 + int('5')).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: '15' in res and ('suma correcta' in res.lower() or ns.get('suma') == 15)
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué tecla rápida de Aprendizaje de Python con NVDA sitúa el cursor directamente en la línea del error del Traceback?\n\nOpciones:\n\n1. F4\n\n2. F1\n\n3. F12\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué tecla rápida de Aprendizaje de Python con NVDA sitúa el cursor directamente en la línea del error del Traceback?',
                "opciones": ['F4', 'F1', 'F12'],
                "correcta": 0,
                "explicacion": 'F4 salta inmediatamente a la línea del error en el editor y lee el diagnóstico.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'archivo guardado con éxito' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "with open('ejemplo.txt', 'w', encoding='utf-8') as f:\n    f.write('Línea 1')\n# Modifica para escribir 'Línea 2':\nprint('Completado')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: 'completado' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Usa with open('mensaje.txt', 'w', encoding='utf-8') as f: y escribe f.write('Python accesible'). Luego imprime: print('Guardado listo').",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'guardado exitoso' in res.lower() and 'open' in src
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": "Pregunta de verificación conceptual:\n\n¿Por qué es recomendable usar 'with open()' al trabajar con archivos?\n\nOpciones:\n\n1. Porque cierra automáticamente el archivo incluso si ocurre un error\n\n2. Porque encripta los datos\n\n3. Porque no usa memoria\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": "¿Por qué es recomendable usar 'with open()' al trabajar con archivos?",
                "opciones": ['Porque cierra automáticamente el archivo incluso si ocurre un error', 'Porque encripta los datos', 'Porque no usa memoria'],
                "correcta": 0,
                "explicacion": 'with actúa como administrador de contexto asegurando la liberación de recursos.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'aprendizaje de python' in res.lower() and '200' in res
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Dispositivo:\n    tipo = 'Lector de pantalla'\n\nlector = Dispositivo()\n# Modifica el atributo tipo a 'Lector Braille':\nlector.tipo = 'Lector de pantalla'\nprint('Dispositivo:', lector.tipo)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: 'braille' in res.lower() or (hasattr(ns.get('lector'), 'tipo') and 'braille' in ns.get('lector').tipo.lower())
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una clase llamada 'Mascota' con un atributo de clase especie = 'Perro'. Crea un objeto perro = Mascota() e imprime: print('Especie:', perro.especie).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: hasattr(ns.get('Mascota'), 'especie') and ns.get('Mascota').especie == 'Perro' and 'perro' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué es una clase en programación orientada a objetos?\n\nOpciones:\n\n1. Un molde o plantilla para crear objetos con datos y funciones\n\n2. Una variable numérica\n\n3. Un bucle de repetición\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué es una clase en programación orientada a objetos?',
                "opciones": ['Un molde o plantilla para crear objetos con datos y funciones', 'Una variable numérica', 'Un bucle de repetición'],
                "correcta": 0,
                "explicacion": 'Una clase es el plano estructural a partir del cual se instancian los objetos.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'ana' in res.lower() and '28' in res
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Cuenta:\n    def __init__(self, titular, saldo):\n        self.titular = titular\n        self.saldo = saldo\n\n# Modifica el saldo inicial a 500:\nc = Cuenta('Carlos', 100)\nprint('Titular:', c.titular, 'Saldo:', c.saldo)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: getattr(ns.get('c'), 'saldo', 0) == 500 and '500' in res
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una clase Usuario con def __init__(self, apodo): que asigne self.apodo = apodo. Crea u = Usuario('Programador') e imprime: print('Apodo:', u.apodo).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'Usuario' in ns and hasattr(ns.get('u'), 'apodo') and ns.get('u').apodo == 'Programador' and 'programador' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Cuál es la función del método especial __init__?\n\nOpciones:\n\n1. Es el constructor que inicializa los atributos del objeto al crearlo\n\n2. Es una función para borrar el objeto\n\n3. Es un bucle for\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Cuál es la función del método especial __init__?',
                "opciones": ['Es el constructor que inicializa los atributos del objeto al crearlo', 'Es una función para borrar el objeto', 'Es un bucle for'],
                "correcta": 0,
                "explicacion": '__init__ se ejecuta automáticamente al instanciar un nuevo objeto.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'reproduciendo' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Termostato:\n    def __init__(self, temp):\n        self.temp = temp\n    def subir(self):\n        self.temp += 1\n\nt = Termostato(20)\n# Invoca el método t.subir() dos veces:\nt.subir()\nprint('Temperatura actual:', t.temp)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: getattr(ns.get('t'), 'temp', 0) >= 22 and ('22' in res or 'temperatura' in res.lower())
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una clase Saludo con def __init__(self, nombre): y un método saludar(self) que imprima: print(f'Hola, {self.nombre}'). Crea s = Saludo('Amigo') e invoca s.saludar().",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'Saludo' in ns and hasattr(ns.get('s'), 'saludar') and 'hola' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": "Pregunta de verificación conceptual:\n\n¿Qué representa el primer parámetro 'self' en los métodos de una clase?\n\nOpciones:\n\n1. La referencia a la instancia específica del objeto que invocó el método\n\n2. Una palabra reservada de Windows\n\n3. Un número entero\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": "¿Qué representa el primer parámetro 'self' en los métodos de una clase?",
                "opciones": ['La referencia a la instancia específica del objeto que invocó el método', 'Una palabra reservada de Windows', 'Un número entero'],
                "correcta": 0,
                "explicacion": 'self permite que el método acceda y modifique los atributos de ese objeto en particular.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'guau' in res.lower() and 'boby' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Empleado:\n    def __init__(self, nombre, sueldo):\n        self.nombre = nombre\n        self.sueldo = sueldo\n\n# Modifica el sueldo a 2500:\ne = Empleado('Marta', 1800)\nprint('Empleado:', e.nombre, 'Sueldo:', e.sueldo)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: getattr(ns.get('e'), 'sueldo', 0) == 2500 and '2500' in res
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una clase Vehiculo con __init__(self, marca). Crea una clase Coche(Vehiculo) que en su __init__(self, marca, modelo) use super().__init__(marca) y self.modelo = modelo. Crea c = Coche('Toyota', 'Corolla') e imprime: print(c.marca, c.modelo).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'Coche' in ns and issubclass(ns.get('Coche'), ns.get('Vehiculo')) and 'toyota' in res.lower() and 'corolla' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué función permite invocar el constructor o métodos de la clase padre en la clase hija?\n\nOpciones:\n\n1. super()\n\n2. parent()\n\n3. base()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué función permite invocar el constructor o métodos de la clase padre en la clase hija?',
                "opciones": ['super()', 'parent()', 'base()'],
                "correcta": 0,
                "explicacion": 'super() otorga acceso directo a la clase base facilitando la extensión de código.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'estudiante: javier' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "class Producto:\n    def __init__(self, item, precio):\n        self.item = item\n        self.precio = precio\n    def __str__(self):\n        return f'{self.item}: ${self.precio}'\n\n# Modifica el precio a 25:\np = Producto('Teclado', 15)\nprint(p)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: '25' in res and 'teclado' in res.lower()
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una clase Punto con __init__(self, x, y) y un método especial __str__(self) que devuelva f'Punto({self.x}, {self.y})'. Crea p = Punto(3, 7) e imprímelo con print(p).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'Punto' in ns and str(ns.get('p')) == 'Punto(3, 4)' and 'punto(3, 4)' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Para qué sirve implementar el método especial __str__ en una clase?\n\nOpciones:\n\n1. Para definir la representación textual legible al imprimir el objeto con print()\n\n2. Para borrar el objeto de la memoria\n\n3. Para convertirlo en lista\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Para qué sirve implementar el método especial __str__ en una clase?',
                "opciones": ['Para definir la representación textual legible al imprimir el objeto con print()', 'Para borrar el objeto de la memoria', 'Para convertirlo en lista'],
                "correcta": 0,
                "explicacion": '__str__ devuelve una cadena amigable y comprensible para el lector de pantalla.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: '8' in res and '3.14' in res
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "import random\n# Modifica el rango para generar números entre 100 y 200:\nazar = random.randint(1, 10)\nprint('Número aleatorio:', azar)",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: 100 <= ns.get('azar', 0) <= 200
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Importa el módulo math y calcula la raíz cuadrada entera de 144 con math.isqrt(144). Imprime: print('Raíz de 144:', math.isqrt(144)).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: '12' in res and '144' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué palabra clave se usa para cargar módulos de la biblioteca estándar de Python?\n\nOpciones:\n\n1. import\n\n2. load\n\n3. include\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué palabra clave se usa para cargar módulos de la biblioteca estándar de Python?',
                "opciones": ['import', 'load', 'include'],
                "correcta": 0,
                "explicacion": 'import enlaza cualquier biblioteca estándar o archivo externo en tu código.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'elena' in res.lower() and 'json' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": 'import json\n# Modifica la duración a 60 horas:\ntexto = \'{"curso": "Python", "duracion_horas": 40}\'\nobjeto = json.loads(texto)\nprint(\'Curso:\', objeto[\'curso\'], \'Horas:\', objeto[\'duracion_horas\'])',
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: ns.get('objeto', {}).get('duracion_horas') == 60 and '60' in res
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Importa json. Crea un diccionario config = {'tema': 'oscuro', 'fuente': 14}. Conviértelo a texto JSON con json.dumps(config) e imprime: print('JSON:', json.dumps(config)).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'oscuro' in res and '14' in res and 'tema' in res
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué función del módulo json convierte un diccionario de Python en una cadena de texto JSON?\n\nOpciones:\n\n1. json.dumps()\n\n2. json.loads()\n\n3. json.parse()\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué función del módulo json convierte un diccionario de Python en una cadena de texto JSON?',
                "opciones": ['json.dumps()', 'json.loads()', 'json.parse()'],
                "correcta": 0,
                "explicacion": 'json.dumps() (dump string) serializa objetos de Python a texto JSON.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'maría' in res.lower() or 'maria' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": 'import sqlite3\ncon = sqlite3.connect(\':memory:\')\ncur = con.cursor()\ncur.execute(\'CREATE TABLE notas (materia TEXT, valor INT)\')\n# Agrega una segunda fila con Materia \'Python\' y Nota 10:\ncur.execute("INSERT INTO notas VALUES (\'Matemáticas\', 8)")\ncur.execute("SELECT * FROM notas")\nfilas = cur.fetchall()\nprint(\'Filas en la tabla:\', filas)',
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: 'python' in res.lower() or len(ns.get('filas', [])) >= 2
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Crea una base de datos SQLite en memoria con con = sqlite3.connect(':memory:'), crea una tabla productos (nombre TEXT) e inserta 'Teclado'. Luego consulta con SELECT y muestra el producto.",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'laptop' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué instrucción SQL se utiliza para consultar y extraer registros de una tabla?\n\nOpciones:\n\n1. SELECT\n\n2. INSERT\n\n3. DELETE\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué instrucción SQL se utiliza para consultar y extraer registros de una tabla?',
                "opciones": ['SELECT', 'INSERT', 'DELETE'],
                "correcta": 0,
                "explicacion": 'SELECT es la sentencia fundamental de consulta en SQL.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: '200' in res and 'servicio activo' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "respuesta = {\n    'codigo': 200,\n    'usuarios': ['Andrea', 'Pablo', 'Lucía']\n}\n# Modifica para agregar 'Marcos' a la lista de usuarios:\nprint('Lista de usuarios recibida:', respuesta['usuarios'])",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: 'marcos' in res.lower() or len(ns.get('respuesta', {}).get('usuarios', [])) >= 4
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Dada la respuesta simulada resp = {'estado': 'OK', 'mensaje': 'Servicio disponible'}, comprueba si resp['estado'] == 'OK' e imprime: print('API:', resp['mensaje']).",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: 'servicio disponible' in res.lower() and 'conectado' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Qué código de estado HTTP estándar indica que una petición web se resolvió con éxito?\n\nOpciones:\n\n1. 200 (OK)\n\n2. 404 (Not Found)\n\n3. 500 (Internal Error)\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Qué código de estado HTTP estándar indica que una petición web se resolvió con éxito?',
                "opciones": ['200 (OK)', '404 (Not Found)', '500 (Internal Error)'],
                "correcta": 0,
                "explicacion": 'El código 200 indica éxito en peticiones HTTP.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
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
                "validar": lambda src, res, ns: 'todas las aserciones superadas' in res.lower()
            },
            {
                "titulo": 'Paso 2: Observación y Modificación guiada',
                "tipo": 'experimentar',
                "instruccion": 'Explora el código en el editor, cambia algún parámetro o texto para comprobar cómo reacciona y ejecuta con Control + Enter.',
                "codigo": "def restar(a, b):\n    return a - b\n\n# Modifica la aserción para verificar que restar(20, 5) == 15:\nassert restar(10, 4) == 6\nprint('Prueba de restar superada')",
                "pistas": ['Modifica algún valor y presiona Control + Enter.'],
                "validar": lambda src, res, ns: 'restar(20, 5)' in src or 'restar(20,5)' in src or ('superada' in res.lower() and '15' in src)
            },
            {
                "titulo": 'Paso 3: Reto Práctico Interactivo',
                "tipo": 'desafio',
                "instruccion": "Define una función es_par(numero) que retorne numero % 2 == 0. Escribe assert es_par(4) == True y luego imprime: print('Todas las pruebas pasaron con éxito').",
                "codigo": '# Escribe aquí tu código para resolver el reto:\n\n',
                "pistas": ['Nivel 1: Sigue las instrucciones del paso.', 'Nivel 2: Comprueba la sintaxis de las variables o funciones.', 'Nivel 3: Ejecuta con Control + Enter para verificar.'],
                "validar": lambda src, res, ns: callable(ns.get('es_par')) and ns.get('es_par')(4) is True and ns.get('es_par')(5) is False and 'superada' in res.lower()
            },
            {
                "titulo": 'Paso 4: Verificación Conceptual',
                "tipo": 'quiz',
                "instruccion": 'Pregunta de verificación conceptual:\n\n¿Cuál es el propósito primordial de escribir pruebas unitarias?\n\nOpciones:\n\n1. Verificar de forma automática que cada pequeña parte del código funciona como se espera\n\n2. Hacer que el programa corra más rápido\n\n3. Cambiar el color del editor\n\nEscribe el número de tu opción (1, 2 o 3) y pulsa Control + Enter.',
                "codigo": '# Escribe aquí tu respuesta (1, 2 o 3):\n',
                "pistas": ['Lee detenidamente las 3 opciones.'],
                "pregunta": '¿Cuál es el propósito primordial de escribir pruebas unitarias?',
                "opciones": ['Verificar de forma automática que cada pequeña parte del código funciona como se espera', 'Hacer que el programa corra más rápido', 'Cambiar el color del editor'],
                "correcta": 0,
                "explicacion": 'Las pruebas unitarias garantizan que el código cumpla sus requisitos y previenen regresiones en el software.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    }
]

# ============================================================================
# Diccionario Completo de Términos de Python (Glosario Tiflotécnico)
# ============================================================================
GLOSARIO = {
    'AttributeError': 'Excepción producida al intentar invocar un atributo o método que no existe en el objeto.',
    'Exception': 'Clase base fundamental de la que heredan todas las excepciones estándar no críticas de Python.',
    'False': 'Valor booleano que representa la falsedad lógica.',
    'FileNotFoundError': 'Excepción producida al intentar abrir un archivo inexistente en la ruta indicada.',
    'IndentationError': 'Error de sintaxis producido por sangrías o indentaciones incorrectas según las normas de Python.',
    'IndexError': 'Excepción lanzada al intentar acceder a un índice fuera de los límites de una secuencia o lista.',
    'KeyError': 'Excepción que ocurre al buscar una clave inexistente dentro de un diccionario.',
    'NameError': 'Excepción lanzada al intentar usar una variable o función que no ha sido definida.',
    'None': 'Valor especial que representa la ausencia de valor o un resultado vacío.',
    'SyntaxError': 'Error que detecta el analizador sintáctico antes de ejecutar el código debido a reglas gramaticales rotas.',
    'Traceback': 'Informe detallado de depuración que describe la pila de llamadas y la línea exacta donde ocurrió un error.',
    'True': 'Valor booleano que representa la verdad lógica.',
    'TypeError': 'Excepción generada al intentar realizar una operación con un tipo de dato no admitido.',
    'ValueError': 'Excepción lanzada cuando una función recibe un argumento del tipo correcto pero con valor inapropiado.',
    'ZeroDivisionError': 'Excepción generada al intentar dividir un número entre cero.',
    '__eq__': 'Método especial que define el comportamiento del operador de igualdad (==) entre dos objetos.',
    '__init__': 'Método constructor especial que se ejecuta automáticamente al crear una nueva instancia de clase.',
    '__len__': 'Método especial que permite a un objeto responder a la función len().',
    '__repr__': 'Método especial que devuelve una cadena formal no ambigua con la representación técnica del objeto.',
    '__str__': 'Método especial que devuelve una representación en texto legible y amigable del objeto para print().',
    'abs': 'Devuelve el valor absoluto positivo de un número.',
    'algoritmo': 'Secuencia ordenada, precisa y finita de instrucciones lógicas para resolver un problema determinado.',
    'all': 'Devuelve True si todos los elementos de un iterable son verdaderos.',
    'and': 'Operador lógico que devuelve True únicamente si todas las condiciones que conecta son verdaderas.',
    'any': 'Devuelve True si al menos un elemento del iterable es verdadero.',
    'as': 'Palabra clave para asignar un alias o nombre alternativo a un módulo importado, gestor de contexto o excepción.',
    'assert': 'Instrucción de comprobación interna. Lanza una excepción AssertionError si la expresión evaluada resulta falsa.',
    'async': 'Define una función corrutina o contexto asíncrono para operaciones concurrentes no bloqueantes.',
    'atributo': 'Variable o dato asociado directamente a una instancia o clase.',
    'await': 'Pausa la ejecución de una corrutina hasta que la operación asíncrona devuelve su resultado.',
    'bin': 'Convierte un número entero en su representación de cadena binaria con prefijo 0b.',
    'bool': 'Tipo de dato booleano que solo puede ser True (verdadero) o False (falso).',
    'break': 'Interrumpe y finaliza de manera inmediata la ejecución del bucle for o while activo.',
    'bytes': 'Secuencia inmutable de bytes utilizada para datos binarios puros.',
    'callable': 'Devuelve True si el argumento pasado puede ser invocado como una función.',
    'casting': "Conversión explícita del valor de un tipo de dato a otro compatible (por ejemplo, int('25')).",
    'chr': 'Devuelve el carácter que corresponde al código Unicode entero proporcionado.',
    'clase': 'Molde o definición estructural que encapsula datos y comportamientos comunes a sus objetos.',
    'class': 'Define una nueva clase o plantilla para instanciar objetos con atributos y métodos propios.',
    'continue': 'Omite el resto del código del ciclo actual y avanza de inmediato a la siguiente iteración del bucle.',
    'def': 'Palabra clave para declarar una nueva función propia o método de clase con sus parámetros.',
    'del': 'Elimina referencias a variables, elementos de una lista o claves de un diccionario.',
    'dict': 'Colección asociativa y mutable de pares clave-valor encerrada entre llaves.',
    'dir': 'Devuelve la lista de atributos y métodos válidos disponibles para un objeto o módulo.',
    'docstring': 'Cadena de texto descriptiva ubicada al inicio de funciones o clases para documentar su funcionamiento.',
    'elif': "Abreviatura de 'else if'. Evalúa una condición alternativa cuando el bloque if previo resultó falso.",
    'else': 'Bloque alternativo final que se ejecuta si ninguna de las condiciones previas fue verdadera.',
    'encapsulamiento': 'Principio de proteger los datos internos de un objeto exponiendo interfaces seguras.',
    'enumerate': 'Agrega un contador a un iterable, devolviendo tuplas formadas por el índice y el elemento.',
    'except': 'Captura y gestiona una o más excepciones lanzadas dentro de un bloque try.',
    'f-string': 'Cadena de texto literal formateada anteponiendo la letra f que permite interpolar variables entre llaves.',
    'filter': 'Filtra elementos de un iterable según el resultado booleano de una función de prueba.',
    'finally': 'Bloque de try/except que se ejecuta siempre y sin excepción, ideal para liberar recursos.',
    'float': 'Tipo de dato numérico decimal o en coma flotante (por ejemplo, 3.14).',
    'for': 'Bucle para recorrer colecciones ordenadas, cadenas o rangos numéricos elemento por elemento.',
    'format': 'Convierte un valor en una representación formateada según una especificación.',
    'from': 'Permite importar partes específicas (funciones o clases) directamente desde un módulo o paquete.',
    'global': 'Declara que una variable dentro de una función pertenece al ámbito global del módulo.',
    'help': 'Invoca el sistema interactivo de documentación y ayuda integrada de Python.',
    'herencia': 'Mecanismo por el cual una subclase adquiere atributos y métodos de una clase superior.',
    'hex': 'Convierte un número entero en su representación de cadena hexadecimal con prefijo 0x.',
    'id': 'Devuelve el identificador numérico único de un objeto en la memoria.',
    'if': 'Estructura de decisión condicional fundamental que ejecuta un bloque si su condición es verdadera.',
    'import': 'Carga un módulo, biblioteca o archivo externo para usar sus herramientas en el script.',
    'in': 'Comprueba pertenencia de un elemento en una secuencia o colección, y se usa en bucles for.',
    'indentacion': 'Espaciado al inicio de las líneas de código que en Python delimita la estructura jerárquica de bloques.',
    'inmutabilidad': 'Propiedad de los tipos de datos cuyos valores no pueden alterarse tras su creación (como tuplas y strings).',
    'input': 'Pausa el script para solicitar datos por teclado al usuario, devolviendo siempre una cadena de texto (str).',
    'instancia': 'Objeto particular generado a partir de una plantilla de clase.',
    'int': 'Tipo de dato numérico entero, sin punto decimal, positivo, negativo o cero.',
    'is': 'Operador de identidad que comprueba si dos variables apuntan exactamente al mismo objeto en memoria.',
    'isinstance': 'Comprueba si un objeto dado es una instancia de una clase particular o tupla de clases.',
    'issubclass': 'Comprueba si una clase dada desciende o hereda directamente de otra clase.',
    'iterador': 'Objeto que produce un flujo sucesivo de valores uno a la vez utilizando el método __next__().',
    'lambda': 'Define una función anónima y compacta en una sola línea de código sin usar def.',
    'len': 'Devuelve la longitud o número total de elementos contenidos en una secuencia o colección.',
    'list': 'Colección ordenada y mutable de elementos entre corchetes, separados por comas.',
    'map': 'Aplica una función dada a cada uno de los elementos de un iterable devolviendo un iterador.',
    'max': 'Devuelve el elemento con el valor más alto dentro de un conjunto o secuencia.',
    'metodo': 'Función que reside y actúa dentro del contexto de una clase u objeto.',
    'min': 'Devuelve el elemento con el valor más bajo dentro de un conjunto o secuencia.',
    'mutabilidad': 'Propiedad de los tipos de datos que pueden modificarse en su lugar (como listas y diccionarios).',
    'nonlocal': 'Indica que una variable pertenece a una función contenedora superior, no al ámbito local ni global.',
    'not': 'Operador lógico de negación que invierte el valor de verdad (convierte True en False y viceversa).',
    'objeto': 'Instancia concreta creada a partir de una clase con su propio estado interno en memoria.',
    'open': 'Abre un archivo del disco para lectura, escritura o adición, devolviendo un objeto de archivo.',
    'or': 'Operador lógico que devuelve True si al menos una de las condiciones conectadas es verdadera.',
    'ord': 'Devuelve el código entero Unicode que representa a un carácter individual.',
    'pass': 'Operación nula o marcador de posición que se usa cuando la sintaxis requiere una línea pero no se desea ejecutar nada.',
    'pep8': 'Guía de estilo oficial del código Python que promueve legibilidad, como el uso de 4 espacios por nivel.',
    'pip': 'Herramienta oficial de gestión e instalación de paquetes de software y bibliotecas externas de Python.',
    'polimorfismo': 'Capacidad de distintas clases de responder a un mismo método de manera personalizada.',
    'pow': 'Eleva un número a una potencia dada (equivalente al operador **).',
    'print': 'Emite datos y mensajes formateados a la consola para su verbalización por el sintetizador de voz.',
    'raise': 'Genera y lanza intencionadamente una excepción para señalar un error o anomalía.',
    'range': 'Genera una secuencia inmutable de números enteros, comúnmente utilizada en bucles for.',
    'return': 'Finaliza la ejecución de una función y devuelve opcionalmente un valor al llamador.',
    'reversed': 'Devuelve un iterador inverso para recorrer los elementos en sentido contrario.',
    'round': 'Redondea un número decimal a un número especificado de posiciones decimales.',
    'scope': 'Ámbito de visibilidad y vida útil de una variable (local dentro de una función o global en el script).',
    'self': 'Primer parámetro convencional de los métodos de instancia que representa al propio objeto concreto.',
    'set': 'Colección desordenada y mutable de elementos únicos sin elementos repetidos, delimitada por llaves.',
    'sorted': 'Devuelve una nueva lista ordenada con todos los elementos de un iterable sin modificar el original.',
    'str': 'Cadena de caracteres o texto alfanumérico rodeado por comillas.',
    'sum': 'Calcula y devuelve la suma total de los elementos numéricos contenidos en un iterable.',
    'super': 'Función que da acceso al constructor y métodos de la clase padre o superior en jerarquías de herencia.',
    'try': 'Inicia un bloque de código vigilado donde se anticipan posibles excepciones o errores en tiempo de ejecución.',
    'tuple': 'Colección ordenada e inmutable de elementos entre paréntesis, separada por comas.',
    'type': 'Devuelve el tipo de dato o la clase a la que pertenece un objeto.',
    'venv': 'Entorno virtual aislado que permite gestionar versiones de paquetes de forma independiente por proyecto.',
    'while': 'Bucle que repite sus instrucciones mientras una condición lógica continúe siendo verdadera.',
    'with': 'Gestor de contexto que garantiza la adquisición y liberación segura de recursos (por ejemplo, cerrar archivos).',
    'yield': 'Pausa una función generadora y emite un valor sucesivo, conservando su estado para la siguiente llamada.',
    'zip': 'Empareja en tuplas elementos correspondientes de múltiples iterables al mismo tiempo.',
}
