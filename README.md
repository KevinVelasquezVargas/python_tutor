# Aprendizaje de Python con NVDA

[![Versión](https://img.shields.io/github/v/release/KevinVelasquezVargas/python_tutor?label=Versi%C3%B3n&color=blue)](https://github.com/KevinVelasquezVargas/python_tutor/releases/latest)
[![Compatibilidad NVDA](https://img.shields.io/badge/NVDA-2022.1%20a%202026.2-005a9c)](https://github.com/KevinVelasquezVargas/python_tutor)
[![Licencia](https://img.shields.io/badge/Licencia-GPL%20v3-green)](COPYING.txt)
[![Pruebas Unitarias](https://github.com/KevinVelasquezVargas/python_tutor/actions/workflows/unitTests.yml/badge.svg)](https://github.com/KevinVelasquezVargas/python_tutor/actions)
[![Descargas](https://img.shields.io/github/downloads/KevinVelasquezVargas/python_tutor/total?label=Descargas&color=orange)](https://github.com/KevinVelasquezVargas/python_tutor/releases)

> 📥 **Descarga Directa del Instalador Oficial:**  
> [**Descargar python_tutor-2.0.0.nvda-addon (856 KB)**](https://github.com/KevinVelasquezVargas/python_tutor/releases/download/v2.0.0/python_tutor-2.0.0.nvda-addon)  
> *(Descarga directa lista para instalar en NVDA simplemente abriendo el archivo o pulsando Enter sobre él)*

Herramienta formativa y editor de código adaptado para la programación en Python mediante NVDA. Proporciona una ruta de aprendizaje estructurada en 32 capítulos conceptuales y prácticos (128 lecciones), complementada con un entorno de trabajo de doble modalidad: modo tutor guiado y modo editor autónomo. Integra navegación por elementos de código como funciones y clases, señales sonoras de sangría y estructura, verificación de delimitadores y simplificación de mensajes de error.

* **Versión:** 2.0.0
* **Autor:** Kevin Andrés Velasquez Vargas
* **Compatibilidad:** NVDA 2022.1.0 hasta 2026.2.0
* **Licencia:** GNU General Public License v3.0 (GPLv3)
* **Repositorio:** [Visitar el repositorio oficial en GitHub](https://github.com/KevinVelasquezVargas/python_tutor)

---

## Tabla de Contenidos
* [1. Introducción](#1-introducción)
* [2. Iniciar el complemento](#2-iniciar-el-complemento)
* [3. Dualidad de Uso](#3-dualidad-de-uso)
* [4. Navegación y Herramientas del Editor](#4-navegación-y-herramientas-del-editor)
* [5. Plan Formativo (32 Capítulos y 128 Lecciones)](#5-plan-formativo)
* [6. Configuración y Preferencias](#6-configuración)
* [7. Registro de Novedades](#7-registro-de-novedades)
* [8. Soporte](#8-soporte)
* [9. Donaciones](#9-donaciones)

---

## 1. Introducción
Aprendizaje de Python con NVDA es un complemento integral diseñado para eliminar las barreras de accesibilidad que experimentan las personas con discapacidad visual al aprender y escribir código en Python.

Combina una pedagogía activa no visual («Conceptos Primero», micro-retos, preguntas conceptuales y explicaciones cotidianas) con un editor tiflotécnico profesional, enfocado y libre de distracciones.

## 2. Iniciar el complemento
* **Atajo global:** `NVDA + Control + Shift + P`
* **Menú de NVDA:** Menú NVDA (`NVDA + N`) > Herramientas > Aprendizaje de Python con NVDA > Aprendizaje de Python con NVDA...

## 3. Dualidad de Uso
Pulsando `Control + M` (o desde el menú Herramientas) se puede alternar en cualquier instante entre:

* **Modo Aprendizaje:** Entorno guiado paso a paso con consignas didácticas, pistas escalonadas y evaluación automatizada de ejercicios.
* **Modo Editor autónomo:** Entorno limpio de edición sin secciones pedagógicas. Maximiza el área de trabajo para escribir, depurar y ejecutar scripts propios con todas las herramientas tiflotécnicas activas y navegación fluida por tabulación.

## 4. Navegación y Herramientas del Editor

### Navegación de Lecciones
* `Alt + Flecha Derecha`: Ir al siguiente paso de la lección.
* `Alt + Flecha Izquierda`: Ir al paso anterior de la lección.

### Navegación Estructural Directa
* `Alt + N` / `Alt + P`: Saltar a la cabecera de la siguiente o anterior función (`def`) o clase (`class`).
* `Control + Shift + O`: Diálogo accesible de símbolos para listar todas las funciones y clases y saltar a ellas al instante.

### Búsqueda y Desplazamiento
* `Control + F`: Diálogo accesible para buscar texto en el editor.
* `Control + G`: Diálogo accesible para ir directamente a un número de línea.

### Gestión de Archivos
* `Control + N`: Crear un nuevo script limpio en el editor.
* `Control + O`: Abrir un archivo Python (`.py`) existente.
* `Control + S`: Guardar el script actual.
* `Control + Shift + S`: Guardar script con un nuevo nombre o ubicación.

### Ejecución y Diagnóstico
* `F5`: Ejecutar el script actual en la consola integrada.
* `F4`: Salto inmediato a la línea exacta del fallo del Traceback o error de sintaxis con lectura accesible del problema.
* `F7`: Verificación en tiempo real de balanceo de delimitadores `()`, `[]`, `{}` y comillas sin cerrar.

### Lectura No Invasiva de Consola
* `Control + Shift + C`: Leer por voz toda la salida de consola sin mover el cursor del editor.
* `Control + 6`: Leer la última línea emitida en la consola.
* `F6`: Alternar el foco físico entre el editor y la consola de resultados.

### Asistencia de Código y Señales Acústicas
* `F1` (Traductor a Lenguaje Cotidiano): Explica la línea de código donde se encuentra el cursor en lenguaje natural y sencillo.
* **Señales sonoras de sangría PEP 8:** Emite tonos en tiempo real para indicar niveles de sangría (0, 4, 8, 12 espacios) y la apertura de bloques sintácticos tras dos puntos (`:`).

### Edición Eficiente
* `Control + /` (o `Control + K`): Comentar o descomentar la línea actual.
* `Control + D`: Duplicar la línea actual hacia abajo.
* `Control + Shift + K`: Eliminar la línea actual.
* `Control + L`: Anunciar línea y columna actual del cursor.
* `Control + Espacio`: Autocompletar palabras clave de Python.

### Herramientas de Apoyo
* `Control + J`: Abrir la consola de pruebas rápidas (REPL).
* `Control + 1`: Selector de capítulos del temario (con control de desbloqueo progresivo).
* `Control + R`: Restablecer el código inicial del ejercicio.
* `F2`: Diálogo con la guía completa de atajos de teclado.
* `F12`: Abrir el manual accesible en el navegador web.
* `Escape`: Cerrar la ventana del tutor inmediatamente desde cualquier control.

## 5. Plan Formativo
* **Fase 0: Fundamentos Conceptuales:** Pensamiento computacional, algoritmos cotidianos, memoria y procesador, lógica booleana elemental (Capítulos 1 a 3).
* **Fase 1: Sintaxis Básica y Tipos Elementales:** Primer print, variables, números enteros y flotantes, cadenas de texto (`str`), entrada del usuario con input (Capítulos 4 a 8).
* **Fase 2: Control de Flujo y Colecciones:** Condiciones relacionales, if y sangría PEP 8, elif/else, listas, métodos mutables, bucles for/range, while, diccionarios clave-valor (Capítulos 9 a 16).
* **Fase 3: Modularidad, Robustez y Archivos:** Tuplas y conjuntos (`set`), funciones con def, retorno con return y ámbito (scope), manejo de excepciones (try/except), lectura accesible de Tracebacks, gestión de archivos con with open (Capítulos 17 a 22).
* **Fase 4: Programación Orientada a Objetos (POO):** Clases y atributos, constructor `__init__` y parámetro self, métodos de instancia, herencia con super(), representación textual con `__str__` (Capítulos 23 a 27).
* **Fase 5: Desarrollo Profesional y Pruebas:** Librerías estándar (math, random, datetime), intercambio de datos con JSON, bases de datos locales con SQLite3, consumo de APIs REST, pruebas unitarias con unittest (Capítulos 28 a 32).

## 6. Configuración
Para personalizar el comportamiento del complemento, diríjase a **Menú NVDA > Preferencias > Opciones > Aprendizaje de Python con NVDA**:

* **Iniciar en Modo Editor autónomo:** Abre directamente el área de edición pura, ocultando las secciones de lecciones del tutor.
* **Efectos sonoros de confirmación y eventos:** Activa o desactiva los tonos al evaluar ejercicios o cambiar de estado.
* **Avisos sonoros de sangría y estructura:** Controla las señales acústicas de espacios de sangría y apertura de bloques.
* **Mostrar diálogo de bienvenida:** Configura si se debe mostrar el mensaje informativo al arrancar el complemento.

## 7. Registro de Novedades

### Versión 2.0.0
* **Incorporación de la Dualidad de Uso:** Posibilidad de alternar con `Control + M` entre el Modo Aprendizaje y el nuevo Modo Editor autónomo para trabajo libre sin distracciones.
* **Ampliación sustancial del temario:** Expansión a 32 capítulos y 128 lecciones prácticas, cubriendo desde lógica computacional hasta POO, SQLite3, APIs REST y pruebas unitarias con unittest.
* **Navegación estructural avanzada:** Implementación de atajos (`Alt + N` / `Alt + P`) y visor de símbolos (`Control + Shift + O`) para saltar rápidamente entre funciones y clases.
* **Diagnóstico y corrección en tiempo real:** Verificación de balanceo de delimitadores y comillas (`F7`) y salto directo a líneas con error en Tracebacks (`F4`).
* **Optimización de lectura de consola:** Modos de lectura no invasivos por sintetizador (`Control + Shift + C` y `Control + 6`).
* **Actualización del motor de compatibilidad:** Soporte extendido para versiones modernas de NVDA (hasta 2026.2.0).

### Versión 1.0.0
* Versión inicial con temario básico de fundamentos y ejecución interactiva en NVDA.

## 8. Soporte
Si deseas reportar un error, proponer una nueva funcionalidad, compartir sugerencias pedagógicas o requieres orientación sobre el uso del complemento, puedes comunicarte a través de los siguientes canales:

* **Correo electrónico:** [Enviar un mensaje de correo electrónico de soporte](mailto:kevinvelasquezvargas@gmail.com?subject=Soporte%20-%20Aprendizaje%20de%20Python%20con%20NVDA)
* **Gestión de incidencias:** [Acceder al sistema de incidencias en GitHub](https://github.com/KevinVelasquezVargas/python_tutor/issues)

## 9. Donaciones
Este proyecto se distribuye de manera libre y gratuita bajo la filosofía del software de código abierto, con el compromiso de garantizar el acceso equitativo a la educación en programación para personas con discapacidad visual.

Si este complemento te ha sido de utilidad en tu proceso de aprendizaje o enseñanza y deseas respaldar su mantenimiento continuo, desarrollo de nuevos módulos y actualización permanente:

* **Enlace directo:** [Realizar una donación voluntaria en PayPal](https://paypal.me/kevinvelasquezvargas)

---

Copyright © 2026 Kevin Andrés Velasquez Vargas.
