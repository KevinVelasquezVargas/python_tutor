# Registro de cambios de Aprendizaje de Python con NVDA

## Versión 1.0.0 (Lanzamiento Oficial)

- **Plan Formativo Integral de 40 Capítulos (160 Lecciones Progresivas):**
  - Estructurado bajo la rigurosa metodología pedagógica *«Conceptos Primero»*, iniciando con fundamentos computacionales, arquitectura de hardware, sistema binario, ciclo de ejecución de la CPU e interacción tiflotécnica antes de avanzar hacia la sintaxis formal.
  - Progresión sistemática desde tipos fundamentales y estructuras de control hasta Programación Orientada a Objetos (POO), manejo seguro de archivos, excepciones, base de datos relacional SQLite3, formatos estructurados JSON y módulos de la biblioteca estándar (`math`, `random`, `datetime`, `urllib`).
- **Navegación Flexible del Temario y Desbloqueo Bajo Demanda:**
  - Diálogo accesible de selección de capítulos con capacidad de acceder directamente a cualquier lección avanzada mediante confirmación explícita, ideal para usuarios experimentados o reanudación de estudios.
- **Persistencia Robusta en Perfil de Usuario de NVDA:**
  - Almacenamiento seguro del progreso en el directorio de configuración de NVDA (`python_tutor/progress.json`), garantizando la preservación total de los avances formativos frente a actualizaciones del complemento.
- **Dualidad Operativa Perfeccionada (Modo Tutor vs. Modo Editor Autónomo):**
  - Conmutación instantánea mediante el atajo exclusivo <kbd>Control + M</kbd> o desde el menú *Herramientas*.
  - Anuncios acústicos diferenciados mediante síntesis y campanas armónicas de transición.
  - *Modo Aprendizaje:* Entorno guiado paso a paso con consignas pedagógicas, pistas escalonadas y evaluación automatizada de ejercicios.
  - *Modo Editor autónomo:* Entorno profesional de trabajo sin paneles didácticos, con navegación fluida y directa entre el área de edición, consola de salida y controles principales.
- **Interfaz Adaptativa por Contexto Pedagógico:**
  - Ocultación automática del editor de código en lecciones puramente teóricas y en cuestionarios de autoevaluación.
  - Selector nativo accesible (`wx.RadioBox`) para preguntas de opción múltiple, con retroalimentación inmediata sobre la opción seleccionada.
- **Asistente Didáctico con Inteligencia Artificial y Soporte Offline:**
  - Explicador de código offline autónomo mediante la tecla <kbd>F1</kbd>, sin requerir conexión a internet ni claves externas.
  - Integración opcional para consultas avanzadas con la API de Google Gemini mediante <kbd>Control + Shift + I</kbd>, con clave configurable de forma segura a través del panel de preferencias de NVDA.
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
