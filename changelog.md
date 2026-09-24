# Registro de cambios de Aprendizaje de Python con NVDA

## Versión 2.0.0
- **Estructura oficial AddonTemplate 2026:** Adaptación integral a la plantilla canónica oficial de complementos de NVDA con herramientas SCons, pre-commit, workflows y linters.
- **Rediseño pedagógico del Capítulo 1:** Explicación de conceptos elementales para personas sin conocimientos previos de programación, comenzando directamente con `print('¡Hola mundo!')` y eliminando ejercicios complejos de reordenación de código.
- **Traductor a Lenguaje Humano (F1 / Control + H):** Función accesible que explica la línea de código actual en lenguaje cotidiano.
- **Manual en formato HTML:** Integración del manual accesible compilado en HTML (`doc/es/readme.html`), con apertura directa en el navegador web predeterminado.
- **Integración en el menú Herramientas de NVDA:** Acceso directo al tutor, enlace de contacto/soporte por correo electrónico y enlace para donaciones voluntarias.
- **Cierre inmediato con la tecla Escape:** Al presionar Escape en cualquier control de la ventana, esta se cierra limpiamente.
- **Editor simplificado:** Etiqueta clara `Editor de código` sin anuncios de atajos en el nombre del control.
- **Diálogo de bienvenida interactivo:** Guía de inicio rápido con opción para recordar la preferencia del usuario.
- **Panel de configuración en Preferencias de NVDA:** Configuración de efectos de sonido, linter de sangría y aviso de bienvenida en las opciones nativas de NVDA.
- **Señales sonoras optimizadas:** Generación instantánea y empaquetada de ondas de audio, con fallback al reproductor nativo `nvwave` de NVDA.
- **Compatibilidad validada:** Desde NVDA 2022.1.0 hasta NVDA 2026.3.0.

## Versión 1.5.0
- Modularización de la arquitectura interna en submódulos especializados.
- Incorporación del Laboratorio Rápido (REPL) para pruebas de una línea.
- Ampliación del temario hasta el Capítulo 15.
- Linter acústico para detección de sangría y dos puntos.

## Versión 1.0.0
- Versión inicial con temario de fundamentos y ejecución interactiva en NVDA.
