# -*- coding: utf-8 -*-
# Módulo: data.py

# Base de datos de 21 Capítulos unificada y secuencial basada en la documentación oficial
LECCIONES = [
    {
        "titulo": "Capítulo 1: Fundamentos de Algoritmia y Flujo de Ejecución Lineal",
        "teoria": "La programación se basa en la construcción de algoritmos: secuencias lógicas, finitas y ordenadas de instrucciones encaminadas a resolver un problema o procesar datos. Python es un lenguaje que, por defecto, ejecuta las instrucciones de manera estrictamente secuencial; esto significa que lee y procesa el código fuente de arriba hacia abajo y de izquierda a derecha. Mantener el orden correcto de las sentencias es indispensable, ya que alterar la secuencia lógica impide que la computadora procese los datos de forma correcta, rompiendo la coherencia del algoritmo.",
        "practica": "🎯 EL DESAFÍO:\nEl editor contiene un script diseñado para inicializar un servicio de software, pero las sentencias se encuentran desordenadas de forma ilógica. Tu objetivo es reorganizar las líneas de código para que sigan el flujo lineal requerido en los sistemas de producción: primero se debe iniciar la conexión con el servidor, en segundo lugar autenticar las credenciales de seguridad y, finalmente, desplegar el panel de usuario.",
        "codigo": "print(\"Paso 3: Panel de usuario desplegado correctamente.\")\nprint(\"Paso 1: Iniciando conexion con el servidor local.\")\nprint(\"Paso 2: Autenticando credenciales de acceso seguro.\")"
    },
    {
        "titulo": "Capítulo 2: El Intérprete de Python y la Salida Estándar (print)",
        "teoria": "Python es un lenguaje interpretado. Esto significa que un programa especializado llamado \"intérprete\" procesa el código fuente línea por línea en tiempo de ejecución, traduciéndolo inmediatamente a instrucciones de bajo nivel que el procesador puede comprender. Para interactuar con el sistema, el lenguaje permite que el usuario reciba cadenas de texto estructuradas. La función print() es la herramienta nativa para enviar información hacia la salida estándar del sistema (sys.stdout). Un error de escritura en el nombre de la función impedirá la interpretación del script, provocando que el sistema se interrumpa y lance una excepción de nombre.",
        "practica": "🎯 EL DESAFÍO:\nEl intérprete ha detenido la ejecución del programa y ha generado una excepción de nombre (NameError) debido a que el programador anterior escribió la función de salida estándar de manera incorrecta. Corrige la sintaxis escribiendo el nombre nativo de la función de forma adecuada y ejecuta el script para validar la salida.",
        "codigo": "prnt(\"Entorno virtual inicializado bajo codificacion estandar.\")"
    },
    {
        "titulo": "Capítulo 3: Espacios de Almacenamiento en Memoria (Variables)",
        "teoria": "Una variable es un identificador o etiqueta de texto que apunta a una dirección o espacio específico dentro de la memoria de la computadora, permitiendo almacenar un dato de forma temporal durante la ejecución del programa. En Python, la declaración e inicialización de una variable se realiza mediante el operador de asignación, representado por el signo igual (=). Este operador toma el valor evaluado a su derecha y guarda su referencia de memoria en la dirección apuntada por el identificador de la izquierda.",
        "practica": "🎯 EL DESAFÍO:\nDispones de un script con una variable denominada usuario_activo cuyo valor de referencia actual en memoria es la cadena \"Invitado\". Tu objetivo es actualizar el estado de la sesión modificando el valor asignado por tu propio nombre de usuario (escrito entre comillas). Al ejecutar el código, la terminal procesará la nueva referencia de memoria asignada.",
        "codigo": "usuario_activo = \"Invitado\"\nprint(\"Conexion exitosa. Bienvenido al sistema: \" + usuario_activo)"
    },
    {
        "titulo": "Capítulo 4: Tipos de Datos Primitivos: Cadenas (str) e Enteros (int)",
        "teoria": "Toda la información procesada en Python está clasificada en tipos de datos específicos que determinan las operaciones permitidas con ellos. Dos de los tipos de datos primitivos más importantes son las cadenas de texto (str) y los números enteros (int). Las cadenas representan secuencias de caracteres alfanuméricos literales y se definen obligatoriamente delimitadas por comillas (simples o dobles). Los enteros representan valores numéricos exactos, positivos o negativos, y se escriben directamente sin delimitadores. Intentar mezclar estos tipos de datos en operaciones aritméticas directas viola las reglas de tipado estricto de Python, obligando al intérprete a lanzar una excepción de incompatibilidad de tipos (TypeError).",
        "practica": "🎯 EL DESAFÍO:\nEl script intenta consolidar un identificador de registro sumando una variable de tipo entero y un literal que se encuentra atrapado como cadena de texto (10 + \"20\"), provocando el bloqueo del programa por incompatibilidad de tipos. Elimina las comillas que rodean al número 20 para que Python pueda procesar ambas variables como enteros (int) y ejecutar la operación matemática de forma correcta.",
        "codigo": "base_datos_id = 10\nregistro_id = \"20\"\n# Corrige la incompatibilidad de tipos en la siguiente linea\nidentificador_final = base_datos_id + registro_id\nprint(\"Identificador de registro consolidado:\", identificador_final)"
    },
    {
        "titulo": "Capítulo 5: Estructuración de Bloques mediante Indentación (PEP 8)",
        "teoria": "A diferencia de otros lenguajes de programación que utilizan llaves ({}) o palabras clave para delimitar bloques de instrucciones, Python utiliza espacios en blanco al inicio de las líneas, un conceptó técnico denominado indentación. De acuerdo con la guía de estilo oficial de la comunidad de Python (PEP 8), cada nivel de indentación estructural debe estar compuesto por exactamente 4 espacios físicos (equivalentes a una tabulación en el editor de este complemento). La indentación es un requerimiento sintáctico estricto: cualquier sentencia que pertenezca a un bloque jerárquico subordinado (como las estructuras condicionales o bucles) debe estar alineada de forma precisa, o de lo contrario el intérprete arrojará una excepción de indentación (IndentationError).",
        "practica": "🎯 EL DESAFÍO:\nSe ha inicializado una bandera lógica de control configurada en verdadero (True). La instrucción encargada de emitir el reporte de validación se encuentra fuera de su bloque condicional debido a que está alineada al margen izquierdo (0 espacios). Navega hasta el inicio de la línea 3 e introduce una tabulación (4 espacios físicos) para solucionar el error sintáctico e integrar la sentencia al bloque del condicional if.",
        "codigo": "sistema_verificado = True\nif sistema_verificado:\nprint(\"Estado del sistema: Operativo y validado.\")"
    },
    {
        "titulo": "Capítulo 6: Conversión de tipos (Type Casting)",
        "teoria": "La documentación oficial de Python establece que este es un lenguaje de tipado dinámico pero fuertemente tipado. Esto significa que una variable puede cambiar de tipo, pero Python no realizará jamás conversiones implícitas que pongan en riesgo la integridad de los datos (como sumar un texto y un número). Para ello, existen funciones nativas de conversión: int() para convertir a números enteros, float() para números con decimales, y str() para transformar cualquier dato en texto. Aprender a moldear el tipo de los datos es un paso esencial antes de realizar cualquier cálculo matemático.",
        "practica": "🎯 EL DESAFÍO:\nTienes un precio almacenado como texto (\"19.99\") y una cantidad como texto (\"3\"). El código intenta multiplicarlos, pero Python arroja un error TypeError al no poder realizar operaciones aritméticas entre cadenas de texto. Modifica la línea del total aplicando float() a precio_texto e int() a cantidad_texto para realizar la multiplicación de forma correcta.",
        "codigo": "precio_texto = \"19.99\"\ncantidad_texto = \"3\"\n# Realiza las conversiones correctas abajo aplicando float e int\ntotal = precio_texto * cantidad_texto\nprint(\"El total de la compra es:\", total)"
    },
    {
        "titulo": "Capítulo 7: Prioridad de Operadores Aritméticos",
        "teoria": "En Python, las operaciones matemáticas se evalúan siguiendo reglas de precedencia estrictas (orden de evaluación), tal como en el álgebra matemática. La prioridad PEMDAS: primero los paréntesis (), luego los exponentes **, seguidos de la multiplicación *, división /, división entera //, módulo % (residuo), y finalmente la suma + y resta -. Cuando los operadores tienen la misma prioridad, se evalúan de izquierda a derecha. Forzar la prioridad usando paréntesis es indispensable para estructurar fórmulas matemáticas fiables.",
        "practica": "🎯 EL DESAFÍO:\nSe desea calcular el promedio final de tres exámenes con notas de 8.0, 9.5 y 7.1. El programa actual no utiliza paréntesis, lo que causa que Python evalúe primero la división (7.1 / 3) y luego sume las demás notas, arrojando un resultado erróneo. Corrige la precedencia agrupando las notas entre paréntesis antes de dividirlas por 3.",
        "codigo": "nota1 = 8.0\nnota2 = 9.5\nnota3 = 7.1\n# Corrige la siguiente linea agregando los parentesis correctos\npromedio = nota1 + nota2 + nota3 / 3\nprint(\"El promedio real es:\", promedio)"
    },
    {
        "titulo": "Capítulo 8: Operadores de Comparación de Datos",
        "teoria": "Los operadores de comparación de datos evalúan la relación entre dos valores y devuelven un valor booleano (True o False). De acuerdo con las especificaciones estándar de Python, disponemos de igualdad (==), desigualdad o diferencia (!=), mayor que (>), menor que (<), mayor o igual (>=) y menor o igual (<=). Un error común de sintaxis es confundir el operador de asignación (=), usado para guardar información en una variable, con el operador de comparación (==), utilizado para evaluar si dos valores son equivalentes.",
        "practica": "🎯 EL DESAFÍO:\nEl código base simula una pantalla de inicio de sesión que compara una clave ingresada con una clave guardada en el sistema. Sin embargo, el programador anterior usó el signo de asignación '=' en lugar del operador de comparación '==' dentro del condicional 'if'. Corrige el operador para que el sistema valide el acceso correctamente.",
        "codigo": "clave_guardada = \"secreto123\"\nclave_ingresada = \"secreto123\"\n# Cambia la asignacion por comparacion en la linea de abajo\nif clave_ingresada = clave_guardada:\n    print(\"Acceso concedido\")"
    },
    {
        "titulo": "Capítulo 9: Operadores Lógicos (and, or, not)",
        "teoria": "Los operadores lógicos permiten enlazar múltiples condiciones booleanas para tomar decisiones complejas. Python implementa tres operadores fundamentales: 'and' (devuelve True solo si ambas condiciones son verdaderas), 'or' (devuelve True si al menos una condición es verdadera) y 'not' (invierte el estado booleano de la expresión). Python realiza una evaluación de cortocircuito (short-circuit), lo que significa que detiene el análisis del código en el momento en que el resultado final está matemáticamente garantizado, aumentando la velocidad de ejecución.",
        "practica": "🎯 EL DESAFÍO:\nQueremos autorizar la descarga de un archivo. La regla oficial dice que el usuario puede descargarlo si está conectado (conectado = True) Y además cumple alguna de estas condiciones: tiene saldo positivo (saldo_positivo = True) O es un administrador (es_admin = True). Utiliza los operadores 'and' y 'or' con paréntesis de agrupación para completar la lógica de la variable 'puede_descargar'.",
        "codigo": "conectado = True\nsaldo_positivo = False\nes_admin = True\n# Falta unir las variables con and y or en la siguiente linea de forma correcta\npuede_descargar = conectado # Completa aqui\nprint(\"Permitir descarga:\", puede_descargar)"
    },
    {
        "titulo": "Capítulo 10: Decisiones Múltiples (La cláusula Elif)",
        "teoria": "En flujos lógicos con más de dos alternativas excluyentes, la documentación oficial de Python introduce la cláusula 'elif' (else if). Su propósito es evitar que anidemos bloques 'if' y 'else' infinitamente hacia la derecha de la pantalla, manteniendo la indentación limpia. Python evalúa la estructura de arriba hacia abajo: en el instante en que encuentra una condición verdadera, ejecuta su bloque de código asociado e ignora por completo todas las demás cláusulas inferiores.",
        "practica": "🎯 EL DESAFÍO:\nTienes una calificación de examen de 85 puntos. El sistema debe imprimir 'Excelente' si la nota es 90 o más, 'Aceptable' si es 80 o más, y 'Reprobado' en cualquier otro caso. El código actual usa condicionales independientes incorrectos que se solapan. Modifícalo reemplazando el segundo 'if' por un 'elif' para que la lógica funcione correctamente de manera excluyente.",
        "codigo": "nota = 85\nif nota >= 90:\n    print(\"Calificacion: Excelente\")\n# Reemplaza la siguiente linea por un elif para optimizar la toma de decisiones\nif nota >= 80:\n    print(\"Calificacion: Aceptable\")\nelse:\n    print(\"Calificacion: Reprobado\")"
    },
    {
        "titulo": "Capítulo 11: Secuencias Ordenadas - Introducción a las Listas",
        "teoria": "Las listas son una de las estructuras de datos más potentes y versátiles de Python. Representan secuencias ordenadas y mutables de elementos separados por comas y delimitados por corchetes []. Cada elemento de una lista tiene una posición numerada llamada índice. La documentación oficial explica que el índice de Python siempre empieza en 0 para el primer elemento y aumenta de izquierda a derecha. También cuenta con soporte para indexación negativa: el índice -1 representa de forma directa al último elemento de la lista, -2 al penúltimo, facilitando el acceso inverso.",
        "practica": "🎯 EL DESAFÍO:\nDispones de una lista que contiene las regiones de servidores activos de la plataforma. Tu desafío es extraer la primera región utilizando indexación positiva (índice 0) y la última región utilizando indexación negativa (índice -1) para asignarlas a las variables correspondientes e imprimirlas.",
        "codigo": "servidores = [\"us-east\", \"eu-central\", \"ap-south\", \"sa-east\"]\n# Extrae el primero y el ultimo usando servidores[indice]\nprimero = servidores[0]\nultimo = servidores[0] # Modifica este indice por uno negativo\nprint(\"Primero:\", primero, \"| Ultimo:\", ultimo)"
    },
    {
        "titulo": "Capítulo 12: Mutabilidad de Listas y Métodos Esenciales",
        "teoria": "A diferencia de los números y las cadenas de texto, las listas son objetos mutables. Esto significa que podemos modificar su tamaño y elementos directamente en la memoria sin crear un objeto nuevo. La documentación oficial detalla métodos clave para manipularlas: '.append(valor)' agrega un elemento al final de la lista, '.insert(indice, valor)' lo inserta en una posición determinada, y '.remove(valor)' elimina la primera aparición del elemento especificado. Aprender a manipular listas es fundamental para gestionar colecciones de datos dinámicas.",
        "practica": "🎯 EL DESAFÍO:\nTienes una lista que representa tu lista de tareas pendientes para hoy. El programador olvidó agregar la tarea \"revisar codigo\" al final de la lista y dejó el método incompleto. Completa la llamada al método '.append()' de forma correcta pasándole como argumento la cadena \"revisar codigo\" y ejecuta el programa.",
        "codigo": "tareas = [\"estudiar\", \"desayunar\"]\n# Agrega 'revisar codigo' a la lista tareas usando .append()\ntareas.append # Completa la llamada al metodo de forma correcta\nprint(\"Lista de tareas actualizada:\", tareas)"
    },
    {
        "titulo": "Capítulo 13: La Técnica de Slicing (Rebanado de Listas)",
        "teoria": "La documentación oficial de Python especifica una herramienta sumamente versátil para trabajar con secuencias llamada 'Slicing' (rebanado). Utilizando la sintaxis 'lista[inicio:fin:paso]', podemos extraer una sublista que va desde el índice 'inicio' hasta el índice 'fin' (pero sin incluir la posición final). Si omites el parámetro 'inicio', Python asume el inicio de la lista; si omites 'fin', asume el término. El parámetro 'paso' determina el incremento de salto entre los índices (por ejemplo, un paso de 2 tomará un elemento de por medio).",
        "practica": "🎯 EL DESAFÍO:\nTienes una lista que registra varias transacciones monetarias. Tu misión es extraer las tres transacciones intermedias (desde la posición con índice 1 hasta el índice 3 inclusive, es decir, rango de índice 1 a 4 sin incluir el 4) utilizando el rebanado de listas. Reemplaza los índices en la sintaxis de corte.",
        "codigo": "transacciones = [100.5, 250.0, 15.0, 80.2, 300.0]\n# Extrae del indice 1 al 4 (sin incluir el 4) usando transacciones[inicio:fin]\ncentro = transacciones[0:0] # Reemplaza los ceros por indices correctos\nprint(\"Transacciones seleccionadas:\", centro)"
    },
    {
        "titulo": "Capítulo 14: Estructuras Estables e Inmutables - Las Tuplas",
        "teoria": "Las tuplas son secuencias ordenadas de elementos muy similares a las listas, pero con una diferencia crítica definida en la documentación de Python: son inmutables. Se definen utilizando paréntesis () en lugar de corchetes []. Una vez declarada una tupla, no es posible añadir, eliminar ni modificar sus elementos. Esta inmutabilidad ofrece dos grandes ventajas: previene la alteración accidental de configuraciones estructurales del programa (como coordenadas geográficas, puertos o claves del sistema) y proporciona una mayor velocidad de ejecución del software.",
        "practica": "🎯 EL DESAFÍO:\nEl código base contiene una variable llamada 'coordenadas' que representa la ubicación del servidor principal. Actualmente está declarada como una lista mutable. Tu desafío es reescribir la declaración convirtiéndola en una tupla inmutable (cambiando los corchetes por paréntesis) de forma que su estructura quede protegida contra cambios accidentales.",
        "codigo": "# Convierte esta lista a una tupla inmutable reemplazando los corchetes por parentesis\ncoordenadas = [4.71, -74.07]\nprint(\"Coordenadas guardadas:\", coordenadas)"
    },
    {
        "titulo": "Capítulo 15: Estructuras Asociativas - Los Diccionarios",
        "teoria": "Los diccionarios en Python son colecciones de parejas clave-valor delimitadas por llaves {}. A diferencia de las secuencias indexadas por números, los diccionarios permiten indexar datos de forma semántica mediante claves inmutables (usualmente cadenas de texto). La sintaxis oficial para acceder a un valor es escribir el nombre del diccionario seguido de la clave entre corchetes, por ejemplo: 'diccionario[\"clave\"]'. Es la estructura ideal para almacenar registros y configuraciones estructuradas con alta velocidad de lectura.",
        "practica": "🎯 EL DESAFÍO:\nTienes un diccionario que almacena la información de configuración de un estudiante. Sin embargo, falta completar el valor de la nueva clave \"lenguaje\" con el texto \"Python\". Completa la línea de asignación para registrar el valor de la clave en el diccionario e imprime el registro.",
        "codigo": "estudiante = {\"nombre\": \"Kevin\", \"nivel\": \"Basico\"}\n# Agrega la clave 'lenguaje' con el valor 'Python'\nestudiante[\"lenguaje\"] = \"\" # Completa el valor correcto entre las comillas\nprint(\"Registro del estudiante:\", estudiante)"
    },
    {
        "titulo": "Capítulo 16: Colecciones Únicas y Sin Duplicados - Los Conjuntos",
        "teoria": "Un conjunto o 'set' es una colección desordenada de elementos únicos en Python. Se define mediante llaves {} (sin pares clave-valor) o mediante la función set(). La documentación oficial de Python explica que los conjuntos no permiten duplicados; cualquier elemento repetido será ignorado automáticamente al crearse o insertarse. Los sets son idóneos para tareas de filtrado de datos repetidos y para realizar operaciones matemáticas tradicionales como uniones, intersecciones y diferencias lógicas.",
        "practica": "🎯 EL DESAFÍO:\nTienes una lista que registra accesos al sistema, pero contiene direcciones IP que se repiten constantemente. Tu desafío es filtrar todas las IP repetidas para quedarte solo con los accesos únicos. Hazlo convirtiendo la lista 'accesos_duplicados' en un conjunto único mediante el uso de la función de conversión 'set()'.",
        "codigo": "accesos_duplicados = [\"192.168.1.1\", \"10.0.0.5\", \"192.168.1.1\", \"172.16.0.2\", \"10.0.0.5\"]\n# Convierte la lista anterior en un conjunto unico usando set(lista)\naccesos_unicos = accesos_duplicados # Reemplaza por la conversion set()\nprint(\"Accesos unicos:\", accesos_unicos)"
    },
    {
        "titulo": "Capítulo 17: Automatización mediante el Ciclo FOR",
        "teoria": "La iteración permite automatizar tareas repetitivas de forma eficiente. El bucle 'for' es la estructura predilecta en Python para recorrer secuencialmente todos los elementos de un objeto iterable (como listas, tuplas o rangos). En cada vuelta del ciclo, Python toma un elemento de la colección y lo asigna automáticamente a una variable temporal de control que nosotros definimos. El ciclo se ejecuta de forma controlada y finaliza de manera limpia una vez que se han procesado todos los elementos del iterable.",
        "practica": "🎯 EL DESAFÍO:\nSe dispone de una lista con los precios de varios productos. Queremos calcular y mostrar el precio con un descuento del 10% aplicado a cada uno. El ciclo 'for' está incompleto porque le falta declarar la lista sobre la cual iterar. Completa la línea del bucle agregando la palabra reservada 'in' seguida de la variable 'precios'.",
        "codigo": "precios = [100, 250, 50, 400]\n# Completa la declaracion del ciclo for para iterar sobre precios\nfor precio in :\n    con_descuento = precio * 0.9\n    print(\"Precio con descuento:\", con_descuento)"
    },
    {
        "titulo": "Capítulo 18: Iteraciones Condicionales - El Ciclo WHILE",
        "teoria": "A diferencia del bucle 'for', el bucle 'while' repite un bloque de código continuamente mientras una condición lógica inicial se evalúe como verdadera (True). Según la documentación de Python, es indispensable que dentro del bloque de código del 'while' se altere la variable evaluada en la condición de entrada. Si la condición nunca cambia a falsa (False), el bucle se ejecutará infinitamente, consumiendo la CPU y congelando la aplicación.",
        "practica": "🎯 EL DESAFÍO:\nEl código base emula el progreso de descarga de un archivo. El programa se encuentra atrapado en un bucle infinito porque el programador anterior olvidó actualizar el porcentaje dentro del bloque de código. Corrige el programa incrementando la variable 'porcentaje' de 20 en 20 ('porcentaje += 20') en la línea señalada para que el ciclo se detenga al llegar a 100.",
        "codigo": "porcentaje = 0\nwhile porcentaje <= 100:\n    print(\"Descargando: \" + str(porcentaje) + \"%\")\n    # Incrementa aqui la variable porcentaje de 20 en 20 para evitar el ciclo infinito\n    \nprint(\"¡Descarga completada!\")"
    },
    {
        "titulo": "Capítulo 19: Estructuración y Modularidad - Las Funciones",
        "teoria": "Las funciones son bloques de código de propósito estructurado y reutilizable creados para realizar una tarea concreta. Se declaran utilizando la palabra clave 'def' seguida del nombre de la función, paréntesis con parámetros de entrada (opcionales) y dos puntos. La documentación oficial destaca que para que una función devuelva un resultado procesado al código exterior, se debe utilizar explícitamente la palabra reservada 'return'. Las funciones evitan la duplicidad de código y mejoran sustancialmente el mantenimiento del software.",
        "practica": "🎯 EL DESAFÍO:\nEscribe una función llamada 'calcular_impuesto' que tome un parámetro llamado 'monto' y devuelva el 19% de ese monto (monto * 0.19) utilizando la palabra clave 'return'. Completa el cuerpo de la función para que el cálculo se devuelva correctamente e imprima el resultado.",
        "codigo": "# Define la funcion calcular_impuesto que retorne monto * 0.19\ndef calcular_impuesto(monto):\n    return\n\n# Realiza la llamada y comprueba el resultado\nresultado = calcular_impuesto(1000)\nprint(\"El impuesto de 1000 es:\", resultado)"
    },
    {
        "titulo": "Capítulo 20: Mitigación de Errores - Bloques Try y Except",
        "teoria": "Durante la ejecución de un programa pueden ocurrir fallos imprevistos debido a datos externos (como intentar dividir por cero o convertir letras a enteros), provocando que Python lance una excepción y detenga el programa bruscamente. Para prevenir esto, la documentación oficial detalla la estructura 'try' y 'except'. El bloque 'try' alberga el código que corre riesgo de fallar, y el bloque 'except' captura la excepción para ejecutar un plan de contingencia seguro, evitando la caída del software.",
        "practica": "🎯 EL DESAFÍO:\nTienes un script que intenta convertir una cadena de texto no numérica ('veinte') en un número entero, lo que provocará una caída por ValueError. Tu desafío es envolver la conversión en un bloque 'try' y añadir una cláusula 'except ValueError:' para capturar el fallo de forma limpia y mostrar un aviso informativo en pantalla.",
        "codigo": "edad_texto = \"veinte\" # Texto invalido para conversion numerica\n# Envuelve las lineas de abajo en una estructura try y except ValueError\nedad = int(edad_texto)\nprint(\"La edad procesada es:\", edad)"
    },
    {
        "titulo": "Capítulo 21: Módulos y la Biblioteca Estándar de Python",
        "teoria": "Python promueve la filosofía de 'baterías incluidas' (batteries included), lo que significa que incluye una enorme biblioteca de módulos estándar listos para usar sin descargar nada de internet. Para acceder a las herramientas de un módulo estándar, se utiliza la instrucción 'import'. Módulos como 'math' proveen funciones matemáticas avanzadas (raíces, logaritmos, trigonometría), mientras que 'random' permite la generación de números aleatorios y simulaciones lógicas.",
        "practica": "🎯 EL DESAFÍO:\nQueremos calcular la raíz cuadrada exacta del número 100. Tu desafío es importar la librería estándar 'math' al inicio del programa y luego utilizar el método matemático integrado 'math.sqrt(100)' asignándole el resultado a la variable 'raiz' para poder imprimirlo en pantalla.",
        "codigo": "# Importa la libreria math oficial de Python\n\n# Calculates la raiz de 100 usando math.sqrt()\nraiz = 0 \nprint(\"La raiz cuadrada de 100 es:\", raiz)"
    }
]

PLANTILLAS_BASE = {
    1: "print('Paso 1: Iniciando conexion con el servidor local.')\nprint('Paso 2: Autenticando credenciales de acceso seguro.')\nprint('Paso 3: Panel de usuario desplegado correctamente.')",
    2: "print('La clave secreta es Accesibilidad')",
    3: "usuario_activo = 'Kevin'\nprint('Conexion exitosa. Bienvenido al sistema: ' + usuario_activo)",
    4: "base_datos_id = 10\nregistro_id = 20\nidentificador_final = base_datos_id + registro_id\nprint('Identificador de registro consolidado:', identificador_final)",
    5: "sistema_verificado = True\nif sistema_verificado:\n    print('Estado del sistema: Operativo y validado.')",
    6: "precio_texto = '19.99'\ncantidad_texto = '3'\ntotal = float(precio_texto) * int(cantidad_texto)\nprint('El total de la compra es:', total)",
    7: "nota1 = 8.0\nnota2 = 9.5\nnota3 = 7.1\npromedio = (nota1 + nota2 + nota3) / 3\nprint('El promedio real es:', promedio)",
    8: "clave_guardada = 'secreto123'\nclave_ingresada = 'secreto123'\nif clave_ingresada == clave_guardada:\n    print('Acceso concedido')",
    9: "conectado = True\nsaldo_positivo = False\nes_admin = True\npuede_descargar = conectado and (saldo_positivo or es_admin)\nprint('Permitir descarga:', puede_descargar)",
    10: "nota = 85\nif nota >= 90:\n    print('Calificacion: Excelente')\nelif nota >= 80:\n    print('Calificacion: Aceptable')\nelse:\n    print('Calificacion: Reprobado')",
    11: "servidores = ['us-east', 'eu-central', 'ap-south', 'sa-east']\nprimero = servidores[0]\nultimo = servidores[-1]\nprint('Primero:', primero, '| Ultimo:', ultimo)",
    12: "tareas = ['estudiar', 'desayunar']\ntareas.append('revisar codigo')\nprint('Lista de tareas actualizada:', tareas)",
    13: "transacciones = [100.5, 250.0, 15.0, 80.2, 300.0]\ncentro = transacciones[1:4]\nprint('Transacciones seleccionadas:', centro)",
    14: "coordenadas = (4.71, -74.07)\nprint('Coordenadas guardadas:', coordenadas)",
    15: "estudiante = {'nombre': 'Kevin', 'nivel': 'Basico'}\nestudiante['lenguaje'] = 'Python'\nprint('Registro del estudiante:', estudiante)",
    16: "accesos_duplicados = ['192.168.1.1', '10.0.0.5', '192.168.1.1', '172.16.0.2', '10.0.0.5']\naccesos_unicos = set(accesos_duplicados)\nprint('Accesos unicos:', accesos_unicos)",
    17: "precios = [100, 250, 50, 400]\nfor precio in precios:\n    con_descuento = precio * 0.9\n    print('Precio con descuento:', con_descuento)",
    18: "porcentaje = 0\nwhile porcentaje <= 100:\n    print('Descargando: ' + str(porcentaje) + '%')\n    porcentaje += 20\nprint('¡Descarga completada!')",
    19: "def calcular_impuesto(monto):\n    return monto * 0.19\n\nresultado = calcular_impuesto(1000)\nprint('El impuesto de 1000 es:', resultado)",
    20: "edad_texto = 'veinte'\ntry:\n    edad = int(edad_texto)\n    print('La edad procesada es:', edad)\nexcept ValueError:\n    print('Error: El texto ingresado no es un numero valido.')",
    21: "import math\nraiz = math.sqrt(100)\nprint('La raiz cuadrada de 100 es:', raiz)"
}

GLOSARIO_RAPIDO = {
    "print": "print(): Función incorporada que envía representaciones de texto hacia la salida estándar (sys.stdout).",
    "if": "if: Declaración de control de flujo que evalúa un bloque si su condición resulta verdadera (True).",
    "else": "else: Bloque alternativo en una instrucción condicional si todas las condiciones anteriores son falsas (False).",
    "elif": "elif: Abreviatura de 'else if'. Permite evaluar de manera consecutiva múltiples condiciones lógicas excluyentes.",
    "for": "for: Declaración de control de flujo que realiza iteraciones sobre una secuencia (listas, tuplas o rangos).",
    "while": "while: Declaración de control de flujo que ejecuta un bloque de instrucciones repetidamente mientras una condición sea verdadera.",
    "def": "def: Palabra clave utilizada para declarar e inicializar funciones estructuradas de código.",
    "try": "try: Delimita un bloque protector donde se controlará la aparición de excepciones en tiempo de ejecución.",
    "except": "except: Captura y gestiona un tipo específico de excepción detectada dentro del bloque protector try.",
    "finally": "finally: Bloque que se ejecuta de forma obligatoria tras un bloque try/except, independientemente de si ocurrió una excepción o no.",
    "import": "import: Instrucción utilizada para enlazar y cargar módulos o bibliotecas en el espacio de nombres de tu script.",
    "return": "return: Instrucción de finalización que detiene una función y devuelve un valor de retorno al llamador.",
    "class": "class: Instrucción usada para declarar la estructura y el comportamiento de un molde de objetos (Programación Orientada a Objetos).",
    "len": "len(): Función incorporada que retorna el número de elementos contenidos en una secuencia u objeto contenedor.",
    "range": "range(): Generador incorporado que produce una secuencia inmutable de números enteros ordenados.",
    "int": "int: Tipo de dato primitivo que representa números enteros sin parte decimal.",
    "float": "float: Tipo de dato primitivo que representa números de punto flotante de precisión doble (con decimales).",
    "str": "str: Tipo de dato primitivo que representa secuencias ordenadas de caracteres de texto (inmutable).",
    "bool": "bool: Tipo de dato primitivo booleano que solo puede admitir valores lógicos True o False.",
    "list": "list: Estructura de datos que representa una colección ordenada, indexada y mutable de elementos variados.",
    "tuple": "tuple: Estructura de datos que representa una secuencia ordenada, indexada e inmutable de elementos variados.",
    "dict": "dict: Colección asociativa mutable y mapeada mediante parejas de claves inmutables y valores libres.",
    "set": "set: Colección de datos mutable, desordenada y compuesta estrictamente por elementos únicos sin duplicados.",
    "and": "and: Operador lógico de conjunción que retorna verdadero si y solo si ambos operandos son verdaderos.",
    "or": "or: Operador lógico de disyunción que retorna verdadero si al menos uno de los operandos es verdadero.",
    "not": "not: Operador lógico unario de negación que invierte el estado lógico booleano de la expresión evaluada.",
    "in": "in: Operador de pertenencia que verifica si un elemento está presente dentro de un objeto contenedor.",
    "is": "is: Operador de identidad que evalúa si dos variables apuntan exactamente al mismo objeto en la memoria física.",
    "pass": "pass: Instrucción nula que actúa como marcador de posición sintáctico en bloques que no requieren código ejecutable.",
    "break": "break: Instrucción que rompe el flujo e interrumpe de inmediato el bucle activo (for o while) más interno.",
    "continue": "continue: Instrucción que interrumpe la iteración actual de un bucle y pasa de inmediato a la siguiente.",
    "lambda": "lambda: Palabra clave para declarar funciones anónimas y de corta expresión (funciones lambda).",
    "with": "with: Estructura utilizada para simplificar la gestión de recursos del sistema mediante administradores de contexto.",
    "as": "as: Alias sintáctico utilizado para renombrar módulos importados o para capturar excepciones.",
    "open": "open(): Función de E/S que permite interactuar, leer o escribir archivos físicos en el sistema de almacenamiento.",
    "self": "self: Referencia estándar en métodos de clases que apunta al objeto instancia actual que está siendo procesado.",
    "none": "None: Objeto constante utilizado en Python para representar la ausencia de valor o nulo (NoneType).",
    "true": "True: Valor constante booleano que representa el estado de validez o veracidad lógica.",
    "false": "False: Valor constante booleano que representa el estado de falsedad lógica.",
    "raise": "raise: Instrucción utilizada para lanzar de forma deliberada una excepción o error en tiempo de ejecución.",
    "assert": "assert: Sentencia de depuración que evalúa una expresión condicional y lanza un AssertionError si es falsa.",
    "yield": "yield: Palabra clave usada dentro de una función para convertirla en un generador, devolviendo valores de forma pausada.",
    "global": "global: Declaración sintáctica que indica que una variable pertenece al ámbito global del módulo.",
    "nonlocal": "nonlocal: Declaración que indica que una variable pertenece al ámbito de la función externa más cercana sin ser global.",
    "del": "del: Instrucción utilizada para eliminar referencias de objetos, variables, elementos de listas o claves de diccionarios.",
    "input": "input(): Función incorporada que lee una línea de entrada desde el teclado del usuario como una cadena de texto (sys.stdin).",
    "type": "type(): Función incorporada que devuelve la clase del tipo de objeto del parámetro evaluado.",
    "dir": "dir(): Función que retorna una lista ordenada con los atributos y métodos válidos pertenecientes al objeto especificado.",
    "help": "help(): Utilidad integrada para acceder de forma interactiva a la documentación y manuales de módulos o funciones.",
    "enumerate": "enumerate(): Función que toma un objeto iterable y devuelve un generador que produce tuplas conteniendo el índice y el valor.",
    "zip": "zip(): Función que toma múltiples iterables y devuelve un iterador de tuplas donde cada tupla agrupa elementos correspondientes.",
    "sum": "sum(): Función que realiza la suma acumulativa de todos los elementos numéricos contenidos en un objeto iterable.",
    "min": "min(): Función incorporada que devuelve el elemento con el valor mínimo contenido en un iterable.",
    "max": "max(): Función incorporada que devuelve el elemento con el valor máximo contenido en un iterable.",
    "abs": "abs(): Función que calcula y retorna el valor absoluto de un número entero o decimal.",
    "round": "round(): Función que devuelve un valor numérico redondeado a la cantidad especificada de dígitos decimales.",
    "super": "super(): Permite acceder temporalmente a métodos y atributos definidos en una clase padre o superclase.",
    "isinstance": "isinstance(): Función que evalúa si un objeto es una instancia o subclase de una clase específica.",
    "map": "map(): Aplica una función específica a cada uno de los elementos de un iterable y devuelve un iterador con los resultados.",
    "filter": "filter(): Construye un iterador a partir de los elementos de un iterable para los cuales una función devuelve verdadero.",
    "any": "any(): Devuelve verdadero si al menos uno de los elementos de un iterable es evaluado como verdadero.",
    "all": "all(): Devuelve verdadero si todos los elementos de un iterable son evaluados como verdaderos.",
    "sorted": "sorted(): Retorna una nueva lista que contiene todos los elementos de un iterable ordenados de forma ascendente o personalizada.",
    "id": "id(): Retorna el identificador entero único y constante para la dirección de memoria de un objeto durante su ciclo de vida.",
    "hash": "hash(): Devuelve el valor hash de un objeto si este es inmutable (hashable), utilizado para búsquedas raíces en diccionarios.",
    "__init__": "__init__(): Método constructor especial invocado automáticamente al instanciar una clase para inicializar el estado del objeto.",
    "__str__": "__str__(): Método especial que define la representación en cadena de texto legible para un objeto (utilizado por print).",
    "__repr__": "__repr__(): Método especial que define la representación textual formal e inequívoca de un objeto para depuración."
}

ATAJOS_TEXTO = """Guia de Atajos de Teclado - Control de Foco y Asistencia Activa

Este manual de referencia le permitira navegar y utilizar el entorno de aprendizaje de manera eficiente mediante atajos de teclado.

1. ATAJOS DE INICIO DEL COMPLEMENTO

* NVDA + Control + Shift + P:
  Inicia el complemento y activa la interfaz de aprendizaje.

2. NAVEGACIÓN RÁPIDA ENTRE PANELES PRINCIPALES

Presione la tecla Control junto con los numeros de la fila superior de teclas para mover el foco directamente al panel deseado:

* Control + 1: Selector de temario - Elige el tema o capitulo.
* Control + 2: Panel de teoria - Contenido explicativo del tema.
* Control + 3: Instrucciones de la practica - Enunciado del ejercicio.
* Control + 4: Editor de texto - Espacio para escribir o pegar codigo.
* Control + 5: Consola de resultados - Muestra la salida del codigo ejecutado.
* Control + 6: Lector de la ultima linea - Anuncia de forma hablada la ultima linea impresa de la consola.

3. ATAJOS DE ASISTENCIA ACTIVA (DENTRO DEL EDITOR/PRÁCTICA)

* Control + E: Ejecutar y analizar el codigo actual del editor de forma directa.
* Control + R: Reiniciar el ejercicio - Vuelve el codigo al estado original del capitulo.
* Control + L: Limpiar la consola - Borra todo el contenido mostrado de los resultados.
* Control + G: Abrir buscador del Glosario Interactivo - Consulta de terminos clave en una ventana independiente.
* Control + T: Cargar plantilla - Inserta un codigo estructural adaptado al capitulo actual.
* Control + D: Consultar comando - Explica de forma verbal el significado del comando bajo el cursor usando el glosario.
* Control + H: Historial de consola - Alterna entre el resultado de salida actual y el anterior.

4. NOTAS DE TECLADO PARA EL EDITOR DE TEXTO

* Tecla Escape (Esc): Sale del cuadro de edicion y enfoca directamente la consola de resultados.
* Tecla Tabulador: Inserta 4 espacios fijos (no una tabulacion de ventana) para mantener el sangrado correcto segun el estandar PEP 8 (Python).

5. CONSEJOS ÚTILES

* Asegurese de que el complemento este activo (usando NVDA + Control + Shift + P) antes de probar cualquier otro atajo.
* La tecla Control siempre se refiere a la del lado izquierdo o derecho del teclado; ambas funcionan.
* En combinaciones con numeros, use los de la fila superior, no los del teclado numerico lateral.
"""
