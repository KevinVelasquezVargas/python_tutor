# Registro de cambios de Aprendizaje de Python con NVDA

## Versión 2.0.0
- **Estructura oficial AddonTemplate 2026:** Adaptación integral a la plantilla canónica oficial de complementos de NVDA con herramientas SCons, pre-commit, dependabot, workflows de CI/CD y linters (`ruff`, `flake8`).
- **Arquitectura modular y robusta:** Desacoplamiento en submódulos especializados (`executor`, `audio_manager`, `curriculum`, `progress`, `gui_frame`, `repl_dialog`, `translator`).
- **Rediseño pedagógico no visual:** Metodología progresiva paso a paso orientada a la no sobrecarga cognitiva, comenzando desde conceptos elementales con `print('¡Hola mundo!')` y eliminando ejercicios abstractos de reordenación de código.
- **Herramientas de edición avanzadas (estilo Visual Studio):**
  - `Control + /`: Comentar o descomentar la línea actual.
  - `Control + D`: Duplicar línea actual hacia abajo.
  - `Control + Shift + K`: Eliminar la línea actual.
  - `Alt + Flecha Arriba / Abajo`: Mover línea actual verticalmente.
  - `F7`: Verificación rápida de sintaxis sin ejecutar el script.
  - `Control + L`: Anunciar línea y columna actual.
  - `Control + Espacio`: Asistente de autocompletado de palabras clave de Python.
  - `F3` / `Control + I`: Lectura inmediata de la instrucción activa sin perder el foco en el editor.
  - `F6`: Alternar el foco entre el editor de código y la consola de resultados.
- **Detección preventiva de escritura y teclado:** Detección de caracteres incompatibles comunes (tildes agudas `´`, comillas tipográficas `“ ”`, punto y coma en lugar de dos puntos `;`, guiones largos `–`) antes de la ejecución para evitar frustración.
- **Retroalimentación formativa y comparativa:** Diagnóstico claro de diferencias entre la salida esperada y la obtenida, redactada en lenguaje natural y accesible.
- **Traductor a Lenguaje Humano (F1):** Explica la línea de código donde se encuentra el cursor en lenguaje cotidiano.
- **Linter acústico PEP 8:** Señales sonoras discretas de sangría (0, 4, 8, 12 espacios) e indicador de apertura de bloque sintáctico.
- **Consola de Pruebas Rápidas (REPL - Control + J):** Espacio interactivo para evaluar expresiones de Python al instante.
- **Diccionario de términos de Python (Control + G):** Glosario interactivo con definiciones accesibles.
- **Manual en formato HTML (F12):** Documentación completa estructurada semánticamente, con apertura directa en el navegador web.
- **Integración en el menú Herramientas de NVDA:** Accesos directos al tutor, soporte y donaciones voluntarias.
- **Cierre inmediato con la tecla Escape:** Salida limpia del tutor desde cualquier control.
- **Compatibilidad verificada:** Totalmente compatible desde NVDA 2022.1.0 hasta NVDA 2026.3.0.

## Versión 1.0.0
- Versión inicial con temario básico de fundamentos y ejecución interactiva en NVDA.
