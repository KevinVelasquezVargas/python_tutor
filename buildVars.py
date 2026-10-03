# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries, SpeechDictionaries
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
	addon_name="python_tutor",
	addon_summary=_("Aprendizaje de Python con NVDA"),
	addon_description=_("""Desbloquea el poder de la programación: aprende Python desde cero con lecciones guiadas por voz y desarrolla tus propios proyectos en un editor diseñado exclusivamente para la accesibilidad con NVDA."""),
	addon_version="3.0.1",
	addon_changelog=_("""Registro de cambios versión 3.0.1:
- Desbloqueo total entre capítulos: navegación y acceso directo a cualquier lección del curso conservando la evaluación estructurada por fases dentro de cada capítulo.
- Corrección crítica en el validador y ejecutor del Capítulo 17 (Paso 3) para permitir el avance fluido en retos con consola en silencio.
- Armonización y tolerancia bilingüe en consignas y verificadores de los 40 capítulos.
- Plan formativo integral de 40 capítulos (160 lecciones) con metodología pedagógica Conceptos Primero.
- Dualidad operativa: alternancia fluida entre Modo Tutor guiado y Modo Editor autónomo (Control + M).
- Interfaz adaptativa: ocultación contextual del editor en lecciones teóricas y selector accesible de quizes (wx.RadioBox).
- Selector de capítulos con navegación flexible y desbloqueo de acceso directo.
- Localización bilingüe oficial en español e inglés (Learning Python with NVDA).
- Asistente explicador local offline (F1) e integración opcional con Google Gemini API (Control + Shift + I).
- Independencia técnica total: basado 100% en la biblioteca estándar de Python (sqlite3, json, math, random).
- Persistencia robusta del usuario en el perfil de configuración de NVDA protegida frente a actualizaciones.
- Compatibilidad certificada desde NVDA 2022.1.0 hasta 2026.2.0."""),
	addon_author="Kevin Andrés Velasquez Vargas",
	addon_url="https://github.com/KevinVelasquezVargas/python_tutor",
	addon_sourceURL="https://github.com/KevinVelasquezVargas/python_tutor",
	addon_docFileName="readme.html",
	addon_minimumNVDAVersion="2022.1.0",
	addon_lastTestedNVDAVersion="2026.2.0",
	addon_updateChannel=None,
	addon_license="GPLv3",
	addon_licenseURL="https://www.gnu.org/licenses/gpl-3.0.html",
)

pythonSources: list[str] = [
	"addon/globalPlugins/python_tutor/*.py",
	"addon/*.py",
]

i18nSources: list[str] = pythonSources + ["buildVars.py"]

excludedFiles: list[str] = [
	"*/__pycache__/*",
	"__pycache__/*",
	"*/user_data/*",
	"user_data/*",
	"*.pyc",
]

baseLanguage: str = "es"

markdownExtensions: list[str] = [
	"markdown.extensions.tables",
	"markdown.extensions.fenced_code",
]

brailleTables: BrailleTables = {}
symbolDictionaries: SymbolDictionaries = {}
speechDictionaries: SpeechDictionaries = {}
