# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries, SpeechDictionaries
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
	addon_name="python_tutor",
	addon_summary=_("Aprendizaje de Python con NVDA"),
	addon_description=_("""Desbloquea el poder de la programación: aprende Python desde cero con lecciones guiadas por voz y desarrolla tus propios proyectos en un editor diseñado exclusivamente para la accesibilidad con NVDA."""),
	addon_version="1.0.0",
	addon_changelog=_("""Registro de cambios versión 1.0.0:
- Plan formativo integral de 40 capítulos estructurados desde fundamentos hasta la biblioteca estándar.
- Interfaz adaptativa según el contexto pedagógico (ocultando el editor en lecciones conceptuales y quizzes).
- Widget nativo accesible de selección para cuestionarios de evaluación conceptual.
- Soporte multilingüe integral con localización completa al inglés (Learning Python with NVDA).
- Diálogo accesible de bienvenida e invitación cordial para donaciones voluntarias vía PayPal.
- Apertura accesible de la documentación en el navegador web mediante F12.
- Ciclo de vida limpio: reinicio de progreso al desinstalar y reinstalar el complemento.
- Compatibilidad garantizada desde NVDA 2022.1.0 hasta 2026.2.0."""),
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
