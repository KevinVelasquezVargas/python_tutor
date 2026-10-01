# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries, SpeechDictionaries
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
	addon_name="python_tutor",
	addon_summary=_("Python Learning with NVDA"),
	addon_description=_("""Training tool and code editor tailored for Python programming with NVDA. Provides a structured learning curriculum across 32 conceptual and practical chapters (128 lessons) (32 capítulos conceptuales y prácticos (128 lecciones)), complemented by a dual-mode workspace: guided tutor mode and standalone editor mode. Features code structure navigation across functions and classes, acoustic indentation and structure cues, delimiter verification, and simplified error diagnostic messages."""),
	addon_version="2.0.0",
	addon_changelog=_("""Changelog version 2.0.0:
- Dual usage modes: Guided Learning Mode and professional standalone Editor Mode (Control + M).
- Agile execution with F5 or Control + Enter and lesson navigation with Alt + Arrows.
- Direct structural navigation across functions and classes (Alt + N / Alt + P and symbol picker Control + Shift + O).
- Automatic jump to Traceback error line with accessible diagnostic reading (F4).
- Real-time delimiter and quote balance checker (F7).
- Non-invasive console reading without losing editor focus (Control + Shift + C and Control + 6).
- Comprehensive curriculum expanded to 32 chapters and 128 micro-steps with "Concepts First" methodology.
- Exhaustive glossary expanded to 114 Python technical terms with interactive search.
- Acoustic PEP 8 linter, everyday human language translator (F1), and interactive REPL (Control + J).
- Advanced IDE tools: Step Debugger (F9), Test Runner (Control + Shift + T), and Interpreter Manager (Control + Shift + I).
- Canonical adaptation to the official 2026 AddonTemplate standard.
- Guaranteed compatibility from NVDA 2022.1.0 to 2026.3.0."""),
	addon_author="Kevin Andrés Velasquez Vargas <kevinvelasquezvargas@gmail.com>",
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

excludedFiles: list[str] = []

baseLanguage: str = "en"

markdownExtensions: list[str] = [
	"markdown.extensions.tables",
	"markdown.extensions.fenced_code",
]

brailleTables: BrailleTables = {}
symbolDictionaries: SymbolDictionaries = {}
speechDictionaries: SpeechDictionaries = {}
