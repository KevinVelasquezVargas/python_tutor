# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/curriculum.py
# Propósito: Temario pedagógico estructurado por micro-pasos interactivos (Action-First).
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

CURRICULUM = [
    {
        "id": 1,
        "titulo": "Capítulo 1: Conceptos Básicos y Primer Programa",
        "resumen": "¿Qué es programar y qué es Python? Descubre los conceptos fundamentales y escribe tu primer saludo con print().",
        "pasos": [
            {
                "titulo": "Paso 1: ¿Qué es Python y cómo le hablamos a la computadora?",
                "tipo": "observar",
                "instruccion": "Una computadora necesita instrucciones exactas para funcionar. Python es un lenguaje de programación diseñado para que las personas podamos escribir esas instrucciones de forma clara y sencilla. La instrucción print() le ordena a la computadora que muestre un mensaje en pantalla y te lo transmita por voz con NVDA. Pulsa Control + Enter para ejecutar tu primer programa y escuchar el saludo.",
                "codigo": "print('¡Hola mundo!')",
                "pistas": [
                    "Solo debes pulsar la combinación de teclas Control + Enter. Escucharás la señal sonora y la confirmación de voz de tu primer programa ejecutado."
                ],
                "pruebas": [
                    {
                        "nombre": "Saludo inicial emitido",
                        "check": lambda src, res, ns: "hola mundo" in res.lower()
                    }
                ],
                "validar": lambda src, res, ns: "hola mundo" in res.lower()
            },
            {
                "titulo": "Paso 2: Comillas y personalización de mensajes",
                "tipo": "experimentar",
                "instruccion": "Para que Python entienda que algo es un mensaje de texto para personas y no una orden de programación, siempre debemos escribirlo dentro de comillas simples o dobles. Cambia el texto '¡Hola mundo!' por tu propio saludo o tu nombre. Por ejemplo: print('Hola, estoy aprendiendo Python'). Luego pulsa Control + Enter.",
                "codigo": "print('Hola, estoy aprendiendo Python')",
                "pistas": [
                    "Nivel 1: Usa las flechas para situarte dentro de las comillas, borra el texto con Retroceso y escribe tu saludo.",
                    "Nivel 2: Es fundamental mantener los paréntesis y las comillas alrededor del mensaje.",
                    "Nivel 3: Por ejemplo, puedes escribir: print('Hola, me llamo Juan')"
                ],
                "pruebas": [
                    {
                        "nombre": "Mensaje personalizado emitido",
                        "check": lambda src, res, ns: len(res.strip()) > 0 and "hola mundo" not in res.lower()
                    }
                ],
                "validar": lambda src, res, ns: len(res.strip()) > 0 and "hola mundo" not in res.lower()
            },
            {
                "titulo": "Paso 3: El orden de ejecución (Flujo secuencial)",
                "tipo": "desafio",
                "instruccion": "Python lee y ejecuta las instrucciones una por una, exactamente en el orden en que las escribes, de arriba hacia abajo. En el editor ya tienes una primera línea. Añade una segunda línea abajo que diga: print('Este es mi segundo mensaje'). Luego pulsa Control + Enter para escuchar las dos frases en orden.",
                "codigo": "print('Mi primera línea de código')\nprint('Este es mi segundo mensaje')",
                "pistas": [
                    "Nivel 1: Cada instrucción print() debe colocarse en su propio renglón.",
                    "Nivel 2: Coloca el cursor al final de la primera línea, presiona la tecla Enter y escribe la segunda línea.",
                    "Nivel 3: El programa final debe contener dos instrucciones print ejecutándose una tras otra."
                ],
                "pruebas": [
                    {
                        "nombre": "Dos líneas impresas secuencialmente",
                        "check": lambda src, res, ns: len([l for l in res.strip().splitlines() if l.strip()]) >= 2
                    }
                ],
                "validar": lambda src, res, ns: len([l for l in res.strip().splitlines() if l.strip()]) >= 2
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Para qué sirve la instrucción print('Hola') en Python?\n\nOpciones:\n1. Para mostrar el texto 'Hola' en la salida de pantalla y transmitirlo al lector.\n2. Para imprimir físicamente una hoja de papel en la impresora.\n3. Para apagar el equipo.\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Para qué sirve la instrucción print('Hola') en Python?",
                "opciones": [
                    "Para mostrar el texto 'Hola' en la salida de pantalla y transmitirlo al lector.",
                    "Para imprimir físicamente una hoja de papel en la impresora.",
                    "Para apagar el equipo."
                ],
                "correcta": 0,
                "explicacion": "¡Exacto! En programación, print() envía información a la salida estándar para que la leas en la consola o la escuches con NVDA.",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 2,
        "titulo": "Capítulo 2: Texto, Mensajes y Números en la Salida",
        "resumen": "Aprende a realizar cálculos directos con print(), combinar varios datos con comas y corregir errores de escritura.",
        "pasos": [
            {
                "titulo": "Paso 1: Cálculos matemáticos directos con print()",
                "tipo": "observar",
                "instruccion": "A diferencia del texto, los números en Python se escriben sin comillas. Si escribes una operación matemática dentro de print(), Python primero realiza el cálculo y luego muestra el resultado numérico. Pulsa Control + Enter para comprobar cómo calcula la suma de 5 más 3.",
                "codigo": "print('La suma de 5 más 3 es:')\nprint(5 + 3)",
                "pistas": ["Pulsa Control + Enter para escuchar el resultado del cálculo."],
                "pruebas": [
                    {
                        "nombre": "Cálculo matemático correcto",
                        "check": lambda src, res, ns: "8" in res
                    }
                ],
                "validar": lambda src, res, ns: "8" in res
            },
            {
                "titulo": "Paso 2: Imprimir múltiples datos separados por coma",
                "tipo": "experimentar",
                "instruccion": "Puedes mostrar varios datos a la vez en una sola llamada de print() separándolos con una coma. Python colocará un espacio automático entre ellos. Cambia el código para imprimir tu edad con: print('Tengo', 20, 'años'). Pulsa Control + Enter.",
                "codigo": "print('Tengo', 25, 'años')",
                "pistas": ["Separa las palabras entre comillas del número con comas."],
                "pruebas": [
                    {
                        "nombre": "Texto y número combinados",
                        "check": lambda src, res, ns: "tengo" in res.lower() and "años" in res.lower()
                    }
                ],
                "validar": lambda src, res, ns: "tengo" in res.lower() and "años" in res.lower()
            },
            {
                "titulo": "Paso 3: Desafío: Detectar y corregir un error de escritura (NameError)",
                "tipo": "desafio",
                "instruccion": "Python es muy exacto. Si escribes mal el nombre de una orden, como 'prnt' en lugar de 'print', la computadora no sabrá qué hacer y emitirá un NameError. Corrige la palabra 'prnt' en la línea para que diga 'print' y pulsa Control + Enter.",
                "codigo": "prnt('¡Sintaxis corregida con éxito!')",
                "pistas": [
                    "Nivel 1: Falta la letra 'i' en la función print.",
                    "Nivel 2: Cambia 'prnt' por 'print' en minúsculas.",
                    "Nivel 3: La línea corregida debe ser: print('¡Sintaxis corregida con éxito!')"
                ],
                "pruebas": [
                    {
                        "nombre": "Sintaxis válida de print",
                        "check": lambda src, res, ns: "Sintaxis corregida" in res and "prnt" not in src
                    }
                ],
                "validar": lambda src, res, ns: "Sintaxis corregida" in res and "prnt" not in src
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Por qué en Python los números a operar se escriben sin comillas y el texto con comillas?\n\nOpciones:\n1. Porque sin comillas Python los reconoce como valores matemáticos y con comillas como texto plano.\n2. Porque las comillas son obligatorias en absolutamente todo.\n3. Para que el texto se imprima en negrita.\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Por qué en Python los números a operar se escriben sin comillas y el texto con comillas?",
                "opciones": [
                    "Porque sin comillas Python los reconoce como valores matemáticos y con comillas como texto plano.",
                    "Porque las comillas son obligatorias en absolutamente todo.",
                    "Para que el texto se imprima en negrita."
                ],
                "correcta": 0,
                "explicacion": "Así es. Sin comillas Python procesa números y realiza cálculos; con comillas los trata como texto literal.",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 3,
        "titulo": "Capítulo 3: Almacenamiento en Memoria y Variables",
        "resumen": "Aprende a guardar datos en la memoria del equipo mediante nombres descriptivos y el operador de asignación (=).",
        "pasos": [
            {
                "titulo": "Paso 1: Observar y Predecir",
                "tipo": "observar",
                "instruccion": "Una variable almacena un valor bajo una etiqueta de texto. Ejecuta este código para ver cómo se usa la variable 'usuario'.",
                "codigo": "usuario = 'Estudiante'\nprint('Sesión activa para:', usuario)",
                "pistas": ["Pulsa Control + Enter para ejecutar."],
                "validar": lambda src, res, ns: ns.get("usuario") == "Estudiante"
            },
            {
                "titulo": "Paso 2: Experimentar y Modificar",
                "tipo": "experimentar",
                "instruccion": "Cambia el valor de 'usuario' por tu propio nombre entre comillas y vuelve a ejecutar.",
                "codigo": "usuario = 'Kevin'\nprint('Sesión activa para:', usuario)",
                "pistas": ["Reemplaza 'Estudiante' por tu nombre, por ejemplo 'Elena' o 'Carlos'."],
                "validar": lambda src, res, ns: "usuario" in ns and ns["usuario"] != "Estudiante"
            },
            {
                "titulo": "Paso 3: Desafío de Construcción",
                "tipo": "desafio",
                "instruccion": "Crea dos variables: 'ciudad' con el valor 'Madrid' y 'pais' con 'España'. Luego imprime ambas separadas por coma.",
                "codigo": "# Declara las variables ciudad y pais abajo:\nciudad = ''\npais = ''\nprint(ciudad, pais)",
                "pistas": [
                    "Nivel 1: Llena las comillas: ciudad = 'Madrid' y pais = 'España'.",
                    "Nivel 2: Comprueba que los identificadores de variable no tengan espacios.",
                    "Nivel 3: El print ya está listo, solo debes dar valor a ciudad y pais."
                ],
                "pruebas": [
                    {
                        "nombre": "Variables declaradas correctamente",
                        "check": lambda src, res, ns: len(str(ns.get("ciudad", ""))) > 0 and len(str(ns.get("pais", ""))) > 0
                    }
                ],
                "validar": lambda src, res, ns: len(str(ns.get("ciudad", ""))) > 0 and len(str(ns.get("pais", ""))) > 0
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué símbolo se utiliza en Python para asignar un valor a una variable?\n\nOpciones:\n1. El signo igual (=)\n2. Dos puntos (:)\n3. El signo de flecha (->)\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Qué símbolo se utiliza en Python para asignar un valor a una variable?",
                "opciones": [
                    "El signo igual (=)",
                    "Dos puntos (:)",
                    "El signo de flecha (->)"
                ],
                "correcta": 0,
                "explicacion": "Correcto. El operador de asignación simple es el signo igual (=).",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 4,
        "titulo": "Capítulo 4: Tipos de Datos Primitivos: str e int",
        "resumen": "Diferencia entre texto (secuencias entre comillas) y números enteros aptos para operaciones matemáticas.",
        "pasos": [
            {
                "titulo": "Paso 1: Observar y Predecir",
                "tipo": "observar",
                "instruccion": "Los números se escriben directamente sin comillas, mientras que los textos van entre comillas. Ejecuta y comprueba cómo se calcula la suma.",
                "codigo": "unidades = 10\npaquete = 5\ntotal = unidades + paquete\nprint('Total de unidades:', total)",
                "pistas": ["Pulsa Control + Enter para evaluar."],
                "validar": lambda src, res, ns: ns.get("total") == 15
            },
            {
                "titulo": "Paso 2: Experimentar y Modificar",
                "tipo": "experimentar",
                "instruccion": "Cambia 'unidades' a 20 y 'paquete' a 10. Ejecuta de nuevo para confirmar que total da 30.",
                "codigo": "unidades = 20\npaquete = 10\ntotal = unidades + paquete\nprint('Total de unidades:', total)",
                "pistas": ["Modifica los valores numéricos sin añadir comillas."],
                "validar": lambda src, res, ns: ns.get("total") == 30
            },
            {
                "titulo": "Paso 3: Desafío de Construcción",
                "tipo": "desafio",
                "instruccion": "El siguiente código falla con TypeError porque el número 50 está atrapado entre comillas como texto ('50'). Quita las comillas para permitir la suma.",
                "codigo": "base = 100\nextra = '50'\nresultado = base + extra\nprint('Resultado consolidado:', resultado)",
                "pistas": [
                    "Nivel 1: Borra las comillas que rodean al 50.",
                    "Nivel 2: Debe quedar extra = 50 en lugar de extra = '50'.",
                    "Nivel 3: El resultado final debe ser el número 150."
                ],
                "pruebas": [
                    {
                        "nombre": "Suma matemática exitosa",
                        "check": lambda src, res, ns: ns.get("resultado") == 150
                    }
                ],
                "validar": lambda src, res, ns: ns.get("resultado") == 150
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué ocurre si ejecutas '10' + '20' en Python?\n\nOpciones:\n1. Une los textos dando '1020'.\n2. Suma los números dando 30.\n3. Genera un error de sintaxis.\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Qué ocurre si ejecutas '10' + '20' en Python?",
                "opciones": [
                    "Une los textos dando '1020'.",
                    "Suma los números dando 30.",
                    "Genera un error de sintaxis."
                ],
                "correcta": 0,
                "explicacion": "Exacto. Al sumar dos cadenas de texto (str), Python realiza una concatenación, juntándolas en '1020'.",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 5,
        "titulo": "Capítulo 5: Estructuración y Sangría PEP 8",
        "resumen": "Aprende el uso fundamental de la sangría (4 espacios físicos) para definir bloques de código subordinados.",
        "pasos": [
            {
                "titulo": "Paso 1: Observar y Predecir",
                "tipo": "observar",
                "instruccion": "En Python, los bloques dentro de un 'if' deben llevar 4 espacios de sangría al inicio. Pulsa Control + Enter para escuchar.",
                "codigo": "conectado = True\nif conectado:\n    print('Acceso autorizado al sistema.')",
                "pistas": ["Pulsa Control + Enter."],
                "validar": lambda src, res, ns: "Acceso autorizado" in res
            },
            {
                "titulo": "Paso 2: Experimentar y Modificar",
                "tipo": "experimentar",
                "instruccion": "Cambia 'conectado = True' a 'conectado = False'. Al ejecutar, notarás que el mensaje ya no se imprime porque la condición no se cumplió.",
                "codigo": "conectado = False\nif conectado:\n    print('Acceso autorizado al sistema.')",
                "pistas": ["Escribe False con la primera letra en mayúscula."],
                "validar": lambda src, res, ns: ns.get("conectado") is False
            },
            {
                "titulo": "Paso 3: Desafío de Construcción",
                "tipo": "desafio",
                "instruccion": "La línea 3 no tiene sangría y provoca un IndentationError. Ve al inicio de la línea 3 y presiona la tecla Tabulador para insertar 4 espacios.",
                "codigo": "verificado = True\nif verificado:\nprint('Identidad confirmada')",
                "pistas": [
                    "Nivel 1: Coloca el cursor antes de la 'p' de print en la línea 3.",
                    "Nivel 2: Presiona la tecla Tabulador; el editor insertará 4 espacios físicos automáticamente.",
                    "Nivel 3: La línea debe quedar: '    print(\"Identidad confirmada\")'"
                ],
                "pruebas": [
                    {
                        "nombre": "Sangría PEP 8 aplicada",
                        "check": lambda src, res, ns: "Identidad confirmada" in res
                    }
                ],
                "validar": lambda src, res, ns: "Identidad confirmada" in res
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Cuántos espacios componen el nivel de sangría estándar según la guía oficial PEP 8 de Python?\n\nOpciones:\n1. 4 espacios físicos.\n2. 2 espacios físicos.\n3. 8 espacios físicos.\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Cuántos espacios componen el nivel de sangría estándar según la guía oficial PEP 8 de Python?",
                "opciones": [
                    "4 espacios físicos.",
                    "2 espacios físicos.",
                    "8 espacios físicos."
                ],
                "correcta": 0,
                "explicacion": "Correcto. El estándar de la comunidad Python establece exactamente 4 espacios por cada nivel de anidación.",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 6,
        "titulo": "Capítulo 6: Conversión de Tipos (Type Casting)",
        "resumen": "Aprende a transformar datos entre texto, enteros y números decimales usando int(), float() y str().",
        "pasos": [
            {
                "titulo": "Paso 1: Observar y Predecir",
                "tipo": "observar",
                "instruccion": "La función int() convierte texto numérico a entero. Ejecuta el código para observar cómo se realiza la conversión.",
                "codigo": "entrada = '25'\nedad = int(entrada)\nprint('Edad el próximo año:', edad + 1)",
                "pistas": ["Pulsa Control + Enter."],
                "validar": lambda src, res, ns: ns.get("edad") == 25
            },
            {
                "titulo": "Paso 2: Experimentar y Modificar",
                "tipo": "experimentar",
                "instruccion": "Para números con decimales usamos float(). Cambia 'precio_str = \"19.99\"' y usa float(precio_str) para calcular el doble.",
                "codigo": "precio_str = '19.99'\nprecio = float(precio_str)\ndoble = precio * 2\nprint('El doble del precio es:', doble)",
                "pistas": ["Usa float() para convertir texto con punto decimal."],
                "validar": lambda src, res, ns: abs(ns.get("doble", 0) - 39.98) < 0.01
            },
            {
                "titulo": "Paso 3: Desafío de Construcción",
                "tipo": "desafio",
                "instruccion": "Dispones de dos variables con texto: 'precio_txt = \"10.50\"' y 'cantidad_txt = \"4\"'. Convierte el precio a float, la cantidad a int, multiplícalos en la variable 'total' e imprímelo.",
                "codigo": "precio_txt = '10.50'\ncantidad_txt = '4'\n# Convierte abajo precio_txt a float y cantidad_txt a int:\ntotal = float(precio_txt) * int(cantidad_txt)\nprint('Total:', total)",
                "pistas": [
                    "Nivel 1: Aplica float(precio_txt) e int(cantidad_txt).",
                    "Nivel 2: La multiplicación es con el asterisco *.",
                    "Nivel 3: total = float(precio_txt) * int(cantidad_txt)"
                ],
                "pruebas": [
                    {
                        "nombre": "Cálculo con conversión",
                        "check": lambda src, res, ns: ns.get("total") == 42.0
                    }
                ],
                "validar": lambda src, res, ns: ns.get("total") == 42.0
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué función convierte cualquier tipo de dato a texto en Python?\n\nOpciones:\n1. str()\n2. text()\n3. toString()\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Qué función convierte cualquier tipo de dato a texto en Python?",
                "opciones": [
                    "str()",
                    "text()",
                    "toString()"
                ],
                "correcta": 0,
                "explicacion": "Así es. str() es la función integrada para transformar números o datos a cadena de texto.",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 7,
        "titulo": "Capítulo 7: Prioridad de Operadores Aritméticos",
        "resumen": "Aprende el orden de evaluación PEMDAS y el uso de paréntesis para garantizar cálculos matemáticos precisos.",
        "pasos": [
            {
                "titulo": "Paso 1: Observar y Predecir",
                "tipo": "observar",
                "instruccion": "La multiplicación tiene prioridad sobre la suma. En 2 + 3 * 4, primero se calcula 3 * 4 = 12 y luego + 2 = 14. Ejecuta y comprueba.",
                "codigo": "calculo = 2 + 3 * 4\nprint('Resultado:', calculo)",
                "pistas": ["Pulsa Control + Enter."],
                "validar": lambda src, res, ns: ns.get("calculo") == 14
            },
            {
                "titulo": "Paso 2: Experimentar y Modificar",
                "tipo": "experimentar",
                "instruccion": "Agrega paréntesis para forzar la suma primero: (2 + 3) * 4. Al ejecutar, el resultado cambiará a 20.",
                "codigo": "calculo = (2 + 3) * 4\nprint('Resultado con paréntesis:', calculo)",
                "pistas": ["Encierra '2 + 3' entre paréntesis."],
                "validar": lambda src, res, ns: ns.get("calculo") == 20
            },
            {
                "titulo": "Paso 3: Desafío de Construcción",
                "tipo": "desafio",
                "instruccion": "Calcula el promedio de tres notas: 8.0, 9.5 y 6.5. Agrupa la suma entre paréntesis antes de dividir entre 3 en la variable 'promedio'.",
                "codigo": "n1 = 8.0\nn2 = 9.5\nn3 = 6.5\n# Agrega parentesis en la siguiente linea:\npromedio = (n1 + n2 + n3) / 3\nprint('Promedio final:', promedio)",
                "pistas": [
                    "Nivel 1: Sin paréntesis, Python solo divide la última nota (6.5 / 3).",
                    "Nivel 2: Agrupa las tres notas: (n1 + n2 + n3).",
                    "Nivel 3: promedio = (n1 + n2 + n3) / 3"
                ],
                "pruebas": [
                    {
                        "nombre": "Promedio exacto",
                        "check": lambda src, res, ns: abs(ns.get("promedio", 0) - 8.0) < 0.01
                    }
                ],
                "validar": lambda src, res, ns: abs(ns.get("promedio", 0) - 8.0) < 0.01
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué operador aritmético calcula la potencia o exponente en Python?\n\nOpciones:\n1. Doble asterisco (**)\n2. Acento circunflejo (^)\n3. Doble barra (//)\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Qué operador aritmético calcula la potencia o exponente en Python?",
                "opciones": [
                    "Doble asterisco (**)",
                    "Acento circunflejo (^)",
                    "Doble barra (//)"
                ],
                "correcta": 0,
                "explicacion": "Correcto. El operador ** se usa para potencias, por ejemplo 2 ** 3 da 8.",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 8,
        "titulo": "Capítulo 8: Operadores de Comparación y Estructura if",
        "resumen": "Aprende a tomar decisiones en el código evaluando igualdades (==) y desigualdades (!=, >, <).",
        "pasos": [
            {
                "titulo": "Paso 1: Observar y Predecir",
                "tipo": "observar",
                "instruccion": "El operador == compara si dos valores son iguales. Ejecuta el código para observar la validación.",
                "codigo": "clave_guardada = 'secreto123'\nclave_ingresada = 'secreto123'\nif clave_ingresada == clave_guardada:\n    print('Acceso concedido')",
                "pistas": ["Pulsa Control + Enter."],
                "validar": lambda src, res, ns: "Acceso concedido" in res
            },
            {
                "titulo": "Paso 2: Experimentar y Modificar",
                "tipo": "experimentar",
                "instruccion": "Cambia clave_ingresada por 'incorrecta'. Al ejecutar, no se imprimirá nada porque no coinciden.",
                "codigo": "clave_guardada = 'secreto123'\nclave_ingresada = 'incorrecta'\nif clave_ingresada == clave_guardada:\n    print('Acceso concedido')",
                "pistas": ["Modifica el texto asignado a clave_ingresada."],
                "validar": lambda src, res, ns: ns.get("clave_ingresada") == "incorrecta"
            },
            {
                "titulo": "Paso 3: Desafío de Construcción",
                "tipo": "desafio",
                "instruccion": "Tienes una variable 'edad = 18'. Escribe una condición que verifique si edad es mayor o igual a 18 (>= 18) e imprima 'Mayor de edad'.",
                "codigo": "edad = 18\n# Escribe el condicional if abajo:\nif edad >= 18:\n    print('Mayor de edad')",
                "pistas": [
                    "Nivel 1: Usa el operador >=.",
                    "Nivel 2: No olvides los dos puntos al final de la línea if.",
                    "Nivel 3: if edad >= 18:\n    print('Mayor de edad')"
                ],
                "pruebas": [
                    {
                        "nombre": "Condicional evaluado",
                        "check": lambda src, res, ns: "Mayor de edad" in res
                    }
                ],
                "validar": lambda src, res, ns: "Mayor de edad" in res
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Cuál es la diferencia entre el signo '=' y el doble signo '==' en Python?\n\nOpciones:\n1. =' asigna un valor a una variable; '==' compara si dos valores son iguales.\n2. Ambos hacen exactamente lo mismo.\n3. ==' solo se usa con números enteros.\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Cuál es la diferencia entre el signo '=' y el doble signo '==' en Python?",
                "opciones": [
                    "'=' asigna un valor a una variable; '==' compara si dos valores son iguales.",
                    "Ambos hacen exactamente lo mismo.",
                    "'==' solo se usa con números enteros."
                ],
                "correcta": 0,
                "explicacion": "Exacto. '=' es asignación (guardar) y '==' es comparación de equivalencia.",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 9,
        "titulo": "Capítulo 9: Operadores Lógicos (and, or, not)",
        "resumen": "Combina múltiples condiciones booleanas para evaluar reglas de negocio complejas.",
        "pasos": [
            {
                "titulo": "Paso 1: Observar y Predecir",
                "tipo": "observar",
                "instruccion": "El operador 'and' exige que ambas condiciones sean verdaderas. Ejecuta para ver el resultado.",
                "codigo": "tiene_ticket = True\ntiene_documento = True\npuede_viajar = tiene_ticket and tiene_documento\nprint('¿Puede viajar?:', puede_viajar)",
                "pistas": ["Pulsa Control + Enter."],
                "validar": lambda src, res, ns: ns.get("puede_viajar") is True
            },
            {
                "titulo": "Paso 2: Experimentar y Modificar",
                "tipo": "experimentar",
                "instruccion": "El operador 'or' da True si al menos una condición es verdadera. Cambia 'and' por 'or' y pon tiene_ticket en False. Comprueba que puede_viajar sigue siendo True.",
                "codigo": "tiene_ticket = False\ntiene_documento = True\npuede_viajar = tiene_ticket or tiene_documento\nprint('¿Puede viajar con or?:', puede_viajar)",
                "pistas": ["Reemplaza 'and' por 'or'."],
                "validar": lambda src, res, ns: ns.get("puede_viajar") is True and ns.get("tiene_ticket") is False
            },
            {
                "titulo": "Paso 3: Desafío de Construcción",
                "tipo": "desafio",
                "instruccion": "Un usuario puede descargar un archivo si está conectado Y (tiene saldo O es administrador). Completa la expresión en 'puede_descargar'.",
                "codigo": "conectado = True\ntiene_saldo = False\nes_admin = True\n# Completa la regla con and, or y parentesis:\npuede_descargar = conectado and (tiene_saldo or es_admin)\nprint('Autorizado:', puede_descargar)",
                "pistas": [
                    "Nivel 1: Usa paréntesis para agrupar (tiene_saldo or es_admin).",
                    "Nivel 2: Une con 'conectado and ...'.",
                    "Nivel 3: puede_descargar = conectado and (tiene_saldo or es_admin)"
                ],
                "pruebas": [
                    {
                        "nombre": "Regla lógica válida",
                        "check": lambda src, res, ns: ns.get("puede_descargar") is True
                    }
                ],
                "validar": lambda src, res, ns: ns.get("puede_descargar") is True
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué hace el operador 'not' en Python?\n\nOpciones:\n1. Invierte el valor booleano: de True pasa a False y viceversa.\n2. Borra la variable de la memoria.\n3. Convierte el número a negativo.\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Qué hace el operador 'not' en Python?",
                "opciones": [
                    "Invierte el valor booleano: de True pasa a False y viceversa.",
                    "Borra la variable de la memoria.",
                    "Convierte el número a negativo."
                ],
                "correcta": 0,
                "explicacion": "Correcto. 'not True' resulta en False y 'not False' resulta en True.",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 10,
        "titulo": "Capítulo 10: Decisiones Múltiples con la Cláusula elif",
        "resumen": "Aprende a evaluar múltiples opciones excluyentes de forma ordenada sin anidar bloques infinitos.",
        "pasos": [
            {
                "titulo": "Paso 1: Observar y Predecir",
                "tipo": "observar",
                "instruccion": "'elif' significa 'si no, prueba si...'. Evalúa secuencialmente y ejecuta solo la primera condición verdadera. Ejecuta.",
                "codigo": "temperatura = 22\nif temperatura > 30:\n    print('Hace calor')\nelif temperatura >= 15:\n    print('Clima templado')\nelse:\n    print('Hace frío')",
                "pistas": ["Pulsa Control + Enter."],
                "validar": lambda src, res, ns: "Clima templado" in res
            },
            {
                "titulo": "Paso 2: Experimentar y Modificar",
                "tipo": "experimentar",
                "instruccion": "Cambia temperatura a 35 y ejecuta de nuevo para comprobar que ahora entra en 'Hace calor'.",
                "codigo": "temperatura = 35\nif temperatura > 30:\n    print('Hace calor')\nelif temperatura >= 15:\n    print('Clima templado')\nelse:\n    print('Hace frío')",
                "pistas": ["Cambia la primera línea a: temperatura = 35."],
                "validar": lambda src, res, ns: "Hace calor" in res
            },
            {
                "titulo": "Paso 3: Desafío de Construcción",
                "tipo": "desafio",
                "instruccion": "Tienes una calificación de 85 puntos. Muestra 'Excelente' si es >= 90, 'Aceptable' si es >= 80 y 'Reprobado' en cualquier otro caso usando if, elif y else.",
                "codigo": "nota = 85\nif nota >= 90:\n    print('Excelente')\nelif nota >= 80:\n    print('Aceptable')\nelse:\n    print('Reprobado')",
                "pistas": [
                    "Nivel 1: Usa 'elif nota >= 80:'.",
                    "Nivel 2: No olvides sangrar 4 espacios dentro de cada bloque.",
                    "Nivel 3: El programa debe imprimir 'Aceptable'."
                ],
                "pruebas": [
                    {
                        "nombre": "Evaluación con elif",
                        "check": lambda src, res, ns: "Aceptable" in res and "Excelente" not in res
                    }
                ],
                "validar": lambda src, res, ns: "Aceptable" in res and "Excelente" not in res
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Cuándo se ejecuta el bloque 'else' final?\n\nOpciones:\n1. Únicamente cuando todas las condiciones anteriores ('if' y 'elif') fueron falsas.\n2. Siempre al terminar el script.\n3. Solo si ocurre un error sintáctico.\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Cuándo se ejecuta el bloque 'else' final?",
                "opciones": [
                    "Únicamente cuando todas las condiciones anteriores ('if' y 'elif') fueron falsas.",
                    "Siempre al terminar el script.",
                    "Solo si ocurre un error sintáctico."
                ],
                "correcta": 0,
                "explicacion": "Exacto. El bloque 'else' es la opción de respaldo por defecto.",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 11,
        "titulo": "Capítulo 11: Secuencias Ordenadas: Introducción a las Listas",
        "resumen": "Aprende a almacenar colecciones de elementos entre corchetes [] y acceder a ellos por índice.",
        "pasos": [
            {
                "titulo": "Paso 1: Observar y Predecir",
                "tipo": "observar",
                "instruccion": "Las listas se indexan desde 0. 'frutas[0]' obtiene el primer elemento. Ejecuta el código.",
                "codigo": "frutas = ['manzana', 'platano', 'naranja']\nprimera = frutas[0]\nprint('Primera fruta:', primera)",
                "pistas": ["Pulsa Control + Enter."],
                "validar": lambda src, res, ns: ns.get("primera") == "manzana"
            },
            {
                "titulo": "Paso 2: Experimentar y Modificar",
                "tipo": "experimentar",
                "instruccion": "Python admite índices negativos: el índice -1 apunta al último elemento. Cambia para extraer 'frutas[-1]'.",
                "codigo": "frutas = ['manzana', 'platano', 'naranja']\nultima = frutas[-1]\nprint('Última fruta:', ultima)",
                "pistas": ["Escribe frutas[-1] para obtener 'naranja'."],
                "validar": lambda src, res, ns: ns.get("ultima") == "naranja"
            },
            {
                "titulo": "Paso 3: Desafío de Construcción",
                "tipo": "desafio",
                "instruccion": "Tienes una lista con 4 servidores: ['s1', 's2', 's3', 's4']. Extrae el primero en 'servidor_a' y el último en 'servidor_b' e imprímelos.",
                "codigo": "servidores = ['s1', 's2', 's3', 's4']\nservidor_a = servidores[0]\nservidor_b = servidores[-1]\nprint(servidor_a, servidor_b)",
                "pistas": [
                    "Nivel 1: Usa servidores[0] para el primero.",
                    "Nivel 2: Usa servidores[-1] para el último.",
                    "Nivel 3: servidor_a = servidores[0]\nservidor_b = servidores[-1]"
                ],
                "pruebas": [
                    {
                        "nombre": "Extracción de extremos",
                        "check": lambda src, res, ns: ns.get("servidor_a") == "s1" and ns.get("servidor_b") == "s4"
                    }
                ],
                "validar": lambda src, res, ns: ns.get("servidor_a") == "s1" and ns.get("servidor_b") == "s4"
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Cuál es el índice del primer elemento de cualquier lista en Python?\n\nOpciones:\n1. 0\n2. 1\n3. -1\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Cuál es el índice del primer elemento de cualquier lista en Python?",
                "opciones": [
                    "0",
                    "1",
                    "-1"
                ],
                "correcta": 0,
                "explicacion": "Así es. En Python, la indexación es base cero (0).",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 12,
        "titulo": "Capítulo 12: Métodos de Listas y Mutabilidad",
        "resumen": "Aprende a modificar listas dinámicamente con .append(), .remove() y a medir su tamaño con len().",
        "pasos": [
            {
                "titulo": "Paso 1: Observar y Predecir",
                "tipo": "observar",
                "instruccion": "El método .append() agrega un nuevo elemento al final de la lista. Ejecuta el código para observar el cambio.",
                "codigo": "tareas = ['leer', 'practicar']\ntareas.append('revisar código')\nprint('Lista actualizada:', tareas)",
                "pistas": ["Pulsa Control + Enter."],
                "validar": lambda src, res, ns: len(ns.get("tareas", [])) == 3
            },
            {
                "titulo": "Paso 2: Experimentar y Modificar",
                "tipo": "experimentar",
                "instruccion": "La función len() nos dice cuántos elementos tiene la lista. Imprime len(tareas) para escuchar el conteo.",
                "codigo": "tareas = ['leer', 'practicar', 'revisar código']\ncantidad = len(tareas)\nprint('Total de tareas pendientes:', cantidad)",
                "pistas": ["Usa len(tareas) para contar."],
                "validar": lambda src, res, ns: ns.get("cantidad") == 3
            },
            {
                "titulo": "Paso 3: Desafío de Construcción",
                "tipo": "desafio",
                "instruccion": "Comienza con una lista vacía 'puntos = []'. Agrega tres números: 10, 20 y 30 usando .append() tres veces consecutivas.",
                "codigo": "puntos = []\n# Agrega 10, 20 y 30 con .append():\npuntos.append(10)\npuntos.append(20)\npuntos.append(30)\nprint('Puntos:', puntos)",
                "pistas": [
                    "Nivel 1: puntos.append(10)",
                    "Nivel 2: Agrega cada número en una línea independiente.",
                    "Nivel 3: Al final, len(puntos) debe ser 3."
                ],
                "pruebas": [
                    {
                        "nombre": "Tres elementos agregados",
                        "check": lambda src, res, ns: ns.get("puntos") == [10, 20, 30]
                    }
                ],
                "validar": lambda src, res, ns: ns.get("puntos") == [10, 20, 30]
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué método elimina un elemento específico de una lista por su valor?\n\nOpciones:\n1. .remove(valor)\n2. .delete(valor)\n3. .pop_out(valor)\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Qué método elimina un elemento específico de una lista por su valor?",
                "opciones": [
                    ".remove(valor)",
                    ".delete(valor)",
                    ".pop_out(valor)"
                ],
                "correcta": 0,
                "explicacion": "Correcto. .remove(valor) busca y elimina la primera aparición de dicho elemento.",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 13,
        "titulo": "Capítulo 13: Automatización mediante el Ciclo for",
        "resumen": "Aprende a recorrer secuencias y repetir operaciones automáticamente con la sentencia for ... in.",
        "pasos": [
            {
                "titulo": "Paso 1: Observar y Predecir",
                "tipo": "observar",
                "instruccion": "El ciclo for toma cada elemento de una lista uno a uno. Ejecuta para escuchar los elementos impresos en orden.",
                "codigo": "elementos = ['raton', 'teclado', 'auriculares']\nfor item in elementos:\n    print('Accesorio:', item)",
                "pistas": ["Pulsa Control + Enter."],
                "validar": lambda src, res, ns: "raton" in res and "teclado" in res
            },
            {
                "titulo": "Paso 2: Experimentar y Modificar",
                "tipo": "experimentar",
                "instruccion": "La función range(1, 6) genera números del 1 al 5. Modifica el ciclo for para iterar con 'for n in range(1, 6):' e imprimir el doble de cada número.",
                "codigo": "for n in range(1, 6):\n    print('El doble de', n, 'es', n * 2)",
                "pistas": ["Usa range(1, 6). Recuerda que el límite final no se incluye."],
                "validar": lambda src, res, ns: "10" in res and "2" in res
            },
            {
                "titulo": "Paso 3: Desafío de Construcción",
                "tipo": "desafio",
                "instruccion": "Tienes una lista con precios: [100, 200, 300]. Itera con un for y calcula la suma total en una variable 'acumulado' iniciada en 0.",
                "codigo": "precios = [100, 200, 300]\nacumulado = 0\n# Completa el ciclo for abajo:\nfor p in precios:\n    acumulado += p\nprint('Total acumulado:', acumulado)",
                "pistas": [
                    "Nivel 1: for p in precios:",
                    "Nivel 2: Dentro del for: acumulado = acumulado + p",
                    "Nivel 3: El acumulado final debe ser 600."
                ],
                "pruebas": [
                    {
                        "nombre": "Suma acumulada",
                        "check": lambda src, res, ns: ns.get("acumulado") == 600
                    }
                ],
                "validar": lambda src, res, ns: ns.get("acumulado") == 600
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué valores genera range(3)?\n\nOpciones:\n1. 0, 1, 2\n2. 1, 2, 3\n3. 0, 1, 2, 3\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Qué valores genera range(3)?",
                "opciones": [
                    "0, 1, 2",
                    "1, 2, 3",
                    "0, 1, 2, 3"
                ],
                "correcta": 0,
                "explicacion": "Así es. range(3) inicia por defecto en 0 y se detiene antes de 3, generando tres enteros: 0, 1 y 2.",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 14,
        "titulo": "Capítulo 14: Funciones y Retorno de Valores (def y return)",
        "resumen": "Estructura código modular y reutilizable definiendo funciones con parámetros y valor de retorno.",
        "pasos": [
            {
                "titulo": "Paso 1: Observar y Predecir",
                "tipo": "observar",
                "instruccion": "Una función se define con 'def' y devuelve un resultado con 'return'. Ejecuta el código para observar la llamada.",
                "codigo": "def saludar(nombre):\n    return 'Hola ' + nombre + ', bienvenido.'\n\nmensaje = saludar('Kevin')\nprint(mensaje)",
                "pistas": ["Pulsa Control + Enter."],
                "validar": lambda src, res, ns: "Kevin" in ns.get("mensaje", "")
            },
            {
                "titulo": "Paso 2: Experimentar y Modificar",
                "tipo": "experimentar",
                "instruccion": "Modifica la llamada a la función para pasarle tu propio nombre como argumento y ejecuta de nuevo.",
                "codigo": "def saludar(nombre):\n    return 'Hola ' + nombre + ', bienvenido.'\n\nmensaje = saludar('Estudiante')\nprint(mensaje)",
                "pistas": ["Cambia el argumento dentro de saludar(...)."],
                "validar": lambda src, res, ns: "mensaje" in ns and len(ns["mensaje"]) > 0
            },
            {
                "titulo": "Paso 3: Desafío de Construcción",
                "tipo": "desafio",
                "instruccion": "Define una función llamada 'calcular_iva' que reciba un parámetro 'precio' y retorne el precio multiplicado por 0.21. Luego llama a la función con 100 y guarda el resultado en 'iva'.",
                "codigo": "# Define calcular_iva(precio) abajo:\ndef calcular_iva(precio):\n    return precio * 0.21\n\niva = calcular_iva(100)\nprint('IVA de 100:', iva)",
                "pistas": [
                    "Nivel 1: def calcular_iva(precio):",
                    "Nivel 2: return precio * 0.21",
                    "Nivel 3: iva = calcular_iva(100)"
                ],
                "pruebas": [
                    {
                        "nombre": "Función con retorno matemático",
                        "check": lambda src, res, ns: callable(ns.get("calcular_iva")) and ns.get("iva") == 21.0
                    }
                ],
                "validar": lambda src, res, ns: callable(ns.get("calcular_iva")) and ns.get("iva") == 21.0
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué ocurre si una función no incluye la instrucción 'return'?\n\nOpciones:\n1. Devuelve implícitamente el valor especial None.\n2. Lanza un error de sintaxis.\n3. Devuelve el número 0.\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Qué ocurre si una función no incluye la instrucción 'return'?",
                "opciones": [
                    "Devuelve implícitamente el valor especial None.",
                    "Lanza un error de sintaxis.",
                    "Devuelve el número 0."
                ],
                "correcta": 0,
                "explicacion": "Correcto. En Python, toda función que termina sin un return explícito devuelve None.",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    },
    {
        "id": 15,
        "titulo": "Capítulo 15: Mitigación de Errores con try y except",
        "resumen": "Aprende a proteger tus aplicaciones contra caídas inesperadas capturando excepciones en tiempo de ejecución.",
        "pasos": [
            {
                "titulo": "Paso 1: Observar y Predecir",
                "tipo": "observar",
                "instruccion": "El bloque 'try' alberga código con riesgo de fallo y 'except' ofrece una contingencia limpia. Ejecuta para comprobar.",
                "codigo": "entrada = 'texto_no_valido'\ntry:\n    numero = int(entrada)\n    print('Número:', numero)\nexcept ValueError:\n    print('Aviso: El dato no es un número entero válido.')",
                "pistas": ["Pulsa Control + Enter."],
                "validar": lambda src, res, ns: "Aviso: El dato no es" in res
            },
            {
                "titulo": "Paso 2: Experimentar y Modificar",
                "tipo": "experimentar",
                "instruccion": "Cambia 'entrada = \"42\"'. Al ejecutar, como el texto sí es un número válido, el bloque try se completa sin entrar al except.",
                "codigo": "entrada = '42'\ntry:\n    numero = int(entrada)\n    print('Número procesado:', numero)\nexcept ValueError:\n    print('Aviso: El dato no es un número.')",
                "pistas": ["Asigna '42' a la variable entrada."],
                "validar": lambda src, res, ns: ns.get("numero") == 42
            },
            {
                "titulo": "Paso 3: Desafío de Construcción",
                "tipo": "desafio",
                "instruccion": "Envuelve la división '10 / 0' en un bloque try y captura 'except ZeroDivisionError:' imprimiendo 'No se puede dividir por cero'.",
                "codigo": "# Protege la division abajo:\ntry:\n    resultado = 10 / 0\nexcept ZeroDivisionError:\n    print('No se puede dividir por cero')",
                "pistas": [
                    "Nivel 1: Escribe 'try:' y en la siguiente línea con sangría la división.",
                    "Nivel 2: Añade 'except ZeroDivisionError:' en la siguiente línea.",
                    "Nivel 3: Imprime el aviso de contingencia."
                ],
                "pruebas": [
                    {
                        "nombre": "Captura de división por cero",
                        "check": lambda src, res, ns: "No se puede dividir por cero" in res and "ZeroDivisionError" not in res
                    }
                ],
                "validar": lambda src, res, ns: "No se puede dividir por cero" in res and "ZeroDivisionError" not in res
            },            {
                "titulo": "Paso 4: Verificación Conceptual",
                "tipo": "quiz",
                "instruccion": "Pregunta de verificación conceptual:\n¿Qué bloque opcional se ejecuta siempre tras un try/except, haya ocurrido error o no?\n\nOpciones:\n1. finally\n2. always\n3. end\n\nEscribe el número de la respuesta (1, 2 o 3) y pulsa Control + Enter.",
                "codigo": "# Escribe aquí el número de tu opción (1, 2 o 3):\n",
                "pregunta": "¿Qué bloque opcional se ejecuta siempre tras un try/except, haya ocurrido error o no?",
                "opciones": [
                    "finally",
                    "always",
                    "end"
                ],
                "correcta": 0,
                "explicacion": "Exacto. El bloque 'finally' se utiliza comúnmente para liberar recursos como cerrar archivos o conexiones.",
                "pistas": [
                    "Nivel 1: Lee las opciones detalladas en la instrucción del paso.",
                    "Nivel 2: Escribe únicamente el número de la respuesta que consideres correcta.",
                    "Nivel 3: Pulsa Control + Enter para evaluar tu respuesta."
                ],
                "validar": lambda src, res, ns: "1" in [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            }
        ]
    }
]

# Glosario Técnico Accesible de Conceptos y Palabras Clave
GLOSARIO = {
    "print": "print(): Función incorporada para enviar mensajes y datos hacia la salida estándar y el lector de pantalla.",
    "input": "input(): Función que detiene la ejecución para leer texto ingresado por el usuario desde el teclado.",
    "if": "if: Estructura condicional que ejecuta su bloque subordinado únicamente si su condición se evalúa como verdadera (True).",
    "else": "else: Bloque condicional alternativo ejecutado cuando ninguna de las condiciones previas fue verdadera.",
    "elif": "elif: Abreviatura de 'else if'. Permite encadenar múltiples condiciones excluyentes de forma ordenada.",
    "for": "for: Bucle de control utilizado para recorrer secuencialmente elementos de una lista, tupla o rango.",
    "while": "while: Bucle que repite un bloque de código continuamente mientras su condición lógica permanezca verdadera.",
    "def": "def: Palabra clave para declarar e inicializar funciones reutilizables con nombre propio.",
    "return": "return: Finaliza la ejecución de una función y devuelve un valor procesado al código que la invocó.",
    "try": "try: Delimita un bloque de código vigilado donde se anticipa la posibilidad de una excepción.",
    "except": "except: Captura y gestiona un error específico dentro de un bloque protector try sin colapsar el programa.",
    "finally": "finally: Bloque que se ejecuta de forma mandataria al concluir un bloque try/except.",
    "import": "import: Carga y enlaza bibliotecas y módulos del sistema en el espacio de nombres de tu script.",
    "class": "class: Molde estructural para la definición de objetos bajo el paradigma de programación orientada a objetos.",
    "len": "len(): Retorna la cantidad total de elementos contenidos en una lista, texto, tupla o diccionario.",
    "range": "range(): Genera una secuencia ordenada e inmutable de números enteros.",
    "int": "int: Tipo de dato primitivo que representa números enteros sin parte fraccionaria.",
    "float": "float: Tipo de dato primitivo para números decimales de coma flotante.",
    "str": "str: Tipo de dato para secuencias de texto alfanumérico delimitadas por comillas.",
    "bool": "bool: Tipo de dato booleano que solo admite dos estados: True (Verdadero) o False (Falso).",
    "list": "list: Estructura de datos ordenada, indexada y mutable delimitada por corchetes [].",
    "tuple": "tuple: Estructura de datos ordenada e inmutable delimitada por paréntesis ().",
    "dict": "dict: Colección asociativa de parejas clave-valor delimitada por llaves {}.",
    "set": "set: Colección de datos desordenada y compuesta estrictamente por elementos únicos sin repeticiones.",
    "and": "and: Operador lógico que retorna True si y solo si ambas expresiones son verdaderas.",
    "or": "or: Operador lógico que retorna True si al menos una de las expresiones es verdadera.",
    "not": "not: Operador de negación que invierte el valor lógico de una condición.",
    "in": "in: Operador de pertenencia que verifica si un elemento está presente dentro de una colección.",
    "is": "is: Operador de identidad que evalúa si dos variables apuntan al mismo objeto en memoria física.",
    "pass": "pass: Instrucción nula utilizada como marcador de posición sintáctico en bloques vacíos.",
    "break": "break: Interrumpe de forma inmediata la ejecución del bucle (for o while) activo.",
    "continue": "continue: Salta el resto de la iteración actual y pasa a la siguiente vuelta del bucle.",
    "with": "with: Estructura para gestión segura de recursos del sistema mediante administradores de contexto.",
    "None": "None: Objeto constante que representa formalmente la ausencia de valor o valor nulo."
}
