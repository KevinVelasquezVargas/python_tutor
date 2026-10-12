# Aprendizaje de Python con NVDA [![Versión](https://img.shields.io/badge/Versi%C3%B3n-3.1.0-blue.svg)](https://github.com/KevinVelasquezVargas/python_tutor/releases/latest) [![Compatibilidad](https://img.shields.io/badge/NVDA-2022.1%20a%202026.2-brightgreen.svg)](https://www.nvaccess.org/) [![Licencia](https://img.shields.io/badge/Licencia-GPLv3-blue.svg)](LICENSE)

Entorno accesible de desarrollo y formación para el aprendizaje de Python mediante el lector de pantallas NVDA. Estructurado en un plan formativo de 40 capítulos y una modalidad dual que combina un tutor interactivo con un editor autónomo sin barreras visuales.

## Contenido

1. [Instalación](#instalación)
2. [Características Principales](#características-principales)
3. [Atajos de Teclado](#atajos-de-teclado)
4. [Plan Formativo](#plan-formativo)
5. [Configuración](#configuración)
6. [Añadir un Nuevo Idioma de Lecciones](#añadir-un-nuevo-idioma-de-lecciones)
7. [Pruebas Automatizadas](#pruebas-automatizadas)
8. [Soporte y Colaboración](#soporte-y-colaboración)
9. [Licencia](#licencia)

---

## Instalación

1. Descargue el paquete oficial más reciente desde la sección de [Lanzamientos (Releases)](https://github.com/KevinVelasquezVargas/python_tutor/releases/latest).
2. Abra el archivo descargado (`.nvda-addon`) para que el gestor de complementos de NVDA inicie el proceso.
3. Confirme la instalación y reinicie el lector de pantalla.
4. Presione `NVDA + Control + Shift + P` para iniciar la aplicación.

---

## Características Principales

* **Plan pedagógico guiado:** 40 capítulos y 190 lecciones distribuidas en 9 módulos secuenciales. Introduce fundamentos conceptuales antes de abordar la sintaxis formal.
* **Modalidad dual de trabajo:** Alternancia inmediata (`Control + M`) entre el modo guiado con retroalimentación automática y un editor autónomo despejado para proyectos personales.
* **Interfaz adaptativa:** Ocultamiento automático del editor y la consola en lecciones teóricas y evaluaciones conceptuales mediante selectores accesibles (`wx.RadioBox`).
* **Arquitectura nativa:** Uso exclusivo de módulos de la biblioteca estándar de Python (`sqlite3`, `json`, `math`, `random`, `datetime`, `urllib`), eliminando dependencias externas y riesgos de compilación.
* **Señales acústicas tiflotécnicas:** Sonificación para niveles de indentación PEP 8, diagnóstico de delimitadores y validación de sintaxis.
* **Asistencia pedagógica:** Explicador de código local sin conexión (`F1`) y soporte opcional para consultas avanzadas con la API de Google Gemini (`Control + Shift + I`).
* **Soporte multilingüe ampliable:** Español, Inglés y Portugués incluidos de forma oficial. Añadir un idioma nuevo no requiere tocar Python: basta con añadir un catálogo JSON de lecciones (véase [Añadir un Nuevo Idioma de Lecciones](#añadir-un-nuevo-idioma-de-lecciones)).

---

## Atajos de Teclado

| Atajo | Categoría | Acción |
| :--- | :--- | :--- |
| `NVDA + Ctrl + Shift + P` | Global | Abrir o enfocar el entorno |
| `Ctrl + M` | Modos | Alternar entre Modo Tutor y Modo Editor Autónomo |
| `Ctrl + Enter` / `Ctrl + E` | Ejecución | Ejecutar código y verificar reto |
| `F5` | Ejecución | Ejecutar script actual |
| `Alt + Flecha Derecha` | Navegación | Avanzar al siguiente paso |
| `Alt + Flecha Izquierda` | Navegación | Retroceder al paso anterior |
| `F3` / `Ctrl + I` | Tutor | Verbalizar instrucción pedagógica activa |
| `Ctrl + P` | Tutor | Solicitar pista escalonada |
| `F1` | Tutor | Explicación local de la línea actual |
| `Shift + F1` | Referencia | Documentación técnica del símbolo bajo el cursor |
| `Ctrl + R` | Tutor | Restablecer código de partida |
| `Ctrl + 1` | Tutor | Selector de capítulos y progreso |
| `Ctrl + J` | Herramientas | Abrir consola interactiva REPL |
| `Ctrl + Shift + I` | Herramientas | Consultar asistente con IA (Gemini API) |
| `F6` | Navegación | Alternar foco entre editor y consola |
| `Ctrl + 4` | Navegación | Situar el foco en el editor |
| `Ctrl + 5` | Navegación | Situar el foco en la consola |
| `Ctrl + 6` | Consola | Leer última línea emitida |
| `Ctrl + Shift + C` | Consola | Leer toda la salida acumulada |
| `Ctrl + L` | Edición | Anunciar línea y columna actual |
| `Ctrl + N` | Archivo | Crear nuevo archivo |
| `Ctrl + O` | Archivo | Abrir archivo `.py` |
| `Ctrl + S` | Archivo | Guardar cambios |
| `Ctrl + Shift + S` | Archivo | Guardar como |
| `Ctrl + F` | Edición | Buscar texto |
| `Ctrl + G` | Edición | Ir a un número de línea |
| `Ctrl + Espacio` | Edición | Autocompletado accesible |
| `Shift + Alt + F` | Edición | Formatear documento según PEP 8 |
| `Ctrl + /` / `Ctrl + K` | Edición | Alternar comentario de línea (`#`) |
| `Ctrl + D` | Edición | Duplicar línea activa |
| `Ctrl + Shift + K` | Edición | Eliminar línea activa |
| `Ctrl + Shift + R` | Refactor | Extraer selección a nueva función |
| `F2` | Refactor | Renombrar identificador |
| `Ctrl + Shift + O` | Estructura | Lista accesible de funciones y clases |
| `Alt + N` / `Alt + P` | Estructura | Saltar a la siguiente / anterior cabecera |
| `F7` | Diagnóstico | Validar sintaxis y balanceo de delimitadores |
| `F4` | Diagnóstico | Saltar a la línea del error del Traceback |
| `F9` | Depuración | Alternar punto de interrupción |
| `F10` | Depuración | Depuración interactiva paso a paso |
| `Ctrl + T` | Pruebas | Ejecutar pruebas unitarias |
| `Ctrl + Shift + P` | Entorno | Gestor de intérpretes y entornos virtuales |
| `Ctrl + Shift + E` | Herramientas | Explorador accesible de archivos y proyectos |
| `F11` | Ayuda | Diálogo accesible de atajos de teclado |
| `F12` | Ayuda | Documentación completa en navegador |
| `Escape` | General | Cerrar cuadro de diálogo activo |

---

## Plan Formativo

| Módulo | Capítulos | Contenido |
| :--- | :--- | :--- |
| **0. Fundamentos de Computación** | 1 a 5 | Arquitectura, sistema binario, CPU, lectores de pantalla y pensamiento algorítmico. |
| **1. Salida, Memoria y Variables** | 6 a 9 | Salida estándar con `print()`, asignación dinámica y PEP 8. |
| **2. Tipos Fundamentales e Interacción** | 10 a 14 | Tipos `int`, `float`, `str`, interpolación con f-strings y captura con `input()`. |
| **3. Lógica Booleana y Control** | 15 a 19 | Expresiones booleanas, conectores lógicos y condicionales `if`, `else`, `elif`. |
| **4. Bucles y Automatización** | 20 a 23 | Bucles `for` con `range()`, bucles `while`, control de ejecución y directivas de flujo. |
| **5. Estructuras de Datos** | 24 a 28 | Listas indexadas, operaciones de mutación, iteración, tuplas y diccionarios. |
| **6. Modularidad y Excepciones** | 29 a 32 | Funciones con `def`, retorno con `return`, ámbito y gestión de fallos (`try`/`except`). |
| **7. Persistencia y Objetos (POO)** | 33 a 36 | Manejo seguro de archivos (`with open`), JSON, clases, instancias y métodos. |
| **8. Biblioteca Estándar y Proyecto** | 37 a 40 | Módulos `math`, `random`, `datetime`, bases de datos `sqlite3` y proyecto final integrador. |

---

## Configuración

Ruta de acceso: **Menú NVDA > Preferencias > Opciones > Aprendizaje de Python con NVDA**

* **Idioma del entorno:** Automático (según el idioma de NVDA), Español, Inglés o Portugués. Los idiomas disponibles se detectan automáticamente a partir de los catálogos `addon/locale/<idioma>/lessons.json`.
* **Modo de inicio:** Modo Aprendizaje Guiado o Modo Editor Autónomo.
* **Señales acústicas:** Habilitación de sonificación de sangría PEP 8 y alertas.
* **Clave API de Gemini:** Configuración opcional para consultas de IA.

---

## Añadir un Nuevo Idioma de Lecciones

Los currículos traducidos viven en catálogos JSON independientes del código (`addon/locale/<idioma>/lessons.json`), junto al resto de la localización del complemento. Al recompilar, el idioma nuevo aparece automáticamente en el selector de idioma, en el menú *Cambiar idioma* y en la detección automática del idioma de NVDA (variaciones como `pt_BR` o `en_US` se normalizan al catálogo disponible).

1. Genere el catálogo base en español desde el código fuente:

   ```bash
   uv run python tools/extract_lessons.py
   ```

2. Copie `addon/locale/es/lessons.json` a `addon/locale/<idioma>/lessons.json` (por ejemplo, `addon/locale/fr/lessons.json`) y traduzca los valores. Las claves permanecen en español. La traducción puede ser parcial (capítulo a capítulo): todo lo que falte se mostrará en español como respaldo.

3. Respete estas reglas en los desafíos de código (los validadores viven en `curriculum.py` y nunca se traducen):
   * `salida_esperada`: debe permanecer byte-idéntica al original.
   * `codigo`: solo se traducen los comentarios `#`; los literales de cadena deben coincidir exactamente con el original.
   * `opciones`: conserve el orden de las opciones (la respuesta correcta se valida por posición) y traduzca cada opción completa.

4. Interfaz del complemento (opcional pero recomendado):
   * Añada una sección para el idioma en el diccionario `DICCIONARIO` de `addon/globalPlugins/python_tutor/i18n.py` (copie la sección `"es"`).
   * Cree `addon/locale/<idioma>/LC_MESSAGES/nvda.po` a partir de `addon/locale/es/LC_MESSAGES/nvda.po` para menús, mensajes y descripción del complemento.

5. Recompile y verifique:

   ```bash
   scons
   python -m unittest tests/test_tutor.py
   ```

---

## Pruebas Automatizadas

El proyecto implementa pruebas unitarias basadas en `unittest` para verificar el correcto funcionamiento del editor y la integridad de las lecciones:

```bash
python -m unittest tests/test_tutor.py
```

---

## Soporte y Colaboración

* **Reporte de problemas:** [Gestor de incidencias en GitHub](https://github.com/KevinVelasquezVargas/python_tutor/issues)
* **Contacto directo:** [kevinvelasquezvargas@gmail.com](mailto:kevinvelasquezvargas@gmail.com)
* **Patrocinio:** [Donaciones voluntarias vía PayPal](https://paypal.me/kevinvelasquezvargas)

---

## Licencia

Este proyecto está bajo la Licencia Pública General de GNU v3.0 (GPLv3). Consulte el archivo [LICENSE](LICENSE) para más detalles.

**Autor:** Kevin Andrés Velasquez Vargas.
