# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries, SpeechDictionaries
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
	addon_name="python_tutor",
	addon_summary=_("Aprendizaje de Python con NVDA"),
	addon_description=_("""Entorno accesible para el aprendizaje práctico del lenguaje de programación Python mediante el lector de pantalla NVDA. Incorpora metodología guiada por micro-pasos, traductor a lenguaje humano, señales acústicas pedagógicas, linter de sangría PEP 8, laboratorio interactivo y temario estructurado."""),
	addon_version="2.0.0",
	addon_changelog=_("""Registro de cambios versión 2.0.0:
- Estructura canónica oficial AddonTemplate 2026 y arquitectura modular desacoplada.
- Rediseño pedagógico paso a paso para personas sin conocimientos previos de programación.
- Herramientas avanzadas de edición (comentar, duplicar, mover líneas, verificar sintaxis F7, lectura de instrucción activa F3 / Ctrl+I, alternar foco F6).
- Detección preventiva de escritura y comparación formativa de salidas esperadas vs. obtenidas.
- Traductor a Lenguaje Humano (F1) para explicar cualquier línea de código.
- Acceso directo en el menú Herramientas de NVDA (Tutor, Soporte y Donaciones).
- Cierre inmediato con la tecla Escape desde cualquier control.
- Manual del usuario en formato HTML accesible en navegador web.
- Señales sonoras instantáneas y panel de configuración en Preferencias de NVDA."""),
	addon_author="Kevin Andrés Velasquez Vargas <kevinvelasquezvargas@gmail.com>",
	addon_url="https://github.com/KevinVelasquezVargas/python_tutor",
	addon_sourceURL="https://github.com/KevinVelasquezVargas/python_tutor",
	addon_docFileName="doc/es/readme.html",
	addon_minimumNVDAVersion="2022.1.0",
	addon_lastTestedNVDAVersion="2026.3.0",
	addon_updateChannel=None,
	addon_license="GPLv3",
	addon_licenseURL="https://www.gnu.org/licenses/gpl-3.0.html",
)

pythonSources: list[str] = [
	"addon/globalPlugins/python_tutor/*.py",
	"addon/*.py",
]

i18nSources: list[str] = pythonSources + ["buildVars.py"]

excludedFiles: list[str] = []

baseLanguage: str = "es"

markdownExtensions: list[str] = [
	"markdown.extensions.tables",
	"markdown.extensions.fenced_code",
]

brailleTables: BrailleTables = {}
symbolDictionaries: SymbolDictionaries = {}
speechDictionaries: SpeechDictionaries = {}
