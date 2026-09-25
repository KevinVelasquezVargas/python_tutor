# Aprendizaje de Python con NVDA

Herramienta formativa y editor de código adaptado para la programación en Python mediante NVDA. Proporciona una ruta de aprendizaje estructurada en 32 lecciones conceptuales y prácticas, complementada con un entorno de trabajo de doble modalidad: modo tutor guiado y modo editor autónomo. Integra navegación por elementos de código como funciones y clases, señales sonoras de sangría y estructura, verificación de delimitadores y simplificación de mensajes de error.

* **Versión:** 2.0.0
* **Autor:** Kevin Andrés Velasquez Vargas
* **Compatibilidad:** NVDA 2022.1.0 hasta 2026.3.0
* **Licencia:** GNU General Public License v3.0 (GPLv3)
* **Repositorio:** https://github.com/KevinVelasquezVargas/python_tutor

---

## 1. Introducción
**Aprendizaje de Python con NVDA** es un complemento integral diseñado para eliminar las barreras de accesibilidad que experimentan las personas con discapacidad visual al aprender y escribir código en Python.

Combina una pedagogía activa no visual (*«Conceptos Primero»*, micro-retos, preguntas conceptuales y explicaciones cotidianas) con un editor tiflotécnico profesional libre de distracciones.

## 2. Iniciar el complemento
- **Atajo global:** `NVDA + Control + Shift + P`
- **Menú de NVDA:** Menú NVDA (`NVDA + N`) > *Herramientas* > *Aprendizaje de Python con NVDA* > *Aprendizaje de Python con NVDA...*

## 3. Dualidad de Uso
Pulsando `Control + M` (o desde el menú *Herramientas*) puede alternar en cualquier instante entre:
- **Modo Aprendizaje:** Entorno guiado paso a paso con consignas didácticas, pistas escalonadas y evaluación automatizada de ejercicios.
- **Modo Editor autónomo:** Entorno limpio de edición profesional sin secciones pedagógicas. Maximiza el área de trabajo para escribir, depurar y ejecutar scripts propios con todas las herramientas tiflotécnicas activas y navegación fluida por tabulación.

## 4. Navegación y Herramientas del Editor
* **Navegación de Lecciones:**
  - `Alt + Flecha Derecha`: Ir al siguiente paso de la lección.
  - `Alt + Flecha Izquierda`: Ir al paso anterior de la lección.
  - *(Nota: Las combinaciones `Control + Flechas` quedan totalmente libres para permitir la lectura palabra por palabra nativa de NVDA).*
* **Navegación Estructural Directa:**
  - `Alt + N` / `Alt + P`: Saltar a la cabecera de la siguiente o anterior función (`def`) o clase (`class`).
  - `Control + Shift + O`: Diálogo accesible de símbolos para listar todas las funciones y clases y saltar a ellas al instante.
* **Búsqueda y Desplazamiento:**
  - `Control + F`: Diálogo accesible para buscar texto en el editor.
  - `Control + G`: Diálogo accesible para ir directamente a un número de línea.
* **Gestión de Archivos:**
  - `Control + N`: Crear un nuevo script limpio en el editor.
  - `Control + O`: Abrir un archivo Python (`.py`) existente.
  - `Control + S`: Guardar el script actual.
  - `Control + Shift + S`: Guardar script con un nuevo nombre o ubicación.
* **Diagnóstico y Corrección:**
  - `F4`: Salto inmediato a la línea exacta del fallo del Traceback o error de sintaxis con lectura accesible del problema.
  - `F7`: Verificación en tiempo real de balanceo de delimitadores `()`, `[]`, `{}` y comillas sin cerrar.
* **Lectura No Invasiva de Consola:**
  - `Control + Shift + C`: Lee por voz toda la salida de consola sin mover el cursor del editor.
  - `Control + 6`: Lee la última línea emitida en la consola.
  - `F6`: Alterna el foco físico entre el editor y la consola de resultados.
* **Traductor a Lenguaje Cotidiano (`F1`):** Explica la línea de código donde se encuentra el cursor en palabras humanas y sencillas.
* **Señales Sonoras y Sangría PEP 8:** Emite señales sonoras en tiempo real para indicar niveles de sangría (0, 4, 8, 12 espacios) y apertura de bloques sintácticos con `:`.
* **Edición Eficiente:**
  - `Control + /` (o `Control + K`): Comentar o descomentar línea.
  - `Control + D`: Duplicar línea actual hacia abajo.
  - `Control + Shift + K`: Eliminar línea actual.
  - `Control + L`: Anunciar línea y columna actual del cursor.
  - `Control + Espacio`: Autocompletar palabras clave de Python.
* **Herramientas de Apoyo:**
  - `Control + J`: Consola de pruebas rápidas (REPL).
  - `Control + 1`: Selector de capítulos del temario (con control de desbloqueo progresivo).
  - `Control + R`: Restablecer código inicial del ejercicio.
  - `F2`: Guía completa de atajos de teclado.
  - `F12`: Abrir manual accesible en el navegador web.
  - `Escape`: Cerrar la ventana del tutor inmediatamente desde cualquier control.

## 5. Plan Formativo (32 Capítulos / 128 Lecciones Prácticas)
* **Fase 0: Fundamentos Conceptuales:** Pensamiento computacional, algoritmos cotidianos, memoria y procesador, lógica booleana elemental (Capítulos 1 a 3).
* **Fase 1: Sintaxis Básica y Tipos Elementales:** Primer `print`, variables, números enteros/flotantes, cadenas (`str`), entrada del usuario con `input` (Capítulos 4 a 8).
* **Fase 2: Control de Flujo y Colecciones:** Condiciones relacionales, `if` y sangría PEP 8, `elif`/`else`, listas, métodos mutables, bucles `for`/`range`, `while`, diccionarios clave-valor (Capítulos 9 a 16).
* **Fase 3: Modularidad, Robustez y Archivos:** Tuplas y conjuntos (`set`), funciones con `def`, retorno con `return` y ámbito (`scope`), manejo de excepciones (`try`/`except`), lectura accesible de Tracebacks, archivos con `with open` (Capítulos 17 a 22).
* **Fase 4: Programación Orientada a Objetos (POO):** Clases y atributos, constructor `__init__` y `self`, métodos de instancia, herencia con `super()`, representación textual con `__str__` (Capítulos 23 a 27).
* **Fase 5: Desarrollo Profesional y Pruebas:** Librerías estándar (`math`, `random`, `datetime`), intercambio de datos con JSON, bases de datos con SQLite3, consumo de APIs REST, pruebas unitarias con `unittest` (Capítulos 28 a 32).

## 6. Opciones y Configuración en NVDA
En `Menú NVDA > Preferencias > Opciones > Aprendizaje de Python con NVDA`:
* Iniciar en Modo Editor autónomo (ocultar lecciones del tutor).
* Efectos sonoros de confirmación y eventos.
* Avisos sonoros de sangría y estructura.
* Mostrar diálogo de bienvenida al iniciar el complemento.

## 7. Soporte y Donaciones
* **Consultas e incidencias:** [Repositorio GitHub del proyecto](https://github.com/KevinVelasquezVargas/python_tutor/issues)
* **Colaboraciones voluntarias:** Disponibles en el menú *Herramientas > Aprendizaje de Python con NVDA > Realizar una donación...* o a través de [PayPal](https://www.paypal.me/kevinvelasquezvargas).
