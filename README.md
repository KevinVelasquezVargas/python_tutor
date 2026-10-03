# Aprendizaje de Python con NVDA

* **Versión:** 1.0.0
* **Autor:** Kevin Andrés Velasquez Vargas
* **Compatibilidad:** NVDA 2022.1 hasta 2026.2
* **Licencia:** GNU General Public License v3.0 (GPLv3)
* **Repositorio:** [Repositorio oficial en GitHub](https://github.com/KevinVelasquezVargas/python_tutor)

---

## Contenido

1. [Introducción](#1-introducción)
2. [Características Principales](#2-características-principales)
3. [Atajos de Teclado](#3-atajos-de-teclado)
4. [Plan Formativo Integral (40 Capítulos)](#4-plan-formativo-integral-40-capítulos)
5. [Configuración](#5-configuración)
6. [Registro de Cambios](#6-registro-de-cambios)
7. [Soporte](#7-soporte)
8. [Colaboración](#8-colaboración)

---

## 1. Introducción

**Aprendizaje de Python con NVDA** es un entorno pedagógico accesible diseñado para personas con discapacidad visual usuarias del lector de pantallas NVDA. El diseño curricular parte de bases computacionales (arquitectura, sistema binario, ciclo de ejecución e interacción tiflotécnica) antes de avanzar hacia la sintaxis formal, asegurando una asimilación técnica sólida y autónoma.

## 2. Características Principales

* **Enfoque pedagógico guiado:** 40 capítulos distribuidos en 9 módulos secuenciales con teoría contextual, retos prácticos y evaluación mediante opciones múltiples nativas (`wx.RadioBox`).
* **Dualidad de trabajo:** Alternancia instantánea entre Modo Aprendizaje Guiado y Modo Editor Autónomo.
* **Independencia técnica:** Basado exclusivamente en módulos de la biblioteca estándar de Python (`sqlite3`, `json`, `math`, `random`, `datetime`), prescindiendo de compiladores de C/C++ o librerías externas inestables.
* **Retroalimentación tiflotécnica:** Indicadores auditivos opcionales para la indentación PEP 8, validación de sintaxis y diagnóstico de fallos en tiempo de ejecución.
* **Entorno de desarrollo accesible:** Autocompletado contextual, formateador PEP 8, analizador de emparejamiento de delimitadores, depurador guiado y consola REPL interactiva.
* **Localización integral:** Compatibilidad bilingüe completa (Español e Inglés) seleccionable desde la configuración.

## 3. Atajos de Teclado

| Atajo | Categoría | Acción |
| :--- | :--- | :--- |
| <kbd>NVDA+Ctrl+Shift+P</kbd> | Global | Abrir o enfocar la ventana del complemento. |
| <kbd>Ctrl+M</kbd> | Modos | Alternar entre Modo Tutor y Modo Editor Autónomo. |
| <kbd>Ctrl+Enter</kbd> | Ejecución | Ejecutar código y verificar solución del reto. |
| <kbd>F5</kbd> | Ejecución | Ejecutar script activo. |
| <kbd>Alt+Flecha Derecha</kbd> | Navegación | Avanzar al siguiente paso de la lección. |
| <kbd>Alt+Flecha Izquierda</kbd> | Navegación | Retroceder al paso anterior de la lección. |
| <kbd>F3</kbd> | Tutor | Verbalizar instrucción activa sin mover el foco. |
| <kbd>Ctrl+P</kbd> | Tutor | Solicitar pista escalonada. |
| <kbd>F1</kbd> | Tutor | Explicar línea de código actual (modo local sin conexión). |
| <kbd>Shift+F1</kbd> | Tutor | Consultar documentación del símbolo bajo el cursor. |
| <kbd>Ctrl+R</kbd> | Tutor | Restablecer código inicial del ejercicio. |
| <kbd>Ctrl+1</kbd> | Tutor | Abrir selector de capítulos y estado de avance. |
| <kbd>Ctrl+J</kbd> | Herramientas | Abrir consola interactiva REPL. |
| <kbd>Ctrl+Shift+I</kbd> | Herramientas | Consultar asistente IA (vía API Gemini). |
| <kbd>F6</kbd> | Navegación | Alternar foco entre editor y consola. |
| <kbd>Ctrl+4</kbd> | Navegación | Mover el foco al editor. |
| <kbd>Ctrl+5</kbd> | Navegación | Mover el foco a la consola de resultados. |
| <kbd>Ctrl+6</kbd> | Consola | Verbalizar la última línea emitida. |
| <kbd>Ctrl+Shift+C</kbd> | Consola | Verbalizar toda la salida acumulada. |
| <kbd>Ctrl+L</kbd> | Edición | Anunciar línea y columna actual. |
| <kbd>Ctrl+N</kbd> | Archivo | Crear nuevo script. |
| <kbd>Ctrl+O</kbd> | Archivo | Abrir archivo `.py` existente. |
| <kbd>Ctrl+S</kbd> | Archivo | Guardar archivo actual. |
| <kbd>Ctrl+Shift+S</kbd> | Archivo | Guardar como. |
| <kbd>Ctrl+F</kbd> | Edición | Buscar texto en el archivo. |
| <kbd>Ctrl+G</kbd> | Edición | Ir a un número de línea específico. |
| <kbd>Ctrl+Espacio</kbd> | Edición | Autocompletado accesible. |
| <kbd>Shift+Alt+F</kbd> | Edición | Dar formato al código según PEP 8. |
| <kbd>Ctrl+/</kbd> | Edición | Alternar comentario de línea (`#`). |
| <kbd>Ctrl+D</kbd> | Edición | Duplicar línea activa. |
| <kbd>Ctrl+Shift+K</kbd> | Edición | Eliminar línea activa. |
| <kbd>Ctrl+Shift+R</kbd> | Refactor | Extraer bloque seleccionado a una nueva función. |
| <kbd>F2</kbd> | Refactor | Renombrar identificador en el archivo. |
| <kbd>Ctrl+Shift+O</kbd> | Estructura | Listar funciones y clases del archivo. |
| <kbd>Alt+N</kbd> | Estructura | Saltar a siguiente función o clase. |
| <kbd>Alt+P</kbd> | Estructura | Saltar a anterior función o clase. |
| <kbd>F7</kbd> | Diagnóstico | Verificar delimitadores y sintaxis. |
| <kbd>F4</kbd> | Diagnóstico | Ubicar cursor en línea del error indicado en consola. |
| <kbd>F9</kbd> | Depuración | Conmutar punto de interrupción (breakpoint). |
| <kbd>F10</kbd> | Depuración | Iniciar depuración interactiva paso a paso. |
| <kbd>Ctrl+T</kbd> | Pruebas | Ejecutar suite de pruebas unitarias. |
| <kbd>Ctrl+Shift+P</kbd> | Entorno | Gestionar intérpretes y entornos virtuales. |
| <kbd>Ctrl+Shift+E</kbd> | Herramientas | Explorador accesible de proyectos. |
| <kbd>F11</kbd> | Ayuda | Ver diálogo de atajos de teclado. |
| <kbd>F12</kbd> | Ayuda | Abrir esta documentación en el navegador. |
| <kbd>Escape</kbd> | General | Cerrar ventana o cuadro de diálogo activo. |

## 4. Plan Formativo Integral (40 Capítulos)

### Módulo 0: Fundamentos de la Computación (Capítulos 1 a 5)
* **Capítulo 1:** Arquitectura de computadores, sistema binario y memoria.
* **Capítulo 2:** Compiladores, intérpretes y ejecución de código.
* **Capítulo 3:** Historia y principios del Zen de Python.
* **Capítulo 4:** Lectores de pantalla y desarrollo accesible con NVDA.
* **Capítulo 5:** Lógica algorítmica y métodos de depuración.

### Módulo 1: Salida, Memoria y Variables (Capítulos 6 a 9)
* **Capítulo 6:** Flujos de salida estándar y función `print()`.
* **Capítulo 7:** Almacenamiento en memoria y asignación de variables.
* **Capítulo 8:** Documentación y estándares de comentarios.
* **Capítulo 9:** Reasignación y ciclo de vida de los datos.

### Módulo 2: Tipos Fundamentales e Interacción (Capítulos 10 a 14)
* **Capítulo 10:** Números enteros (`int`) y aritmética básica.
* **Capítulo 11:** Números decimales (`float`) y precisión matemática.
* **Capítulo 12:** Cadenas de texto (`str`) y secuencias de escape.
* **Capítulo 13:** Interpolación moderna con f-strings.
* **Capítulo 14:** Entrada de datos con `input()` y conversión de tipos.

### Módulo 3: Lógica Booleana y Control de Flujo (Capítulos 15 a 19)
* **Capítulo 15:** Tipo booleano (`bool`) y operadores relacionales.
* **Capítulo 16:** Conectores lógicos (`and`, `or`, `not`).
* **Capítulo 17:** Condicionales: sentencia `if` y sangrado PEP 8.
* **Capítulo 18:** Bifurcaciones alternativas: sentencia `else`.
* **Capítulo 19:** Condiciones múltiples: sentencia `elif`.

### Módulo 4: Bucles e Iteraciones (Capítulos 20 a 23)
* **Capítulo 20:** Bucles definidos: sentencia `for` y función `range()`.
* **Capítulo 21:** Bucles basados en condición: sentencia `while`.
* **Capítulo 22:** Control de ejecución y prevención de bloqueos.
* **Capítulo 23:** Sentencias `break`, `continue` y cláusula `else` en bucles.

### Módulo 5: Estructuras de Datos (Capítulos 24 a 28)
* **Capítulo 24:** Listas mutables y direccionamiento indexado.
* **Capítulo 25:** Operaciones esenciales: `append`, `insert`, `remove` y `pop`.
* **Capítulo 26:** Recorridos eficientes con `enumerate()`.
* **Capítulo 27:** Tuplas inmutables y desempaquetado de secuencias.
* **Capítulo 28:** Diccionarios y estructuras clave-valor.

### Módulo 6: Modularidad, Funciones y Excepciones (Capítulos 29 a 32)
* **Capítulo 29:** Definición de subrutinas mediante `def` y paso de parámetros.
* **Capítulo 30:** Retorno de datos: `return` frente a salida estándar.
* **Capítulo 31:** Ámbito y visibilidad de variables (local vs. global).
* **Capítulo 32:** Gestión de errores mediante bloques `try`, `except` y `finally`.

### Módulo 7: Persistencia y Programación Orientada a Objetos (Capítulos 33 a 36)
* **Capítulo 33:** Manejo seguro de archivos de texto con `with open()`.
* **Capítulo 34:** Serialización e intercambio de datos con JSON.
* **Capítulo 35:** Clases, instancias y modelado orientado a objetos.
* **Capítulo 36:** Encapsulamiento, método `__init__` y parámetro `self`.

### Módulo 8: Biblioteca Estándar y Proyecto Final (Capítulos 37 a 40)
* **Capítulo 37:** Utilidades estándar: `math`, `random` y `datetime`.
* **Capítulo 38:** Gestión de bases de datos relacionales con `sqlite3`.
* **Capítulo 39:** Interfaces auditivas y diseño de software accesible.
* **Capítulo 40:** Proyecto integrador: Aplicación accesible de gestión de datos.

## 5. Configuración

Disponible en **Menú NVDA > Preferencias > Opciones > Aprendizaje de Python con NVDA**:

* **Idioma:** Selección entre detección automática (según NVDA), Español o Inglés.
* **Modo predeterminado:** Selección del modo activo al iniciar la sesión (Tutor o Editor).
* **Señales auditivas:** Activación de tonos para comprobación y niveles de sangría.
* **Clave de API Gemini:** Permite habilitar el asistente pedagógico interactivo con IA (<kbd>Ctrl+Shift+I</kbd>). El explicador local (<kbd>F1</kbd>) opera de forma autónoma sin necesidad de clave.

## 6. Registro de Cambios

### Versión 1.0.0
* Lanzamiento inicial oficial.

## 7. Soporte

Para notificar incidencias o proponer mejoras, puede utilizar los siguientes canales:

* **Correo de contacto:** [kevinvelasquezvargas@gmail.com](mailto:kevinvelasquezvargas@gmail.com)
* **Seguimiento de problemas:** [Rastreador de incidencias en GitHub](https://github.com/KevinVelasquezVargas/python_tutor/issues)

## 8. Colaboración

Aprendizaje de Python con NVDA es un proyecto libre, gratuito y sin fines de lucro, desarrollado con el compromiso de ofrecer igualdad de oportunidades en la formación tecnológica inclusiva. Si este complemento resulta valioso para su aprendizaje, docencia o desarrollo profesional, puede realizar una contribución voluntaria para apoyar su mantenimiento y la creación de futuros recursos formativos accesibles:

* **Realizar una donación vía PayPal:** [https://paypal.me/kevinvelasquezvargas](https://paypal.me/kevinvelasquezvargas)

---

Copyright © 2026 Kevin Andrés Velasquez Vargas. Distribuido bajo la Licencia Pública General de GNU v3.0 (GPLv3).
