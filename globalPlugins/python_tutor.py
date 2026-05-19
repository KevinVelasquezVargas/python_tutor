# -*- coding: utf-8 -*-
# Módulo: python_tutor.py
# Autor: Kevin Andrés Velasquez Vargas <kevinvelasquezvargas@gmail.com>
# Donaciones: https://www.paypal.me/KevinVelasquezVargas
# Versión: 1.0

import globalPluginHandler
import scriptHandler
import wx
import threading
import winsound
import sys
import io
import traceback
import os
import webbrowser
import ast
import re
import wave
import struct
import math
import tempfile

# Importación segura de módulos específicos de NVDA para evitar fallos de carga en el arranque
try:
    import speech
    import ui
except ImportError:
    speech = None
    ui = None

# --- SINTETIZADOR DINÁMICO NATIVO DE AUDIO WAV (SISTEMA FUTURISTA PREMIUM - SÍNTESIS ADITIVA MULTIHARMÓNICA) ---
class SoundManager:
    _paths = {}
    _initialized = False

    @classmethod
    def initialize(cls):
        """Inicializa la síntesis procedural en un hilo secundario para evitar congelar el arranque de NVDA."""
        if cls._initialized:
            return
        t = threading.Thread(target=cls._generate_all_waves)
        t.daemon = True
        t.start()
        cls._initialized = True

    @classmethod
    def _generate_all_waves(cls):
        temp_dir = tempfile.gettempdir()
        cls._paths = {
            'inicio': os.path.join(temp_dir, 'pytutor_inicio.wav'),
            'exito': os.path.join(temp_dir, 'pytutor_exito.wav'),
            'error': os.path.join(temp_dir, 'pytutor_error.wav'),
            'indent0': os.path.join(temp_dir, 'pytutor_indent0.wav'),
            'indent4': os.path.join(temp_dir, 'pytutor_indent4.wav'),
            'indent8': os.path.join(temp_dir, 'pytutor_indent8.wav'),
            'indent12': os.path.join(temp_dir, 'pytutor_indent12.wav'),
            'fin_bloque': os.path.join(temp_dir, 'pytutor_fin_bloque.wav'),
            'glosario': os.path.join(temp_dir, 'pytutor_glosario.wav')
        }

        # Síntesis matemática directa de ondas sinusoidales, modulaciones FM y arpegios
        try:
            cls._write_click(cls._paths['indent0'])
            cls._write_fm_bell(cls._paths['indent4'], 880, 0.35)
            cls._write_fm_bell(cls._paths['indent8'], 1100, 0.35)
            cls._write_fm_bell(cls._paths['indent12'], 1320, 0.35)
            cls._write_sweep(cls._paths['fin_bloque'], 320, 1400, 0.25)
            cls._write_fm_bell(cls._paths['glosario'], 587.33, 0.5, 3.0, 1.5)
            # SÍNTESIS ADITIVA MULTIHARMÓNICA PARA EL ERROR (Altamente audible en cualquier laptop)
            cls._write_deep_pulse(cls._paths['error'], 150, 80, 0.4)
            cls._write_arpeggio(cls._paths['exito'], [523.25, 659.25, 783.99, 1046.50], 0.08, 0.35)
            cls._write_arpeggio(cls._paths['inicio'], [130.81, 261.63, 392.00, 523.25, 659.25, 987.77], 0.12, 0.45)
        except Exception:
            pass 

    @classmethod
    def _write_wav_file(cls, path, data, sample_rate=44100):
        with wave.open(path, 'wb') as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(sample_rate)
            for val in data:
                val_int = max(-32767, min(32767, int(val * 32767)))
                f.writeframesraw(struct.pack('<h', val_int))

    @classmethod
    def _write_click(cls, path):
        sr = 44100
        dur = 0.04
        num_s = int(sr * dur)
        data = []
        for i in range(num_s):
            t = i / float(sr)
            val = math.sin(2 * math.pi * 110 * t) * math.exp(-120 * t) * 0.4
            data.append(val)
        cls._write_wav_file(path, data)

    @classmethod
    def _write_fm_bell(cls, path, freq, duration, mod_coeff=2.0, mod_idx=1.3):
        sr = 44100
        num_s = int(sr * duration)
        data = []
        for i in range(num_s):
            t = i / float(sr)
            modulator = math.sin(2 * math.pi * freq * mod_coeff * t) * math.exp(-25 * t)
            val = math.sin(2 * math.pi * freq * t + mod_idx * modulator) * math.exp(-8 * t) * 0.3
            data.append(val)
        cls._write_wav_file(path, data)

    @classmethod
    def _write_sweep(cls, path, start_f, end_f, duration):
        sr = 44100
        num_s = int(sr * duration)
        data = []
        for i in range(num_s):
            t = i / float(sr)
            ratio = t / duration
            curr_f = start_f * ((end_f / float(start_f)) ** ratio)
            val = math.sin(2 * math.pi * curr_f * t) * (1.0 - ratio) * 0.2
            data.append(val)
        cls._write_wav_file(path, data)

    @classmethod
    def _write_deep_pulse(cls, path, start_f, end_f, duration):
        sr = 44100
        num_s = int(sr * duration)
        data = []
        for i in range(num_s):
            t = i / float(sr)
            ratio = t / duration
            curr_f = start_f - (start_f - end_f) * ratio
            val = (math.sin(2 * math.pi * curr_f * t) * 0.5 + 
                   math.sin(2 * math.pi * curr_f * 2.0 * t) * 0.3 + 
                   math.sin(2 * math.pi * curr_f * 3.0 * t) * 0.15) * math.exp(-6 * t) * 0.4
            data.append(val)
        cls._write_wav_file(path, data)

    @classmethod
    def _write_arpeggio(cls, path, notes, time_step, note_dur):
        sr = 44100
        total_duration = time_step * len(notes) + note_dur
        num_s = int(sr * total_duration)
        data = [0.0] * num_s

        for idx, freq in enumerate(notes):
            start_s = int(idx * time_step * sr)
            note_len = int(note_dur * sr)
            for i in range(note_len):
                target_idx = start_s + i
                if target_idx < num_s:
                    t = i / float(sr)
                    modulator = math.sin(2 * math.pi * freq * 2.01 * t) * math.exp(-25 * t)
                    val = math.sin(2 * math.pi * freq * t + 1.2 * modulator) * math.exp(-8 * t) * 0.25
                    data[target_idx] += val

        max_val = max(abs(x) for x in data) if data else 1.0
        if max_val > 0.9:
            data = [x / max_val * 0.9 for x in data]

        cls._write_wav_file(path, data)

    @classmethod
    def play(cls, name):
        """Reproduce el audio sintetizado de forma asíncrona usando la API nativa del SO."""
        if name in cls._paths and os.path.exists(cls._paths[name]):
            try:
                winsound.PlaySound(cls._paths[name], winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception:
                pass

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
        "teoria": "A diferencia de otros lenguajes de programación que utilizan llaves ({}) o palabras clave para delimitar bloques de instrucciones, Python utiliza espacios en blanco al inicio de las líneas, un concepto técnico denominado indentación. De acuerdo con la guía de estilo oficial de la comunidad de Python (PEP 8), cada nivel de indentación estructural debe estar compuesto por exactamente 4 espacios físicos (equivalentes a una tabulación en el editor de este complemento). La indentación es un requerimiento sintáctico estricto: cualquier sentencia que pertenezca a un bloque jerárquico subordinado (como las estructuras condicionales o bucles) debe estar alineada de forma precisa, o de lo contrario el intérprete arrojará una excepción de indentación (IndentationError).",
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

# Plantillas de asistencia rápida (Atajo Ctrl + T)
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

# Glosario de Python optimizado
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

# MANUAL DE ATAJOS ACCESIBLE Y LIMPIO (Atajo de inicio de complemento corregido)
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

* Asegurese de que el complemento este activo (usando NVDA + Control + Shift + T) antes de probar cualquier otro atajo.
* La tecla Control siempre se refiere a la del lado izquierdo o derecho del teclado; ambas funcionan.
* En combinaciones con numeros, use los de la fila superior, no los del teclado numerico lateral.
"""

class AccessibleManualDialog(wx.Dialog):
    def __init__(self, parent, title, text):
        super(AccessibleManualDialog, self).__init__(parent, title=title, size=(650, 520))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.text_ctrl.SetValue(text)
        self.text_ctrl.SetName("Contenido del Manual de Atajos. Navegue por este texto con sus flechas de direccion.")
        
        btn_ok = wx.Button(panel, wx.ID_OK, label="Cerrar Manual")
        btn_ok.SetName("Boton Cerrar Ventana")
        
        vbox.Add(self.text_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=15)
        vbox.Add(btn_ok, proportion=0, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=15)
        panel.SetSizer(vbox)
        
        # Cierre prioritario al pulsar Escape
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.text_ctrl.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

# CUADRO DE EDICIÓN PARA MOSTRAR LA INFORMACIÓN DE "ACERCA DE" DE FORMA ACCESIBLE
class AccessibleAboutDialog(wx.Dialog):
    def __init__(self, parent, title, text):
        super(AccessibleAboutDialog, self).__init__(parent, title=title, size=(650, 520))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.text_ctrl.SetValue(text)
        self.text_ctrl.SetName("Contenido Informativo del Complemento. Navegue por este texto con sus flechas de direccion.")
        
        btn_ok = wx.Button(panel, wx.ID_OK, label="Cerrar Acerca de")
        btn_ok.SetName("Boton Cerrar Ventana")
        
        vbox.Add(self.text_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=15)
        vbox.Add(btn_ok, proportion=0, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=15)
        panel.SetSizer(vbox)
        
        # Cierre prioritario al pulsar Escape
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.text_ctrl.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

class GlossaryDialog(wx.Dialog):
    def __init__(self, parent, glosario_dict):
        super(GlossaryDialog, self).__init__(parent, title="Glosario Interactivo de Conceptos", size=(750, 550))
        self.glosario = glosario_dict
        self.terminos_ordenados = sorted(list(glosario_dict.keys()))
        self.filtrados = list(self.terminos_ordenados)
        
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Buscador
        search_box = wx.BoxSizer(wx.HORIZONTAL)
        search_box.Add(wx.StaticText(panel, label="Buscador de terminos:"), flag=wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border=5)
        self.search_ctrl = wx.TextCtrl(panel)
        self.search_ctrl.SetName("Escribe aqui la palabra para filtrar el glosario.")
        search_box.Add(self.search_ctrl, proportion=1, flag=wx.EXPAND)
        main_sizer.Add(search_box, flag=wx.EXPAND | wx.ALL, border=10)
        
        # Zona de listas y definiciones
        content_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Lista de palabras
        list_sizer = wx.BoxSizer(wx.VERTICAL)
        list_sizer.Add(wx.StaticText(panel, label="Terminos disponibles:"), flag=wx.BOTTOM, border=5)
        self.list_box = wx.ListBox(panel, choices=self.terminos_ordenados)
        self.list_box.SetName("Lista de terminos. Presione flechas abajo o arriba para seleccionar.")
        list_sizer.Add(self.list_box, proportion=1, flag=wx.EXPAND)
        content_sizer.Add(list_sizer, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=10)
        
        # Significado
        def_sizer = wx.BoxSizer(wx.VERTICAL)
        def_sizer.Add(wx.StaticText(panel, label="Significado:"), flag=wx.BOTTOM, border=5)
        self.def_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.def_ctrl.SetName("Significado del termino seleccionado. Presione tabulador para acceder y leer.")
        def_sizer.Add(self.def_ctrl, proportion=1, flag=wx.EXPAND)
        content_sizer.Add(def_sizer, proportion=2, flag=wx.EXPAND)
        
        main_sizer.Add(content_sizer, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)
        
        # Boton de cerrar
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_cerrar = wx.Button(panel, label="Cerrar Glosario")
        self.btn_cerrar.SetName("Boton cerrar glosario")
        btn_sizer.Add(self.btn_cerrar)
        main_sizer.Add(btn_sizer, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)
        
        panel.SetSizer(main_sizer)
        
        # Eventos
        self.search_ctrl.Bind(wx.EVT_TEXT, self.on_search_change)
        self.list_box.Bind(wx.EVT_LISTBOX, self.on_list_select)
        self.btn_cerrar.Bind(wx.EVT_BUTTON, lambda e: self.Close())
        self.search_ctrl.Bind(wx.EVT_KEY_DOWN, self.on_search_key_down)
        self.list_box.Bind(wx.EVT_KEY_DOWN, self.on_list_key_down)
        
        # Cierre prioritario al pulsar Escape en cualquier control de este diálogo
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        
        # Iniciar
        if self.terminos_ordenados:
            self.list_box.SetSelection(0)
            self.actualizar_definicion()
            
        self.search_ctrl.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()
        
    def on_search_change(self, event):
        query = self.search_ctrl.GetValue().lower().strip()
        self.filtrados = [t for t in self.terminos_ordenados if query in t]
        self.list_box.Set(self.filtrados)
        if self.filtrados:
            self.list_box.SetSelection(0)
        self.actualizar_definicion()
        
    def on_list_select(self, event):
        self.actualizar_definicion()
        
    def actualizar_definicion(self):
        sel = self.list_box.GetStringSelection()
        if sel and sel in self.glosario:
            self.def_ctrl.SetValue(self.glosario[sel])
            if ui: ui.message(sel)
        else:
            self.def_ctrl.SetValue("")
            
    def on_search_key_down(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_DOWN:
            self.list_box.SetFocus()
        elif keycode == wx.WXK_ESCAPE:
            self.Close()
        else:
            event.Skip()
            
    def on_list_key_down(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_UP and self.list_box.GetSelection() == 0:
            self.search_ctrl.SetFocus()
        elif keycode == wx.WXK_ESCAPE:
            self.Close()
        else:
            event.Skip()

class TutorFrame(wx.Frame):
    def __init__(self, parent):
        super(TutorFrame, self).__init__(parent, title="Python Tutor", size=(950, 850))
        
        self.linter_activo = True
        self.exito_activo = True
        self.error_activo = True
        self.historial_anterior = "" 
        self.archivo_actual = None 
        
        self.crear_barra_menus()
        
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        vbox.Add(wx.StaticText(panel, label="1. Selector de Capitulos (Atajo: Control + 1):"), flag=wx.LEFT|wx.TOP, border=10)
        self.lista_capitulos = wx.ListBox(panel, choices=[l["titulo"] for l in LECCIONES])
        self.lista_capitulos.SetName("Selector de Capitulos")
        vbox.Add(self.lista_capitulos, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        
        vbox.Add(wx.StaticText(panel, label="2. Panel de Teoria (Atajo: Control + 2):"), flag=wx.LEFT|wx.TOP, border=10)
        self.teoria = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)
        self.teoria.SetName("Panel de Teoria. Navegue con las flechas de direccion.")
        vbox.Add(self.teoria, proportion=3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        
        vbox.Add(wx.StaticText(panel, label="3. Actividad Practica Dirigida (Atajo: Control + 3):"), flag=wx.LEFT|wx.TOP, border=10)
        self.practica = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)
        self.practica.SetName("Instrucciones del Desafio Practico.")
        vbox.Add(self.practica, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        
        vbox.Add(wx.StaticText(panel, label="4. Consola de Edicion de Codigo (Atajo: Control + 4):"), flag=wx.LEFT|wx.TOP, border=10)
        self.edicion = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_PROCESS_TAB)
        self.edicion.SetName("Consola de Edicion de Codigo Fuente")
        vbox.Add(self.edicion, proportion=3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        
        vbox.Add(wx.StaticText(panel, label="5. Consola de Resultados (Atajo: Control + 5):"), flag=wx.LEFT|wx.TOP, border=10)
        self.salida = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)
        self.salida.SetName("Consola de Resultados de ejecucion.")
        vbox.Add(self.salida, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn_ejecutar = wx.Button(panel, label="Ejecutar Codigo (Ctrl + E)")
        self.btn_ejecutar.SetName("Boton Ejecutar")
        
        self.btn_consola_nvda = wx.Button(panel, label="Abrir Consola de NVDA")
        self.btn_consola_nvda.SetName("Boton Abrir Consola de NVDA")
        
        self.btn_reiniciar = wx.Button(panel, label="Reiniciar Acertijo (Ctrl + R)")
        self.btn_reiniciar.SetName("Boton Restablecer Codigo")
        
        self.btn_limpiar = wx.Button(panel, label="Limpiar Consola (Ctrl + L)")
        self.btn_limpiar.SetName("Boton Limpiar Consola")
        
        self.btn_exportar = wx.Button(panel, label="Exportar Script (.py)")
        self.btn_exportar.SetName("Boton Exportar Codigo")
        
        self.btn_cerrar = wx.Button(panel, label="Cerrar Panel")
        self.btn_cerrar.SetName("Boton Cerrar")
        
        hbox.Add(self.btn_ejecutar, flag=wx.RIGHT, border=5)
        hbox.Add(self.btn_consola_nvda, flag=wx.RIGHT, border=5)
        hbox.Add(self.btn_reiniciar, flag=wx.RIGHT, border=5)
        hbox.Add(self.btn_limpiar, flag=wx.RIGHT, border=5)
        hbox.Add(self.btn_exportar, flag=wx.RIGHT, border=5)
        hbox.Add(self.btn_cerrar)
        
        vbox.Add(hbox, flag=wx.ALIGN_CENTER|wx.ALL, border=15)
        panel.SetSizer(vbox)
        
        self.lista_capitulos.Bind(wx.EVT_LISTBOX, self.on_seleccionar_capitulo)
        self.edicion.Bind(wx.EVT_KEY_DOWN, self.on_key_down_edicion)
        self.edicion.Bind(wx.EVT_KEY_UP, self.on_key_up_edicion)
        self.edicion.Bind(wx.EVT_LEFT_UP, self.on_left_up_edicion)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook_global)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        
        self.btn_ejecutar.Bind(wx.EVT_BUTTON, self.on_ejecutar)
        self.btn_consola_nvda.Bind(wx.EVT_BUTTON, self.on_abrir_consola_nvda)
        self.btn_reiniciar.Bind(wx.EVT_BUTTON, self.on_reiniciar_acertijo)
        self.btn_limpiar.Bind(wx.EVT_BUTTON, self.on_limpiar_consola)
        self.btn_exportar.Bind(wx.EVT_BUTTON, self.on_exportar_script)
        self.btn_cerrar.Bind(wx.EVT_BUTTON, lambda e: self.Close())
        
        self.teoria.SetValue("Navega al Selector de Capitulos (Control + 1) para comenzar a estudiar.")
        
        # Sonido celestial premium de inicio de la interfaz
        SoundManager.play('inicio')

    def crear_barra_menus(self):
        menu_bar = wx.MenuBar()
        
        # Archivo
        menu_archivo = wx.Menu()
        item_abrir = menu_archivo.Append(wx.ID_ANY, "Abrir archivo...	Ctrl+O", "Cargar script Python")
        item_guardar = menu_archivo.Append(wx.ID_ANY, "Guardar	Ctrl+S", "Guardar el codigo")
        item_guardar_como = menu_archivo.Append(wx.ID_ANY, "Guardar como...", "Guardar como un nuevo archivo")
        
        self.Bind(wx.EVT_MENU, self.on_abrir_archivo, id=item_abrir.GetId())
        self.Bind(wx.EVT_MENU, self.on_guardar_archivo, id=item_guardar.GetId())
        self.Bind(wx.EVT_MENU, self.on_guardar_como, id=item_guardar_como.GetId())
        
        # Configuración (RENOMBRADO DESDE "Ajustes" PARA COINCIDIR CON LA SEMÁNTICA OFICIAL)
        menu_ajustes = wx.Menu()
        self.item_linter = menu_ajustes.AppendCheckItem(wx.ID_ANY, "Activar Linter Acústico", "Tonos al navegar por la sangria")
        self.item_exito = menu_ajustes.AppendCheckItem(wx.ID_ANY, "Activar Sonido de Éxito", "Arpegios armónicos de cristal")
        self.item_error = menu_ajustes.AppendCheckItem(wx.ID_ANY, "Activar Sonido de Error", "Pulsación sorda analógica")
        
        self.item_linter.Check(True)
        self.item_exito.Check(True)
        self.item_error.Check(True)
        
        self.Bind(wx.EVT_MENU, self.on_toggle_linter, id=self.item_linter.GetId())
        self.Bind(wx.EVT_MENU, self.on_toggle_exito, id=self.item_exito.GetId())
        self.Bind(wx.EVT_MENU, self.on_toggle_error, id=self.item_error.GetId())
        
        # Glosario
        menu_glosario = wx.Menu()
        item_glosario = menu_glosario.Append(wx.ID_ANY, "Consultar Glosario...	Ctrl+G", "Abre el buscador interactivo")
        self.Bind(wx.EVT_MENU, self.on_abrir_glosario_dialog, id=item_glosario.GetId())
        
        # Ayuda
        menu_ayuda = wx.Menu()
        item_atajos = menu_ayuda.Append(wx.ID_ANY, "Manual de Atajos", "Muestra la guia rapida")
        item_acerca = menu_ayuda.Append(wx.ID_ANY, "Acerca de Python Tutor", "Autor e info")
        item_donar = menu_ayuda.Append(wx.ID_ANY, "Donar en PayPal", "Soporte de desarrollo")
        item_correo = menu_ayuda.Append(wx.ID_ANY, "Enviar Correo a Soporte", "Contacto directo")
        
        self.Bind(wx.EVT_MENU, self.on_ver_atajos, id=item_atajos.GetId())
        self.Bind(wx.EVT_MENU, self.on_ver_acerca, id=item_acerca.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_donaciones, id=item_donar.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_correo, id=item_correo.GetId())
        
        menu_bar.Append(menu_archivo, "&Archivo")
        menu_bar.Append(menu_ajustes, "&Configuración")
        menu_bar.Append(menu_glosario, "&Glosario")
        menu_bar.Append(menu_ayuda, "&Ayuda")
        self.SetMenuBar(menu_bar)

    def on_abrir_archivo(self, event=None):
        dlg = wx.FileDialog(self, "Abrir archivo Python", wildcard="Archivos Python (*.py)|*.py", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    codigo = f.read()
                self.edicion.SetValue(codigo)
                self.archivo_actual = path
                msg = f"Archivo cargado correctamente: {os.path.basename(path)}"
                if ui: ui.message(msg)
                self.edicion.SetFocus()
            except Exception as e:
                wx.MessageBox(f"Error al abrir archivo: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)
        dlg.Destroy()

    def on_guardar_archivo(self, event=None):
        if self.archivo_actual:
            try:
                codigo = self.edicion.GetValue()
                with open(self.archivo_actual, 'w', encoding='utf-8') as f:
                    f.write(codigo)
                msg = f"Guardado en: {os.path.basename(self.archivo_actual)}"
                if ui: ui.message(msg)
            except Exception as e:
                wx.MessageBox(f"Error al guardar: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)
        else:
            self.on_guardar_como(event)

    def on_guardar_como(self, event=None):
        codigo = self.edicion.GetValue()
        dlg = wx.FileDialog(self, "Guardar archivo como", wildcard="Archivos Python (*.py)|*.py", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(codigo)
                self.archivo_actual = path
                msg = f"Guardado correctamente en: {os.path.basename(path)}"
                if ui: ui.message(msg)
            except Exception as e:
                wx.MessageBox(f"Error al guardar: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)
        dlg.Destroy()

    def on_exportar_script(self, event=None):
        self.on_guardar_como(event)

    def on_abrir_glosario_dialog(self, event=None):
        dlg = GlossaryDialog(self, GLOSARIO_RAPIDO)
        dlg.ShowModal()
        dlg.Destroy()

    def on_toggle_linter(self, event):
        self.linter_activo = self.item_linter.IsChecked()
        if ui: ui.message("Linter acustico " + ("activado" if self.linter_activo else "desactivado"))

    def on_toggle_exito(self, event):
        self.exito_activo = self.item_exito.IsChecked()
        if ui: ui.message("Sonido de exito " + ("activado" if self.exito_activo else "desactivado"))

    def on_toggle_error(self, event):
        self.error_activo = self.item_error.IsChecked()
        if ui: ui.message("Sonido de error " + ("activado" if self.error_activo else "desactivado"))

    def on_ver_atajos(self, event):
        dlg = AccessibleManualDialog(self, "Manual de Atajos", ATAJOS_TEXTO)
        dlg.ShowModal()
        dlg.Destroy()

    def on_ver_acerca(self, event):
        acerca_info = (
            "Acerca de este Complemento\n\n"
            "¿Qué es?\n\n"
            "Este complemento para NVDA (NonVisual Desktop Access) está diseñado para facilitar el aprendizaje del lenguaje de programación Python a personas con discapacidad visual. Actúa como una interfaz de navegación y control rápida, permitiendo al estudiante o desarrollador moverse entre los paneles esenciales de un entorno de enseñanza (temario, teoría, instrucciones, editor de código y consola de resultados) y ejecutar acciones clave sin necesidad de usar el ratón ni recorrer la interfaz visual con el cursor.\n\n"
            "Créditos y licencia\n"
            "- Autor: Kevin Andrés Velasquez Vargas.\n"
            "- Año: 2026.\n"
            "- Licencia: GNU General Public License v3.0 (GPLv3). El complemento es de código abierto y puede ser redistribuido, modificado y mejorado bajo los términos de esta licencia."
        )
        dlg = AccessibleAboutDialog(self, "Acerca de Python Tutor", acerca_info)
        dlg.ShowModal()
        dlg.Destroy()

    def on_abrir_donaciones(self, event):
        try:
            webbrowser.open("https://www.paypal.me/KevinVelasquezVargas")
            if ui: ui.message("Abriendo PayPal.")
        except:
            pass

    def on_abrir_correo(self, event):
        try:
            webbrowser.open("mailto:kevinvelasquezvargas@gmail.com?subject=Reporte%20Python%20Tutor")
            if ui: ui.message("Abriendo correo.")
        except:
            pass

    def on_seleccionar_capitulo(self, event):
        idx = self.lista_capitulos.GetSelection()
        if idx != wx.NOT_FOUND:
            lec = LECCIONES[idx]
            self.teoria.SetValue(lec["teoria"])
            self.practica.SetValue(lec["practica"])
            self.edicion.SetValue(lec["codigo"])
            self.salida.SetValue("")
            if ui:
                ui.message("Cargado correctamente: " + lec["titulo"])

    def on_char_hook_global(self, event):
        keycode = event.GetKeyCode()
        modifiers = event.GetModifiers()
        if modifiers == wx.MOD_CONTROL:
            if keycode in (ord('C'), ord('V'), ord('X'), ord('Z'), ord('Y')):
                event.Skip()
                return
            
            if keycode == ord('A'):
                focused = wx.Window.FindFocus()
                if isinstance(focused, wx.TextCtrl):
                    focused.SetSelection(-1, -1)
                return
                
            elif keycode == ord('1'): self.lista_capitulos.SetFocus(); return
            elif keycode == ord('2'): self.teoria.SetFocus(); return
            elif keycode == ord('3'): self.practica.SetFocus(); return
            elif keycode == ord('4'): self.edicion.SetFocus(); return
            elif keycode == ord('5'): self.salida.SetFocus(); return
            elif keycode == ord('6'): self.leer_ultima_salida(); return
            
            elif keycode == ord('E'): self.on_ejecutar(None); return
            elif keycode == ord('R'): self.on_reiniciar_acertijo(None); return
            elif keycode == ord('L'): self.on_limpiar_consola(None); return
            elif keycode == ord('G'): self.on_abrir_glosario_dialog(None); return
            
            elif keycode == ord('O'): self.on_abrir_archivo(None); return
            elif keycode == ord('S'): self.on_guardar_archivo(None); return
            elif keycode == ord('T'): self.insertar_plantilla_base(); return
            elif keycode == ord('D'): self.consultar_glosario(); return
            elif keycode == ord('H'): self.recuperar_historial(); return
            else:
                event.Skip()
        else:
            if keycode == ord(':'):
                SoundManager.play('fin_bloque')
            event.Skip()

    def on_key_down_edicion(self, event):
        keycode = event.GetKeyCode()
        modifiers = event.GetModifiers()
        if keycode == wx.WXK_ESCAPE:
            self.salida.SetFocus()
            return
        elif keycode == wx.WXK_TAB:
            if event.ShiftDown():
                self.practica.SetFocus()
            else:
                self.edicion.WriteText("    ")
            return
        if modifiers == wx.MOD_CONTROL:
            event.Skip()
            return
        event.Skip()

    def on_key_up_edicion(self, event):
        self.ejecutar_linter_acustico()
        event.Skip()

    def on_left_up_edicion(self, event):
        self.ejecutar_linter_acustico()
        event.Skip()

    def ejecutar_linter_acustico(self):
        if not self.linter_activo:
            return
        try:
            pt = self.edicion.GetInsertionPoint()
            txt = self.edicion.GetValue()
            
            text_up_to_pt = txt[:pt]
            row = text_up_to_pt.count('\n')
            
            linea_txt = self.edicion.GetLineText(row)
            espacios = len(linea_txt) - len(linea_txt.lstrip(' '))
            
            if espacios == 0: SoundManager.play('indent0')
            elif espacios == 4: SoundManager.play('indent4')
            elif espacios == 8: SoundManager.play('indent8')
            elif espacios >= 12: SoundManager.play('indent12')
        except:
            pass

    def insertar_plantilla_base(self):
        idx = self.lista_capitulos.GetSelection()
        cap = idx + 1
        if cap in PLANTILLAS_BASE:
            self.edicion.SetValue(PLANTILLAS_BASE[cap])
            self.edicion.SetFocus()
            if ui: ui.message(f"Plantilla base cargada para el capitulo {cap}")
        else:
            self.edicion.SetValue("# Escribe tu practica aqui...\n")
            self.edicion.SetFocus()
            if ui: ui.message("Plantilla en blanco insertada")

    def consultar_glosario(self):
        pt = self.edicion.GetInsertionPoint()
        txt = self.edicion.GetValue()
        
        palabras = list(re.finditer(r'\w+', txt))
        palabra_detectada = None
        for p in palabras:
            if p.start() <= pt <= p.end():
                palabra_detectada = p.group(0).lower()
                break
        
        if palabra_detectada and palabra_detectada in GLOSARIO_RAPIDO:
            definicion = GLOSARIO_RAPIDO[palabra_detectada]
            SoundManager.play('glosario')
            if ui: ui.message(definicion)
            wx.MessageBox(definicion, "Glosario de Concepto", wx.OK | wx.ICON_INFORMATION)
        else:
            msg = "Coloque el cursor sobre un comando para consultar"
            if ui: ui.message(msg)

    def recuperar_historial(self):
        if self.historial_anterior:
            actual = self.salida.GetValue()
            self.salida.SetValue(self.historial_anterior)
            self.historial_anterior = actual
            if ui: ui.message("Consola restaurada al resultado anterior")
        else:
            if ui: ui.message("No hay ejecuciones anteriores en el historial")

    def leer_ultima_salida(self):
        txt = self.salida.GetValue()
        if not txt.strip() or "La salida de ejecucion" in txt:
            if ui: ui.message("Consola vacia")
            return
        lineas = [l.strip() for l in txt.split('\n') if l.strip()]
        if lineas:
            ultima = lineas[-1]
            if ui: ui.message(ultima)

    def on_limpiar_consola(self, event=None):
        self.salida.SetValue("")
        if ui: ui.message("Consola limpiada.")
        SoundManager.play('indent0')

    def validar_desafio(self, cap, src, res, namespace_local):
        try:
            if cap == 1:
                lineas = [l.strip() for l in res.split('\n') if l.strip()]
                esperado = [
                    "Paso 1: Iniciando conexion con el servidor local.",
                    "Paso 2: Autenticando credenciales de acceso seguro.",
                    "Paso 3: Panel de usuario desplegado correctamente."
                ]
                pasos = [l for l in lineas if "Paso " in l]
                if pasos == esperado:
                    return True, "Solucion correcta. Se ha mantenido el flujo secuencial lineal esperado."
                return False, "Orden incorrecto. Debe iniciar conexion (Paso 1), autenticar (Paso 2) y desplegar (Paso 3)."

            elif cap == 2:
                if "Entorno virtual inicializado bajo codificacion estandar." in res:
                    return True, "Solucion correcta. Sintaxis de print() corregida."
                return False, "Fallo. La salida no coincide. Verifique que la funcion sea 'print'."

            elif cap == 3:
                usuario = namespace_local.get("usuario_activo", "Invitado")
                if usuario != "Invitado" and len(str(usuario).strip()) > 0:
                    return True, f"Solucion correcta. Nombre de usuario actualizado a: '{usuario}'."
                return False, "Fallo. La variable 'usuario_activo' aun tiene el valor 'Invitado'."

            elif cap == 4:
                val = namespace_local.get("identificador_final")
                if val == 30:
                    return True, "Solucion correcta. Tipos unificados y suma realizada."
                return False, "Fallo. El identificador final debe ser el entero 30. Remueva las comillas de '20'."

            elif cap == 5:
                if "Estado del sistema: Operativo y validado." in res:
                    return True, "Solucion correcta. Indentacion aplicada con exito."
                return False, "Fallo. Asegurese de sangrar la linea del print con exactamente 4 espacios."

            elif cap == 6:
                total = namespace_local.get("total")
                if total and abs(float(total) - 59.97) < 0.01:
                    return True, "Solucion correcta. Conversion de tipos aplicada."
                return False, "Fallo. Aplique float() a precio_texto e int() a cantidad_texto."

            elif cap == 7:
                promedio = namespace_local.get("promedio")
                if promedio and abs(float(promedio) - 8.2) < 0.01:
                    return True, "Solucion correcta. Prioridad agrupada con parentesis."
                return False, "Fallo. Agrupe la suma de las notas entre parentesis antes de dividir."

            elif cap == 8:
                if "Acceso concedido" in res and "==" in src:
                    return True, "Solucion correcta. Se ha implementado el operador de comparacion."
                return False, "Fallo. Recuerde utilizar el operador de comparacion '==' dentro de la clausula if."

            elif cap == 9:
                p_desc = namespace_local.get("puede_descargar")
                if p_desc is True:
                    return True, "Solucion correcta. Clausulas logicas anidadas perfectamente."
                return False, "Fallo. La expresion debe ser: conectado and (saldo_positivo or es_admin)."

            elif cap == 10:
                if "Calificacion: Aceptable" in res and "Calificacion: Excelente" not in res:
                    return True, "Solucion correcta. Decisiones excluyentes mapeadas."
                return False, "Fallo. Reemplace el segundo 'if' por 'elif' para que la evaluacion sea secuencial."

            elif cap == 11:
                primero = namespace_local.get("primero")
                ultimo = namespace_local.get("ultimo")
                if primero == "us-east" and ultimo == "sa-east":
                    return True, "Solucion correcta. Indexacion de extremos resuelta."
                return False, "Fallo. Extrae con servidores[0] y servidores[-1]."

            elif cap == 12:
                tareas = namespace_local.get("tareas", [])
                if len(tareas) == 3 and tareas[-1] == "revisar codigo":
                    return True, "Solucion correcta. Elemento agregado de forma dinamica."
                return False, "Fallo. Agregue la cadena 'revisar codigo' mediante el metodo .append()."

            elif cap == 13:
                centro = namespace_local.get("centro", [])
                if centro == [250.0, 15.0, 80.2]:
                    return True, "Solucion correcta. Rebanado de rango intermedio exitoso."
                return False, "Fallo. El corte correcto de sublista es transacciones[1:4]."

            elif cap == 14:
                coord = namespace_local.get("coordenadas")
                if isinstance(coord, tuple):
                    return True, "Solucion correcta. Tipo de dato inmutable declarado."
                return False, "Fallo. Reemplace los corchetes [] por parentesis () para declarar una tupla."

            elif cap == 15:
                est = namespace_local.get("estudiante", {})
                if est.get("lenguaje") == "Python":
                    return True, "Solucion correcta. Clave y valor inyectados al diccionario."
                return False, "Fallo. Asigne el valor 'Python' a la clave 'lenguaje' de estudiante."

            elif cap == 16:
                unicos = namespace_local.get("accesos_unicos")
                if isinstance(unicos, set) and len(unicos) == 3:
                    return True, "Solucion correcta. Coleccion filtrada sin duplicados."
                return False, "Fallo. Convierta la lista aplicando la funcion set(accesos_duplicados)."

            elif cap == 17:
                lineas = [l.strip() for l in res.split('\n') if l.strip()]
                descuentos = [float(l.split(":")[-1].strip()) for l in lineas if "Precio con descuento:" in l]
                if descuentos == [90.0, 225.0, 45.0, 360.0]:
                    return True, "Solucion correcta. Iteracion de elementos completada."
                return False, "Fallo. Complete la linea con: for precio in precios:"

            elif cap == 18:
                if "¡Descarga completada!" in res and "Descargando: 100%" in res:
                    return True, "Solucion correcta. Incremento de control implementado."
                return False, "Fallo. Agregue el incremento 'porcentaje += 20' para evitar un bucle infinito."

            elif cap == 19:
                func = namespace_local.get("calcular_impuesto")
                if func and func(1000) == 190.0:
                    return True, "Solucion correcta. Retorno de la funcion procesado."
                return False, "Fallo. La funcion debe retornar el calculo exacto usando 'return monto * 0.19'."

            elif cap == 20:
                if "ValueError" not in res and any(x in res.lower() for x in ["error", "invalido", "no es un", "veinte"]):
                    return True, "Solucion correcta. Excepcion mitigada de manera segura."
                return False, "Fallo. Envuelva la linea de conversion en un bloque try y gestione el ValueError."

            elif cap == 21:
                raiz = namespace_local.get("raiz")
                if raiz and abs(float(raiz) - 10.0) < 0.01:
                    return True, "Solucion correcta. Modulo estandar importado y resuelto."
                return False, "Fallo. Importe el modulo math y use math.sqrt(100) en la variable raiz."

            return True, "Codigo ejecutado con exito."
        except Exception as e:
            return False, f"Fallo en comprobacion logica: {str(e)}"

    def on_ejecutar(self, event=None):
        idx = self.lista_capitulos.GetSelection()
        cap = idx + 1
        src = self.edicion.GetValue()
        self.historial_anterior = self.salida.GetValue()
        
        buf = io.StringIO()
        sys.stdout = buf
        sys.stderr = buf
        exito_total = True
        linea_error = None
        error_msg = ""
        tipo_error = "Error"
        namespace_local = {}
        
        try:
            exec(src, {}, namespace_local)
            res = buf.getvalue()
            if not res: res = "Codigo ejecutado (sin salidas impresas)."
        except Exception as e:
            tb = traceback.extract_tb(sys.exc_info()[2])
            for frame in reversed(tb):
                if frame.filename == "<string>":
                    linea_error = frame.lineno
                    break
            if not linea_error:
                linea_error = 1
            error_msg = str(e)
            tipo_error = type(e).__name__
            res = f"Error en la línea {linea_error}: {tipo_error} - {error_msg}"
            exito_total = False
        finally:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

        # Radiografía Estructural
        variables = 0
        condicionales = 0
        bucles = 0
        impresiones = 0
        lineas_reales = 0
        
        try:
            tree = ast.parse(src)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    variables += 1
                elif isinstance(node, ast.If):
                    condicionales += 1
                elif isinstance(node, (ast.For, ast.While)):
                    bucles += 1
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "print":
                    impresiones += 1
        except Exception:
            variables = len(re.findall(r'^\s*\w+\s*=[^=]', src, re.M))
            condicionales = len(re.findall(r'^\s*if\s', src, re.M))
            bucles = len(re.findall(r'^\s*(for|while)\s', src, re.M))
            impresiones = len(re.findall(r'print\s*\(', src))

        for line in src.splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith('#'):
                lineas_reales += 1

        exito_validado, explicacion_validada = self.validar_desafio(cap, src, res, namespace_local)

        if exito_total and exito_validado:
            reporte = (
                f"[SALIDA DE CONSOLA]\n{res}\n\n"
                f"[RADIOGRAFÍA ESTRUCTURAL]\n"
                f"- Variables encontradas: {variables}\n"
                f"- Estructuras condicionales: {condicionales}\n"
                f"- Bucles de repencion: {bucles}\n"
                f"- Funciones de impresion: {impresiones}\n\n"
                f"[REVISIÓN]: {explicacion_validada}\n\n"
                f"[MÉTRICA DE EFICIENCIA]\n"
                f"- Lineas de codigo activas utilizadas: {lineas_reales} (¡Buen trabajo!)"
            )
            self.salida.SetValue(reporte)
            self.salida.SetFocus()
            
            if ui: ui.message(f"Ejecutado con exito. {explicacion_validada}")
            if self.exito_activo:
                SoundManager.play('exito')
        else:
            if not exito_total:
                msg_error = f"Error en la línea {linea_error}: {tipo_error} - {error_msg}"
                revision = "Corrige la excepcion o error de sintaxis detallado en consola."
            else:
                msg_error = "Validacion fallida: El desafio no se ha completado de forma logica."
                revision = explicacion_validada
                
            reporte = (
                f"[SALIDA DE CONSOLA]\n{msg_error if not exito_total else res}\n\n"
                f"[RADIOGRAFÍA ESTRUCTURAL (Previo al fallo)]\n"
                f"- Variables encontradas: {variables}\n"
                f"- Estructuras condicionales: {condicionales}\n"
                f"- Bucles de repeticion: {bucles}\n"
                f"- Funciones de impresion: {impresiones}\n\n"
                f"[CORRECCIÓN]: {revision}"
            )
            self.salida.SetValue(reporte)
            self.salida.SetFocus()
            
            if ui: ui.message(f"Error detectado o validacion fallida. {revision}")
            if self.error_activo:
                SoundManager.play('error')

    def on_reiniciar_acertijo(self, event=None):
        idx = self.lista_capitulos.GetSelection()
        if idx != wx.NOT_FOUND:
            self.edicion.SetValue(LECCIONES[idx]["codigo"])
            self.salida.SetValue("")
            self.edicion.SetFocus()
            if ui: ui.message("Acertijo restablecido al estado original.")

    def on_close(self, event):
        self.Destroy()

    def on_abrir_consola_nvda(self, event):
        try:
            import gui
            wx.CallAfter(gui.mainFrame.onPythonConsoleCommand, None)
        except Exception:
            self.salida.SetValue("Incapaz de enlazar de forma directa con la consola interna.")

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    """Clase principal del plugin global de NVDA con importación dinámica ultrasegura."""
    scriptCategory = "Python Tutor"
    
    gestures = {
        "kb:NVDA+control+shift+p": "openPythonTutor",
    }

    def __init__(self, *args, **kwargs):
        super(GlobalPlugin, self).__init__(*args, **kwargs)
        self.gui_frame = None
        SoundManager.initialize()

    def script_openPythonTutor(self, gesture):
        """Abre el entorno interactivo Python Tutor."""
        wx.CallAfter(self._crear_interfaz)

    def _crear_interfaz(self):
        parent_window = None
        try:
            import gui
            if hasattr(gui, 'mainFrame') and gui.mainFrame:
                parent_window = gui.mainFrame
        except:
            pass
            
        if not self.gui_frame:
            try:
                self.gui_frame = TutorFrame(parent_window)
                self.gui_frame.Bind(wx.EVT_WINDOW_DESTROY, self.on_frame_destroy)
            except Exception as e:
                if ui: ui.message("Error al iniciar interfaz: " + str(e))
                return
        try:
            self.gui_frame.Show()
            self.gui_frame.Raise()
            self.gui_frame.lista_capitulos.SetFocus()
        except (RuntimeError, wx.PyDeadObjectError):
            self.gui_frame = TutorFrame(parent_window)
            self.gui_frame.Show()
            self.gui_frame.Raise()
            self.gui_frame.lista_capitulos.SetFocus()

    def on_frame_destroy(self, event):
        if event.GetEventObject() == self.gui_frame:
            self.gui_frame = None
        event.Skip()
