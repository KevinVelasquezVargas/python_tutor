# Aprendizaje de Python con NVDA

<p align="center">
  <a href="https://github.com/KevinVelasquezVargas/python_tutor/releases/latest">
    <img src="https://img.shields.io/badge/Versi%C3%B3n-3.0.0-0078D4.svg?style=for-the-badge&logo=github" alt="Versión 3.0.0 Oficial">
  </a>
  <a href="https://www.gnu.org/licenses/gpl-3.0.html">
    <img src="https://img.shields.io/badge/Licencia-GNU%20GPLv3-28a745.svg?style=for-the-badge" alt="Licencia GNU General Public License v3.0">
  </a>
  <a href="https://www.nvaccess.org/">
    <img src="https://img.shields.io/badge/NVDA-2022.1%20%E2%86%92%202026.2-blue.svg?style=for-the-badge" alt="Compatibilidad NVDA 2022.1 hasta 2026.2">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.14-3776AB.svg?style=for-the-badge&logo=python" alt="Python 3.10, 3.11, 3.14">
  </a>
  <a href="https://github.com/KevinVelasquezVargas/python_tutor/actions">
    <img src="https://img.shields.io/badge/Pruebas-26%2F26%20Superadas-brightgreen.svg?style=for-the-badge" alt="26 de 26 pruebas unitarias pasadas con éxito">
  </a>
  <a href="https://www.w3.org/WAI/standards-guidelines/wcag/">
    <img src="https://img.shields.io/badge/Accesibilidad-WCAG%202.1%20AA-success.svg?style=for-the-badge" alt="Conformidad de Accesibilidad WCAG 2.1 Nivel AA">
  </a>
</p>

---

## Resumen Ejecutivo

**Aprendizaje de Python con NVDA** es un entorno de desarrollo formativo e inclusivo de nivel profesional, diseñado específicamente para personas ciegas o con baja visión que utilizan el lector de pantallas **NVDA**. 

Construido bajo una filosofía pedagógica de **«Conceptos Primero»**, el entorno guía al alumno desde la arquitectura de hardware, la memoria y el pensamiento algorítmico abstracto hasta el dominio de la Programación Orientada a Objetos, bases de datos relacionales, manejo de archivos y pruebas automatizadas, todo ello respaldado por una experiencia acústica tiflotécnica enriquecida y un editor autónomo sin barreras visuales.

---

## Tabla de Contenidos

1. [Descarga e Instalación Rápida](#descarga-e-instalación-rápida)
2. [Pilares de Diseño y Arquitectura](#pilares-de-diseño-y-arquitectura)
3. [Doble Modalidad de Trabajo](#doble-modalidad-de-trabajo)
4. [Referencia Completa de Atajos de Teclado](#referencia-completa-de-atajos-de-teclado)
5. [Plan Formativo Integral (40 Capítulos)](#plan-formativo-integral-40-capítulos)
6. [Asistencia Inteligente y Diagnóstico](#asistencia-inteligente-y-diagnóstico)
7. [Panel de Preferencias en NVDA](#panel-de-preferencias-en-nvda)
8. [Estándares de Calidad y Pruebas Unitarias](#estándares-de-calidad-y-pruebas-unitarias)
9. [Compromiso de Accesibilidad (WCAG 2.1 AA)](#compromiso-de-accesibilidad-wcag-21-aa)
10. [Gobernanza, Soporte y Colaboración](#gobernanza-soporte-y-colaboración)

---

## Descarga e Instalación Rápida

### Descarga del Paquete Oficial
El complemento se distribuye empaquetado en formato canónico para NVDA:

* 📦 **Paquete Oficial para NVDA:** [**Descargar python_tutor-3.0.0.nvda-addon**](https://github.com/KevinVelasquezVargas/python_tutor/releases/download/v3.0.0/python_tutor-3.0.0.nvda-addon) *(694 KB)*

### Pasos de Instalación
1. Descarga el archivo `python_tutor-3.0.0.nvda-addon`.
2. Pulsa <kbd>Enter</kbd> sobre el archivo descargado para que NVDA inicie el gestor de instalación.
3. Confirma la instalación y reinicia NVDA cuando el sistema lo solicite.
4. Pulsa el atajo global **<kbd>NVDA + Ctrl + Shift + P</kbd>** en cualquier momento para iniciar el entorno.

---

## Pilares de Diseño y Arquitectura

* 🎓 **Pedagogía «Conceptos Primero»:** Estructurado en 40 capítulos que inician sin abrumar con sintaxis abstracta; explora primero la arquitectura del ordenador, el sistema binario, el ciclo de instrucciones de la CPU y la interacción tiflotécnica.
* ⚡ **Doble Modalidad de Trabajo:** Alternancia instantánea con un solo atajo (<kbd>Ctrl + M</kbd>) entre un tutor didáctico paso a paso y un editor de código profesional limpio para desarrollar proyectos libres.
* 🔊 **Ingeniería Tiflotécnica y Sonificación (Earcons):** Indicadores acústicos armónicos diferenciados para la indentación PEP 8 (niveles de 0 a 12 espacios), validación sintáctica, transiciones de modo y alertas de delimitadores.
* 🛡️ **Independencia Técnica y Cero Dependencias Inestables:** Construido exclusivamente sobre la biblioteca estándar de Python (`sqlite3`, `json`, `math`, `random`, `datetime`, `urllib`), garantizando funcionamiento autónomo sin requerir compiladores de C/C++ ni gestores externos inestables.
* 🤖 **Asistente Híbrido (Local y en la Nube):** Incluye un explicador de línea totalmente local y sin conexión (<kbd>F1</kbd>) y una integración opcional con la API de Google Gemini (<kbd>Ctrl + Shift + I</kbd>) para consultas avanzadas.
* 🌐 **Localización Bilingüe Integral:** Soporte completo en Español e Inglés (*Learning Python with NVDA*), con traducción de menús, diálogos, manuales y código inicial de las lecciones.

---

## Doble Modalidad de Trabajo

El complemento soluciona la desconexión habitual entre aprender teoría y programar software real ofreciendo dos modos complementarios:

### 1. Modo Aprendizaje Guiado
* **Consignas pedagógicas claras:** Cada paso detalla el concepto teórico antes de solicitar código.
* **Interfaz adaptativa:** En lecciones de fundamentación y cuestionarios conceptuales, el editor de código se oculta automáticamente para centrar la atención del lector en el contenido teórico.
* **Evaluación en tiempo de ejecución:** Valida el resultado real de tu programa mediante un sandbox vigilado, evitando aprobaciones falsas o bloqueos por sintaxis.
* **Pistas escalonadas (<kbd>Ctrl + P</kbd>):** Ayuda progresiva en tres niveles para desbloquear cualquier ejercicio sin dar la solución directamente.

### 2. Modo Editor Autónomo
* **Entorno IDE libre de distracciones:** Oculta los paneles didácticos para ofrecer un flujo de trabajo ágil entre el área de edición (<kbd>Ctrl + 4</kbd>) y la consola (<kbd>Ctrl + 5</kbd>).
* **Navegación estructural (<kbd>Ctrl + Shift + O</kbd>):** Lista accesible de funciones y clases presentes en el script para salto directo.
* **Formateador PEP 8 integrado (<kbd>Shift + Alt + F</kbd>):** Corrige automáticamente la sangría y espaciado de operadores conforme al estándar oficial.
* **Consola REPL Interactiva (<kbd>Ctrl + J</kbd>):** Para probar expresiones rápidas de Python en tiempo real.

---

## Referencia Completa de Atajos de Teclado

### Atajos Globales y de Navegación

| Atajo | Categoría | Acción |
| :--- | :--- | :--- |
| <kbd>NVDA + Ctrl + Shift + P</kbd> | Global | Abrir o enfocar la ventana principal del entorno. |
| <kbd>Ctrl + M</kbd> | Modos | Alternar entre Modo Tutor y Modo Editor Autónomo. |
| <kbd>Ctrl + Enter</kbd> | Ejecución | Ejecutar código y verificar solución del ejercicio activo. |
| <kbd>F5</kbd> | Ejecución | Ejecutar el script completo sin comprobación de reto. |
| <kbd>Alt + Flecha Derecha</kbd> | Tutor | Avanzar al siguiente paso de la lección. |
| <kbd>Alt + Flecha Izquierda</kbd> | Tutor | Retroceder al paso anterior de la lección. |
| <kbd>F6</kbd> | Temario | Abrir el selector accesible de capítulos con desbloqueo flexible. |
| <kbd>F3</kbd> | Tutor | Leer la instrucción pedagógica activa sin mover el foco del editor. |
| <kbd>Ctrl + P</kbd> | Tutor | Solicitar una pista escalonada de asistencia. |
| <kbd>Ctrl + R</kbd> | Tutor | Restablecer el código inicial sugerido para el ejercicio. |

### Atajos de Edición y Tiflotecnología

| Atajo | Categoría | Acción |
| :--- | :--- | :--- |
| <kbd>Ctrl + Espacio</kbd> | Edición | Desplegar lista de autocompletado accesible. |
| <kbd>Shift + Alt + F</kbd> | Formato | Formatear código según los estándares de estilo PEP 8. |
| <kbd>Ctrl + /</kbd> | Edición | Alternar comentario de línea (`#`). |
| <kbd>Ctrl + D</kbd> | Edición | Duplicar la línea o selección activa. |
| <kbd>Ctrl + Shift + K</kbd> | Edición | Eliminar la línea actual completa. |
| <kbd>Ctrl + G</kbd> | Navegación | Cuadro de diálogo para saltar a un número de línea específico. |
| <kbd>Ctrl + L</kbd> | Estado | Verbalizar número de línea y columna donde se encuentra el cursor. |
| <kbd>Ctrl + 4</kbd> | Foco | Mover el foco directamente al editor de código. |
| <kbd>Ctrl + 5</kbd> | Foco | Mover el foco a la consola de resultados. |
| <kbd>Ctrl + 6</kbd> | Consola | Leer la última línea emitida en la consola. |
| <kbd>Ctrl + Shift + C</kbd> | Consola | Verbalizar toda la salida de consola acumulada. |

### Diagnóstico, Estructura y Depuración

| Atajo | Categoría | Acción |
| :--- | :--- | :--- |
| <kbd>F7</kbd> | Diagnóstico | Comprobar balanceo de delimitadores (paréntesis, corchetes, llaves). |
| <kbd>F4</kbd> | Diagnóstico | Situar el cursor en la línea exacta del fallo reportado en el Traceback. |
| <kbd>F1</kbd> | Asistencia | Explicación en lenguaje humano de la línea activa (Modo Offline). |
| <kbd>Shift + F1</kbd> | Referencia | Consultar la documentación oficial del símbolo bajo el cursor. |
| <kbd>Ctrl + Shift + I</kbd> | IA | Realizar consulta contextual al Asistente Didáctico con IA. |
| <kbd>Ctrl + Shift + O</kbd> | Estructura | Explorar lista de funciones y clases para salto directo. |
| <kbd>Alt + N</kbd> / <kbd>Alt + P</kbd> | Estructura | Saltar a la siguiente o anterior función/clase. |
| <kbd>Ctrl + J</kbd> | Consola | Abrir consola interactiva REPL. |
| <kbd>F9</kbd> / <kbd>F10</kbd> | Depuración | Alternar punto de interrupción y depurar paso a paso. |
| <kbd>Ctrl + T</kbd> | Pruebas | Ejecutar suite integrada de pruebas unitarias (`unittest`). |
| <kbd>F12</kbd> | Ayuda | Abrir el manual completo de usuario en el navegador web predeterminado. |
| <kbd>Escape</kbd> | Ventana | Cerrar inmediatamente el entorno o cuadro de diálogo activo. |

---

## Plan Formativo Integral (40 Capítulos)

El plan curricular consta de **160 lecciones prácticas y conceptuales** organizadas en 9 módulos secuenciales:

| Módulo | Capítulos | Temas Clave |
| :--- | :---: | :--- |
| **0. Fundamentos de Computación** | 1 a 5 | Arquitectura Von Neumann, sistema binario, ciclo CPU, lectores de pantalla y lógica algorítmica. |
| **1. Salida, Memoria y Variables** | 6 a 9 | Salida estándar con `print()`, asignación en RAM, PEP 8 y ciclo de vida de variables. |
| **2. Tipos Primitivos e Interacción** | 10 a 14 | Enteros (`int`), decimales (`float`), cadenas (`str`), interpolación f-strings y entrada con `input()`. |
| **3. Lógica Booleana y Control** | 15 a 19 | Expresiones booleanas, operadores relacionales, lógica `and`/`or`/`not`, `if`, `else` y `elif`. |
| **4. Bucles y Automatización** | 20 a 23 | Bucle `for` con `range()`, bucle condicional `while`, control de bucles infinitos, `break` y `continue`. |
| **5. Estructuras de Datos** | 24 a 28 | Listas indexadas, métodos mutables (`append`, `pop`, `remove`), `enumerate()`, tuplas y diccionarios. |
| **6. Funciones y Excepciones** | 29 a 32 | Subrutinas con `def`, principio DRY, retorno con `return`, ámbito de variables y bloques `try`/`except`/`finally`. |
| **7. Persistencia y Objetos (POO)** | 33 a 36 | Manejo seguro de archivos con `with open()`, serialización JSON, clases, instancias, `__init__` y `self`. |
| **8. Biblioteca Estándar y Proyecto**| 37 a 40 | Módulos `math`, `random`, `datetime`, bases de datos con `sqlite3`, diseño sonoro y Proyecto Integrador Final. |

---

## Asistencia Inteligente y Diagnóstico

### 1. Explicador Pedagógico Local (<kbd>F1</kbd>)
No requiere conexión a Internet ni claves de acceso. Analiza la instrucción bajo el cursor y explica en lenguaje llano qué acción realizará el intérprete de Python, traduciendo construcciones complejas a conceptos intuitivos para usuarios no visuales.

### 2. Asistente con Inteligencia Artificial (<kbd>Ctrl + Shift + I</kbd>)
Permite conectar con modelos de lenguaje de vanguardia mediante la **API oficial de Google Gemini**. Ideal para solicitar explicaciones ampliadas de ejercicios, proponer variaciones didácticas o resolver dudas conceptuales sin salir del entorno de NVDA. La clave se configura de manera privada en las preferencias de NVDA y no se transmite a terceros.

---

## Panel de Preferencias en NVDA

El complemento se integra en la interfaz de configuración estándar de NVDA:

* **Ruta de acceso:** `Menú NVDA > Preferencias > Opciones > Aprendizaje de Python con NVDA`
* **Opciones configurables:**
  * **Idioma del Entorno:** Automático (según NVDA), Español o Inglés.
  * **Modo de Inicio Preferido:** Iniciar en Modo Aprendizaje Guiado o en Modo Solo Editor.
  * **Señales Auditivas (Earcons):** Activar o silenciar los tonos acústicos de sangría PEP 8 y confirmación.
  * **Clave de API Gemini:** Almacenamiento seguro de la clave para el asistente opcional con IA.

---

## Estándares de Calidad y Pruebas Unitarias

El proyecto cuenta con una batería integral de **26 pruebas unitarias automatizadas** que certifican cada componente crítico:

```bash
# Ejecución local de la suite de pruebas
python -m unittest tests/test_tutor.py
```

### Métricas de Validación
* **Suite de Pruebas:** 26/26 pruebas aprobadas (`Ran 26 tests in 1.493s - OK`).
* **Validación del Plan Formativo:** 100% de los 190 pasos auditados y libres de bloqueos.
* **Compatibilidad de Plataforma:** NVDA 2022.1.0 hasta NVDA 2026.2.0 en sistemas Windows de 64 bits.

---

## Compromiso de Accesibilidad (WCAG 2.1 AA)

El desarrollo se adhiere rigurosamente a las **Pautas de Accesibilidad para el Contenido Web (WCAG 2.1 Nivel AA)** y a las buenas prácticas tiflotécnicas:

* **Operabilidad por Teclado:** 100% de las características, diálogos y comandos cuentan con atajos dedicados accesibles.
* **Nombres Accesibles Semánticos:** Todos los controles (`wxPython`) exponen descripciones claras mediante `SetName()` y `SetHelpText()`.
* **Prevención de Fatiga Auditiva:** La síntesis de voz se complementa con señales acústicas de audio PCM de corta duración, evitando la saturación por mensajes verbales excesivos.
* **Gestión Segura del Foco:** Al cerrar diálogos o cambiar de lección, el foco se sitúa de forma predecible sobre el control activo sin pérdidas de navegación.

---

## Gobernanza, Soporte y Colaboración

### Reporte de Errores y Sugerencias
* **Rastreador de Incidencias:** [Reportar un problema o sugerencia en GitHub Issues](https://github.com/KevinVelasquezVargas/python_tutor/issues)
* **Correo Electrónico de Contacto:** [kevinvelasquezvargas@gmail.com](mailto:kevinvelasquezvargas@gmail.com)

### Contribución al Código
Revisa nuestras directrices comunitarias antes de colaborar:
* [Guía de Contribución (CONTRIBUTING.md)](.github/CONTRIBUTING.md)
* [Código de Conducta (CODE_OF_CONDUCT.md)](.github/CODE_OF_CONDUCT.md)
* [Política de Seguridad (SECURITY.md)](.github/SECURITY.md)

### Apoyo y Patrocinio
**Aprendizaje de Python con NVDA** es una iniciativa de código abierto, libre y gratuita, desarrollada con la convicción de que el acceso a la educación tecnológica de calidad es un derecho universal. Si este proyecto te resulta valioso para tu aprendizaje o actividad docente, puedes apoyar su mantenimiento continuo mediante una donación voluntaria:

* 💖 **Contribuir vía PayPal:** [https://paypal.me/kevinvelasquezvargas](https://paypal.me/kevinvelasquezvargas)

---

### Licencia

Distribuido bajo la **GNU General Public License v3.0 (GPLv3)**. Consulta el archivo [`COPYING.txt`](COPYING.txt) y [`LICENSE`](LICENSE) para más detalles.

**Autor y Mantenedor Principal:**  
**Kevin Velasquez** *(Kevin Andrés Velasquez Vargas)*  
Bogotá D.C., Colombia  
Correo: [kevinvelasquezvargas@gmail.com](mailto:kevinvelasquezvargas@gmail.com)
