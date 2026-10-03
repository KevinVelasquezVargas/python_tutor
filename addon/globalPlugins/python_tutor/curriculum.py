# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/curriculum.py
# Propósito: Temario pedagógico integral de 40 capítulos accesibles desde cero.
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

CURRICULUM = [
    {
        'id': 1,
        'titulo': 'Capítulo 1: Arquitectura del Ordenador: El Sistema Binario, la CPU y la Memoria RAM',
        'resumen': 'Comprende qué ocurre físicamente dentro del computador antes de programar: el procesador, la memoria de trabajo y el sistema binario.',
        'pasos': [
            {
                'titulo': 'Paso 1: Modelo Mental: El Hardware del Computador',
                'tipo': 'concepto',
                'instruccion': 'Antes de escribir código, es indispensable comprender qué es una computadora. Un computador se compone de tres piezas fundamentales: 1. La CPU (Unidad Central de Procesamiento): Es el cerebro ejecutor. No improvisa, no duda y no tiene intuición; solo ejecuta millones de instrucciones secuenciales por segundo a velocidad electromagnética. 2. La Memoria RAM (Memoria de Acceso Aleatorio): Es el espacio de trabajo rápido y volátil del sistema. Imagínala como una gran mesa donde se colocan los datos con los que el programa trabaja en este preciso instante. Si el ordenador se apaga o el programa se cierra, todo lo que estaba en la RAM se borra de inmediato. 3. El Almacenamiento Secundario (Disco Duro o SSD): Es el archivador permanente. Guarda tus archivos, programas y el sistema operativo de forma duradera, aunque no haya corriente eléctrica. Cuando abres un programa, este viaja desde el disco hasta la memoria RAM para que la CPU pueda procesar sus instrucciones. Pulsa Enter o Alt + Flecha Derecha para avanzar al siguiente concepto.',
                'codigo': '',
                'pistas': ['Lee la explicación con las flechas y pulsa Enter o Alt + Flecha Derecha para continuar.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Modelo Mental: El Sistema Binario y los Bits',
                'tipo': 'concepto',
                'instruccion': 'Los seres humanos nos comunicamos mediante lenguajes naturales como el español o el inglés, utilizando alfabetos de decenas de letras y el sistema decimal (dígitos del 0 al 9). Sin embargo, los procesadores electrónicos están formados por microscópicos transistores que solo pueden adoptar dos estados físicos: encendido (pasa corriente eléctrica) o apagado (no pasa corriente). A este estado elemental se le denomina Bit (Binary Digit o Dígito Binario): un 1 representa encendido y un 0 representa apagado. Agrupando 8 bits consecutivos se forma un Byte, capaz de representar 256 combinaciones distintas (suficiente para codificar cualquier letra, número o símbolo del teclado en el estándar ASCII o Unicode). Todo lo que escuchas a través de NVDA —cada palabra, cada sonido y cada instrucción de software— es en su nivel más profundo una sinfonía de ceros y unos coordinados por el procesador. Pulsa Enter o Alt + Flecha Derecha para verificar tu comprensión en el siguiente paso.',
                'codigo': '',
                'pistas': ['Pulsa Enter o Alt + Flecha Derecha para ir a la pregunta conceptual.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 3: Verificación Conceptual: Arquitectura del Computador',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Recuerda la analogía de la mesa de trabajo temporal.'],
                'pregunta': '¿Cuál es la función principal de la Memoria RAM durante la ejecución de un programa?',
                'opciones': ['Almacenar datos e instrucciones temporales a alta velocidad mientras el programa está activo.', 'Guardar permanentemente los archivos cuando el ordenador se apaga.', 'Generar la señal eléctrica para que funcionen los altavoces.'],
                'correcta': 0,
                'explicacion': 'La Memoria RAM es el espacio de trabajo rápido y volátil donde residen los datos activos. Al apagarse el equipo, su contenido desaparece.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 2,
        'titulo': 'Capítulo 2: El Software y los Lenguajes de Programación: El Puente Humano-Máquina',
        'resumen': 'Descubre qué es el software, por qué no le hablamos en lenguaje natural al computador y la diferencia entre lenguajes compilados e interpretados.',
        'pasos': [
            {
                'titulo': 'Paso 1: Modelo Mental: ¿Por qué Existen los Lenguajes de Programación?',
                'tipo': 'concepto',
                'instruccion': "El hardware sin software es un conjunto inerte de silicio y cobre. El software es el conjunto de órdenes lógicas que le indican al hardware qué hacer. ¿Por qué no podemos simplemente decirle al ordenador en español: 'Por favor, calcula la nómina del mes'? Porque el lenguaje humano está lleno de ambigüedad, dobles sentidos, contexto y omisiones implícitas. Las computadoras, en cambio, requieren una precisión absoluta y matemática. En los primeros años de la informática, los ingenieros programaban directamente en código máquina (largas series de ceros y unos) o en lenguaje ensamblador, lo cual era agotador y propenso a errores catastróficos. Para solucionar esto, la ciencia de la computación inventó los 'Lenguajes de Alto Nivel'. Son lenguajes que utilizan palabras legibles por los humanos (generalmente en inglés) con una gramática estricta para expresar algoritmos con total claridad. Pulsa Enter o Alt + Flecha Derecha para avanzar al siguiente concepto.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Modelo Mental: Compiladores frente a Intérpretes',
                'tipo': 'concepto',
                'instruccion': "Para que la CPU pueda ejecutar un programa escrito en un lenguaje de alto nivel, ese texto debe traducirse a lenguaje máquina binario. Existen dos formas principales de hacer esta traducción: 1. Compilación (Lenguajes Compilados como C, C++ o Rust): Un programa especial llamado 'compilador' toma todo el archivo de código fuente, lo analiza por completo de una sola vez y genera un archivo ejecutable binario independiente (como un archivo .exe en Windows). Es análogo a un traductor que traduce un libro entero del inglés al español y lo imprime: una vez impreso, no necesitas al traductor presente para leerlo. 2. Interpretación (Lenguajes Interpretados como Python o JavaScript): Un programa llamado 'intérprete' lee tu código fuente línea por línea y lo traduce y ejecuta en tiempo real sobre la marcha. Es análogo a un intérprete diplomático en una conferencia: escucha una frase, la traduce de inmediato al instante y continúa con la siguiente. Python es un lenguaje interpretado. Esto significa que podemos escribir una instrucción, ejecutarla al instante y escuchar el resultado con nuestro lector de pantalla sin esperar largas compilaciones. Pulsa Enter o Alt + Flecha Derecha para pasar a la verificación conceptual.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 3: Verificación Conceptual: Intérprete de Python',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Recuerda la analogía del traductor simultáneo en vivo.'],
                'pregunta': '¿Cómo procesa el intérprete de Python el código que escribimos?',
                'opciones': ['Lee, traduce y ejecuta las instrucciones línea por línea en tiempo real.', 'Imprime el código en hojas de papel antes de que funcione.', 'Traduce todo el código a un archivo .exe cerrado que no se puede modificar.'],
                'correcta': 0,
                'explicacion': 'El intérprete de Python lee y ejecuta las instrucciones sucesivamente sobre la marcha, permitiendo una retroalimentación ágil e interactiva.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 3,
        'titulo': 'Capítulo 3: ¿Qué es Python?: Historia, Filosofía del Zen de Python y Ecosistema',
        'resumen': 'Conoce los orígenes de Python con Guido van Rossum, los principios de diseño que lo hacen único y su impacto en la accesibilidad y la industria.',
        'pasos': [
            {
                'titulo': 'Paso 1: Modelo Mental: El Origen y Propósito de Python',
                'tipo': 'concepto',
                'instruccion': "A finales de 1989, el ingeniero de software holandés Guido van Rossum se propuso crear un lenguaje de programación diferente. En aquella época, lenguajes como C exigían escribir docenas de líneas repletas de llaves, puntos y comas y detalles mecánicos para tareas simples. Guido concibió Python con un objetivo revolucionario: priorizar la legibilidad y la productividad humana por encima de la complejidad técnica. El nombre 'Python' no proviene de la serpiente, sino del grupo humorístico británico 'Monty Python', reflejando que programar no debe ser una experiencia rígida ni abrumadora. Hoy en día, Python es uno de los lenguajes más utilizados del planeta. Es el motor detrás de la Inteligencia Artificial, la astronomía en la NASA, el análisis de datos masivos y, fundamentalmente, es el lenguaje con el que está construido gran parte del lector de pantalla NVDA. Pulsa Enter o Alt + Flecha Derecha para descubrir los principios filosóficos de Python.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Modelo Mental: El Zen de Python',
                'tipo': 'concepto',
                'instruccion': "A diferencia de otros lenguajes, Python se guía por un conjunto explícito de principios de ingeniería conocido como 'El Zen de Python' (escrito por Tim Peters). Sus aforismos más célebres son: 1. 'Bello es mejor que feo': El código debe ser limpio y placentero de leer y auditar. 2. 'Explícito es mejor que implícito': Las intenciones del programador deben expresarse con claridad, sin trucos ocultos. 3. 'Simple es mejor que complejo': Si una solución sencilla resuelve el problema, no añadas complicaciones innecesarias. 4. 'La legibilidad cuenta': El código se lee muchísimas más veces de las que se escribe; por eso, escribirlo pensando en quien lo leerá (incluyendo a tu lector de pantalla) es una regla de oro. En este entorno aprenderás a programar bajo estos mismos principios profesionales. Pulsa Enter o Alt + Flecha Derecha para avanzar al quiz de verificación.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 3: Verificación Conceptual: Filosofía de Python',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Piensa en la facilidad de lectura y mantenimiento.'],
                'pregunta': '¿Cuál es uno de los principios rectores esenciales del Zen de Python?',
                'opciones': ['La legibilidad cuenta: el código debe ser claro y sencillo de entender por humanos.', 'Escribir todo en una sola línea larguísima para ahorrar espacio en disco.', 'Ocultar las intenciones del programa para que nadie pueda entenderlo.'],
                'correcta': 0,
                'explicacion': "'La legibilidad cuenta' es uno de los pilares fundacionales de Python, convirtiéndolo en el lenguaje más accesible y limpio del mundo.",
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 4,
        'titulo': 'Capítulo 4: Programación Accesible: Cómo Programa una Persona Ciega con NVDA',
        'resumen': 'Desmitifica el código: cómo se interactúa con el código mediante texto plano, navegación por teclado y el concepto espacial de la sangría.',
        'pasos': [
            {
                'titulo': 'Paso 1: Modelo Mental: El Código es Texto Plano Puro',
                'tipo': 'concepto',
                'instruccion': "Existe el mito popular de que los programadores trabajan frente a pantallas gráficas llenas de gráficos misteriosos y ventanas visuales incomprensibles. La realidad técnica es mucho más sencilla y accesible: un programa informático es, en su esencia más pura, un archivo de texto plano (como un documento de Bloc de Notas) que termina en la extensión '.py'. Para programar no se necesita el ratón ni la vista. Una persona ciega utiliza exactamente las mismas herramientas que los ingenieros de software más avanzados: 1. Un editor de texto para redactar las instrucciones. 2. Las teclas de dirección (flechas arriba, abajo, izquierda, derecha) para explorar línea por línea y carácter por carácter. 3. El atajo Control + Flecha para saltar de palabra en palabra. 4. El lector de pantalla NVDA configurado para verbalizar signos de puntuación esenciales como comillas, paréntesis y dos puntos. Pulsa Enter o Alt + Flecha Derecha para conocer el concepto espacial de la sangría.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Modelo Mental: La Sangría (Indentación) y la Percepción Tiflotécnica',
                'tipo': 'concepto',
                'instruccion': "En la mayoría de lenguajes como C o Java, los bloques de código se delimitan con llaves visuales '{' y '}'. Python tomó una decisión magistral: los bloques se definen mediante la Sangría o Indentación (espacios en blanco al inicio de la línea). Por estándar oficial (PEP 8), cada nivel subordinado de código se sangra con exactamente 4 espacios. ¿Cómo percibe esto una persona ciega? NVDA cuenta con funciones nativas de accesibilidad tiflotécnica: - Al moverte verticalmente con flechas, NVDA anuncia: 'sangría de 4 espacios', 'sangría de 8 espacios' o 'sin sangría'. - También puedes activar tonos audibles en NVDA (Opciones de NVDA -> Formato de documento -> Notificar sangría con tonos): un tono más agudo indica un nivel más profundo y un tono más grave indica el regreso al nivel exterior. En este tutor, además, hemos integrado avisos acústicos automáticos para que siempre tengas certeza absoluta de la jerarquía de tu código. Pulsa Enter o Alt + Flecha Derecha para avanzar al quiz de verificación.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 3: Verificación Conceptual: Estructura del Código en Python',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Recuerda los 4 espacios anunciados por NVDA.'],
                'pregunta': '¿Cómo define Python qué instrucciones pertenecen a un bloque subordinado?',
                'opciones': ['Mediante la sangría o espacios en blanco al inicio de la línea (4 espacios por nivel).', 'Cambiando el color del texto a azul o rojo en la pantalla.', 'Dibujando un círculo con el ratón alrededor de las líneas.'],
                'correcta': 0,
                'explicacion': 'Python utiliza la sangría estricta (4 espacios en blanco) para definir los bloques lógicos de código, haciendo que sea perfectamente medible y audible por lectores de pantalla.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 5,
        'titulo': 'Capítulo 5: Pensamiento Algorítmico, Descomposición de Problemas y Psicología del Error',
        'resumen': 'Aprende a descomponer problemas complejos en pasos finitos, comprende el ciclo universal del software y aprende a ver los errores como valiosos diagnósticos.',
        'pasos': [
            {
                'titulo': 'Paso 1: Modelo Mental: El Algoritmo y el Ciclo Universal del Software',
                'tipo': 'concepto',
                'instruccion': "Un algoritmo es una serie ordenada, no ambigua y finita de instrucciones para resolver un problema o alcanzar un objetivo. Todo programa informático del mundo, desde una calculadora sencilla hasta un sistema de navegación por satélite, obedece al 'Ciclo Universal del Software': 1. Entrada (Input): Recepción de datos del exterior (pulsaciones de teclado, archivos de audio o información de red). 2. Memoria: Almacenamiento temporal de los datos en variables dentro de la memoria RAM. 3. Procesamiento: Transformación matemática y lógica de esos datos por parte de la CPU (sumas, comparaciones, decisiones). 4. Salida (Output): Emisión de los resultados procesados hacia el exterior (texto en la consola, sonido en los altavoces o guardado en disco). Programar consiste en diseñar con exactitud qué ocurre en cada una de estas cuatro fases. Pulsa Enter o Alt + Flecha Derecha para aprender sobre la psicología del error.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Modelo Mental: La Psicología del Error en Programación',
                'tipo': 'concepto',
                'instruccion': "El mayor obstáculo de quien aprende a programar no es la matemática ni la sintaxis: es la frustración ante los mensajes de error. Es común pensar: 'Me ha salido un error, esto no es para mí o he roto el programa'. En la ingeniería de software profesional, un error jamás es un fracaso ni una falta de inteligencia: es un reporte diagnóstico de alta precisión. Cuando Python no comprende una línea, detiene la ejecución y emite un mensaje llamado 'Traceback' (traza de error), indicando: - El archivo y el número exacto de la línea donde se detuvo. - El tipo de error (por ejemplo, SyntaxError si olvidaste cerrar una comilla o NameError si nombraste una variable que no existe). En este entorno, la tecla F4 sitúa el cursor directamente en la línea del error para que puedas corregirlo sin perder tiempo. Los programadores experimentados cometen errores a cada minuto; la diferencia es que saben leer el mensaje de error con calma para entender qué necesita el intérprete. Pulsa Enter o Alt + Flecha Derecha para avanzar al quiz de verificación.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 3: Verificación Conceptual: Ciclo del Software',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Piensa en el error como un informe técnico de ayuda.'],
                'pregunta': '¿Cuál es la actitud correcta de un programador ante un mensaje de error del intérprete?',
                'opciones': ['Leer el mensaje con calma como un reporte diagnóstico para saber en qué línea intervenir.', 'Asumir que la computadora está rota y apagar el equipo.', 'Borrar todo el código escrito y comenzar de cero sin leer el fallo.'],
                'correcta': 0,
                'explicacion': 'Un mensaje de error es información de diagnóstico precisa que nos orienta para corregir y perfeccionar el software.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 6,
        'titulo': 'Capítulo 6: La Salida Estándar: Nuestra Primera Comunicación (print)',
        'resumen': 'Aprende a emitir datos hacia la consola de salida y comprende la anatomía formal de una llamada a función en Python.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Anatomía de la Función print()',
                'tipo': 'concepto',
                'instruccion': 'Ahora que comprendes cómo funciona el intérprete, escribirás tu primera instrucción formal. Para comunicarnos desde el programa hacia el usuario, utilizamos el canal de \'Salida Estándar\' (stdout). En Python, esto se logra invocando la función integrada `print()`. Analicemos su anatomía: 1. El nombre del comando: `print` le indica al intérprete qué acción ejecutar. 2. Los paréntesis `(` y `)`: Son los operadores de llamada o invocación. Todo lo que esté dentro de los paréntesis es el argumento o dato que la función debe procesar. 3. Las comillas simples `\'` o dobles `"`: Le indican a Python que lo que está dentro es texto literal (cadena de caracteres). Si olvidas las comillas, Python creerá que intentas buscar una variable en memoria y fallará con un error `NameError`. Pulsa Enter o Alt + Flecha Derecha para ver el primer código en acción.',
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Emitiendo tu Primer Mensaje',
                'tipo': 'observar',
                'instruccion': 'Examina el código en el editor. Observa el uso de comillas y paréntesis. Pulsa Control + Enter para ejecutarlo y escuchar la salida en NVDA.',
                'codigo': "print('Hola, mundo accesible')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar el script.'],
                'validar': lambda s, r, n: (('hola' in r.lower() or 'hello' in r.lower()) and ('mundo' in r.lower() or 'world' in r.lower()))
            },
            {
                'titulo': 'Paso 3: Experimentación: Saludo Personalizado',
                'tipo': 'experimentar',
                'instruccion': "Modifica el texto dentro de las comillas para que salude con tu nombre o profesión (por ejemplo: 'Hola, estudiante de programación') y pulsa Control + Enter.",
                'codigo': "print('Hola, estudiante de programación')\n",
                'pistas': ['Asegúrate de conservar las comillas simples al principio y al final del texto.'],
                'validar': lambda s, r, n: len(r.strip()) > 3 and r.strip() not in ('Hola, mundo accesible', 'Hello, accessible world')
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Salida en Dos Líneas Independientes',
                'tipo': 'desafio',
                'instruccion': "Escribe dos instrucciones print() independientes: en la primera muestra 'Iniciando sistema' y en la segunda 'Sistema listo'. Ejecuta con Control + Enter para comprobar.",
                'codigo': '# Escribe aquí tus dos instrucciones print:\n\n',
                'salida_esperada': 'Iniciando sistema\nSistema listo',
                'pistas': ["Usa una línea para print('Iniciando sistema') y la siguiente para print('Sistema listo')."],
                'validar': lambda s, r, n: ((('iniciando' in r.lower() and 'listo' in r.lower()) or ('starting' in r.lower() and 'ready' in r.lower())) and len(r.strip().splitlines()) >= 2)
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Delimitadores de Texto',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Distingue entre texto literal e identificadores de memoria.'],
                'pregunta': "¿Por qué es obligatorio rodear con comillas el texto dentro de print('Hola')?",
                'opciones': ['Para indicar a Python que es texto literal y no el nombre de una variable en memoria.', 'Porque las comillas aceleran la velocidad del procesador.', 'Es opcional; en Python las comillas no son necesarias.'],
                'correcta': 0,
                'explicacion': 'Sin comillas, Python busca un identificador o variable con ese nombre en la memoria RAM y arroja un NameError si no existe.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 7,
        'titulo': 'Capítulo 7: La Memoria del Ordenador: Variables y el Operador de Asignación',
        'resumen': 'Comprende cómo se almacenan datos en la memoria RAM utilizando variables y la convención de nomenclatura snake_case.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: La Variable como Etiqueta en Memoria',
                'tipo': 'concepto',
                'instruccion': "Un programa que solo imprime textos fijos no tiene utilidad real. Para procesar datos, necesitamos guardarlos en la memoria RAM. Una variable es un nombre simbólico que apunta a una dirección de la memoria donde reside un dato. Imagina la memoria RAM como un casillero gigante: crear una variable es colocar una etiqueta legible en una casilla para recuperar su contenido cuando lo necesites. Para guardar un dato, se utiliza el 'Operador de Asignación', representado por el signo igual `=`. Regla vital: En programación, `=` NO significa igualdad matemática; significa: 'Evalúa lo que está a la derecha y guárdalo en la variable de la izquierda'. Convención oficial (PEP 8): Los nombres de variables se escriben en minúsculas separando palabras con guion bajo (por ejemplo, `nombre_usuario`), convención llamada `snake_case`. Pulsa Enter o Alt + Flecha Derecha para avanzar al código de observación.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Asignación y Lectura de Variables',
                'tipo': 'observar',
                'instruccion': 'Observa cómo se crea la variable `herramienta` y luego se pasa al print() sin comillas. Ejecuta con Control + Enter para escuchar el resultado.',
                'codigo': "herramienta = 'NVDA'\nprint(herramienta)\n",
                'pistas': ['Fíjate que al imprimir la variable no se usan comillas.'],
                'validar': lambda s, r, n: (n.get('herramienta') == 'NVDA' or n.get('tool') == 'NVDA') and 'nvda' in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Modificar el Valor Guardado',
                'tipo': 'experimentar',
                'instruccion': "Cambia el texto asignado a `herramienta` por 'Lector de pantalla accesible' y ejecuta con Control + Enter.",
                'codigo': "herramienta = 'Lector de pantalla accesible'\nprint(herramienta)\n",
                'pistas': ['Mantén la asignación a la variable herramienta.'],
                'validar': lambda s, r, n: ('accesible' in str(n.get('herramienta', n.get('tool', ''))).lower() or 'accessible' in str(n.get('herramienta', n.get('tool', ''))).lower()) and ('accesible' in r.lower() or 'accessible' in r.lower())
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Perfil de Estudiante',
                'tipo': 'desafio',
                'instruccion': 'Crea una variable llamada `estudiante` con tu nombre como texto. En la siguiente línea, muestra el contenido de la variable usando print(). Ejecuta con Control + Enter.',
                'codigo': '# Crea la variable estudiante e imprímela:\n\n',
                'pistas': ["Escribe: estudiante = 'Tu Nombre' y abajo print(estudiante)."],
                'validar': lambda s, r, n: ('estudiante' in n or 'student' in n) and len(str(n.get('estudiante', n.get('student', '')))) > 0 and len(r.strip()) > 0
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: El Operador =',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Recuerda que = no es comparación matemática.'],
                'pregunta': '¿Qué operación realiza la sentencia: edad = 20?',
                'opciones': ['Asigna el valor 20 a la variable llamada edad en la memoria RAM.', 'Comprueba si la variable edad es matemáticamente igual a 20.', 'Borra el número 20 del computador.'],
                'correcta': 0,
                'explicacion': 'El operador = realiza una asignación destructiva hacia la izquierda: evalúa el dato derecho y lo almacena en la variable.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 8,
        'titulo': 'Capítulo 8: Documentación y Legibilidad: Comentarios con #',
        'resumen': 'Aprende a documentar tus intenciones en el código con comentarios ignorados por el intérprete pero vitales para la comprensión.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: El Carácter Almohadilla (#)',
                'tipo': 'concepto',
                'instruccion': "El código fuente no solo lo lee la computadora; principalmente lo leen seres humanos. A menudo necesitamos dejar notas explicativas para recordar por qué escribimos una lógica determinada o para guiar a otros desarrolladores. En Python, cualquier texto que comience con el símbolo almohadilla `#` (numeral o hash) es un 'Comentario'. El intérprete de Python ignora por completo todo lo que esté a la derecha del `#` hasta el final de esa línea. ¿Cómo interactúa NVDA con los comentarios? Tu lector de pantalla verbalizará la palabra 'almohadilla' o 'comentario' seguida del texto, permitiéndote auditar el propósito de cada sección sin alterar la ejecución del programa. Pulsa Enter o Alt + Flecha Derecha para ver los comentarios en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Código Documentado',
                'tipo': 'observar',
                'instruccion': 'Examina el código. Observa cómo las líneas que inician con # no generan salida en la consola. Pulsa Control + Enter.',
                'codigo': "# Este es un comentario explicativo\n# La siguiente línea emite el mensaje oficial:\nprint('Código documentado con éxito')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'documentado' in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Añadir una Nota Propia',
                'tipo': 'experimentar',
                'instruccion': "Agrega una nueva línea arriba con tu propio comentario (por ejemplo: '# Autor: mi nombre') y ejecuta con Control + Enter.",
                'codigo': "# Autor: Kevin\nprint('Comentarios activos')\n",
                'pistas': ['Empieza la línea con el símbolo #.'],
                'validar': lambda s, r, n: '#' in s and ('comentarios activos' in r.lower() or 'active comments' in r.lower())
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Desactivar Código Obsoleto',
                'tipo': 'desafio',
                'instruccion': 'En el editor hay dos instrucciones print(). Coloca un símbolo # al inicio de la primera línea para deshabilitarla (comentarla), de modo que solo se ejecute la segunda. Pulsa Control + Enter.',
                'codigo': "print('Mensaje antiguo que debe ser desactivado')\nprint('Mensaje vigente')\n",
                'salida_esperada': 'Mensaje vigente',
                'pistas': ["Agrega # al inicio de la primera línea: # print('Mensaje antiguo...')"],
                'validar': lambda s, r, n: ('antiguo' not in r.lower() and 'old' not in r.lower()) and ('vigente' in r.lower() or 'current' in r.lower())
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Comportamiento de los Comentarios',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Recuerda que el intérprete omite estas líneas.'],
                'pregunta': '¿Qué acción realiza el intérprete de Python cuando encuentra el símbolo #?',
                'opciones': ['Ignora todo el texto restante en esa línea y continúa con la siguiente.', 'Lanza un error SyntaxError y detiene el programa.', 'Imprime el comentario en la consola con sonido grave.'],
                'correcta': 0,
                'explicacion': 'Los comentarios son invisibles para la ejecución de la CPU; existen exclusivamente para guiar a los humanos.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 9,
        'titulo': 'Capítulo 9: Reasignación de Variables y Flujo Secuencial en Memoria',
        'resumen': 'Aprende cómo el intérprete ejecuta de arriba hacia abajo y cómo la reasignación actualiza el estado de las variables en la memoria RAM.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: El Flujo de Arriba hacia Abajo y la Sobrescritura',
                'tipo': 'concepto',
                'instruccion': 'El intérprete de Python lee y ejecuta las instrucciones en estricto orden secuencial: de arriba hacia abajo y de izquierda a derecha. Las variables en memoria son dinámicas. Si a una variable existente le asignas un nuevo valor mediante `=`, el valor anterior se descarta de la memoria y es sustituido por el nuevo dato. Por ejemplo: si en la línea 1 escribes `puntos = 10` y en la línea 3 escribes `puntos = 20`, al llegar a la línea 4 la variable `puntos` valdrá 20. Rastrear con la mente cómo cambian los valores a medida que avanzan las líneas es una de las habilidades analíticas más importantes de un programador profesional. Pulsa Enter o Alt + Flecha Derecha para observar la reasignación en acción.',
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Dos Estados en el Tiempo',
                'tipo': 'observar',
                'instruccion': 'Observa cómo la variable `estado` cambia entre la línea 1 y la línea 3. Pulsa Control + Enter para escuchar las dos salidas consecutivas.',
                'codigo': "estado = 'Cargando datos...'\nprint(estado)\nestado = 'Proceso completado'\nprint(estado)\n",
                'pistas': ['Pulsa Control + Enter para ver la evolución de la variable.'],
                'validar': lambda s, r, n: 'cargando' in r.lower() and 'completado' in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Actualizar el Estado Final',
                'tipo': 'experimentar',
                'instruccion': "Modifica la segunda asignación para que `estado` sea 'Operación exitosa en NVDA' y ejecuta con Control + Enter.",
                'codigo': "estado = 'Iniciando'\nprint(estado)\nestado = 'Operación exitosa en NVDA'\nprint(estado)\n",
                'pistas': ['Reasigna la variable estado en la línea 3.'],
                'validar': lambda s, r, n: 'exitosa' in r.lower() and n.get('estado') == 'Operación exitosa en NVDA'
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Marcador de Juego',
                'tipo': 'desafio',
                'instruccion': 'Crea una variable `puntuacion = 0`. Imprime su valor. Luego reasigna `puntuacion = 100` e imprime nuevamente su valor. Ejecuta con Control + Enter.',
                'codigo': '# Declara puntuacion = 0, imprime, reasigna a 100 e imprime:\n\n',
                'salida_esperada': '0\n100',
                'pistas': ['Escribe puntuacion = 0, print(puntuacion), puntuacion = 100, print(puntuacion).'],
                'validar': lambda s, r, n: n.get('puntuacion') == 100 and '0' in r and '100' in r
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Ciclo de Vida de la Reasignación',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Piensa en la sobreescritura del contenido de la casilla de memoria.'],
                'pregunta': 'Si una variable x vale 5 en la línea 1 y le asignas x = 12 en la línea 2, ¿qué valor tiene x en la línea 3?',
                'opciones': ['Vale 12, porque la última asignación reemplaza el valor anterior.', 'Vale 17, porque Python suma automáticamente todos los valores anteriores.', 'Vale 5, porque las variables nunca pueden cambiar de valor.'],
                'correcta': 0,
                'explicacion': 'Las variables en Python retienen el valor de la asignación más reciente ejecutada en el flujo temporal.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 10,
        'titulo': 'Capítulo 10: Números Enteros (int) y Operadores Aritméticos',
        'resumen': 'Aprende a realizar cálculos matemáticos con números enteros y comprende las reglas de precedencia de operadores (PEMDAS).',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: El Tipo int y Operaciones Básicas',
                'tipo': 'concepto',
                'instruccion': 'En Python, los números sin parte decimal pertenecen al tipo `int` (entero). Pueden ser positivos, negativos o cero. Para operar con números, Python ofrece operadores aritméticos directos: - Suma: `+` - Resta: `-` - Multiplicación: `*` (asterisco) - Potencia o exponente: `**` (doble asterisco, ej. `2 ** 3` es 8). Regla de Precedencia (PEMDAS): Al igual que en matemáticas, Python evalúa primero los Paréntesis, luego Exponentes, luego Multiplicación y División, y finalmente Suma y Resta. Por ejemplo: en `2 + 3 * 4`, primero se multiplica `3 * 4 = 12` y luego se suma 2, dando 14. Si deseas que se sume primero, usas paréntesis: `(2 + 3) * 4 = 20`. Pulsa Enter o Alt + Flecha Derecha para ver el cálculo en acción.',
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Cálculo y Precedencia',
                'tipo': 'observar',
                'instruccion': 'Examina cómo se calcula la variable `resultado` y se muestra en consola. Pulsa Control + Enter para escuchar la salida.',
                'codigo': 'base = 10\naltura = 5\narea = base * altura\nprint(area)\n',
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: n.get('area') == 50 and '50' in r
            },
            {
                'titulo': 'Paso 3: Experimentación: Paréntesis para Alterar Precedencia',
                'tipo': 'experimentar',
                'instruccion': 'Calcula el promedio de tres notas sumándolas entre paréntesis y dividiéndolas: `promedio = (8 + 9 + 10) // 3`. Muestra el resultado y pulsa Control + Enter.',
                'codigo': 'promedio = (8 + 9 + 10) // 3\nprint(promedio)\n',
                'pistas': ['Usa paréntesis para garantizar que la suma ocurra antes de la división.'],
                'validar': lambda s, r, n: n.get('promedio') == 9 and '9' in r
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Perímetro de un Rectángulo',
                'tipo': 'desafio',
                'instruccion': 'Declara `ancho = 6` y `alto = 4`. Calcula el perímetro usando la fórmula `perimetro = 2 * (ancho + alto)`. Imprime `perimetro` y ejecuta con Control + Enter.',
                'codigo': '# Declara ancho, alto, calcula perimetro e imprime:\n\n',
                'salida_esperada': '20',
                'pistas': ['Define ancho = 6, alto = 4, perimetro = 2 * (ancho + alto), y print(perimetro).'],
                'validar': lambda s, r, n: n.get('perimetro') == 20 and '20' in r
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Precedencia Aritmética',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Calcula 2 * 3 primero.'],
                'pregunta': '¿Cuál es el resultado de evaluar la expresión: 5 + 2 * 3?',
                'opciones': ['11, porque la multiplicación (2 * 3 = 6) tiene mayor precedencia que la suma (+ 5).', '21, porque se evalúa de izquierda a derecha sin importar el operador.', '10, porque se redondea al múltiplo más cercano.'],
                'correcta': 0,
                'explicacion': 'En Python y en matemáticas estándar, la multiplicación se ejecuta antes que la suma a menos que se usen paréntesis.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 11,
        'titulo': 'Capítulo 11: Números Decimales de Coma Flotante (float) y Divisiones',
        'resumen': 'Diferencia enteros de decimales y domina las tres modalidades de división en Python: real (/), entera (//) y residuo (%).',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: El Tipo float y los Tres Operadores de División',
                'tipo': 'concepto',
                'instruccion': 'Cuando un número contiene parte fraccionaria (decimal), Python lo representa como `float` (punto flotante). Nota para lectores de pantalla: En programación internacional se usa siempre el PUNTO `.` decimal y jamás la coma `,` (por ejemplo, `3.14`). La coma se reserva exclusivamente para separar elementos en listas o argumentos. Python cuenta con tres operadores distintos para dividir: 1. División Real o Verdadera `/`: Siempre devuelve un `float`, incluso si el resultado es exacto. Por ejemplo: `10 / 2` produce `5.0`. 2. División Entera o Truncada `//`: Descarta la parte decimal y entrega únicamente el cociente entero. Por ejemplo: `10 // 3` produce `3`. 3. Módulo o Residuo `%`: Entrega el sobrante o resto de una división entera. Por ejemplo: `10 % 3` produce `1` (porque 3 cabe 3 veces en 10 y sobra 1). El módulo es fundamental en informática para determinar si un número es par o impar. Pulsa Enter o Alt + Flecha Derecha para escuchar las tres divisiones en acción.',
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Comparando las Tres Divisiones',
                'tipo': 'observar',
                'instruccion': 'Ejecuta el código con Control + Enter y escucha con atención cómo cada operador produce un resultado diferente para los mismos números.',
                'codigo': "print('División real:', 15 / 4)\nprint('División entera:', 15 // 4)\nprint('Residuo o módulo:', 15 % 4)\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: '3.75' in r and '3' in r
            },
            {
                'titulo': 'Paso 3: Experimentación: Cálculo con Precios Flotantes',
                'tipo': 'experimentar',
                'instruccion': 'Calcula el precio final con descuento: `precio = 49.99`, `descuento = 10.50`, `total = precio - descuento`. Muestra `total` con print() y ejecuta con Control + Enter.',
                'codigo': 'precio = 49.99\ndescuento = 10.50\ntotal = precio - descuento\nprint(total)\n',
                'pistas': ['Ejecuta con Control + Enter para ver la resta decimal.'],
                'validar': lambda s, r, n: abs(n.get('total', 0) - 39.49) < 0.01 and '39.49' in r
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Reparto Equitativo de Dulces',
                'tipo': 'desafio',
                'instruccion': 'Tienes `dulces = 23` y `ninos = 5`. Calcula cuántos dulces le tocan a cada niño enteros (`por_nino = dulces // ninos`) y cuántos sobran (`sobrantes = dulces % ninos`). Imprime ambos valores y ejecuta con Control + Enter.',
                'codigo': '# Calcula por_nino y sobrantes e imprímelos:\n\n',
                'pistas': ['Usa // para por_nino y % para sobrantes, luego print(por_nino) y print(sobrantes).'],
                'validar': lambda s, r, n: (n.get('por_nino') == 4 or n.get('per_child') == 4) and (n.get('sobrantes') == 3 or n.get('leftovers') == 3)
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: El Operador Módulo (%)',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Multiplica 5 * 3 y mira cuánto falta para 17.'],
                'pregunta': '¿Qué resultado devuelve la expresión: 17 % 5?',
                'opciones': ['2, porque 5 cabe 3 veces en 17 (15) y sobran 2.', '3.4, porque es el resultado exacto con decimales.', '0, porque no hay residuo.'],
                'correcta': 0,
                'explicacion': 'El operador % entrega exclusivamente el sobrante o residuo de la división entera.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 12,
        'titulo': 'Capítulo 12: Cadenas de Texto (str): Delimitadores, Caracteres de Escape y Saltos de Línea',
        'resumen': 'Domina la manipulación de cadenas de texto (str), comillas internas y secuencias de escape especiales como \\n y \\t.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Caracteres Especiales y Barra Invertida',
                'tipo': 'concepto',
                'instruccion': 'En Python, cualquier secuencia de caracteres rodeada por comillas simples `\'...\'` o dobles `"..."` es un objeto del tipo `str` (string). ¿Qué ocurre si deseas que tu texto incluya comillas internas? Si abres la cadena con comillas dobles, puedes usar comillas simples adentro sin conflicto: `"Dijo \'hola\' y sonrió"`. Secuencias de Escape con la Barra Invertida `\\`: La barra invertida `\\` es el carácter de escape. Le avisa a Python que el carácter siguiente tiene un significado especial: - `\\n` (barra n): Inserta un Salto de Línea inmediato en el texto, obligando al lector de pantalla a iniciar una nueva línea. - `\\t` (barra t): Inserta una Tabulación o sangría horizontal. - `\\\'` o `\\"`: Permite escribir una comilla literal sin cerrar la cadena. Pulsa Enter o Alt + Flecha Derecha para observar los saltos de línea en acción.',
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Salto de Línea con \\n',
                'tipo': 'observar',
                'instruccion': 'Observa cómo un solo print() genera dos líneas independientes gracias a \\n. Pulsa Control + Enter.',
                'codigo': "print('Línea superior accesible\\nLínea inferior procesada')\n",
                'pistas': ['Pulsa Control + Enter para escuchar las dos líneas.'],
                'validar': lambda s, r, n: len(r.strip().splitlines()) >= 2 and ('superior' in r.lower() or 'upper' in r.lower())
            },
            {
                'titulo': 'Paso 3: Experimentación: Comillas Mixtas',
                'tipo': 'experimentar',
                'instruccion': 'Imprime una frase que contenga comillas internas utilizando comillas dobles externas: `print("El lenguaje \'Python\' es accesible")`. Ejecuta con Control + Enter.',
                'codigo': 'print("El lenguaje \'Python\' es accesible")\n',
                'pistas': ['Usa comillas dobles en los extremos y simples adentro.'],
                'validar': lambda s, r, n: 'python' in r.lower() and ('accesible' in r.lower() or 'accessible' in r.lower())
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Menú en Tres Renglones',
                'tipo': 'desafio',
                'instruccion': "Crea una variable llamada `menu` que contenga un texto con tres opciones separadas por `\\n`: '1. Abrir\\n2. Guardar\\n3. Salir'. Luego muéstrala con print(menu). Ejecuta con Control + Enter.",
                'codigo': '# Crea menu con saltos de línea e imprímelo:\n\n',
                'salida_esperada': '1. Abrir\n2. Guardar\n3. Salir',
                'pistas': ["Escribe menu = '1. Abrir\\n2. Guardar\\n3. Salir' y luego print(menu)."],
                'validar': lambda s, r, n: len(r.strip().splitlines()) >= 3 and ('abrir' in r.lower() or 'open' in r.lower()) and ('salir' in r.lower() or 'exit' in r.lower())
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Secuencias de Escape',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ["Piensa en la n de 'newline' precedida por barra invertida."],
                'pregunta': '¿Qué carácter de control se utiliza para crear un salto de línea dentro de un string?',
                'opciones': ['\\n (barra invertida seguida de la letra n)', '/enter (barra normal con enter)', '#linea (almohadilla con linea)'],
                'correcta': 0,
                'explicacion': '\\n es el estándar universal de salto de línea en lenguajes derivados de C y en Python.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 13,
        'titulo': 'Capítulo 13: Interpolación Moderna de Cadenas: Las F-Strings',
        'resumen': 'Aprende el estándar profesional moderno para combinar texto y variables sin conversiones engorrosas usando f-strings.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: La Letra f y las Llaves {}',
                'tipo': 'concepto',
                'instruccion': "En versiones antiguas de Python, combinar variables y texto requería concatenar con `+` y convertir números con `str()` (ejemplo: `'Edad: ' + str(edad)`), lo cual era tedioso y propenso a errores `TypeError`. A partir de Python 3.6, la industria adoptó las **Formatted String Literals** o simplemente **f-strings**. ¿Cómo funciona una f-string? 1. Colocas la letra `f` minúscula inmediatamente antes de abrir las comillas: `f'...'`. 2. Dentro del texto, colocas llaves `{}` alrededor de cualquier variable o expresión. 3. El intérprete evalúa automáticamente lo que está dentro de las llaves, lo convierte a texto y lo reemplaza en su lugar exacto. Ejemplo: Si `nombre = 'Kevin'`, escribir `f'Bienvenido, {nombre}'` produce `'Bienvenido, Kevin'`. Las f-strings son el estándar oficial de legibilidad en el código moderno. Pulsa Enter o Alt + Flecha Derecha para verlas en funcionamiento.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Interpolando Múltiples Variables',
                'tipo': 'observar',
                'instruccion': 'Examina cómo se mezclan texto, números y variables dentro de una sola f-string. Pulsa Control + Enter para ejecutar.',
                'codigo': "usuario = 'Elena'\ncapitulo = 13\nprint(f'Estudiante {usuario} cursando el Capítulo {capitulo}')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'elena' in r.lower() and '13' in r
            },
            {
                'titulo': 'Paso 3: Experimentación: Expresiones Matemáticas Dentro de Llaves',
                'tipo': 'experimentar',
                'instruccion': "Dentro de las llaves puedes colocar operaciones matemáticas directas. Modifica el código para calcular el doble: `f'El doble de {valor} es {valor * 2}'`. Ejecuta con Control + Enter.",
                'codigo': "valor = 25\nprint(f'El doble de {valor} es {valor * 2}')\n",
                'pistas': ['Escribe la operación valor * 2 dentro de las segundas llaves.'],
                'validar': lambda s, r, n: '50' in r and '25' in r
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Resumen Financiero con F-Strings',
                'tipo': 'desafio',
                'instruccion': "Crea `producto = 'Teclado'`, `precio = 35` y `cantidad = 2`. Muestra con una sola f-string: 'Producto: Teclado, Total: 70' calculando `precio * cantidad` dentro de las llaves. Ejecuta con Control + Enter.",
                'codigo': '# Declara producto, precio, cantidad e imprime con f-string:\n\n',
                'salida_esperada': 'Producto: Teclado, Total: 70',
                'pistas': ["Usa print(f'Producto: {producto}, Total: {precio * cantidad}')"],
                'validar': lambda s, r, n: 'teclado' in r.lower() and '70' in r
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Sintaxis de F-Strings',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ["Es la inicial de 'format'."],
                'pregunta': '¿Qué letra debe colocarse justo antes de las comillas para activar una f-string?',
                'opciones': ['La letra f (minúscula o mayúscula)', 'La letra p (de print)', 'El signo de porcentaje %'],
                'correcta': 0,
                'explicacion': 'El prefijo f (de formatted string) le indica al analizador de Python que evalúe las llaves dentro del texto.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 14,
        'titulo': 'Capítulo 14: Entrada de Datos (input) y Conversión Explícita de Tipos (Casting)',
        'resumen': 'Aprende a pausar el programa para capturar datos del usuario y domina la conversión de tipos con int(), float() y str().',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: La Regla de Oro de input() y el Type Casting',
                'tipo': 'concepto',
                'instruccion': "Para interactuar con el usuario, Python ofrece la función `input()`. Cuando el intérprete llega a una línea con `input('Escribe algo: ')`, detiene la ejecución del programa y espera pacientemente a que el usuario escriba en el teclado y pulse la tecla Enter. **La Regla de Oro de input():** Sin importar lo que el usuario escriba (incluso si escribe números como `25` o `100`), la función `input()` SIEMPRE devuelve un dato de tipo cadena de texto (`str`). Si intentas sumar matemáticamente el resultado de un `input()`, Python fallará con un error `TypeError` porque no se pueden sumar textos y números directamente. Conversión Explícita de Tipos (*Type Casting*): Para transformar un dato de un tipo a otro, utilizamos funciones constructoras: - `int('25')`: Convierte el texto '25' en el número entero 25. - `float('19.99')`: Convierte el texto '19.99' en el número decimal 19.99. - `str(100)`: Convierte el número 100 en la cadena de texto '100'. Pulsa Enter o Alt + Flecha Derecha para ver el casting en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Conversión de Texto a Número',
                'tipo': 'observar',
                'instruccion': 'Observa cómo se toma una entrada numérica textual y se convierte a entero con int() antes de operar. Pulsa Control + Enter.',
                'codigo': "edad_texto = '20'\nedad = int(edad_texto)\nmeses = edad * 12\nprint(f'Edad: {edad} años, equivalente a {meses} meses')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: n.get('meses') == 240 and '240' in r
            },
            {
                'titulo': 'Paso 3: Experimentación: Suma de Dos Números Convertidos',
                'tipo': 'experimentar',
                'instruccion': "Cambia los textos `num1_str = '50'` y `num2_str = '25'`. Conviértelos a enteros y calcula `suma = int(num1_str) + int(num2_str)`. Muestra la suma y pulsa Control + Enter.",
                'codigo': "num1_str = '50'\nnum2_str = '25'\nsuma = int(num1_str) + int(num2_str)\nprint(f'Suma total: {suma}')\n",
                'pistas': ['Asegúrate de envolver ambas cadenas con int().'],
                'validar': lambda s, r, n: n.get('suma') == 75 and '75' in r
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Calculadora de Doble y Mitad',
                'tipo': 'desafio',
                'instruccion': "Dada la variable `entrada = '80'`, conviértela a número entero en `numero`. Luego calcula `doble = numero * 2` y `mitad = numero // 2`. Imprime ambos resultados en una f-string: 'Doble: 160, Mitad: 40'. Pulsa Control + Enter.",
                'codigo': "entrada = '80'\n# Convierte a int, calcula doble y mitad e imprime con f-string:\n\n",
                'salida_esperada': 'Doble: 160, Mitad: 40',
                'pistas': ["numero = int(entrada), doble = numero * 2, mitad = numero // 2, print(f'Doble: {doble}, Mitad: {mitad}')"],
                'validar': lambda s, r, n: ((n.get('doble') == 160 or n.get('double') == 160) and (n.get('mitad') == 40 or n.get('half') == 40) and '160' in r and '40' in r)
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Tipo Devuelto por input()',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Recuerda la regla de oro de input().'],
                'pregunta': '¿Qué tipo de dato devuelve SIEMPRE la función input() de Python?',
                'opciones': ['str (cadena de texto), incluso si el usuario tipea dígitos numéricos.', 'int (número entero) automáticamente si no hay letras.', 'bool (verdadero o falso).'],
                'correcta': 0,
                'explicacion': 'input() captura la secuencia de teclas como caracteres de texto puros; por ello siempre es necesario convertir con int() o float() si se requiere aritmética.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 15,
        'titulo': 'Capítulo 15: El Tipo Booleano (bool) y Operadores Relacionales de Comparación',
        'resumen': 'Aprende los dos estados de la verdad digital (True y False) y domina los seis operadores de comparación.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: La Verdad Binaria y los Operadores Relacionales',
                'tipo': 'concepto',
                'instruccion': "Toda decisión que toma un computador se reduce a una pregunta lógica que solo puede tener dos respuestas posibles: Verdadero o Falso. En Python, este tipo de dato se llama `bool` (booleano, en honor al matemático George Boole) y solo admite dos valores literales con mayúscula inicial: `True` y `False`. Para comparar valores y obtener un booleano, utilizamos los 'Operadores Relacionales': - `==` (doble igual): Comprueba si dos valores son iguales. (¡Cuidado!: un solo `=` asigna en memoria; dos `==` comparan igualdad). - `!=` (signo de exclamación e igual): Comprueba si dos valores son diferentes o desiguales. - `<` (menor que) y `>` (mayor que). - `<=` (menor o igual que) y `>=` (mayor o igual que). Pulsa Enter o Alt + Flecha Derecha para ver estas comparaciones en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Evaluando Comparaciones',
                'tipo': 'observar',
                'instruccion': 'Ejecuta el código con Control + Enter y escucha cómo Python evalúa cada comparación a True o False.',
                'codigo': "print('¿10 es mayor que 5?:', 10 > 5)\nprint('¿4 es igual a 9?:', 4 == 9)\nprint('¿7 es diferente de 7?:', 7 != 7)\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'true' in r.lower() and 'false' in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Comprobación de Mayoría de Edad',
                'tipo': 'experimentar',
                'instruccion': 'Crea `edad = 20`. Evalúa la condición booleana `es_mayor = edad >= 18` e imprime `es_mayor`. Pulsa Control + Enter.',
                'codigo': "edad = 20\nes_mayor = edad >= 18\nprint(f'¿Es mayor de edad?: {es_mayor}')\n",
                'pistas': ['Usa el operador >= para comparar con 18.'],
                'validar': lambda s, r, n: (n.get('es_mayor') is True or n.get('is_adult') is True) and 'true' in r.lower()
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Validador de Acceso con Contraseña',
                'tipo': 'desafio',
                'instruccion': "Tienes `clave_guardada = 'python2026'` y `clave_ingresada = 'python2026'`. Compara si ambas son exactamente iguales en una variable booleana `acceso_concedido = (clave_guardada == clave_ingresada)`. Muestra el resultado con print(acceso_concedido) y ejecuta con Control + Enter.",
                'codigo': "clave_guardada = 'python2026'\nclave_ingresada = 'python2026'\n# Compara con == e imprime acceso_concedido:\n\n",
                'salida_esperada': 'True',
                'pistas': ['acceso_concedido = (clave_guardada == clave_ingresada), luego print(acceso_concedido).'],
                'validar': lambda s, r, n: (n.get('acceso_concedido') is True or n.get('access_granted') is True) and 'true' in r.lower()
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Diferencia entre = y ==',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Recuerda que un solo igual asigna.'],
                'pregunta': '¿Cuál es la diferencia técnica fundamental entre = y == en Python?',
                'opciones': ['= asigna un valor a una variable en memoria; == compara si dos valores son iguales.', 'Son idénticos y se pueden usar indistintamente.', '= es para números y == es para texto.'],
                'correcta': 0,
                'explicacion': 'Confundir el operador de asignación (=) con el de comparación relacional (==) es un error común; Python mantiene una distinción estricta.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 16,
        'titulo': 'Capítulo 16: Operadores Lógicos (and, or, not) y Tablas de Verdad',
        'resumen': 'Aprende a conectar múltiples condiciones mediante conjunciones, disyunciones y negaciones con evaluación en cortocircuito.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Conectores Lógicos y Cortocircuito',
                'tipo': 'concepto',
                'instruccion': 'En la vida real las decisiones rara vez dependen de un único factor. Para evaluar múltiples condiciones a la vez, Python cuenta con tres palabras reservadas lógicas: 1. `and` (Y lógico): Exige que AMBAS condiciones sean verdaderas para dar `True`. Si al menos una es falsa, el resultado total es `False`. 2. `or` (O lógico): Requiere que AL MENOS UNA de las condiciones sea verdadera para dar `True`. Solo dará `False` si ambas son falsas. 3. `not` (Negación): Invierte el valor lógico. Si una condición es `True`, `not True` produce `False`, y viceversa. Evaluación en Cortocircuito (*Short-Circuit Evaluation*): Python es muy inteligente: en una expresión `A and B`, si `A` es falso, Python ya sabe que el resultado final será falso y ni siquiera pierde tiempo evaluando `B`. De igual forma, en `A or B`, si `A` es verdadero, no evalúa `B`. Pulsa Enter o Alt + Flecha Derecha para ver los operadores lógicos en acción.',
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Tablas de Verdad en Acción',
                'tipo': 'observar',
                'instruccion': 'Ejecuta el código con Control + Enter y analiza cómo and exige cumplimiento simultáneo mientras or es más flexible.',
                'codigo': "tiene_llave = True\nsabe_clave = False\nprint('¿Entra con and (llave Y clave)?:', tiene_llave and sabe_clave)\nprint('¿Entra con or (llave O clave)?:', tiene_llave or sabe_clave)\nprint('Negación de sabe_clave con not:', not sabe_clave)\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'false' in r.lower() and 'true' in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Negación con not',
                'tipo': 'experimentar',
                'instruccion': 'Verifica si un sistema está desocupado: `bloqueado = False`, `disponible = not bloqueado`. Muestra `disponible` con print() y pulsa Control + Enter.',
                'codigo': "bloqueado = False\ndisponible = not bloqueado\nprint(f'¿Sistema disponible?: {disponible}')\n",
                'pistas': ['not False se convierte en True.'],
                'validar': lambda s, r, n: (n.get('disponible') is True or n.get('available') is True) and 'true' in r.lower()
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Verificación de Beca Universitaria',
                'tipo': 'desafio',
                'instruccion': 'Un estudiante califica para una beca si su promedio es mayor o igual a 90 Y su asistencia es mayor o igual al 85%. Declara `promedio = 92`, `asistencia = 90` y evalúa `obtiene_beca = (promedio >= 90) and (asistencia >= 85)`. Imprime `obtiene_beca` y ejecuta con Control + Enter.',
                'codigo': '# Declara promedio, asistencia, evalúa obtiene_beca e imprime:\n\n',
                'salida_esperada': 'True',
                'pistas': ['Usa el operador and para unir las dos comparaciones.'],
                'validar': lambda s, r, n: (n.get('obtiene_beca') is True or n.get('gets_scholarship') is True) and 'true' in r.lower()
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Evaluación del Operador and',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Ambas condiciones deben cumplirse simultáneamente.'],
                'pregunta': '¿Qué resultado arroja la expresión booleana: True and False?',
                'opciones': ['False, porque el operador and exige que ambas partes sean verdaderas.', 'True, porque al menos una parte es verdadera.', 'None, porque hay un empate lógico.'],
                'correcta': 0,
                'explicacion': 'El operador and solo produce True cuando absolutamente todos sus operandos son True.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 17,
        'titulo': 'Capítulo 17: Bifurcación Condicional: La Estructura if y la Sangría de 4 Espacios',
        'resumen': 'Aprende a bifurcar la ejecución del programa y domina la regla de oro de Python: los dos puntos (:) y la sangría obligatoria.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: La Estructura if y los Dos Puntos (:)',
                'tipo': 'concepto',
                'instruccion': "Hasta ahora, nuestros programas han sido completamente lineales. Una bifurcación permite que el programa tome caminos diferentes según los datos. La sentencia fundamental para bifurcar es `if` (que significa 'si condicional'). Anatomía de un bloque if: 1. Escribes la palabra `if` seguida de una condición booleana. 2. Al final de la línea colocas obligatoriamente el carácter Dos Puntos `:`. 3. Las líneas de código que deseas que se ejecuten SOLO cuando la condición sea verdadera se sangran con exactamente 4 espacios a la derecha. ¿Cómo auditar la sangría con NVDA? Cuando bajas con la flecha vertical a una línea dentro del `if`, NVDA anunciará: 'sangría de 4 espacios' (o emitirá un tono acústico agudo). Si olvidas los 4 espacios o los dos puntos, Python arrojará un `IndentationError` o un `SyntaxError`. Pulsa Enter o Alt + Flecha Derecha para ver el primer if en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Ejecución Condicional y Sangría',
                'tipo': 'observar',
                'instruccion': 'Observa los 4 espacios de sangría en la línea 2. Ejecuta con Control + Enter para escuchar el mensaje autorizado.',
                'codigo': "edad = 20\nif edad >= 18:\n    print('Acceso autorizado por mayoría de edad')\n",
                'pistas': ['Fíjate en los dos puntos al final de la línea del if.'],
                'validar': lambda s, r, n: ('autorizado' in r.lower() or 'granted' in r.lower() or 'authorized' in r.lower())
            },
            {
                'titulo': 'Paso 3: Experimentación: Condición No Cumplida',
                'tipo': 'experimentar',
                'instruccion': 'Cambia `edad = 15`. Al ejecutar con Control + Enter, la condición `edad >= 18` será falsa y la línea sangrada NO se ejecutará, dejando la consola en silencio. Comprueba este comportamiento.',
                'codigo': "edad = 15\nif edad >= 18:\n    print('Acceso autorizado por mayoría de edad')\n",
                'pistas': ['Ejecuta con Control + Enter y comprueba que no se imprime nada.'],
                'validar': lambda s, r, n: n.get('edad') == 15 and len(r.strip()) == 0
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Alerta de Temperatura',
                'tipo': 'desafio',
                'instruccion': "Crea `temperatura = 35`. Escribe una sentencia if que verifique si `temperatura > 30:`. Dentro del bloque sangrado con 4 espacios, imprime: 'Alerta: Temperatura elevada'. Pulsa Control + Enter.",
                'codigo': 'temperatura = 35\n# Escribe el if con sangría de 4 espacios:\n\n',
                'salida_esperada': 'Alerta: Temperatura elevada',
                'pistas': ["if temperatura > 30: seguido en la siguiente línea de 4 espacios y print('Alerta: Temperatura elevada')."],
                'validar': lambda s, r, n: (('alerta' in r.lower() or 'alert' in r.lower() or 'temperature' in r.lower()) and ('elevada' in r.lower() or 'high' in r.lower() or '35' in r))
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: El Carácter al Final del if',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Abre la puerta al bloque sangrado.'],
                'pregunta': '¿Qué carácter de puntuación es obligatorio al final de la línea de encabezado del if?',
                'opciones': ['Dos puntos (:)', 'Punto y coma (;)', 'Signo de interrogación (?)'],
                'correcta': 0,
                'explicacion': 'En Python, todas las cabeceras de bloques compuestos (if, else, for, while, def, class) deben terminar estrictamente con dos puntos (:).',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 18,
        'titulo': 'Capítulo 18: El Camino Alternativo: La Cláusula else',
        'resumen': 'Aprende a definir el camino de contingencia cuando una condición no se cumple utilizando el bloque else.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: La Decisión Binaria Completa',
                'tipo': 'concepto',
                'instruccion': "Un `if` solitario solo actúa si la condición es verdadera; si es falsa, el programa simplemente continúa de largo. Sin embargo, la mayoría de procesos requieren un 'Plan B': 'Si ocurre A, haz esto; DE LO CONTRARIO, haz aquello'. Para esto utilizamos la cláusula `else:` (que significa 'de lo contrario' o 'si no'). Reglas de la cláusula else: 1. Se alinea al mismo nivel que el `if` (sin sangría respecto al `if`). 2. Termina obligatoriamente con dos puntos `:`. 3. Sus instrucciones internas se sangran con 4 espacios a la derecha. 4. El bloque `else` NUNCA lleva condición; se ejecuta de forma automática cuando la condición del `if` fue falsa. Pulsa Enter o Alt + Flecha Derecha para ver el if/else en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: La Bifurcación Binaria',
                'tipo': 'observar',
                'instruccion': 'Examina la estructura if/else. Como edad es 16, la condición falla y se ejecuta el bloque else. Ejecuta con Control + Enter.',
                'codigo': "edad = 16\nif edad >= 18:\n    print('Acceso permitido')\nelse:\n    print('Acceso denegado: debes ser mayor de 18')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: ('denegado' in r.lower() or 'denied' in r.lower())
            },
            {
                'titulo': 'Paso 3: Experimentación: Cambiar el Flujo Hacia el if',
                'tipo': 'experimentar',
                'instruccion': "Modifica `edad = 25`. Al ejecutar con Control + Enter, ahora se activará la primera rama ('Acceso permitido') y el bloque else será ignorado.",
                'codigo': "edad = 25\nif edad >= 18:\n    print('Acceso permitido')\nelse:\n    print('Acceso denegado: debes ser mayor de 18')\n",
                'pistas': ['Cambia edad a 25 y pulsa Control + Enter.'],
                'validar': lambda s, r, n: (n.get('edad') == 25 or n.get('age') == 25) and ('permitido' in r.lower() or 'granted' in r.lower() or 'allowed' in r.lower())
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Clasificador de Número Par o Impar',
                'tipo': 'desafio',
                'instruccion': "Dado `numero = 14`, usa el operador módulo `% 2 == 0` para verificar si es par. Si es par imprime: 'El número es par'. Si no (else), imprime: 'El número es impar'. Pulsa Control + Enter.",
                'codigo': 'numero = 14\n# Comprueba si numero % 2 == 0 con if/else:\n\n',
                'salida_esperada': 'El número es par',
                'pistas': ["if numero % 2 == 0: print('El número es par') else: print('El número es impar')"],
                'validar': lambda s, r, n: ('es par' in r.lower() or 'is even' in r.lower() or 'even' in r.lower())
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Momento de Ejecución del else',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Es el plan de contingencia.'],
                'pregunta': '¿Cuándo se ejecutan las instrucciones contenidas dentro de un bloque else?',
                'opciones': ['Únicamente cuando la condición del if anterior evaluó a False.', 'Siempre, sin importar lo que haya ocurrido en el if.', 'Solo si hay un error de sintaxis en el archivo.'],
                'correcta': 0,
                'explicacion': 'El bloque else es el camino alternativo automático que se dispara cuando la prueba del if resulta falsa.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 19,
        'titulo': 'Capítulo 19: Decisiones Múltiples Encadenadas: Bloques elif',
        'resumen': 'Aprende a clasificar situaciones complejas con múltiples alternativas mutuamente excluyentes usando elif.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: La Cascada de Decisiones con elif',
                'tipo': 'concepto',
                'instruccion': "¿Qué ocurre si tenemos más de dos alternativas posibles? Por ejemplo: un semáforo puede estar en verde, amarillo o rojo. En lugar de anidar múltiples if confusos, Python ofrece la palabra reservada `elif` (abreviatura de *else if*, es decir, 'si no, comprueba si...'). Flujo de una cascada `if / elif / else`: 1. Python evalúa el primer `if`. Si es verdadero, ejecuta su bloque y TERMINA toda la estructura (salta hasta el final sin evaluar los demás). 2. Si el primer `if` fue falso, salta al siguiente `elif` y evalúa su condición. 3. Puedes encadenar todos los `elif` que necesites. 4. Si ningún `if` ni `elif` se cumplió, se ejecuta el bloque `else` final como red de seguridad. Pulsa Enter o Alt + Flecha Derecha para ver una clasificación con elif.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Clasificación de Calificaciones',
                'tipo': 'observar',
                'instruccion': 'Examina la cascada. Como puntaje es 75, el primer if (>= 90) falla y entra en el elif (>= 70). Pulsa Control + Enter.',
                'codigo': "puntaje = 75\nif puntaje >= 90:\n    print('Calificación: Sobresaliente')\nelif puntaje >= 70:\n    print('Calificación: Aprobado')\nelse:\n    print('Calificación: Requiere refuerzo')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: ('aprobado' in r.lower() or 'passed' in r.lower())
            },
            {
                'titulo': 'Paso 3: Experimentación: Activar la Rama Sobresaliente',
                'tipo': 'experimentar',
                'instruccion': 'Modifica `puntaje = 95`. Ejecuta con Control + Enter y observa cómo se activa la primera rama sin evaluar las siguientes.',
                'codigo': "puntaje = 95\nif puntaje >= 90:\n    print('Calificación: Sobresaliente')\nelif puntaje >= 70:\n    print('Calificación: Aprobado')\nelse:\n    print('Calificación: Requiere refuerzo')\n",
                'pistas': ['Cambia puntaje a 95 y ejecuta.'],
                'validar': lambda s, r, n: (n.get('puntaje') == 95 or n.get('score') == 95) and ('sobresaliente' in r.lower() or 'outstanding' in r.lower())
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Clasificador Térmico en Tres Niveles',
                'tipo': 'desafio',
                'instruccion': "Dada `temp = 22`: si `temp > 28` imprime 'Clima cálido'; elif `temp >= 15` imprime 'Clima templado'; else imprime 'Clima frío'. Ejecuta con Control + Enter.",
                'codigo': 'temp = 22\n# Escribe la estructura if / elif / else con sangría de 4 espacios:\n\n',
                'salida_esperada': 'Clima templado',
                'pistas': ["if temp > 28: print('Clima cálido') elif temp >= 15: print('Clima templado') else: print('Clima frío')"],
                'validar': lambda s, r, n: ('templado' in r.lower() or 'mild' in r.lower() or 'warm' in r.lower() or 'moderate' in r.lower())
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Comportamiento de elif',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Recuerda que solo se toma un camino.'],
                'pregunta': 'Si la primera condición de un if resulta verdadera en una cadena con varios elif, ¿qué ocurre con los elif posteriores?',
                'opciones': ['Se omiten por completo y la ejecución continúa después de la estructura condicional.', 'Se ejecutan todos obligatoriamente uno tras otro.', 'El programa se reinicia desde la línea 1.'],
                'correcta': 0,
                'explicacion': 'Las ramas if/elif son mutuamente excluyentes: tan pronto una rama se cumple, todas las demás se descartan.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 20,
        'titulo': 'Capítulo 20: Repetición Definida: El Bucle for y la Función range()',
        'resumen': 'Aprende a automatizar tareas repetitivas recorriendo secuencias numéricas con el bucle for y range().',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Iteración y la Función range()',
                'tipo': 'concepto',
                'instruccion': "Una de las mayores virtudes de una computadora es su capacidad para repetir una tarea millones de veces sin cansarse ni cometer errores. Un 'Bucle' o ciclo es una estructura que repite un bloque de código. El bucle `for` se utiliza cuando sabemos de antemano cuántas veces queremos repetir algo o cuando queremos recorrer una colección de elementos. La Función `range()`: `range()` genera una secuencia inmutable de números enteros. - `range(stop)`: Inicia en 0 y avanza hasta `stop - 1`. Ejemplo: `range(5)` produce 0, 1, 2, 3, 4. - `range(start, stop)`: Inicia en `start` y termina en `stop - 1`. Ejemplo: `range(1, 6)` produce 1, 2, 3, 4, 5. - `range(start, stop, step)`: El tercer parámetro define el paso o incremento. Ejemplo: `range(0, 10, 2)` produce números pares: 0, 2, 4, 6, 8. En cada repetición (iteración), la variable del bucle toma el siguiente valor de la secuencia y ejecuta el bloque sangrado con 4 espacios. Pulsa Enter o Alt + Flecha Derecha para ver el bucle for en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Repitiendo con for y range()',
                'tipo': 'observar',
                'instruccion': 'Observa cómo el bucle repite el print() cinco veces variando la variable `i`. Pulsa Control + Enter.',
                'codigo': "for i in range(1, 6):\n    print(f'Paso número: {i}')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: len(r.strip().splitlines()) == 5 and '5' in r
            },
            {
                'titulo': 'Paso 3: Experimentación: Salto de Dos en Dos',
                'tipo': 'experimentar',
                'instruccion': 'Genera números pares usando el parámetro step: `range(2, 11, 2)`. Muestra cada número y pulsa Control + Enter.',
                'codigo': "for n in range(2, 11, 2):\n    print(f'Par: {n}')\n",
                'pistas': ['El rango va de 2 a 10 con saltos de 2.'],
                'validar': lambda s, r, n: '10' in r and '2' in r and len(r.strip().splitlines()) == 5
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Acumulador de Suma',
                'tipo': 'desafio',
                'instruccion': 'Inicializa `total = 0`. Mediante un bucle `for n in range(1, 6):`, suma cada número al acumulador con `total += n` (o `total = total + n`). Al finalizar el bucle (sin sangría), imprime: print(total). Pulsa Control + Enter.',
                'codigo': 'total = 0\n# Itera con for sumando a total e imprime total al final:\n\n',
                'salida_esperada': '15',
                'pistas': ['1 + 2 + 3 + 4 + 5 = 15. Asegúrate de imprimir total fuera del bucle (sin sangría).'],
                'validar': lambda s, r, n: n.get('total') == 15 and '15' in r.strip()
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Límite Superior de range()',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['El número final queda por fuera.'],
                'pregunta': '¿Qué secuencia de números enteros genera exactamente la llamada range(1, 5)?',
                'opciones': ['1, 2, 3, 4 (el límite superior 5 nunca se incluye)', '1, 2, 3, 4, 5 (incluyendo el 5)', '0, 1, 2, 3, 4, 5'],
                'correcta': 0,
                'explicacion': 'En Python, los rangos e índices son siempre semiabiertos [inicio, fin): el valor de stop queda estrictamente excluido.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 21,
        'titulo': 'Capítulo 21: Repetición Condicional: El Bucle while',
        'resumen': 'Aprende a repetir instrucciones basadas en condiciones dinámicas usando el bucle while y variables de control.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: El Bucle Basado en Condición',
                'tipo': 'concepto',
                'instruccion': "Mientras que el bucle `for` se utiliza para secuencias de tamaño conocido, el bucle `while` (que significa 'mientras') se usa cuando no sabemos cuántas veces habrá que repetir algo. El bucle `while` evalúa una condición booleana antes de cada iteración: - Si la condición es `True`, ejecuta el bloque de código sangrado. - Vuelve a subir y evalúa la condición nuevamente. - En el instante en que la condición se vuelve `False`, el bucle termina y el programa continúa con las líneas siguientes. Componentes indispensables de un bucle while: 1. Inicialización: Definir una variable de control antes del bucle (ejemplo: `contador = 1`). 2. Condición: La prueba que se evalúa (ejemplo: `while contador <= 5:`). 3. Actualización o Paso: Modificar la variable de control dentro del bloque (ejemplo: `contador += 1`). Si olvidas este paso, la condición siempre será verdadera y el programa se quedará atrapado para siempre en un bucle infinito. Pulsa Enter o Alt + Flecha Derecha para ver el bucle while en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Cuenta Progresiva Controlada',
                'tipo': 'observar',
                'instruccion': 'Observa cómo la variable `contador` inicia en 1, se incrementa en cada paso con `contador += 1` y el bucle finaliza al llegar a 4. Pulsa Control + Enter.',
                'codigo': "contador = 1\nwhile contador <= 3:\n    print(f'Iteración: {contador}')\n    contador += 1\nprint('Bucle finalizado con éxito')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'iteración: 3' in r.lower() and 'finalizado' in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Cuenta Regresiva',
                'tipo': 'experimentar',
                'instruccion': "Crea una cuenta regresiva que inicie en `cuenta = 5`, reste con `cuenta -= 1` mientras `cuenta > 0` y al salir imprima '¡Despegue!'. Pulsa Control + Enter.",
                'codigo': "cuenta = 5\nwhile cuenta > 0:\n    print(f'T menos {cuenta}')\n    cuenta -= 1\nprint('¡Despegue!')\n",
                'pistas': ['Asegúrate de decrementar cuenta en cada vuelta.'],
                'validar': lambda s, r, n: ('despegue' in r.lower() or 'liftoff' in r.lower())
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Duplicador Exponencial',
                'tipo': 'desafio',
                'instruccion': 'Inicia `energia = 1`. Con un bucle `while energia < 30:`, imprime `energia` y duplícala en cada vuelta con `energia *= 2` (o `energia = energia * 2`). Ejecuta con Control + Enter.',
                'codigo': 'energia = 1\n# Escribe el bucle while que duplica energia e imprime:\n\n',
                'salida_esperada': '1\n2\n4\n8\n16',
                'pistas': ['while energia < 30: print(energia) energia *= 2'],
                'validar': lambda s, r, n: n.get('energia') == 32 and '16' in r
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: El Peligro del Bucle Infinito',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Piensa en una condición que nunca cambia.'],
                'pregunta': '¿Qué ocurre si dentro del cuerpo de un bucle while olvidas actualizar la variable de control?',
                'opciones': ['La condición nunca cambiará a False y el bucle se repetirá indefinidamente (bucle infinito).', 'Python apaga la pantalla del ordenador de inmediato.', 'El bucle se convierte mágicamente en un bucle for.'],
                'correcta': 0,
                'explicacion': 'Sin actualización del estado de control, la condición permanece perpetuamente verdadera consumiendo ciclos de CPU.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 22,
        'titulo': 'Capítulo 22: Prevención de Bucles Infinitos y Cómo Detener la Ejecución',
        'resumen': 'Aprende a diagnosticar bucles infinitos, comprende los mecanismos de seguridad por tiempo límite (timeout) y cómo cancelar ejecuciones.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Anatomía de un Bucle Infinito y Temporizadores de Seguridad',
                'tipo': 'concepto',
                'instruccion': "Un bucle infinito ocurre cuando la condición de salida de un bucle nunca llega a cumplirse. Por ejemplo: `while True:` o un contador que en lugar de sumar disminuye alejándose de la meta. Cuando esto ocurre, la CPU se satura ejecutando miles de millones de instrucciones repetitivas, provocando que la aplicación no responda y congelando la interfaz. Mecanismos de Protección en Entornos Profesionales: Para evitar que un error congele NVDA o tu sistema operativo, este entorno formativo incluye un 'Temporizador de Seguridad Aislado' (*Execution Timeout*). Si un script tarda más de 4 segundos sin terminar, el ejecutor seguro interrumpe el proceso a la fuerza y te informa de inmediato por voz: 'Tiempo límite de ejecución excedido (posible bucle infinito)'. En una consola del sistema operativo, el atajo estándar para interrumpir un proceso desbocado es `Control + C`. Pulsa Enter o Alt + Flecha Derecha para ver cómo se corrige un bucle defectuoso.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Corrección de un Bucle Defectuoso',
                'tipo': 'observar',
                'instruccion': 'Examina el código. Observa cómo la línea `paso += 1` garantiza que `paso < 5` se vuelva falsa tras 4 iteraciones. Pulsa Control + Enter.',
                'codigo': "paso = 1\nwhile paso < 5:\n    print(f'Procesando bloque seguro #{paso}')\n    paso += 1\nprint('Ejecución segura completada sin bloqueos')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'bloque seguro #4' in r.lower() and 'segura' in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Añadir la Condición de Salida Faltante',
                'tipo': 'experimentar',
                'instruccion': 'En el código del editor, añade la línea `nivel += 1` dentro del while para que el bucle avance hacia el límite 4 y termine limpiamente. Ejecuta con Control + Enter.',
                'codigo': "nivel = 1\nwhile nivel <= 4:\n    print(f'Nivel auditivo: {nivel}')\n    # Agrega aquí la línea: nivel += 1\n    nivel += 1\nprint('Niveles completados')\n",
                'pistas': ['Asegúrate de que nivel += 1 esté sangrado con 4 espacios.'],
                'validar': lambda s, r, n: (n.get('nivel') == 5 or n.get('level') == 5) and ('completados' in r.lower() or 'completed' in r.lower() or 'cleared' in r.lower())
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Carga de Batería Segura',
                'tipo': 'desafio',
                'instruccion': "Simula la carga de un dispositivo: `bateria = 70`. Mediante un bucle `while bateria < 100:`, incrementa `bateria += 10`. Al salir del bucle (sin sangría), imprime: print(f'Carga completa: {bateria}%'). Ejecuta con Control + Enter.",
                'codigo': 'bateria = 70\n# Incrementa bateria de 10 en 10 hasta 100 e imprime al final:\n\n',
                'salida_esperada': 'Carga completa: 100%',
                'pistas': ["while bateria < 100: bateria += 10, y al salir print(f'Carga completa: {bateria}%')"],
                'validar': lambda s, r, n: n.get('bateria') == 100 and '100%' in r
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Atajo Universal de Interrupción',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Es el atajo universal de cancelación en terminales.'],
                'pregunta': '¿Qué combinación de teclas envía una señal de interrupción (KeyboardInterrupt) a un script trabado en una terminal?',
                'opciones': ['Control + C', 'Alt + F4', 'Barra espaciadora'],
                'correcta': 0,
                'explicacion': 'Control + C genera una excepción KeyboardInterrupt estándar que detiene la ejecución en consolas de sistemas operativos.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 23,
        'titulo': 'Capítulo 23: Control Fino de Bucles: Las Sentencias break, continue y else en Bucles',
        'resumen': 'Aprende a interrumpir búsquedas anticipadamente con break y a saltar iteraciones selectivas con continue.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Interrupción con break y Omisión con continue',
                'tipo': 'concepto',
                'instruccion': 'A menudo necesitamos un control más quirúrgico dentro de un bucle sin esperar a que termine de recorrer toda la secuencia. Python provee dos sentencias clave: 1. `break` (romper): Cancela e interrumpe el bucle de inmediato. En cuanto Python ejecuta `break`, salta fuera del bucle y continúa con la primera línea que no esté sangrada. Se utiliza típicamente en algoritmos de búsqueda: cuando encuentras lo que buscabas, no tiene sentido seguir gastando tiempo de procesador. 2. `continue` (continuar): Omite el resto de la iteración actual y salta de inmediato al siguiente ciclo del bucle. Todo lo que esté debajo de `continue` en esa vuelta no se ejecuta. Cláusula `else` en bucles: Una característica exclusiva y elegante de Python: puedes añadir un bloque `else:` a un bucle for o while. Este bloque se ejecuta ÚNICAMENTE si el bucle terminó de forma natural sin haber sido interrumpido por un `break`. Pulsa Enter o Alt + Flecha Derecha para ver estas sentencias en acción.',
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Búsqueda Temprana con break',
                'tipo': 'observar',
                'instruccion': 'Observa cómo el bucle range(1, 10) se detiene tan pronto encuentra el número 3 gracias a break. Pulsa Control + Enter.',
                'codigo': "for n in range(1, 10):\n    if n == 3:\n        print('¡Objetivo 3 encontrado! Deteniendo bucle.')\n        break\n    print(f'Revisando: {n}')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'objetivo 3' in r.lower() and 'revisando: 4' not in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Omitir con continue',
                'tipo': 'experimentar',
                'instruccion': 'Usa continue para saltarte los números impares: si `n % 2 != 0: continue`. Observa cómo solo se imprimen los números pares. Ejecuta con Control + Enter.',
                'codigo': "for n in range(1, 7):\n    if n % 2 != 0:\n        continue\n    print(f'Número par: {n}')\n",
                'pistas': ['continue omite la llamada a print para los impares.'],
                'validar': lambda s, r, n: 'par: 2' in r.lower() and 'par: 4' in r.lower() and '1' not in r
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Detenerse ante un Número Negativo',
                'tipo': 'desafio',
                'instruccion': "Dada la lista `lecturas = [15, 22, -1, 30]`, recorre cada elemento con un bucle `for val in lecturas:`. Si `val < 0`, imprime 'Lectura anómala detectada' y sal con `break`. De lo contrario, imprime `val`. Pulsa Control + Enter.",
                'codigo': 'lecturas = [15, 22, -1, 30]\n# Itera e interrumpe con break ante números negativos:\n\n',
                'salida_esperada': '15\n22\nLectura anómala detectada',
                'pistas': ["if val < 0: print('Lectura anómala detectada') break else: print(val)"],
                'validar': lambda s, r, n: 'anómala' in r.lower() and '30' not in r
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: La Sentencia continue',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Distingue entre cancelar el bucle entero y saltar una vuelta.'],
                'pregunta': '¿Qué ocurre cuando el intérprete ejecuta la sentencia continue dentro de un bucle?',
                'opciones': ['Omite las líneas restantes de la vuelta actual y salta al inicio de la siguiente iteración.', 'Cancela y destruye el bucle permanentemente.', 'Imprime un mensaje de error y apaga el lector de pantalla.'],
                'correcta': 0,
                'explicacion': 'continue no destruye el bucle (eso lo hace break); únicamente salta el resto de la iteración presente.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 24,
        'titulo': 'Capítulo 24: Listas (list): Colecciones Ordenadas, Índices y Mutabilidad',
        'resumen': 'Aprende a agrupar múltiples datos ordenados en memoria usando corchetes [], indexación basada en cero e índices negativos.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: La Lista como Contenedor Secuencial Mutable',
                'tipo': 'concepto',
                'instruccion': "Hasta el momento, cada variable almacenaba un solo dato (un número o un texto). ¿Qué ocurre si necesitas gestionar una lista de 100 alumnos o 500 artículos de una tienda? Crear 500 variables individuales sería insostenible. Una **Lista** (`list`) es una colección ordenada y mutable de elementos agrupados entre corchetes `[` y `]`, separados por comas. Propiedades fundamentales de las listas: 1. Ordenadas por Posición (Índices basados en 0): El primer elemento se encuentra en el índice `0`, el segundo en el `1`, el tercero en el `2`, etc. Ejemplo: si `frutas = ['manzana', 'pera']`, `frutas[0]` es `'manzana'`. 2. Índices Negativos: Python permite acceder desde el final hacia atrás: el índice `-1` es siempre el último elemento, `-2` el penúltimo. 3. Mutabilidad: A diferencia de las cadenas de texto, las listas son mutables. Puedes cambiar cualquier elemento en su lugar asignando a su índice: `frutas[0] = 'fresa'`. Pulsa Enter o Alt + Flecha Derecha para ver listas en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Acceso por Índice Positivo y Negativo',
                'tipo': 'observar',
                'instruccion': 'Examina la lista de lenguajes. Observa cómo `lenguajes[0]` accede al primero y `lenguajes[-1]` al último. Pulsa Control + Enter.',
                'codigo': "lenguajes = ['Python', 'C', 'JavaScript', 'Rust']\nprint('Primer lenguaje:', lenguajes[0])\nprint('Último lenguaje:', lenguajes[-1])\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'python' in r.lower() and 'rust' in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Mutar un Elemento de la Lista',
                'tipo': 'experimentar',
                'instruccion': "Modifica el segundo elemento (índice 1) para que sea 'C++': `lenguajes[1] = 'C++'`. Muestra la lista completa y pulsa Control + Enter.",
                'codigo': "lenguajes = ['Python', 'C', 'JavaScript']\nlenguajes[1] = 'C++'\nprint(lenguajes)\n",
                'pistas': ["Usa lenguajes[1] = 'C++' para reemplazar en memoria."],
                'validar': lambda s, r, n: 'c++' in str(n.get('lenguajes', [])).lower()
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Colección de Tres Herramientas',
                'tipo': 'desafio',
                'instruccion': "Crea una lista llamada `herramientas` con tres textos: 'NVDA', 'Python', 'VSCode'. Luego imprime con un solo print() el primer elemento y el último separados por una coma: `print(herramientas[0], herramientas[-1])`. Ejecuta con Control + Enter.",
                'codigo': '# Crea herramientas e imprime el primer y último elemento:\n\n',
                'salida_esperada': 'NVDA VSCode',
                'pistas': ["herramientas = ['NVDA', 'Python', 'VSCode'] y print(herramientas[0], herramientas[-1])"],
                'validar': lambda s, r, n: 'nvda' in r.lower() and 'vscode' in r.lower()
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: El Índice del Primer Elemento',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['La cuenta siempre comienza en cero.'],
                'pregunta': '¿Cuál es el índice que referencia al primer elemento de cualquier lista en Python?',
                'opciones': ['0 (cero)', '1 (uno)', '-0'],
                'correcta': 0,
                'explicacion': 'Python utiliza indexación basada en cero: el desplazamiento desde el inicio del arreglo para el primer elemento es 0.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 25,
        'titulo': 'Capítulo 25: Métodos Fundamentales de Listas (append, insert, pop, remove, len)',
        'resumen': 'Aprende a añadir elementos, eliminarlos de la memoria y medir el tamaño de listas con sus métodos integrados.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Métodos de Mutación de Listas',
                'tipo': 'concepto',
                'instruccion': 'Una lista no tiene un tamaño estático; puede crecer o encogerse dinámicamente según las necesidades del programa. Para modificar listas, Python ofrece métodos específicos utilizando la notación de punto (`lista.metodo()`): - `lista.append(elemento)`: Agrega un nuevo elemento al final de la lista. - `lista.insert(posicion, elemento)`: Inserta un elemento en un índice específico, desplazando los demás hacia la derecha. - `lista.pop()`: Extrae y elimina el último elemento. Si le pasas un índice (`lista.pop(0)`), elimina el elemento en esa posición. - `lista.remove(valor)`: Busca y elimina la primera aparición del valor exacto indicado. Si no existe, genera un `ValueError`. - `len(lista)`: Función que devuelve la cantidad total de elementos que contiene la lista. Pulsa Enter o Alt + Flecha Derecha para ver estos métodos en acción.',
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Crecimiento y Medición con append() y len()',
                'tipo': 'observar',
                'instruccion': 'Observa cómo la lista tareas crece con append() y se mide con len(). Pulsa Control + Enter.',
                'codigo': "tareas = ['Repasar Python', 'Configurar NVDA']\ntareas.append('Escribir script accesible')\nprint('Total tareas:', len(tareas))\nprint('Lista completa:', tareas)\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: len(n.get('tareas', [])) == 3 and '3' in r
            },
            {
                'titulo': 'Paso 3: Experimentación: Extracción de Elementos con pop()',
                'tipo': 'experimentar',
                'instruccion': 'Extrae el último elemento de la lista con `eliminado = tareas.pop()` e imprime `eliminado` y la lista resultante. Ejecuta con Control + Enter.',
                'codigo': "tareas = ['Lección 1', 'Lección 2', 'Lección 3']\neliminado = tareas.pop()\nprint('Tarea extraída:', eliminado)\nprint('Tareas restantes:', tareas)\n",
                'pistas': ['pop() devuelve el elemento retirado.'],
                'validar': lambda s, r, n: (n.get('eliminado') or n.get('removed')) and len(n.get('tareas', n.get('tasks', []))) == 2
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Cola de Espera Dinámica',
                'tipo': 'desafio',
                'instruccion': "Inicia `cola = ['Ana', 'Bernardo']`. Agrega a 'Carlos' al final con append(). Luego extrae al primer cliente atendido usando `cola.pop(0)`. Imprime `cola` y ejecuta con Control + Enter.",
                'codigo': "cola = ['Ana', 'Bernardo']\n# Agrega a Carlos con append, extrae el índice 0 con pop e imprime cola:\n\n",
                'salida_esperada': "['Bernardo', 'Carlos']",
                'pistas': ["cola.append('Carlos'), cola.pop(0), print(cola)"],
                'validar': lambda s, r, n: n.get('cola') == ['Bernardo', 'Carlos'] and 'bernardo' in r.lower() and 'carlos' in r.lower()
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: El Método append()',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Añadir a la cola.'],
                'pregunta': '¿En qué posición de la lista coloca el método append(x) al nuevo elemento?',
                'opciones': ['Al final de la lista, incrementando su longitud en 1.', 'Al inicio de la lista en el índice 0.', 'En una posición aleatoria elegida por el computador.'],
                'correcta': 0,
                'explicacion': 'append() añade siempre al final de la colección en tiempo constante O(1).',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 26,
        'titulo': 'Capítulo 26: Recorrido e Iteración sobre Listas (for ... in y enumerate())',
        'resumen': 'Aprende el patrón idiomático para recorrer listas elemento por elemento y utiliza enumerate() para numerar elementos.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: El Patrón for ... in y la Función enumerate()',
                'tipo': 'concepto',
                'instruccion': 'En otros lenguajes antiguos, recorrer un arreglo requería crear un contador manual `i = 0` y consultar `lista[i]`. Python diseñó una sintaxis infinitamente más limpia e idiomática: `for elemento in lista:`. El intérprete se encarga de extraer automáticamente cada elemento de la colección uno por uno hasta llegar al final. La Función `enumerate()`: ¿Qué ocurre si necesitas el elemento Y también su número de posición (índice)? Envolver la lista con `enumerate(lista, start=1)` entrega en cada vuelta una pareja: `indice, elemento`. Esto es especialmente útil en software accesible para presentar listas numeradas verbalizadas con total claridad para lectores de pantalla. Pulsa Enter o Alt + Flecha Derecha para ver el recorrido en acción.',
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Recorrido Secuencial Limpio',
                'tipo': 'observar',
                'instruccion': 'Examina cómo `for fruta in frutas:` extrae directamente cada texto. Pulsa Control + Enter para escuchar cada fruta en una línea.',
                'codigo': "frutas = ['Manzana', 'Pera', 'Plátano']\nfor fruta in frutas:\n    print(f'Fruta disponible: {fruta}')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'manzana' in r.lower() and 'plátano' in r.lower() or 'platano' in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Numeración Accesible con enumerate()',
                'tipo': 'experimentar',
                'instruccion': 'Usa `enumerate(canales, start=1)` para numerar canales accesibles del 1 en adelante. Ejecuta con Control + Enter.',
                'codigo': "canales = ['Audio sintetizado', 'Línea Braille', 'Consola interactiva']\nfor num, canal in enumerate(canales, start=1):\n    print(f'{num}. Canal: {canal}')\n",
                'pistas': ['Observa cómo start=1 numera desde el 1 en lugar de 0.'],
                'validar': lambda s, r, n: ('braille' in r.lower() or 'speech' in r.lower())
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Suma de Precios de un Carrito',
                'tipo': 'desafio',
                'instruccion': "Dada la lista `precios = [12.50, 8.00, 24.50]`, inicia `total = 0.0`. Recorre la lista con un bucle for sumando cada precio a `total`. Al finalizar el bucle, imprime: print(f'Total compra: {total}'). Ejecuta con Control + Enter.",
                'codigo': 'precios = [12.50, 8.00, 24.50]\ntotal = 0.0\n# Itera con for sumando a total e imprime el total al final:\n\n',
                'salida_esperada': 'Total compra: 45.0',
                'pistas': ["for p in precios: total += p, y al salir print(f'Total compra: {total}')"],
                'validar': lambda s, r, n: abs(n.get('total', 0) - 45.0) < 0.01 and '45' in r
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: La Función enumerate()',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Devuelve la posición y el dato.'],
                'pregunta': '¿Qué dos valores entrega enumerate(iterable) en cada vuelta del bucle?',
                'opciones': ['El número de índice y el elemento correspondiente.', 'El primer elemento y el último elemento.', 'El tipo de dato y su tamaño en memoria.'],
                'correcta': 0,
                'explicacion': 'enumerate() produce pares (índice, elemento), evitando la necesidad de gestionar contadores manuales.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 27,
        'titulo': 'Capítulo 27: Tuplas (tuple): Inmutabilidad, Seguridad de Datos y Desempaquetado',
        'resumen': 'Aprende a proteger datos críticos mediante colecciones de solo lectura (tuplas) y domina el desempaquetado de variables.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Tuplas frente a Listas e Inmutabilidad',
                'tipo': 'concepto',
                'instruccion': 'En muchas situaciones de ingeniería de software, permitir que una colección sea modificable es un riesgo de seguridad. Por ejemplo: las coordenadas geográficas de un sensor, los códigos de error del sistema o las dimensiones fijas de una ventana. Una **Tupla** (`tuple`) es una colección ordenada e INMUTABLE delimitada por paréntesis `(` y `)`. Diferencia fundamental con las listas: Una vez creada una tupla, sus elementos están sellados: no puedes agregar, borrar ni modificar valores. Intentar hacer `tupla[0] = 5` arrojará un error `TypeError`. Desempaquetado Elegante (*Tuple Unpacking*): Python permite extraer todos los elementos de una tupla en variables individuales en una sola línea: `lat, lon = (4.71, -74.07)`. Esto crea un código sumamente limpio, rápido y seguro. Pulsa Enter o Alt + Flecha Derecha para ver las tuplas en acción.',
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Creación y Desempaquetado de Tuplas',
                'tipo': 'observar',
                'instruccion': 'Observa cómo la tupla `resolucion = (1920, 1080)` se desempaqueta en `ancho, alto`. Pulsa Control + Enter.',
                'codigo': "resolucion = (1920, 1080)\nancho, alto = resolucion\nprint(f'Ancho: {ancho} píxeles, Alto: {alto} píxeles')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: n.get('ancho') == 1920 and n.get('alto') == 1080
            },
            {
                'titulo': 'Paso 3: Experimentación: Comprobar la Inmutabilidad de la Tupla',
                'tipo': 'experimentar',
                'instruccion': 'Accede por índice al primer elemento de `coordenadas = (10, 25)` e imprímelo con `print(coordenadas[0])`. Ejecuta con Control + Enter.',
                'codigo': "coordenadas = (10, 25)\nprint(f'Eje X inmutable: {coordenadas[0]}')\n",
                'pistas': ['Las tuplas admiten lectura por corchetes [0] pero no modificación.'],
                'validar': lambda s, r, n: '10' in r
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Desempaquetar un Registro de Usuario',
                'tipo': 'desafio',
                'instruccion': "Dada la tupla `usuario = ('Elena', 'Desarrolladora', 2026)`, desempaquétala en tres variables: `nombre, rol, anio = usuario`. Imprime con una f-string: 'Elena es Desarrolladora desde 2026'. Pulsa Control + Enter.",
                'codigo': "usuario = ('Elena', 'Desarrolladora', 2026)\n# Desempaqueta e imprime con f-string:\n\n",
                'salida_esperada': 'Elena es Desarrolladora desde 2026',
                'pistas': ["nombre, rol, anio = usuario y print(f'{nombre} es {rol} desde {anio}')"],
                'validar': lambda s, r, n: (n.get('nombre') == 'Elena' or n.get('name') == 'Elena') and ('desarrolladora' in r.lower() or 'developer' in r.lower()) and '2026' in r
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Inmutabilidad de Tuplas',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['La inmutabilidad protege contra modificaciones.'],
                'pregunta': '¿Qué ocurre si intentas modificar un elemento de una tupla mediante asignación (ejemplo: mi_tupla[0] = 99)?',
                'opciones': ['Python genera un error TypeError indicando que las tuplas no admiten asignación de elementos.', 'La tupla se modifica sin problemas.', 'El elemento se añade al final de la tupla.'],
                'correcta': 0,
                'explicacion': 'Las tuplas son inmutables por diseño; cualquier intento de modificar su estructura genera una excepción TypeError.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 28,
        'titulo': 'Capítulo 28: Diccionarios (dict): El Mapeo Clave-Valor',
        'resumen': 'Aprende la estructura asociativa más poderosa de Python: búsqueda ultrarrápida por clave en llaves {} y el método seguro get().',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Mapeos Asociativos y Tablas Hash',
                'tipo': 'concepto',
                'instruccion': "En una lista, los datos se recuperan por su posición numérica (`lista[0]`, `lista[1]`). Pero en el mundo real, los datos se asocian por significado: un documento de identidad se asocia a un nombre, una palabra a su definición o una configuración a su parámetro. Un **Diccionario** (`dict`) es una colección asociativa delimitada por llaves `{` y `}` que almacena pares de `clave: valor`. Reglas clave de los diccionarios: 1. Acceso por Clave: En lugar de un índice numérico, colocas la clave entre corchetes: `persona['nombre']`. 2. Claves Únicas: Cada clave es única; si asignas a una clave existente, su valor se actualiza. 3. Acceso Seguro con `.get()`: Si intentas acceder a una clave que no existe mediante `d['inexistente']`, Python lanza un error `KeyError`. Con `d.get('clave', 'Valor por defecto')`, evitas el fallo y recibes un valor de respaldo seguro si la clave falta. Pulsa Enter o Alt + Flecha Derecha para ver los diccionarios en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Creación y Consulta de Diccionarios',
                'tipo': 'observar',
                'instruccion': 'Examina cómo se almacenan datos estructurados de un usuario y se consultan por clave. Pulsa Control + Enter.',
                'codigo': "config = {'idioma': 'es', 'volumen': 85, 'lector': 'NVDA'}\nprint('Lector activo:', config['lector'])\nprint('Nivel de volumen:', config['volumen'])\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'nvda' in r.lower() and '85' in r
            },
            {
                'titulo': 'Paso 3: Experimentación: Acceso Seguro con get() y Adición de Claves',
                'tipo': 'experimentar',
                'instruccion': "Agrega una nueva clave `config['braille'] = True` y consulta con `.get()` una clave inexistente con valor de respaldo. Pulsa Control + Enter.",
                'codigo': "config = {'idioma': 'es', 'volumen': 85}\nconfig['braille'] = True\nvelocidad = config.get('velocidad', 50)\nprint('Configuración actualizada:', config)\nprint('Velocidad por defecto:', velocidad)\n",
                'pistas': ['get() evita que el programa lance KeyError.'],
                'validar': lambda s, r, n: n.get('config', {}).get('braille') is True and '50' in r
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Ficha de Perfil Profesional',
                'tipo': 'desafio',
                'instruccion': "Crea un diccionario `perfil` con las claves: `'nombre': 'Elena'`, `'rol': 'Programadora'` y `'experiencia': 3`. Luego imprime en una sola f-string: 'Elena es Programadora con 3 años de experiencia'. Pulsa Control + Enter.",
                'codigo': '# Crea el diccionario perfil e imprime con f-string:\n\n',
                'salida_esperada': 'Elena es Programadora con 3 años de experiencia',
                'pistas': ['perfil = {\'nombre\': \'Elena\', \'rol\': \'Programadora\', \'experiencia\': 3}, print(f"{perfil[\'nombre\']} es {perfil[\'rol\']} con {perfil[\'experiencia\']} años de experiencia")'],
                'validar': lambda s, r, n: 'elena' in r.lower() and ('programadora' in r.lower() or 'developer' in r.lower() or 'programmer' in r.lower()) and '3' in r
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Ventaja del Método get()',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Piensa en la prevención de caídas del software.'],
                'pregunta': "¿Por qué es una práctica profesional preferible usar diccionario.get('clave') en lugar de diccionario['clave']?",
                'opciones': ['Porque si la clave no existe, get() devuelve None o un valor por defecto sin romper el programa con un KeyError.', 'Porque get() borra la clave automáticamente tras consultarla.', 'Porque get() solo funciona con números enteros.'],
                'correcta': 0,
                'explicacion': 'El método get() proporciona tolerancia a fallos y previene excepciones KeyError ante claves ausentes o dinámicas.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 29,
        'titulo': 'Capítulo 29: Funciones Propias con def: Principio DRY y Reutilización',
        'resumen': 'Aprende a crear tus propias funciones con def, empaquetar bloques de código reutilizables y aplicar el principio DRY.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: El Principio DRY y la Anatomía de def',
                'tipo': 'concepto',
                'instruccion': "A medida que los programas crecen, repetir el mismo bloque de 10 líneas en cinco lugares distintos es una pésima práctica de ingeniería. El principio fundamental del diseño de software se llama **DRY** (*Don't Repeat Yourself* o 'No te repitas'): cada porción de lógica debe existir en un único lugar. Para encapsular y reutilizar código, definimos nuestras propias **Funciones** mediante la palabra reservada `def`. Anatomía de una función: 1. La palabra `def` seguida del nombre de la función en `snake_case`. 2. Paréntesis `(` y `)` que pueden contener parámetros (variables que la función espera recibir para trabajar). 3. Dos puntos obligatorios `:` al final del encabezado. 4. El cuerpo de la función sangrado con 4 espacios. Definir una función solo le enseña al intérprete una receta; la función no se ejecutará hasta que la 'invoques' o 'llames' por su nombre con sus paréntesis en una línea posterior. Pulsa Enter o Alt + Flecha Derecha para ver una función en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Definición e Invocación',
                'tipo': 'observar',
                'instruccion': 'Examina la función `saludar_usuario(nombre)`. Observa cómo se define primero y luego se invoca dos veces con argumentos distintos. Pulsa Control + Enter.',
                'codigo': "def saludar_usuario(nombre):\n    print(f'Hola, {nombre}. Bienvenido al entorno accesible.')\n\nsaludar_usuario('Elena')\nsaludar_usuario('Kevin')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'elena' in r.lower() and 'kevin' in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Función con Múltiples Parámetros',
                'tipo': 'experimentar',
                'instruccion': 'Crea una función que reciba dos parámetros `mostrar_progreso(capitulo, total)` e imprima el estado. Invócala y pulsa Control + Enter.',
                'codigo': "def mostrar_progreso(capitulo, total):\n    print(f'Avanzando: Capítulo {capitulo} de {total}')\n\nmostrar_progreso(29, 40)\n",
                'pistas': ['Pasa los dos números dentro de los paréntesis al llamar a la función.'],
                'validar': lambda s, r, n: 'capítulo 29 de 40' in r.lower() or 'capitulo 29 de 40' in r.lower()
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Función Calculadora de Rectángulo',
                'tipo': 'desafio',
                'instruccion': "Define una función llamada `calcular_area(base, altura):` que calcule `area = base * altura` e imprima `print(f'Área calculada: {area}')`. Luego invócala con los valores 7 y 6. Pulsa Control + Enter.",
                'codigo': '# Define calcular_area e invócala con 7 y 6:\n\n',
                'salida_esperada': 'Área calculada: 42',
                'pistas': ["def calcular_area(base, altura): area = base * altura print(f'Área calculada: {area}') calcular_area(7, 6)"],
                'validar': lambda s, r, n: '42' in r
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: La Palabra Reservada def',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Es una palabra de 3 letras.'],
                'pregunta': '¿Qué palabra reservada se utiliza en Python para declarar una nueva función?',
                'opciones': ['def (abreviatura de define)', 'function', 'fn'],
                'correcta': 0,
                'explicacion': 'Python utiliza exclusivamente la palabra def de 3 letras para definir funciones y métodos.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 30,
        'titulo': 'Capítulo 30: El Retorno de Valores (return) frente a print()',
        'resumen': 'Comprende la vital diferencia entre emitir sonido en pantalla con print() y entregar un dato procesado a la memoria con return.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: ¿Por qué return no es print?',
                'tipo': 'concepto',
                'instruccion': 'Este es el error conceptual más extendido entre quienes inician en programación: confundir `print()` con `return`. Comprende bien la distinción: - `print()`: Es un acto de comunicación externa. Toma un dato y lo envía a la pantalla y al sintetizador de voz de NVDA. Pero ese dato NO se conserva en el flujo de ejecución; la función no le entrega nada al programa (devuelve el valor vacío `None`). - `return`: Es un acto de entrega interna a la memoria del programa. Finaliza la función de inmediato y entrega el resultado procesado al punto exacto donde la función fue llamada, permitiendo guardar ese dato en una variable o usarlo en otros cálculos. Regla mnemotécnica: Si deseas que el usuario humano escuche algo, usas `print()`; si deseas que tu propio software use el resultado para continuar calculando, usas `return`. Pulsa Enter o Alt + Flecha Derecha para ver el valor de return.',
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Capturando el Resultado de return',
                'tipo': 'observar',
                'instruccion': 'Observa cómo la función `cuadrado(x)` devuelve el resultado con return y este se almacena en la variable `res`. Pulsa Control + Enter.',
                'codigo': "def cuadrado(x):\n    return x * x\n\nres = cuadrado(8)\nprint(f'El resultado guardado en memoria es: {res}')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: n.get('res') == 64 and '64' in r
            },
            {
                'titulo': 'Paso 3: Experimentación: Encadenando Funciones con return',
                'tipo': 'experimentar',
                'instruccion': 'Observa cómo el retorno de una función puede pasarse directamente a otra operación matemática: `resultado = cuadrado(5) + 10`. Pulsa Control + Enter.',
                'codigo': "def cuadrado(n):\n    return n * n\n\nresultado = cuadrado(5) + 10\nprint(f'Cálculo encadenado: {resultado}')\n",
                'pistas': ['cuadrado(5) devuelve 25 y suma 10 = 35.'],
                'validar': lambda s, r, n: n.get('resultado') == 35 and '35' in r
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Función Validadora de Mayoría de Edad',
                'tipo': 'desafio',
                'instruccion': 'Define una función `es_adulto(edad):` que retorne con `return` el valor booleano de `edad >= 18`. Guarda el resultado de `es_adulto(21)` en una variable `autorizado` y muéstrala con print(autorizado). Ejecuta con Control + Enter.',
                'codigo': '# Define es_adulto con return, asigna a autorizado e imprime:\n\n',
                'salida_esperada': 'True',
                'pistas': ['def es_adulto(edad): return edad >= 18, autorizado = es_adulto(21), print(autorizado)'],
                'validar': lambda s, r, n: (n.get('autorizado') is True or n.get('authorized') is True or n.get('is_adult') is True) and 'true' in r.lower()
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Retorno Implícito',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ["Piensa en la palabra inglesa para 'ninguno'."],
                'pregunta': '¿Qué valor devuelve en memoria una función de Python que solo contiene instrucciones print() y carece de return?',
                'opciones': ['None (el objeto que representa la ausencia de valor en Python)', 'El número 0', "Una cadena de texto vacía ''"],
                'correcta': 0,
                'explicacion': 'Toda función sin sentencia return explícita concluye entregando implícitamente None.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 31,
        'titulo': 'Capítulo 31: Ámbito de Variables (Scope): Variables Locales vs Globales (Regla LEGB)',
        'resumen': 'Aprende el ciclo de vida y visibilidad de las variables: por qué las variables locales nacen y mueren dentro de su función.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: El Ámbito Léxico y el Aislamiento de Memoria',
                'tipo': 'concepto',
                'instruccion': "El 'Ámbito' (*Scope*) es la región del programa donde una variable es visible y accesible. Python divide el ámbito en dos categorías principales: 1. Ámbito Local: Toda variable creada dentro del cuerpo de una función es LOCAL a esa función. Nace cuando la función comienza y se destruye en la memoria en cuanto la función termina. El resto del programa NO puede ver ni modificar esa variable local. 2. Ámbito Global: Una variable creada en el cuerpo principal del script (sin sangría) es GLOBAL y puede ser leída desde cualquier lugar. ¿Por qué existe este aislamiento? Porque si todas las variables fueran globales, dos funciones creadas por programadores distintos que usaran el nombre `contador` se pisarían la memoria mutuamente, causando errores impredecibles. Regla LEGB de Python: Para buscar una variable, Python mira primero en lo Local, luego Enclosing, luego Global y finalmente Built-in. Pulsa Enter o Alt + Flecha Derecha para ver el aislamiento local en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Variables Locales Protegidas',
                'tipo': 'observar',
                'instruccion': 'Observa cómo `mensaje_local` solo existe dentro de la función y se entrega al exterior mediante return. Pulsa Control + Enter.',
                'codigo': "def generar_reporte():\n    mensaje_local = 'Reporte interno seguro'\n    return mensaje_local\n\nreporte = generar_reporte()\nprint(reporte)\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: ('reporte' in r.lower() or 'report' in r.lower())
            },
            {
                'titulo': 'Paso 3: Experimentación: Variables Globales vs Locales',
                'tipo': 'experimentar',
                'instruccion': 'Examina cómo la variable global `version = 3` puede ser leída dentro de la función sin conflicto. Ejecuta con Control + Enter.',
                'codigo': "version = 3\n\ndef consultar_version():\n    return f'Versión global activa: {version}'\n\nprint(consultar_version())\n",
                'pistas': ['Las funciones pueden leer variables globales si no las reasignan.'],
                'validar': lambda s, r, n: 'versión global activa: 3' in r.lower() or 'version global activa: 3' in r.lower()
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Comunicación Limpia mediante Parámetros',
                'tipo': 'desafio',
                'instruccion': 'Evita variables globales. Crea una función `calcular_iva(subtotal)` que calcule y retorne `subtotal * 0.19`. Guarda el IVA de un subtotal de 200 en `iva` e imprime `iva`. Ejecuta con Control + Enter.',
                'codigo': '# Define calcular_iva con subtotal como parámetro y retorna el 19%:\n\n',
                'salida_esperada': '38.0',
                'pistas': ['def calcular_iva(subtotal): return subtotal * 0.19, iva = calcular_iva(200), print(iva)'],
                'validar': lambda s, r, n: abs(n.get('iva', 0) - 38.0) < 0.01 and '38' in r
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Ciclo de Vida de Variables Locales',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Las variables locales tienen vida efímera.'],
                'pregunta': '¿Qué sucede con una variable creada dentro de una función cuando esa función finaliza su ejecución?',
                'opciones': ['Se destruye y desaparece de la memoria RAM automáticamente.', 'Se guarda permanentemente en el disco duro.', 'Se convierte en una variable global accesible en todo el archivo.'],
                'correcta': 0,
                'explicacion': 'El recolector de basura de Python libera la memoria de las variables locales al concluir el marco de ejecución de la función.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 32,
        'titulo': 'Capítulo 32: Manejo Profesional de Excepciones: try, except, finally y Lectura del Traceback con F4',
        'resumen': 'Aprende a anticipar errores en tiempo de ejecución para evitar caídas del software y domina la lectura accesible de trazas de error.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Errores Previstos y la Estructura try / except',
                'tipo': 'concepto',
                'instruccion': "En el mundo real, los programas se enfrentan a situaciones imprevistas: el usuario escribe letras donde se esperaba un número, un archivo solicitado no existe o se pierde la conexión de red. Si no protegemos nuestro código, Python lanza una 'Excepción' y el programa colapsa abruptamente. Para construir software tolerante a fallos, utilizamos la estructura `try / except`: 1. Bloque `try:`: Colocas las instrucciones 'arriesgadas' que podrían fallar. 2. Bloque `except TipoDeError:`: Si ocurre ese error específico dentro del try, Python salta de inmediato aquí sin romper el programa, permitiéndonos emitir un mensaje amable o tomar una ruta alternativa. 3. Bloque `finally:` (opcional): Se ejecuta SIEMPRE, haya ocurrido o no un error (ideal para cerrar archivos o conexiones). Diagnóstico con la Tecla F4: En este entorno, cuando se produce una excepción no controlada, pulsar F4 coloca tu cursor directamente en la línea exacta del fallo para que puedas examinarla al instante. Pulsa Enter o Alt + Flecha Derecha para ver el control de errores en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Captura de ZeroDivisionError',
                'tipo': 'observar',
                'instruccion': 'Observa cómo dividir por cero no rompe el programa gracias al bloque except. Pulsa Control + Enter para escuchar el mensaje controlado.',
                'codigo': "try:\n    divisor = 0\n    resultado = 100 / divisor\n    print(resultado)\nexcept ZeroDivisionError:\n    print('Aviso seguro: No es posible dividir por cero.')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: ('no es posible dividir' in r.lower() or 'cannot divide' in r.lower() or 'zero' in r.lower())
            },
            {
                'titulo': 'Paso 3: Experimentación: Captura de Conversión Inválida (ValueError)',
                'tipo': 'experimentar',
                'instruccion': 'Prueba a convertir un texto no numérico dentro de un try y captura el `ValueError` para avisar al usuario. Pulsa Control + Enter.',
                'codigo': "entrada_usuario = 'veinte'\ntry:\n    numero = int(entrada_usuario)\n    print(numero)\nexcept ValueError:\n    print('Error de formato: La entrada no contiene dígitos numéricos válidos.')\n",
                'pistas': ['ValueError se dispara cuando int() recibe letras.'],
                'validar': lambda s, r, n: ('formato' in r.lower() or 'format' in r.lower() or 'digits' in r.lower() or 'valid' in r.lower())
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Función de Conversión Segura',
                'tipo': 'desafio',
                'instruccion': "Define una función `convertir_a_entero(texto):` que intente `return int(texto)` dentro de un bloque try. Si ocurre `ValueError`, captura el error y devuelve `None`. Prueba con `res = convertir_a_entero('abc')` e imprime `res`. Pulsa Control + Enter.",
                'codigo': '# Define convertir_a_entero con try/except ValueError, asigna a res e imprime:\n\n',
                'salida_esperada': 'None',
                'pistas': ['def convertir_a_entero(texto): try: return int(texto) except ValueError: return None'],
                'validar': lambda s, r, n: n.get('res') is None and 'none' in r.lower()
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: El Bloque finally',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Es la garantía final incondicional.'],
                'pregunta': '¿Bajo qué circunstancias se ejecutan las sentencias ubicadas dentro de una cláusula finally?',
                'opciones': ['Se ejecutan SIEMPRE de forma garantizada, haya ocurrido o no una excepción en el try.', 'Únicamente si ocurrió un error en el try.', 'Solo si no ocurrió ningún error en el try.'],
                'correcta': 0,
                'explicacion': 'La cláusula finally garantiza la ejecución de código de limpieza y cierre de recursos sin importar el resultado del bloque try.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 33,
        'titulo': 'Capítulo 33: Entrada y Salida de Archivos de Texto: open() y el Context Manager with',
        'resumen': 'Aprende a leer y escribir archivos en el disco duro de forma segura garantizando el cierre de recursos con with open().',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Persistencia en Disco y Administradores de Contexto',
                'tipo': 'concepto',
                'instruccion': "Hasta ahora, todos nuestros datos residían en la memoria RAM y desaparecían al terminar el programa. Para que los datos sobrevivan a reinicios del equipo, debemos guardarlos en el disco duro en forma de archivos. En Python, interactuamos con archivos mediante la función `open()`. Modos de apertura principales: - `'w'` (*write* o escritura): Crea un archivo nuevo o SOBREESCRIBE por completo el archivo existente si ya existía. - `'r'` (*read* o lectura): Abre un archivo existente para leer su contenido; si no existe, lanza `FileNotFoundError`. - `'a'` (*append* o adición): Escribe al final del archivo sin borrar lo que ya contenía. El Administrador de Contexto `with`: En lugar de abrir y acordarse de llamar a `f.close()`, usamos: `with open('archivo.txt', 'w', encoding='utf-8') as f:`. La sentencia `with` garantiza que el archivo se cierre automáticamente al salir del bloque, incluso si ocurre un error inesperado, protegiendo contra fugas de recursos en el sistema operativo. Pulsa Enter o Alt + Flecha Derecha para ver la escritura y lectura en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Escritura y Lectura Segura',
                'tipo': 'observar',
                'instruccion': "Observa el ciclo completo: primero se escribe una frase en 'notas.txt' y luego se lee y muestra en consola. Pulsa Control + Enter.",
                'codigo': "with open('notas.txt', 'w', encoding='utf-8') as f:\n    f.write('Python es accesible con NVDA')\n\nwith open('notas.txt', 'r', encoding='utf-8') as f:\n    contenido = f.read()\n\nprint(f'Contenido recuperado del disco: {contenido}')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'python es accesible' in r.lower()
            },
            {
                'titulo': "Paso 3: Experimentación: Añadir Líneas con Modo Append ('a')",
                'tipo': 'experimentar',
                'instruccion': "Abre en modo 'a' para agregar una segunda línea con salto de línea `\\n` y luego lee todo el archivo. Pulsa Control + Enter.",
                'codigo': "with open('registro.txt', 'w', encoding='utf-8') as f:\n    f.write('Entrada 1\\n')\n\nwith open('registro.txt', 'a', encoding='utf-8') as f:\n    f.write('Entrada 2 agregada\\n')\n\nwith open('registro.txt', 'r', encoding='utf-8') as f:\n    print(f.read().strip())\n",
                'pistas': ["El modo 'a' agrega al final sin sobreescribir."],
                'validar': lambda s, r, n: 'entrada 1' in r.lower() and 'entrada 2' in r.lower()
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Guardar y Leer Mensaje del Alumno',
                'tipo': 'desafio',
                'instruccion': "Escribe en el archivo 'mensaje.txt' la frase 'Estudiante activo en NVDA'. Luego ábrelo en modo 'r', lee su texto en `texto_leido` e imprime `print(texto_leido)`. Ejecuta con Control + Enter.",
                'codigo': '# Escribe en mensaje.txt y luego lee e imprime:\n\n',
                'salida_esperada': 'Estudiante activo en NVDA',
                'pistas': ["with open('mensaje.txt', 'w', encoding='utf-8') as f: f.write('Estudiante activo en NVDA') y luego abrir en 'r' y leer."],
                'validar': lambda s, r, n: ('estudiante' in r.lower() or 'student' in r.lower()) and ('activo' in r.lower() or 'active' in r.lower())
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Ventaja de with open()',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Piensa en el cierre automático garantizado.'],
                'pregunta': '¿Por qué es una regla de ingeniería de software usar with open() en lugar de f = open() y f.close()?',
                'opciones': ['Garantiza que el archivo se cierre y libere de memoria automáticamente aunque ocurra un error.', 'Hace que el archivo sea invisible para otros usuarios.', 'Convierte automáticamente el texto en un archivo de audio MP3.'],
                'correcta': 0,
                'explicacion': 'El gestor de contexto with invoca el método __exit__ garantizando la liberación de descriptores de archivo en el sistema operativo.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 34,
        'titulo': 'Capítulo 34: Persistencia de Datos Estructurados con JSON (json.dump y json.load)',
        'resumen': 'Aprende el estándar mundial de intercambio y almacenamiento estructurado de datos (JSON) usando la biblioteca estándar nativa.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: El Estándar JSON y la Serialización',
                'tipo': 'concepto',
                'instruccion': "Guardar texto plano suelto en un archivo es útil para notas, pero insuficiente para estructuras complejas como diccionarios, listas de usuarios o configuraciones del sistema. **JSON** (*JavaScript Object Notation*) es el estándar universal más utilizado en el planeta para guardar e intercambiar información estructurada entre aplicaciones. Lo fascinante de JSON es que su sintaxis es prácticamente idéntica a los diccionarios y listas nativas de Python: usa llaves `{}` para pares clave-valor y corchetes `[]` para listas. El módulo estándar `json` de Python ofrece dos funciones clave: - `json.dump(datos, archivo, indent=2)`: 'Vuelca' o serializa un diccionario/lista de Python directamente a un archivo de disco en formato JSON legible. - `json.load(archivo)`: Lee un archivo JSON y lo reconstruye en memoria RAM como un diccionario nativo de Python listo para operar. Al ser parte de la biblioteca estándar, NO requiere instalar nada externo. Pulsa Enter o Alt + Flecha Derecha para ver la persistencia con JSON.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Guardar y Cargar Estructuras con json',
                'tipo': 'observar',
                'instruccion': "Observa cómo se guarda un diccionario en 'config.json' con dump() y luego se recupera con load(). Pulsa Control + Enter.",
                'codigo': "import json\n\nusuario = {'nombre': 'Elena', 'nivel': 3, 'accesible': True}\n\nwith open('config.json', 'w', encoding='utf-8') as f:\n    json.dump(usuario, f, indent=2)\n\nwith open('config.json', 'r', encoding='utf-8') as f:\n    datos_cargados = json.load(f)\n\nprint('Datos recuperados de JSON:', datos_cargados['nombre'], datos_cargados['nivel'])\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'elena 3' in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Modificar y Re-serializar',
                'tipo': 'experimentar',
                'instruccion': 'Modifica un dato del diccionario cargado y vuelve a guardarlo en disco. Pulsa Control + Enter.',
                'codigo': "import json\n\ndatos = {'app': 'Python Tutor', 'version': 2.0}\ndatos['version'] = 3.0\n\nwith open('app_meta.json', 'w', encoding='utf-8') as f:\n    json.dump(datos, f)\n\nwith open('app_meta.json', 'r', encoding='utf-8') as f:\n    print(json.load(f))\n",
                'pistas': ['Comprueba que la versión se actualice a 3.0.'],
                'validar': lambda s, r, n: '3.0' in r or '3' in r
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Lista de Tareas Persistente en JSON',
                'tipo': 'desafio',
                'instruccion': "Crea una lista `mis_tareas = ['Aprender JSON', 'Dominar NVDA']`. Guárdala en 'tareas.json' con `json.dump()`. Luego léela con `json.load()` en `tareas_recuperadas` e imprime la primera tarea con `print(tareas_recuperadas[0])`. Pulsa Control + Enter.",
                'codigo': "import json\n\nmis_tareas = ['Aprender JSON', 'Dominar NVDA']\n# Guarda en tareas.json, lee en tareas_recuperadas e imprime el primer elemento:\n\n",
                'salida_esperada': 'Aprender JSON',
                'pistas': ["json.dump(mis_tareas, f) en modo 'w', luego tareas_recuperadas = json.load(f) en 'r' y print(tareas_recuperadas[0])."],
                'validar': lambda s, r, n: ('aprender json' in r.lower() or 'learn json' in r.lower())
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: La Función json.load()',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Piensa en cargar desde disco a la memoria.'],
                'pregunta': '¿Qué hace la función json.load(archivo) en Python?',
                'opciones': ['Lee un archivo formateado en JSON y lo transforma en un diccionario o lista nativa en memoria.', 'Descarga un archivo desde internet automáticamente.', 'Borra el archivo JSON del disco.'],
                'correcta': 0,
                'explicacion': 'json.load deserializa texto JSON desde un objeto archivo hacia estructuras de datos nativas de Python.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 35,
        'titulo': 'Capítulo 35: Paradigma Orientado a Objetos (POO): Clases, Instancias y Atributos',
        'resumen': 'Aprende el paradigma de la Programación Orientada a Objetos: modela entidades del mundo real usando clases como moldes y objetos concretos.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: El Modelo Mental de la Clase y el Objeto',
                'tipo': 'concepto',
                'instruccion': "Hasta el momento hemos programado de forma 'procedimental' (variables sueltas y funciones que las procesan). La **Programación Orientada a Objetos** (POO) es un paradigma donde agrupamos datos (atributos) y comportamientos (métodos) dentro de una sola entidad llamada **Objeto**. La gran analogía: 1. La **Clase** (`class`): Es el plano arquitectónico o el molde de galletas. Define qué propiedades tendrá un tipo de entidad, pero la clase en sí no es una galleta física. 2. El **Objeto** o **Instancia**: Es la galleta horneada o el edificio construido a partir del plano. Puedes construir 100 edificios independientes a partir del mismo plano; cada uno tendrá su propia dirección y estado interno en la memoria RAM. Para definir una clase en Python usamos la palabra reservada `class`, seguida del nombre con mayúscula inicial en formato `PascalCase` (ejemplo: `class Usuario:`). Pulsa Enter o Alt + Flecha Derecha para ver clases e instancias en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Definición de Clase e Instanciación',
                'tipo': 'observar',
                'instruccion': 'Observa cómo se define la clase `Estudiante` y luego se crean dos objetos independientes: `alumno1` y `alumno2`. Pulsa Control + Enter.',
                'codigo': "class Estudiante:\n    institucion = 'Academia Accesible NVDA'\n\nalumno1 = Estudiante()\nalumno2 = Estudiante()\n\nprint('Alumno 1 pertenece a:', alumno1.institucion)\nprint('Alumno 2 pertenece a:', alumno2.institucion)\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: ('academia' in r.lower() or 'academy' in r.lower() or 'nvda' in r.lower())
            },
            {
                'titulo': 'Paso 3: Experimentación: Asignar Atributos Propios a una Instancia',
                'tipo': 'experimentar',
                'instruccion': "Asigna atributos específicos a cada alumno usando la notación de punto: `alumno1.nombre = 'Elena'` y `alumno2.nombre = 'Kevin'`. Imprime ambos y pulsa Control + Enter.",
                'codigo': "class Estudiante:\n    pass\n\nalumno1 = Estudiante()\nalumno1.nombre = 'Elena'\n\nalumno2 = Estudiante()\nalumno2.nombre = 'Kevin'\n\nprint(f'Estudiantes registrados: {alumno1.nombre} y {alumno2.nombre}')\n",
                'pistas': ['La notación de punto vincula el atributo al objeto concreto.'],
                'validar': lambda s, r, n: 'elena y kevin' in r.lower()
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Modelar una Tarea de Software',
                'tipo': 'desafio',
                'instruccion': "Crea una clase vacía `class Tarea: pass`. Instancia un objeto `t = Tarea()`. Asigna `t.titulo = 'Aprender POO'` y `t.completada = True`. Imprime en una f-string: 'Tarea: Aprender POO, Estado: True'. Pulsa Control + Enter.",
                'codigo': '# Define la clase Tarea, crea t, asigna atributos e imprime:\n\n',
                'salida_esperada': 'Tarea: Aprender POO, Estado: True',
                'pistas': ["class Tarea: pass, t = Tarea(), t.titulo = 'Aprender POO', t.completada = True, print(f'Tarea: {t.titulo}, Estado: {t.completada}')"],
                'validar': lambda s, r, n: 'aprender poo' in r.lower() and 'true' in r.lower()
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Relación Clase vs Objeto',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Recuerda la analogía del plano arquitectónico y el edificio construido.'],
                'pregunta': '¿Cuál es la relación conceptual entre una Clase y un Objeto en programación orientada a objetos?',
                'opciones': ['La clase es el molde o plano conceptual; el objeto es la entidad concreta instanciada en memoria.', 'Son idénticos y significan exactamente lo mismo.', 'La clase solo guarda números y el objeto solo guarda texto.'],
                'correcta': 0,
                'explicacion': 'Una clase es la definición abstracta de estructura y comportamiento; un objeto es la manifestación concreta creada a partir de ella.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 36,
        'titulo': 'Capítulo 36: El Constructor __init__, el Parámetro self y Métodos de Instancia',
        'resumen': 'Aprende a inicializar objetos automáticamente con el constructor __init__, desmitifica self y define comportamientos con métodos de instancia.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: El Constructor __init__ y el Parámetro self',
                'tipo': 'concepto',
                'instruccion': "Asignar atributos a mano uno por uno (`objeto.x = 1`) es engorroso y peligroso. En POO profesional, cada objeto debe nacer completamente configurado desde el primer milisegundo de su existencia. Para esto utilizamos el método constructor especial `__init__()` (con doble guion bajo al inicio y al final, conocido como método mágico o *dunder init*). Desmitificando el parámetro `self`: El primer parámetro de cualquier método dentro de una clase SIEMPRE se llama `self`. `self` (que significa 'yo mismo') es una referencia que el objeto tiene de su propia identidad en la memoria RAM. Cuando escribes `self.nombre = nombre`, le dices a Python: 'Guarda este dato dentro de MI propio cuerpo de objeto, no en una variable suelta'. Los métodos son simplemente funciones que viven dentro de la clase y reciben a `self` para consultar o modificar el estado interno del objeto. Pulsa Enter o Alt + Flecha Derecha para ver el constructor en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Clase con __init__ y Método de Instancia',
                'tipo': 'observar',
                'instruccion': 'Examina la clase `CanalAccesible`. Observa cómo `__init__` inicializa el nombre y `describir()` emite el mensaje. Pulsa Control + Enter.',
                'codigo': "class CanalAccesible:\n    def __init__(self, nombre, tipo):\n        self.nombre = nombre\n        self.tipo = tipo\n\n    def describir(self):\n        return f'Canal: {self.nombre} ({self.tipo})'\n\ncanal1 = CanalAccesible('Voz NVDA', 'Audio Sintetizado')\nprint(canal1.describir())\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'voz nvda' in r.lower() and 'sintetizado' in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Modificar Estado Interno con un Método',
                'tipo': 'experimentar',
                'instruccion': 'Crea una clase `Contador` con un método `incrementar()` que sume `self.valor += 1`. Ejecuta con Control + Enter.',
                'codigo': "class Contador:\n    def __init__(self):\n        self.valor = 0\n\n    def incrementar(self):\n        self.valor += 1\n\nc = Contador()\nc.incrementar()\nc.incrementar()\nprint(f'Valor actual del contador: {c.valor}')\n",
                'pistas': ['Llamar c.incrementar() dos veces eleva el valor a 2.'],
                'validar': lambda s, r, n: '2' in r and getattr(n.get('c'), 'valor', 0) == 2
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Cuenta de Ahorros Segura',
                'tipo': 'desafio',
                'instruccion': "Define `class CuentaBancaria:`. En `__init__(self, titular):` asigna `self.titular = titular` y `self.saldo = 0`. Añade un método `depositar(self, monto):` que sume `self.saldo += monto`. Instancia `cuenta = CuentaBancaria('Elena')`, deposita 150 e imprime: `print(f'Titular: {cuenta.titular}, Saldo: {cuenta.saldo}')`. Ejecuta con Control + Enter.",
                'codigo': '# Define CuentaBancaria, deposita 150 e imprime:\n\n',
                'salida_esperada': 'Titular: Elena, Saldo: 150',
                'pistas': ["Define __init__ y depositar con self. Instancia cuenta = CuentaBancaria('Elena'), llama cuenta.depositar(150) e imprime."],
                'validar': lambda s, r, n: 'elena' in r.lower() and '150' in r and getattr(n.get('cuenta'), 'saldo', 0) == 150
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: El Significado de self',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['self se refiere al propio objeto individual.'],
                'pregunta': '¿Qué representa el primer parámetro convencional self en los métodos de una clase?',
                'opciones': ['Representa la instancia u objeto concreto sobre el cual se está invocando el método.', 'Es una palabra secreta para conectarse a internet.', 'Representa el número de línea del código fuente.'],
                'correcta': 0,
                'explicacion': 'self enlaza el método a la memoria individual del objeto concreto, permitiendo acceder y modificar sus propios atributos.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 37,
        'titulo': 'Capítulo 37: La Biblioteca Estándar de Python (math, random, datetime, pathlib)',
        'resumen': "Descubre las 'baterías incluidas' de Python: herramientas profesionales preinstaladas de fábrica sin necesidad de gestores externos.",
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Las Baterías Incluidas de Python',
                'tipo': 'concepto',
                'instruccion': "Una de las razones por las que Python domina la industria de software es su filosofía de 'Baterías Incluidas' (*Batteries Included*). A diferencia de otros ecosistemas donde necesitas descargar decenas de paquetes inestables de internet, Python viene de fábrica con cientos de módulos profesionales listos para usar con solo escribir `import`. Módulos esenciales de la Biblioteca Estándar: - `math`: Funciones matemáticas de alta precisión: raíces cuadradas (`math.sqrt`), trigonometría, constantes como `math.pi`. - `random`: Generación de números pseudoaleatorios, simulaciones y selecciones al azar (`random.randint`, `random.choice`). - `datetime`: Manejo de fechas, calendarios, marcas de tiempo y cronómetros. - `pathlib`: Gestión de rutas de archivos del sistema operativo de forma multiplataforma y segura. Todo esto está disponible de forma nativa en cualquier instalación de Python y dentro de NVDA con cero fallos de dependencias. Pulsa Enter o Alt + Flecha Derecha para ver estos módulos en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Módulos math y random',
                'tipo': 'observar',
                'instruccion': 'Examina cómo importamos math y random sin instalar nada externo. Pulsa Control + Enter.',
                'codigo': "import math\nimport random\n\nraiz = math.sqrt(64)\ndado = random.randint(1, 6)\n\nprint(f'Raíz cuadrada de 64: {raiz}')\nprint(f'Tirada de dado aleatoria: {dado}')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: '8.0' in r or '8' in r
            },
            {
                'titulo': 'Paso 3: Experimentación: Marcas de Tiempo con datetime',
                'tipo': 'experimentar',
                'instruccion': 'Usa `datetime.date.today()` para obtener la fecha de hoy y formatéala en pantalla. Pulsa Control + Enter.',
                'codigo': "import datetime\n\nhoy = datetime.date.today()\nprint(f'Fecha registrada por el sistema: {hoy}')\n",
                'pistas': ['datetime forma parte de la biblioteca estándar nativa.'],
                'validar': lambda s, r, n: 'fecha registrada' in r.lower()
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Generador de Claves Seguras Aleatorias',
                'tipo': 'desafio',
                'instruccion': 'Usa `import random`. Dada una lista de caracteres `caracteres = [\'A\', \'B\', \'C\', \'1\', \'2\', \'3\']`, selecciona 4 caracteres al azar con `token = [random.choice(caracteres) for _ in range(4)]`. Conviértelo en texto con `\'\'.join(token)` e imprime: `print(f\'Token generado: {"".join(token)}\')`. Pulsa Control + Enter.',
                'codigo': "import random\ncaracteres = ['A', 'B', 'C', '1', '2', '3']\n# Genera un token aleatorio de 4 caracteres e imprímelo:\n\n",
                'pistas': ["Usa random.choice dentro de una lista o bucle y únelos con ''.join."],
                'validar': lambda s, r, n: 'token generado' in r.lower() and len(r.strip()) > 15
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: La Biblioteca Estándar',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ["Recuerda la filosofía de 'baterías incluidas'."],
                'pregunta': '¿Por qué los módulos de la Biblioteca Estándar (como math, random, json o sqlite3) no requieren instalación con pip?',
                'opciones': ["Porque vienen preinstalados e integrados de fábrica con cualquier intérprete de Python ('baterías incluidas').", 'Porque se descargan en secreto cada vez que ejecutas un print.', 'Porque solo funcionan en computadoras de la NASA.'],
                'correcta': 0,
                'explicacion': 'La Biblioteca Estándar forma parte indivisible del runtime oficial de Python en cualquier plataforma.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 38,
        'titulo': 'Capítulo 38: Bases de Datos Relacionales con SQLite (sqlite3): Tablas y Consultas Parametrizadas',
        'resumen': 'Aprende a gestionar bases de datos relacionales SQL profesionales utilizando el motor sqlite3 integrado sin instalar servidores.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Bases de Datos Relacionales y el Motor sqlite3',
                'tipo': 'concepto',
                'instruccion': "Cuando una aplicación maneja miles de registros relacionados (clientes, facturas, productos), guardar todo en archivos de texto o JSON se vuelve ineficiente y lento. Para esto, la industria utiliza **Bases de Datos Relacionales** mediante el lenguaje de consultas **SQL** (*Structured Query Language*). Python incluye de forma 100% nativa **SQLite**, el motor de base de datos SQL más utilizado del mundo (presente en teléfonos, navegadores y en el propio NVDA). Ventajas de SQLite: - Cero configuración: No requiere instalar MySQL, Postgres ni servidores externos. Toda la base de datos reside en un único archivo local (o incluso en memoria RAM con `':memory:'`). - Consultas SQL Parametrizadas: Para evitar ataques de seguridad (*Inyección SQL*), NUNCA concatenamos variables con strings; usamos el marcador de posición `?` para pasar tuplas de datos de forma blindada. Pulsa Enter o Alt + Flecha Derecha para ver SQLite en acción.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Crear Tabla e Insertar Registros',
                'tipo': 'observar',
                'instruccion': 'Examina cómo conectamos con sqlite3 en memoria, creamos una tabla de usuarios y consultamos con SELECT. Pulsa Control + Enter.',
                'codigo': "import sqlite3\n\nconexion = sqlite3.connect(':memory:')\ncursor = conexion.cursor()\n\ncursor.execute('CREATE TABLE alumnos (id INTEGER PRIMARY KEY, nombre TEXT, nota REAL)')\ncursor.execute('INSERT INTO alumnos (nombre, nota) VALUES (?, ?)', ('Elena', 9.5))\ncursor.execute('INSERT INTO alumnos (nombre, nota) VALUES (?, ?)', ('Kevin', 9.0))\nconexion.commit()\n\ncursor.execute('SELECT nombre, nota FROM alumnos')\nfor fila in cursor.fetchall():\n    print(f'Alumno: {fila[0]}, Nota: {fila[1]}')\n\nconexion.close()\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: 'elena' in r.lower() and 'kevin' in r.lower() and '9.5' in r
            },
            {
                'titulo': 'Paso 3: Experimentación: Filtrar Registros con Cláusula WHERE',
                'tipo': 'experimentar',
                'instruccion': 'Filtra la consulta SQL usando `WHERE nota >= 9.0` para recuperar únicamente estudiantes destacados. Pulsa Control + Enter.',
                'codigo': "import sqlite3\n\ncon = sqlite3.connect(':memory:')\ncur = con.cursor()\ncur.execute('CREATE TABLE cursos (titulo TEXT, horas INTEGER)')\ncur.execute('INSERT INTO cursos VALUES (?, ?)', ('Python Accesible', 40))\ncur.execute('INSERT INTO cursos VALUES (?, ?)', ('HTML Rápido', 10))\ncon.commit()\n\ncur.execute('SELECT titulo FROM cursos WHERE horas >= 20')\nfor fila in cur.fetchall():\n    print(f'Curso intensivo: {fila[0]}')\ncon.close()\n",
                'pistas': ['WHERE filtra los registros en la base de datos.'],
                'validar': lambda s, r, n: 'python accesible' in r.lower() and 'html rápido' not in r.lower()
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Inventario Accesible con SQLite',
                'tipo': 'desafio',
                'instruccion': "Conéctate a `:memory:`, crea tabla `articulos (nombre TEXT, cantidad INTEGER)`. Inserta con parámetros `('Teclado', 15)`. Realiza un `SELECT nombre, cantidad FROM articulos` e imprime: 'Teclado: 15 unidades'. Cierra la conexión y ejecuta con Control + Enter.",
                'codigo': 'import sqlite3\n# Crea la base de datos en memoria, inserta el artículo e imprime:\n\n',
                'salida_esperada': 'Teclado: 15 unidades',
                'pistas': ["cursor.execute('INSERT INTO articulos VALUES (?, ?)', ('Teclado', 15)), luego fetchall() y print."],
                'validar': lambda s, r, n: (('teclado' in r.lower() or 'keyboard' in r.lower()) and '15' in r)
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Inserción Parametrizada con ?',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Piensa en la seguridad contra ataques informáticos.'],
                'pregunta': '¿Por qué es obligatorio en software profesional usar marcadores ? en lugar de concatenar cadenas en sentencias SQL?',
                'opciones': ['Para prevenir vulnerabilidades graves de inyección SQL (SQL Injection) y garantizar seguridad.', 'Porque las computadoras no saben leer comillas en SQL.', 'Para que la base de datos ocupe la mitad del espacio en disco.'],
                'correcta': 0,
                'explicacion': 'Las consultas parametrizadas separan la instrucción de código de los datos del usuario, neutralizando cualquier intento de inyección maliciosa.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 39,
        'titulo': 'Capítulo 39: Tiflotecnología y Desarrollo Accesible por Software: Integración con NVDA y Síntesis de Voz',
        'resumen': 'Aprende cómo el software interactúa con lectores de pantalla, síntesis de voz y señales acústicas para crear interfaces inclusivas.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: La Tiflotecnología y la Accesibilidad en la Arquitectura de Software',
                'tipo': 'concepto',
                'instruccion': "La 'Tiflotecnología' es la rama de la ingeniería dedicada a diseñar tecnologías y adaptaciones para personas ciegas o con baja visión. Cuando desarrollas una aplicación accesible, no basta con que el código funcione; la experiencia de usuario debe comunicar el estado del sistema con claridad meridiana a través de dos canales sensoriales principales: 1. Canal de Voz (Síntesis de voz / Speech): Mensajes descriptivos, concisos y no redundantes que informan qué acción se completó o qué opción está seleccionada. 2. Canal Acústico (Tonos de Audio / Earcons): Pitidos breves y sutiles con frecuencias distintas que confirman eventos instantáneamente sin interrumpir la voz (por ejemplo, un tono agudo para éxito y un tono grave para error). En Windows y dentro de NVDA, Python puede emitir tonos acústicos nativos mediante la biblioteca estándar `winsound` con `winsound.Beep(frecuencia, duracion)`. Diseñar software accesible desde el primer día es una de las marcas distintivas de los mejores ingenieros del mundo. Pulsa Enter o Alt + Flecha Derecha para escuchar señales auditivas accesibles.",
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Emisión de Señales Acústicas Accesibles',
                'tipo': 'observar',
                'instruccion': 'Observa cómo se emiten tonos de audio con winsound para confirmar estados del sistema. Pulsa Control + Enter para escuchar.',
                'codigo': "import winsound\n\nprint('Emitiendo señal acústica de éxito (frecuencia 880 Hz)...')\nwinsound.Beep(880, 150)\nprint('Notificación acústica completada.')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar y escuchar el tono.'],
                'validar': lambda s, r, n: 'notificación acústica' in r.lower() or 'notificacion acustica' in r.lower()
            },
            {
                'titulo': 'Paso 3: Experimentación: Señal Acústica de Alerta',
                'tipo': 'experimentar',
                'instruccion': 'Emite una señal de advertencia con un tono más grave (440 Hz) de mayor duración (250 ms). Pulsa Control + Enter.',
                'codigo': "import winsound\n\nprint('Señal de advertencia acústica (440 Hz):')\nwinsound.Beep(440, 250)\nprint('Aviso emitido.')\n",
                'pistas': ['winsound.Beep(440, 250) emite un tono más grave.'],
                'validar': lambda s, r, n: ('aviso emitido' in r.lower() or 'notice emitted' in r.lower() or 'warning' in r.lower())
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Función Notificadora Accesible',
                'tipo': 'desafio',
                'instruccion': "Define una función `notificar(tipo_evento, mensaje):` que imprima `f'[{tipo_evento.upper()}]: {mensaje}'`. Si `tipo_evento == 'exito'` debe emitir `winsound.Beep(880, 100)`; si no, `winsound.Beep(440, 100)`. Pruébala con `notificar('exito', 'Datos guardados correctamente')`. Pulsa Control + Enter.",
                'codigo': 'import winsound\n# Define notificar con tono diferenciado y pruébala:\n\n',
                'salida_esperada': '[EXITO]: Datos guardados correctamente',
                'pistas': ["def notificar(tipo_evento, mensaje): print(f'[{tipo_evento.upper()}]: {mensaje}') if tipo_evento == 'exito': winsound.Beep(880, 100) else: winsound.Beep(440, 100) notificar('exito', 'Datos guardados correctamente')"],
                'validar': lambda s, r, n: (('exito' in r.lower() or 'success' in r.lower()) and ('guardados' in r.lower() or 'saved' in r.lower()))
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Beneficio de la Retroalimentación Auditiva',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Piensa en la velocidad y en evitar la fatiga auditiva.'],
                'pregunta': '¿Cuál es la principal ventaja de combinar síntesis de voz con tonos de audio (earcons) en software accesible?',
                'opciones': ['Permite confirmaciones instantáneas de estado sin saturar la atención del usuario con mensajes de voz excesivos.', 'Hace que el procesador gaste menos electricidad.', 'Obliga al usuario a memorizar números matemáticos.'],
                'correcta': 0,
                'explicacion': 'Los earcons o tonos acústicos transmiten confirmación instantánea sin retrasos ni sobrecarga cognitiva de voz.',
                'validar': lambda s, r, n: True
            },
        ]
    },
    {
        'id': 40,
        'titulo': 'Capítulo 40: Proyecto Integrador Final: Creación de un Gestor Accesible de Información y Tareas',
        'resumen': 'Integra todos los conocimientos del curso: arquitectura en capas, POO, persistencia estructurada, control de errores y salida accesible.',
        'pasos': [
            {
                'titulo': 'Paso 1: Fundamento: Arquitectura Limpia por Capas',
                'tipo': 'concepto',
                'instruccion': '¡Felicitaciones por llegar al capítulo culminante de tu formación! Para convertirte en un profesional de software, debes saber cómo ensamblar todas las piezas que has aprendido en una **Arquitectura Limpia** (*Clean Architecture*). Un software profesional nunca mezcla todo en un solo archivo revuelto; se divide en cuatro capas de responsabilidad: 1. Capa de Dominio / Modelo: Clases que representan las entidades del negocio (ejemplo: `Tarea`, con título, fecha y estado). 2. Capa de Persistencia: Lógica encargada de guardar y cargar datos en disco (usando JSON o SQLite) de forma segura con `with open()`. 3. Capa de Servicios / Negocio: Lógica que valida, agrega, elimina y busca elementos evitando duplicados. 4. Capa de Interfaz y Accesibilidad: Comunicación respetuosa con el usuario mediante voz de NVDA y confirmaciones auditivas. Pulsa Enter o Alt + Flecha Derecha para ver el Gestor Integrador funcionando.',
                'codigo': '',
                'pistas': ['Avanza con Enter o Alt + Flecha Derecha.'],
                'validar': lambda s, r, n: True
            },
            {
                'titulo': 'Paso 2: Observación: Inspección del Gestor Accesible',
                'tipo': 'observar',
                'instruccion': 'Examina la arquitectura completa del Gestor. Observa la clase Tarea, el guardado en JSON y el reporte final. Pulsa Control + Enter.',
                'codigo': "import json\n\nclass Tarea:\n    def __init__(self, id_tarea, titulo):\n        self.id_tarea = id_tarea\n        self.titulo = titulo\n        self.completada = False\n\n    def to_dict(self):\n        return {'id': self.id_tarea, 'titulo': self.titulo, 'completada': self.completada}\n\nclass GestorTareas:\n    def __init__(self):\n        self.tareas = []\n\n    def agregar(self, titulo):\n        nueva = Tarea(len(self.tareas) + 1, titulo)\n        self.tareas.append(nueva)\n        return nueva\n\n    def guardar_json(self, ruta):\n        datos = [t.to_dict() for t in self.tareas]\n        with open(ruta, 'w', encoding='utf-8') as f:\n            json.dump(datos, f, indent=2)\n\ngestor = GestorTareas()\ngestor.agregar('Completar curso de Python con NVDA')\ngestor.guardar_json('tareas_final.json')\nprint(f'Sistema integrado activo: {len(gestor.tareas)} tareas gestionadas con éxito.')\n",
                'pistas': ['Pulsa Control + Enter para ejecutar.'],
                'validar': lambda s, r, n: (('sistema' in r.lower() or 'system' in r.lower()) and ('activo' in r.lower() or 'active' in r.lower()))
            },
            {
                'titulo': 'Paso 3: Experimentación: Marcar Tarea como Completada',
                'tipo': 'experimentar',
                'instruccion': 'Añade un método `completar()` en la clase Tarea y verifica que su estado cambie a True. Ejecuta con Control + Enter.',
                'codigo': "class Tarea:\n    def __init__(self, titulo):\n        self.titulo = titulo\n        self.completada = False\n\n    def completar(self):\n        self.completada = True\n\nt = Tarea('Graduación en Python')\nt.completar()\nprint(f'Estado final de la tarea: {t.titulo} -> Completada: {t.completada}')\n",
                'pistas': ['t.completada debe ser True.'],
                'validar': lambda s, r, n: (getattr(n.get('t'), 'completada', False) is True or getattr(n.get('t'), 'completed', False) is True) and 'true' in r.lower()
            },
            {
                'titulo': 'Paso 4: Reto Práctico: Despliegue del Sistema Completo',
                'tipo': 'desafio',
                'instruccion': "Crea una clase `Proyecto` con `__init__(self, nombre)` que inicialice `self.nombre = nombre` y una lista vacía `self.modulos = []`. Añade un método `agregar_modulo(self, mod)` que haga `append`. Instancia `p = Proyecto('Sistema Accesible')`, agrega 'Núcleo Python' y 'Lector NVDA'. Imprime: `print(f'Proyecto {p.nombre} con {len(p.modulos)} módulos activos')`. Pulsa Control + Enter.",
                'codigo': '# Desarrolla la clase Proyecto e integra los módulos:\n\n',
                'salida_esperada': 'Proyecto Sistema Accesible con 2 módulos activos',
                'pistas': ['class Proyecto con __init__ y agregar_modulo. Instancia p, agrega los dos módulos e imprime con la f-string solicitada.'],
                'validar': lambda s, r, n: (('sistema accesible' in r.lower() or 'accessible system' in r.lower() or 'system' in r.lower()) and '2' in r)
            },
            {
                'titulo': 'Paso 5: Verificación Conceptual: Separación de Responsabilidades',
                'tipo': 'quiz',
                'instruccion': 'Selecciona la opción correcta con las flechas y pulsa Enter para comprobar.',
                'codigo': '',
                'pistas': ['Piensa en el principio de modularidad y mantenimiento.'],
                'pregunta': '¿Por qué es fundamental en ingeniería de software profesional separar la lógica de negocio de la interfaz de usuario?',
                'opciones': ['Permite modificar, probar y hacer accesible la interfaz sin romper las reglas de cálculo internas del programa.', 'Hace que el archivo de Python pese exactamente 1 kilobyte.', 'Es un requisito legal exclusivo de los bancos.'],
                'correcta': 0,
                'explicacion': 'La separación de responsabilidades (Separation of Concerns) garantiza mantenibilidad, escalabilidad y accesibilidad a largo plazo.',
                'validar': lambda s, r, n: True
            },
        ]
    },
]

GLOSARIO = {
    'algoritmo': 'Serie ordenada, no ambigua y finita de instrucciones lógicas para resolver un problema determinado.',
    'ambito': 'Región del programa donde un identificador o variable es accesible y visible (local, global o integrado).',
    'and': 'Operador lógico que devuelve True únicamente si todas las condiciones evaluadas son verdaderas.',
    'append': 'Método que añade un nuevo elemento al final de una lista en tiempo constante.',
    'argumento': 'Valor real que se suministra entre los paréntesis de una función al momento de invocarla.',
    'aritmetica': 'Operaciones matemáticas elementales (+, -, *, /, //, %, **) evaluadas bajo reglas de precedencia.',
    'array': 'Estructura contigua de memoria para almacenar elementos secuenciales homogéneos.',
    'ascii': 'Estándar numérico que codifica 128 caracteres del teclado en valores binarios de 7 bits.',
    'asignacion': 'Operación realizada por el signo = que evalúa el operando derecho y lo guarda en la variable izquierda.',
    'asincronia': 'Modelo de ejecución no bloqueante que permite procesar múltiples eventos concurrentes.',
    'atributo': 'Variable vinculada directamente al estado interno de una clase o de una instancia de objeto.',
    'autocompletado': 'Herramienta de desarrollo que sugiere identificadores y palabras clave para reducir errores de tipeo.',
    'binario': 'Sistema de numeración en base 2 utilizado internamente por la CPU, compuesto exclusivamente por ceros y unos.',
    'bit': 'Dígito binario elemental que representa el estado mínimo de información (0 o 1) en un circuito electrónico.',
    'booleano': 'Tipo de dato primitivo que únicamente puede adoptar uno de dos valores: True o False.',
    'braille': 'Sistema de lectoescritura táctil que permite leer código y texto mediante líneas braille electrónicas.',
    'break': 'Sentencia de control que interrumpe e interrumpe de forma inmediata la ejecución de un bucle.',
    'bucle': 'Estructura de control de flujo que repite un bloque de instrucciones múltiples veces.',
    'byte': 'Unidad fundamental de información digital conformada por una secuencia contigua de 8 bits.',
    'call_stack': 'Estructura de pila en memoria que rastrea el orden de llamadas a funciones activas.',
    'capstone': 'Proyecto integrador que consolida todas las competencias y conceptos aprendidos a lo largo de un programa formativo.',
    'casting': 'Conversión explícita de un dato de un tipo a otro utilizando constructores como int(), float() o str().',
    'clase': 'Molde, plantilla o plano de diseño que define la estructura y comportamiento de los objetos.',
    'codigo_fuente': 'Conjunto de instrucciones legibles escritas por un ser humano en un lenguaje de programación.',
    'coleccion': 'Estructura de datos capaz de almacenar múltiples elementos agrupados bajo una misma variable.',
    'comentario': 'Nota en el código fuente que inicia con #, ignorada por el intérprete y destinada a lectura humana.',
    'compilador': 'Programa que traduce todo el código fuente a código binario ejecutable antes de iniciar la ejecución.',
    'concatenacion': 'Operación que une dos o más cadenas de texto consecutivas formando una sola.',
    'condicion': 'Expresión lógica que al evaluarse produce un resultado booleano (True o False).',
    'consola': 'Canal de entrada y salida basado en texto donde los programas emiten mensajes y reciben comandos.',
    'constructor': 'Método especial (__init__) que se ejecuta automáticamente al crear un nuevo objeto para inicializarlo.',
    'context_manager': 'Estructura gestionada por with que garantiza la adquisición y liberación segura de recursos.',
    'continue': 'Sentencia que omite el resto de la iteración actual y salta al inicio de la siguiente vuelta.',
    'cpu': 'Unidad Central de Procesamiento encargada de decodificar y ejecutar las instrucciones de máquina a alta velocidad.',
    'debugging': 'Proceso metódico de diagnosticar, rastrear y corregir fallos o anomalías en el software.',
    'def': 'Palabra reservada fundamental que se utiliza para declarar una nueva función o método en Python.',
    'delimitador': 'Símbolos de apertura y cierre (como comillas, paréntesis, corchetes y llaves) que agrupan código.',
    'desempaquetado': 'Técnica idiomática para asignar los elementos de una tupla o lista a variables individuales simultáneas.',
    'diccionario': 'Colección asociativa de pares clave-valor delimitada por llaves con búsqueda en tiempo constante.',
    'dry': 'Acrónimo de Don’t Repeat Yourself: principio de ingeniería que prohíbe la duplicación de lógica.',
    'earcon': 'Señal acústica o tono de audio breve que comunica un evento de software sin saturar la voz.',
    'elif': 'Abreviatura de else if: cláusula condicional para evaluar alternativas múltiples en cascada.',
    'else': 'Rama alternativa de respaldo que se ejecuta cuando ninguna condición previa fue verdadera.',
    'encapsulamiento': 'Principio de ocultar el estado interno de un objeto para proteger su integridad.',
    'enumerate': 'Función integrada que devuelve en cada iteración un par compuesto por el índice y el elemento.',
    'es_par': 'Algoritmo que utiliza el operador módulo % 2 == 0 para comprobar la divisibilidad exacta por dos.',
    'escape': 'Mecanismo que usa la barra invertida (\\) para otorgar un significado especial a un carácter en una cadena.',
    'estado': 'Conjunto de valores que residen en la memoria RAM en un momento determinado de la ejecución.',
    'excepcion': 'Evento anómalo que ocurre durante la ejecución del programa y que puede ser capturado con try/except.',
    'f_string': 'Cadena literal prefijada con f que interpola variables y expresiones encerradas en llaves {}.',
    'finally': 'Bloque de código dentro de try/except que se ejecuta siempre de forma incondicional.',
    'float': 'Tipo de dato numérico que representa números reales con parte decimal de punto flotante.',
    'for': 'Bucle de repetición definida que recorre los elementos de un iterable o secuencia.',
    'funcion': 'Bloque de instrucciones empaquetado bajo un nombre propio que puede recibir argumentos y devolver valores.',
    'hardware': 'Componentes físicos y electrónicos que integran un sistema informático (CPU, RAM, discos).',
    'identificador': 'Nombre simbólico asignado a una variable, función o clase siguiendo la convención snake_case.',
    'if': 'Sentencia de bifurcación condicional que ejecuta un bloque subordinado si su expresión es verdadera.',
    'inmutabilidad': 'Propiedad de los tipos de datos (como tuplas y cadenas) que no pueden ser modificados tras su creación.',
    'input': 'Función integrada que detiene la ejecución para capturar texto del usuario desde el teclado.',
    'instancia': 'Objeto concreto manifestado en la memoria RAM a partir de la plantilla de una clase.',
    'int': 'Tipo de dato numérico que representa números enteros positivos, negativos o cero.',
    'interprete': 'Motor que lee, analiza y ejecuta el código fuente instrucción por instrucción en tiempo real.',
    'iteracion': 'Acto de repetir una secuencia de instrucciones una vez por cada elemento de una colección.',
    'json': 'JavaScript Object Notation, formato de intercambio de datos textual, ligero y universalmente interoperable.',
    'lector_pantalla': 'Software tiflotécnico como NVDA que convierte la información visual de la pantalla en voz sintética y braille.',
    'len': 'Función integrada que mide y entrega la cantidad total de elementos contenidos en una secuencia.',
    'lista': 'Colección ordenada y mutable de elementos delimitada por corchetes [].',
    'metodo': 'Función que reside y actúa dentro del ámbito de una clase u objeto recibiendo a self.',
    'modulo': 'Archivo con código reutilizable de Python que puede ser importado mediante la sentencia import.',
    'mutabilidad': 'Propiedad de las colecciones (como listas y diccionarios) que permite alterar su contenido en memoria.',
    'name_error': 'Excepción lanzada por Python cuando se intenta utilizar un identificador que no existe en memoria.',
    'none': 'Objeto singular de Python que representa formalmente la ausencia de valor o la nada.',
    'not': 'Operador lógico que invierte el valor de verdad de una proposición booleana.',
    'nvda': 'NonVisual Desktop Access, lector de pantalla libre, accesible y de código abierto para sistemas Windows.',
    'objeto': 'Entidad en memoria RAM que encapsula datos a través de atributos y comportamientos a través de métodos.',
    'open': 'Función integrada que conecta con el sistema de archivos del disco duro para lectura o escritura.',
    'operador': 'Símbolo especial (+, -, ==, and) que ejecuta una operación matemática, lógica o relacional.',
    'or': 'Operador lógico que devuelve True si al menos una de las condiciones conectadas es verdadera.',
    'parametrizada': 'Consulta SQL que utiliza marcadores ? para separar instrucciones de datos previniendo inyección SQL.',
    'parametro': 'Variable formal declarada en el encabezado de una función para recibir datos del exterior.',
    'pass': 'Instrucción nula que sirve como marcador de posición cuando la gramática exige una línea sangrada.',
    'pep8': 'Guía oficial de estilo y buenas prácticas de ingeniería de software para el código Python.',
    'persistencia': 'Capacidad de preservar información más allá de la finalización del proceso en memoria secundaria o disco.',
    'pop': 'Método de listas que extrae y elimina un elemento en un índice especificado o el último por defecto.',
    'precedencia': 'Orden jerárquico estricto en el que se evalúan los operadores matemáticos y lógicos.',
    'print': 'Función fundamental que envía datos hacia la consola de salida estándar para su verbalización.',
    'ram': 'Memoria de Acceso Aleatorio rápida y volátil donde residen los datos activos de los programas.',
    'range': 'Generador inmutable de secuencias aritméticas enteras utilizado en bucles for.',
    'reasignacion': 'Acto de sustituir el valor contenido en una variable por un nuevo dato evaluado.',
    'refactorizacion': 'Proceso de reestructurar y mejorar la calidad interna del código sin alterar su comportamiento externo.',
    'relacional': 'Operadores que comparan magnitudes y producen un valor booleano (==, !=, <, >, <=, >=).',
    'return': 'Sentencia que concluye una función y devuelve un dato a la memoria del llamador.',
    'salida_estandar': 'Canal de comunicación (stdout) donde el software emite sus reportes y resultados textuales.',
    'sangria': 'Espacios en blanco al inicio de la línea (4 espacios PEP 8) que definen la estructura de bloques.',
    'self': 'Referencia convencional que un objeto tiene de su propia identidad dentro de sus métodos.',
    'sentencia': 'Instrucción completa de código que el intérprete de Python puede procesar y ejecutar.',
    'serializacion': 'Proceso de convertir estructuras complejas de la memoria en secuencias de bytes o texto (JSON).',
    'short_circuit': 'Optimización lógica donde Python detiene la evaluación al conocer anticipadamente el resultado.',
    'sintaxis': 'Conjunto de reglas gramaticales estrictas que determinan cómo deben escribirse las instrucciones.',
    'sistema_operativo': 'Software fundamental que administra los recursos de hardware y brinda servicios a las aplicaciones.',
    'snake_case': 'Convención de nombres en minúsculas con palabras unidas por guiones bajos (nombre_usuario).',
    'software': 'Conjunto de programas y reglas lógicas que indican al hardware cómo operar.',
    'sqlite': 'Motor de base de datos relacional ligero y autónomo embebido directamente en la biblioteca estándar de Python.',
    'sqlite3': 'Motor de base de datos relacional SQL embebido y autónomo incluido en la biblioteca estándar de Python.',
    'ssl': 'Capa de sockets seguros para comunicaciones cifradas a través de redes informáticas.',
    'str': 'Tipo de dato primitivo que representa cadenas de caracteres alfanuméricos entre comillas.',
    'syntax_error': 'Fallo gramatical en el código que impide al intérprete iniciar la ejecución del programa.',
    'tabla_verdad': 'Esquema algebraico que resume todos los resultados posibles de las operaciones lógicas.',
    'tiflotecnologia': 'Ingeniería enfocada en diseñar y desarrollar tecnologías accesibles para personas con discapacidad visual.',
    'timeout': 'Límite de tiempo máximo concedido a una operación para completarse antes de forzar su detención.',
    'traceback': 'Informe técnico que detalla la pila de llamadas y la línea exacta donde ocurrió una excepción.',
    'true_false': 'Los dos únicos valores booleanos admitidos por el procesador para representar la verdad lógica.',
    'try_except': 'Estructura de control de errores diseñada para construir software resiliente y tolerante a fallos.',
    'tupla': 'Colección ordenada e inmutable de elementos delimitada por paréntesis ().',
    'type_error': 'Excepción arrojada cuando se intenta aplicar una operación sobre un tipo de dato incompatible.',
    'unicode': 'Estándar internacional que asigna un identificador numérico único a cada carácter de todos los idiomas.',
    'unittest': 'Módulo de la biblioteca estándar para escribir pruebas automáticas que certifiquen el software.',
    'variable': 'Nombre simbólico que apunta a una casilla de memoria RAM donde reside un dato modificable.',
    'while': 'Bucle de repetición condicional que ejecuta su cuerpo mientras una condición lógica sea verdadera.',
    'winsound': 'Módulo nativo de Windows en Python para emitir tonos acústicos y pitidos de frecuencias precisas.',
    'with': 'Sentencia que gestiona administradores de contexto garantizando la liberación automática de recursos.',
    'zen_python': 'Colección de 19 principios de diseño e ingeniería que definen la filosofía del lenguaje Python.',
}

# Integración de traducciones pedagógicas en inglés
try:
    from .curriculum_translations import APLICAR_TRADUCCIONES, GLOSARIO_EN, obtener_glosario
    APLICAR_TRADUCCIONES(CURRICULUM)
except (ImportError, ValueError):
    try:
        import os, sys
        _cur_dir = os.path.dirname(__file__)
        if _cur_dir and _cur_dir not in sys.path:
            sys.path.insert(0, _cur_dir)
        from curriculum_translations import APLICAR_TRADUCCIONES, GLOSARIO_EN, obtener_glosario
        APLICAR_TRADUCCIONES(CURRICULUM)
    except Exception:
        pass
except Exception:
    pass
