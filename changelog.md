# Registro de cambios de Aprendizaje de Python con NVDA

## Versión 2.0.0
- **Dualidad de Uso (Modo Aprendizaje guiado vs. Modo Editor autónomo):**
  - Conmutación ágil mediante `Control + M` o desde el menú *Herramientas*.
  - *Modo Aprendizaje:* Entorno guiado paso a paso con consignas pedagógicas, pistas escalonadas y evaluación automatizada de ejercicios.
  - *Modo Editor autónomo:* Entorno profesional limpio que desactiva y oculta por completo las cajas didácticas, dejando una navegación por tabulación limpia y directa entre editor, consola y botones principales.
  - Ajuste persistente en las Preferencias de NVDA para iniciar opcionalmente en el Modo Editor autónomo.
- **Navegación de Pasos y Compatibilidad con NVDA:**
  - Desplazamiento entre pasos mediante `Alt + Flecha Derecha` (siguiente) y `Alt + Flecha Izquierda` (anterior), preservando `Control + Flechas` para la lectura palabra por palabra nativa del lector de pantalla.
  - Desbloqueo progresivo de capítulos: para acceder a un nuevo capítulo es requisito haber superado todas las lecciones del capítulo previo.
- **Herramientas de Edición y Navegación de Código:**
  - **Búsqueda y Desplazamiento Rápido:** Diálogos accesibles para buscar texto (`Control + F`) e ir directamente a una línea (`Control + G`).
  - **Gestión de Archivos:** Opciones de nuevo script (`Control + N`), abrir archivo (`Control + O`), guardar (`Control + S`) y guardar como (`Control + Shift + S`).
  - **Navegación Estructural Directa:** Salto entre cabeceras de funciones (`def`) y clases (`class`) con `Alt + N` (siguiente) y `Alt + P` (anterior).
  - **Diálogo de Símbolos (`Control + Shift + O`):** Lista todas las funciones y clases del archivo con su número de línea para saltar de forma instantánea.
  - **Salto al Error del Traceback (`F4`):** Desplaza el cursor de inmediato a la línea exacta del fallo de ejecución o compilación con anuncio sonoro y diagnóstico por voz.
  - **Balanceador de Delimitadores en Tiempo Real (`F7` y al ejecutar):** Comprobación preventiva de paréntesis `()`, corchetes `[]`, llaves `{}` y comillas sin cerrar.
  - **Lectura No Invasiva de Consola:** `Control + Shift + C` para verbalizar toda la salida sin mover el cursor del editor, y `Control + 6` para leer la última línea.
  - **Consola con Formato Natural:** Eliminación de banners decorativos y símbolos gráficos; presentación de salidas, avisos y resultados en lenguaje limpio y comprensible.
- **Plan Formativo Ampliado a 32 Capítulos (128 Lecciones) con «Conceptos Primero»:**
  - *Fase 0 (Capítulos 1 a 3):* Pensamiento computacional, algoritmos cotidianos, arquitectura computacional y lógica booleana elemental.
  - *Fase 1 (Capítulos 4 a 8):* Salida con `print`, variables en memoria, tipos numéricos enteros/flotantes, cadenas (`str`) y entrada de usuario (`input`).
  - *Fase 2 (Capítulos 9 a 16):* Comparaciones relacionales, condicionales `if` con sangría PEP 8, ramas `elif`/`else`, listas mutables, bucles `for`/`range`, `while` y diccionarios clave-valor.
  - *Fase 3 (Capítulos 17 a 22):* Tuplas y conjuntos (`set`), funciones modulares con `def`, retorno con `return` y ámbito (`scope`), control de excepciones con `try`/`except`, lectura de Tracebacks y gestión de archivos con `with open`.
  - *Fase 4 (Capítulos 23 a 27):* Programación Orientada a Objetos: clases, atributos, `__init__`, `self`, métodos de instancia, herencia con `super()` y representación textual con `__str__`.
  - *Fase 5 (Capítulos 28 a 32):* Librerías estándar (`math`, `random`, `datetime`), serialización JSON, persistencia SQLite3, APIs REST y pruebas unitarias con `unittest`.
- **Experiencia de Usuario Optimizada:**
  - Diálogo de bienvenida simplificado y cordial, derivando la consulta detallada de atajos a la tecla `F2` y a la opción *Acerca de*.
  - Integración limpia en la barra de menús sin menús redundantes de configuración.
  - Diccionario técnico interactivo con 43 conceptos y buscador en tiempo real.
  - Traductor a lenguaje cotidiano (`F1`), linter acústico PEP 8 y consola REPL (`Control + J`).
  - Cierre inmediato con la tecla `Escape` desde cualquier control.
  - Adaptación canónica a la plantilla oficial AddonTemplate 2026 y soporte verificado desde NVDA 2022.1.0 hasta 2026.3.0.

## Versión 1.0.0
- Versión inicial con temario básico de fundamentos y ejecución interactiva en NVDA.
