# Learning Python with NVDA [![Version](https://img.shields.io/badge/Version-3.1.0-blue.svg)](https://github.com/KevinVelasquezVargas/python_tutor/releases/latest) [![Compatibility](https://img.shields.io/badge/NVDA-2022.1%20to%202026.2-brightgreen.svg)](https://www.nvaccess.org/) [![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

Accessible development and training environment for learning Python with the NVDA screen reader. Structured as a 40-chapter training plan with a dual mode that combines an interactive tutor and a barrier-free standalone editor.

## Contents

1. [Installation](#installation)
2. [Main Features](#main-features)
3. [Keyboard Shortcuts](#keyboard-shortcuts)
4. [Training Plan](#training-plan)
5. [Configuration](#configuration)
6. [Adding a New Lesson Language](#adding-a-new-lesson-language)
7. [Automated Tests](#automated-tests)
8. [Support and Collaboration](#support-and-collaboration)
9. [License](#license)

---

## Installation

1. Download the latest official package from the [Releases](https://github.com/KevinVelasquezVargas/python_tutor/releases/latest) section.
2. Open the downloaded file (`.nvda-addon`) so that the NVDA add-on manager starts the process.
3. Confirm the installation and restart the screen reader.
4. Press `NVDA + Control + Shift + P` to launch the application.

---

## Main Features

* **Guided pedagogical plan:** 40 chapters and 190 lessons distributed across 9 sequential modules. Conceptual fundamentals are introduced before formal syntax.
* **Dual working mode:** Instant switching (`Control + M`) between the guided mode with automatic feedback and a clear standalone editor for personal projects.
* **Adaptive interface:** Automatic hiding of the editor and console in theoretical lessons and conceptual assessments via accessible selectors (`wx.RadioBox`).
* **Native architecture:** Exclusive use of Python standard library modules (`sqlite3`, `json`, `math`, `random`, `datetime`, `urllib`), eliminating external dependencies and compilation risks.
* **Tiflotecnical acoustic signals:** Sonification for PEP 8 indentation levels, delimiter diagnostics, and syntax validation.
* **Pedagogical assistance:** Offline local code explainer (`F1`) and optional support for advanced queries with the Google Gemini API (`Control + Shift + I`).
* **Extensible multilingual support:** Spanish, English, and Portuguese officially included. Adding a new language requires no Python changes: it is enough to add a JSON lesson catalog (see [Adding a New Lesson Language](#adding-a-new-lesson-language)).

---

## Keyboard Shortcuts

| Shortcut | Category | Action |
| :--- | :--- | :--- |
| `NVDA + Ctrl + Shift + P` | Global | Open or focus the environment |
| `Ctrl + M` | Modes | Toggle between Tutor Mode and Standalone Editor Mode |
| `Ctrl + Enter` / `Ctrl + E` | Execution | Run code and verify the challenge |
| `F5` | Execution | Run the current script |
| `Alt + Right Arrow` | Navigation | Advance to the next step |
| `Alt + Left Arrow` | Navigation | Go back to the previous step |
| `F3` / `Ctrl + I` | Tutor | Speak the active pedagogical instruction |
| `Ctrl + P` | Tutor | Request a graduated hint |
| `F1` | Tutor | Local explanation of the current line |
| `Shift + F1` | Reference | Technical documentation of the symbol under the cursor |
| `Ctrl + R` | Tutor | Restore the starting code |
| `Ctrl + 1` | Tutor | Chapter selector and progress |
| `Ctrl + J` | Tools | Open interactive REPL console |
| `Ctrl + Shift + I` | Tools | Query the AI assistant (Gemini API) |
| `F6` | Navigation | Toggle focus between editor and console |
| `Ctrl + 4` | Navigation | Move focus to the editor |
| `Ctrl + 5` | Navigation | Move focus to the console |
| `Ctrl + 6` | Console | Read the last output line |
| `Ctrl + Shift + C` | Console | Read all accumulated output |
| `Ctrl + L` | Editing | Announce current line and column |
| `Ctrl + N` | File | Create new file |
| `Ctrl + O` | File | Open `.py` file |
| `Ctrl + S` | File | Save changes |
| `Ctrl + Shift + S` | File | Save as |
| `Ctrl + F` | Editing | Find text |
| `Ctrl + G` | Editing | Go to a line number |
| `Ctrl + Space` | Editing | Accessible autocompletion |
| `Shift + Alt + F` | Editing | Format document according to PEP 8 |
| `Ctrl + /` / `Ctrl + K` | Editing | Toggle line comment (`#`) |
| `Ctrl + D` | Editing | Duplicate active line |
| `Ctrl + Shift + K` | Editing | Delete active line |
| `Ctrl + Shift + R` | Refactor | Extract selection to a new function |
| `F2` | Refactor | Rename identifier |
| `Ctrl + Shift + O` | Structure | Accessible list of functions and classes |
| `Alt + N` / `Alt + P` | Structure | Jump to the next / previous header |
| `F7` | Diagnostics | Validate syntax and delimiter balancing |
| `F4` | Diagnostics | Jump to the Traceback error line |
| `F9` | Debugging | Toggle breakpoint |
| `F10` | Debugging | Interactive step-by-step debugging |
| `Ctrl + T` | Tests | Run unit tests |
| `Ctrl + Shift + P` | Environment | Interpreter and virtual environment manager |
| `Ctrl + Shift + E` | Tools | Accessible file and project explorer |
| `F11` | Help | Accessible keyboard shortcuts dialog |
| `F12` | Help | Full documentation in the browser |
| `Escape` | General | Close the active dialog |

---

## Training Plan

| Module | Chapters | Content |
| :--- | :--- | :--- |
| **0. Computing Foundations** | 1 to 5 | Architecture, binary system, CPU, screen readers, and algorithmic thinking. |
| **1. Output, Memory, and Variables** | 6 to 9 | Standard output with `print()`, dynamic assignment, and PEP 8. |
| **2. Fundamental Types and Interaction** | 10 to 14 | Types `int`, `float`, `str`, interpolation with f-strings, and capture with `input()`. |
| **3. Boolean Logic and Control** | 15 to 19 | Boolean expressions, logical connectors, and `if`, `else`, `elif` conditionals. |
| **4. Loops and Automation** | 20 to 23 | `for` loops with `range()`, `while` loops, execution control, and flow directives. |
| **5. Data Structures** | 24 to 28 | Indexed lists, mutation operations, iteration, tuples, and dictionaries. |
| **6. Modularity and Exceptions** | 29 to 32 | Functions with `def`, return with `return`, scope, and failure handling (`try`/`except`). |
| **7. Persistence and Objects (OOP)** | 33 to 36 | Safe file handling (`with open`), JSON, classes, instances, and methods. |
| **8. Standard Library and Project** | 37 to 40 | Modules `math`, `random`, `datetime`, `sqlite3` databases, and the final capstone project. |

---

## Configuration

Access path: **NVDA Menu > Preferences > Settings > Learning Python with NVDA**

* **Startup mode:** Guided Learning Mode or Standalone Editor Mode.
* **Acoustic signals:** Enable PEP 8 indentation sonification and alerts.
* **F1 key mode:** Offline local explanation or AI query.
* **Gemini API key:** Optional configuration for AI queries.

The environment language is detected automatically from the NVDA language (variants such as `pt_BR` or `en_US` are normalized to the available catalog) and can be changed on the fly at any time from the **Help > Switch language** menu of the tutor window.

---

## Adding a New Lesson Language

Translated curricula live in JSON catalogs independent of the code (`addon/locale/<language>/lessons.json`), alongside the rest of the add-on localization. Upon recompilation, the new language appears automatically in the NVDA language detection (variants such as `pt_BR` or `en_US` are normalized to the available catalog) and in the *Switch language* menu.

1. Generate the Spanish base catalog from the source code:

   ```bash
   uv run python tools/extract_lessons.py
   ```

2. Copy `addon/locale/es/lessons.json` to `addon/locale/<language>/lessons.json` (for example, `addon/locale/fr/lessons.json`) and translate the values. Keys remain in Spanish. The translation can be partial (chapter by chapter): anything missing will be shown in Spanish as a fallback.

3. Respect these rules in code challenges (validators live in `curriculum.py` and are never translated):
   * `salida_esperada`: must remain byte-identical to the original.
   * `codigo`: only `#` comments are translated; string literals must match the original exactly.
   * `opciones`: keep the order of the options (the correct answer is validated by position) and translate each complete option.

4. Add-on interface (optional but recommended), via the official gettext flow:
   * Generate the template and create the language catalog (requires gettext on the PATH):

     ```bash
     scons pot
     msginit -i python_tutor.pot -o addon/locale/<language>/LC_MESSAGES/nvda.po
     ```

     (or copy `addon/locale/es/LC_MESSAGES/nvda.po`, already aligned with the template).
   * Fill in the `msgstr` values (the `msgid` keys remain in Spanish, the base language) and recompile with `scons`: the `.mo` files, the translated manifest, and the HTML documentation are generated automatically.
   * Also translate `addon/doc/<language>/readme.md` (the documentation opened with `F12`); `scons` generates the corresponding HTML automatically.

5. Recompile and verify:

   ```bash
   scons
   python -m unittest tests/test_tutor.py
   ```

---

## Automated Tests

The project implements unit tests based on `unittest` to verify the correct functioning of the editor and the integrity of the lessons:

```bash
python -m unittest tests/test_tutor.py
```

---

## Support and Collaboration

* **Issue reporting:** [GitHub issue tracker](https://github.com/KevinVelasquezVargas/python_tutor/issues)
* **Direct contact:** [kevinvelasquezvargas@gmail.com](mailto:kevinvelasquezvargas@gmail.com)
* **Sponsorship:** [Voluntary donations via PayPal](https://paypal.me/kevinvelasquezvargas)

---

## License

This project is licensed under the GNU General Public License v3.0 (GPLv3). See the [LICENSE](LICENSE) file for more details.

**Author:** Kevin Andrés Velasquez Vargas.
