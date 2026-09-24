# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries, SpeechDictionaries
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
	addon_name="python_tutor",
	addon_summary=_("Aprendizaje de Python con NVDA"),
	addon_description=_("""Entorno integral accesible para el aprendizaje práctico de Python y editor tiflotécnico de alto rendimiento con NVDA. Incorpora dualidad de uso (Modo Aprendizaje guiado y Modo Solo Editor profesional), navegación estructural de funciones y clases, salto automático a errores de Traceback, verificador de delimitadores, linter acústico PEP 8, traductor a lenguaje humano y currículo completo de 32 capítulos desde pensamiento computacional hasta bases de datos y pruebas unitarias."""),
	addon_version="2.0.0",
	addon_changelog=_("""Registro de cambios versión 2.0.0:
- Dualidad de uso: Modo Aprendizaje guiado y Modo Solo Editor profesional (Control + M).
- Navegación estructural directa por funciones y clases (Alt + N / Alt + P y diálogo de símbolos Control + Shift + O).
- Salto automático a la línea del error del Traceback con lectura diagnóstica (F4).
- Verificador en tiempo real de delimitadores y comillas sin cerrar (F7).
- Lectura de consola no invasiva sin perder el foco del editor (Control + Shift + C y Control + 6).
- Plan formativo ampliado a 32 capítulos y 128 micro-pasos con «Conceptos Primero» (fases conceptual, sintaxis, flujo, modularidad, POO y software profesional).
- Glosario ampliado a 43 términos técnicos con buscador interactivo.
- Linter acústico PEP 8, traductor a lenguaje humano (F1) y REPL interactivo (Control + J).
- Adaptación canónica a la plantilla oficial AddonTemplate 2026.
- Compatibilidad garantizada desde NVDA 2022.1.0 hasta 2026.3.0."""),
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
