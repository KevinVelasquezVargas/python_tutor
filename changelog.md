# Registro de cambios de Aprendizaje de Python con NVDA

## Versión 2.0.0
- **Dualidad de Uso (Modo Aprendizaje vs. Modo Solo Editor):**
  - Conmutación ágil mediante `Control + M` o desde el menú de opciones/configuración.
  - *Modo Aprendizaje:* Entorno guiado paso a paso con consignas pedagógicas, pistas escalonadas y evaluación automatizada de ejercicios.
  - *Modo Solo Editor:* Entorno profesional limpio que oculta las cajas de consignas didácticas y maximiza el espacio para programar y depurar scripts libres con todas las herramientas tiflotécnicas.
  - Ajuste persistente en las Preferencias de NVDA para iniciar opcionalmente directo en el Modo Solo Editor.
- **Herramientas Tiflotécnicas de Edición de Alto Rendimiento:**
  - **Navegación Estructural Directa:** Salto entre definiciones de funciones (`def`) y clases (`class`) mediante `Alt + N` (siguiente) y `Alt + P` (anterior).
  - **Diálogo de Símbolos (`Control + Shift + O`):** Lista todas las funciones y clases del archivo con su número de línea para saltar de forma instantánea.
  - **Salto Inmediato al Error del Traceback (`F4`):** Desplaza el cursor de inmediato a la línea exacta del fallo de ejecución o error de compilación y anuncia el diagnóstico por voz y braille.
  - **Balanceador de Delimitadores en Tiempo Real (`F7` y al ejecutar):** Detección preventiva de paréntesis `()`, corchetes `[]`, llaves `{}` y comillas simples o dobles sin cerrar.
  - **Lectura No Invasiva de Consola:** `Control + Shift + C` para verbalizar toda la salida de consola sin mover el cursor del editor, y `Control + 6` para leer la última línea.
- **Plan Formativo Ampliado a 32 Capítulos (128 Micro-pasos) con «Conceptos Primero»:**
  - *Fase 0 (Capítulos 1 a 3):* Pensamiento computacional, algoritmos de la vida cotidiana, arquitectura de computadoras y lógica booleana elemental.
  - *Fase 1 (Capítulos 4 a 8):* Salida con `print`, variables en memoria, tipos numéricos enteros/decimales, cadenas de texto (`str`) y entrada del usuario (`input`).
  - *Fase 2 (Capítulos 9 a 16):* Comparaciones relacionales, condicionales `if` con sangría PEP 8, ramas `elif`/`else`, listas y métodos mutables, bucles `for`/`range`, `while` y diccionarios asociativos.
  - *Fase 3 (Capítulos 17 a 22):* Tuplas y conjuntos (`set`), funciones modulares con `def`, retorno con `return` y ámbito (`scope`), control de excepciones con `try`/`except`, lectura no visual de Tracebacks y gestión de archivos con `with open`.
  - *Fase 4 (Capítulos 23 a 27):* Programación Orientada a Objetos: clases, atributos, `__init__`, `self`, métodos de instancia, herencia con `super()` y representación textual accesible con `__str__`.
  - *Fase 5 (Capítulos 28 a 32):* Librerías estándar (`math`, `random`, `datetime`), intercambio de datos con JSON, persistencia con SQLite3, consumo de APIs REST y calidad de software mediante pruebas unitarias con `unittest`.
- **Diccionario Técnico Ampliado:** 43 conceptos y palabras reservadas de Python con explicaciones accesibles y buscador en tiempo real (`Control + G`).
- **Traductor a Lenguaje Humano (`F1`):** Explica en lenguaje cotidiano la línea de código donde está situado el cursor.
- **Linter Acústico PEP 8:** Señales auditivas diferenciadas para niveles de sangría (0, 4, 8, 12 espacios) y confirmación de apertura de bloques con dos puntos (`:`).
- **Consola de Pruebas Rápidas (REPL - `Control + J`):** Entorno emergente para evaluar expresiones de Python al vuelo.
- **Edición Ágil:** Comentar/descomentar (`Control + /`), duplicar línea (`Control + D`), eliminar línea (`Control + Shift + K`), mover líneas (`Alt + Arriba/Abajo`), anunciar posición (`Control + L`) y autocompletado (`Control + Espacio`).
- **Detección Preventiva de Escritura:** Alertas inmediatas ante caracteres incompatibles de teclado (tildes agudas, comillas tipográficas, etc.).
- **Manual en Formato HTML (`F12`):** Documentación completa estructurada semánticamente para su lectura en cualquier navegador web.
- **Integración en Herramientas de NVDA:** Accesos directos al tutor, soporte por correo y colaboraciones voluntarias.
- **Cierre Inmediato:** Tecla `Escape` cierra limpiamente la ventana desde cualquier control.
- **Estructura Oficial AddonTemplate 2026:** Adaptación canónica a la plantilla oficial de complementos de NVDA con herramientas SCons, pre-commit, dependabot y workflows CI/CD.
- **Compatibilidad Verificada:** Soporte garantizado desde NVDA 2022.1.0 hasta NVDA 2026.3.0.

## Versión 1.0.0
- Versión inicial con temario básico de fundamentos y ejecución interactiva en NVDA.
