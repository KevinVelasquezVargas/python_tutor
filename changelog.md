# Registro de cambios de Aprendizaje de Python con NVDA

## Versión 3.0.0

- **Plan Formativo Insignia de 40 Capítulos (160 Lecciones Progresivas):**
  - Estructurado bajo la rigurosa metodología pedagógica *«Conceptos Primero»*, iniciando con fundamentos computacionales, arquitectura de hardware, sistema binario, ciclo de ejecución de la CPU e interacción tiflotécnica antes de avanzar hacia la sintaxis formal.
  - Progresión sistemática desde tipos fundamentales y estructuras de control hasta Programación Orientada a Objetos (POO), manejo seguro de archivos, excepciones, base de datos relacional SQLite3, formatos estructurados JSON y módulos de la biblioteca estándar (`math`, `random`, `datetime`, `urllib`).
- **Navegación Flexible del Temario y Desbloqueo Bajo Demanda (<kbd>F6</kbd>):**
  - Diálogo accesible de selección de capítulos con capacidad de acceder directamente a cualquier lección avanzada mediante confirmación explícita, ideal para usuarios experimentados o reanudación de estudios.
- **Persistencia Robusta en Perfil de Usuario de NVDA:**
  - Almacenamiento seguro del progreso en el directorio de configuración de NVDA (`python_tutor/progress.json`), garantizando la preservación total de los avances formativos frente a actualizaciones del complemento.
  - Migración automática y no destructiva de archivos de configuración de versiones anteriores.
- **Dualidad Operativa Perfeccionada (Modo Tutor vs. Modo Editor Autónomo):**
  - Conmutación instantánea mediante el atajo exclusivo <kbd>Control + M</kbd> o desde el menú *Herramientas*.
  - Anuncios acústicos diferenciados mediante síntesis y campanas armónicas de transición.
  - *Modo Aprendizaje:* Entorno guiado paso a paso con consignas pedagógicas, pistas escalonadas y evaluación automatizada de ejercicios.
  - *Modo Editor autónomo:* Entorno profesional de trabajo sin paneles didácticos, con navegación fluida y directa entre el área de edición, consola de salida y controles principales.
- **Interfaz Adaptativa por Contexto Pedagógico:**
  - Ocultación automática del editor de código en lecciones puramente teóricas y en cuestionarios de autoevaluación.
  - Selector nativo accesible (`wx.ListBox`) para preguntas de opción múltiple, con retroalimentación inmediata sobre la opción seleccionada.
- **Asistente Didáctico con Inteligencia Artificial (Google Gemini API):**
  - Integración accesible de consultas didácticas contextuales mediante <kbd>Control + Shift + I</kbd>.
  - Explicador de código offline autónomo mediante la tecla <kbd>F1</kbd>, sin requerir conexión a internet ni claves externas.
  - Clave de API de Gemini configurable de forma segura a través del panel de preferencias de NVDA.
- **Soporte Multilingüe Oficial (Español e Inglés):**
  - Localización completa de la interfaz de usuario, menús, diálogos, atajos de teclado y mensajes del sistema (*Learning Python with NVDA*).
  - Ejercicios y códigos iniciales bilingües según el idioma seleccionado.
- **Entorno de Edición y Diagnóstico Tiflotécnico:**
  - Linter acústico en tiempo real para sangría PEP 8 y advertencias de sintaxis.
  - Verificación preventiva de balanceo de delimitadores (<kbd>F7</kbd>).
  - Salto directo a la línea de error del Traceback con <kbd>F4</kbd>.
  - Formateador automático de código según PEP 8 (<kbd>Shift + Alt + F</kbd>).
  - Explorador estructural de funciones y clases (<kbd>Control + Shift + O</kbd>).
  - Consola interactiva REPL (<kbd>Control + J</kbd>).
- **Independencia Técnica Absoluta:**
  - Basado 100% en la biblioteca estándar de Python, prescindiendo de compiladores de C/C++ o librerías externas propensas a incompatibilidades.
- **Compatibilidad Extensa Certificada:**
  - Soporte garantizado desde NVDA 2022.1.0 hasta la versión actual 2026.2.0.

## Versión 2.0.0

- **Introducción de la Modalidad Dual de Trabajo:**
  - Incorporación del Modo Solo Editor autónomo para permitir el desarrollo de scripts libres sin las limitaciones de los paneles de lecciones.
  - Atajo <kbd>Control + M</kbd> para alternar entre el modo formativo y el entorno de edición.
- **Ampliación Curricular Inicial:**
  - Expansión del plan de estudios a 32 capítulos didácticos, cubriendo estructuras condicionales, bucles `for` y `while`, funciones y colecciones.
- **Herramientas de Productividad Accesible:**
  - Primeras versiones del depurador guiado paso a paso y explorador de símbolos en el editor.
  - Salto accesible entre funciones y clases en archivos de código.
- **Retroalimentación Acústica:**
  - Incorporación de señales sonoras iniciales para el reporte de sangría y avisos de compilación.

## Versión 1.0.0

- **Lanzamiento Fundacional del Proyecto:**
  - Publicación del primer entorno pedagógico guiado por voz diseñado exclusivamente para el aprendizaje de Python mediante NVDA.
  - Implementación de lecciones básicas estructuradas con instrucciones leídas por el sintetizador.
  - Ejecución de código interactiva en consola integrada accesible.
  - Sistema inicial de verificación de resultados de retos prácticos.
  - Panel de ayuda y atajos de teclado elementales para el estudiante.
