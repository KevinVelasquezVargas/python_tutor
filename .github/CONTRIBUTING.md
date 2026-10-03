# Guía de Contribución a Aprendizaje de Python con NVDA

¡Gracias por tu interés en contribuir a **Aprendizaje de Python con NVDA**! Este proyecto tiene como misión brindar una formación inclusiva, profesional y de primer nivel para personas ciegas o con baja visión usuarias del lector de pantallas NVDA.

---

## 1. Principios de Diseño del Proyecto

Toda contribución de código o contenido debe alinearse con nuestros pilares fundamentales:
1. **Accesibilidad Nativa Prioritaria:** Todo control visual (`wxPython`), diálogo o mensaje debe poseer nombres accesibles claros (`SetName`), roles semánticos y atajos de teclado accesibles sin depender del ratón.
2. **Pedagogía «Conceptos Primero»:** Explicaciones rigurosas y estructuradas que no asumen conocimientos previos y priorizan el entendimiento de la arquitectura y la lógica antes de la sintaxis.
3. **Resiliencia e Independencia Técnica:** El núcleo del complemento opera exclusivamente con módulos de la biblioteca estándar de Python (`sqlite3`, `json`, `math`, `random`, `datetime`, `urllib`), evitando librerías binarias de C/C++ propensas a incompatibilidades.
4. **Retroalimentación Acústica No Invasiva:** Las señales acústicas (*earcons*) confirman estados y niveles de sangría de forma rápida sin saturar la síntesis de voz.

---

## 2. Cómo Empezar

### Requisitos de Desarrollo
* **Python:** Versión 3.10 o superior (recomendado Python 3.11 o 3.14).
* **SCons:** Para la compilación automatizada del paquete `.nvda-addon`.
* **Lector de Pantalla NVDA:** 2022.1 o superior para pruebas locales de integración.

### Clonar el Repositorio
```bash
git clone https://github.com/KevinVelasquezVargas/python_tutor.git
cd python_tutor
```

### Ejecutar Pruebas Automatizadas
Antes de proponer cualquier cambio, asegúrate de que toda la suite de pruebas unitarias se ejecute y apruebe al 100%:
```bash
python -m unittest tests/test_tutor.py
```

### Compilar el Complemento
Para generar el archivo distribuible `.nvda-addon`:
```bash
scons -Q
```
El archivo resultante `python_tutor-1.0.0.nvda-addon` se generará en la raíz del repositorio.

---

## 3. Flujo de Trabajo para Pull Requests

1. Haz un *Fork* del repositorio oficial.
2. Crea una rama descriptiva para tu funcionalidad o corrección:
   ```bash
   git checkout -b feature/nombre-de-la-mejora
   ```
3. Realiza tus modificaciones respetando las guías de estilo PEP 8.
4. Añade o actualiza pruebas unitarias en `tests/test_tutor.py` si incorporas nueva lógica.
5. Ejecuta la suite de pruebas y verifica que no existan regresiones.
6. Haz commit con mensajes claros y descriptivos siguiendo la convención [Conventional Commits](https://www.conventionalcommits.org/):
   * `feat: ...` para nuevas funcionalidades.
   * `fix: ...` para resolución de incidencias.
   * `docs: ...` para cambios en la documentación.
   * `test: ...` para adición o ajuste de pruebas.
7. Abre un Pull Request hacia la rama `main` del repositorio oficial describiendo con detalle el cambio realizado.

---

## 4. Localización e Internacionalización (i18n)

El proyecto ofrece soporte bilingüe completo (Español e Inglés):
* Las cadenas de la interfaz de usuario se gestionan mediante gettext (`addon/locale/<lang>/LC_MESSAGES/nvda.po`).
* El plan formativo bilingüe se sincroniza a través de `addon/globalPlugins/python_tutor/curriculum_translations.py`.
* La documentación técnica se mantiene sincronizada en `addon/doc/es/readme.md` y `addon/doc/en/readme.md`.

---

## 5. Reporte de Incidencias

Si encuentras un error o deseas sugerir una nueva funcionalidad:
* Revisa las [incidencias existentes](https://github.com/KevinVelasquezVargas/python_tutor/issues) para evitar duplicados.
* Utiliza las plantillas oficiales de incidencias proporcionando el comportamiento esperado, el comportamiento observado y los pasos precisos de reproducción.
