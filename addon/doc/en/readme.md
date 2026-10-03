# Learning Python with NVDA

* **Version:** 1.0.0
* **Author:** Kevin Andrés Velasquez Vargas
* **Compatibility:** NVDA 2022.1 to 2026.2
* **License:** GNU General Public License v3.0 (GPLv3)
* **Repository:** [Official GitHub Repository](https://github.com/KevinVelasquezVargas/python_tutor)

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Key Features](#2-key-features)
3. [Keyboard Shortcuts](#3-keyboard-shortcuts)
4. [Comprehensive Curriculum (40 Chapters)](#4-comprehensive-curriculum-40-chapters)
5. [Configuration](#5-configuration)
6. [Changelog](#6-changelog)
7. [Support](#7-support)
8. [Collaboration and Donations](#8-collaboration-and-donations)

---

## 1. Introduction

**Learning Python with NVDA** is a fully accessible pedagogical environment engineered specifically for blind and visually impaired individuals using the NVDA screen reader. The syllabus strictly follows a "Concepts First" approach, establishing computer architecture, execution pipelines, and accessible workflow mental models prior to formal code authoring, guaranteeing self-reliant proficiency.

## 2. Key Features

* **Guided pedagogical workflow:** 40 chapters organized across 9 modular phases, providing step-by-step guidance, progressive hints, and native multiple-choice quizzes (`wx.RadioBox`).
* **Dual workspace modes:** Seamlessly switch between Guided Learning Mode and clean Standalone Editor Mode via <kbd>Ctrl+M</kbd>.
* **Zero external runtime dependencies:** Relies exclusively on Python's built-in standard library (`sqlite3`, `json`, `math`, `random`, `datetime`), ensuring maximum security and cross-version stability.
* **Non-visual auditory feedback:** Optional acoustic cues for PEP 8 indentation depth, syntax warnings, and real-time traceback error locator.
* **Accessible IDE tools:** Contextual code autocompletion, PEP 8 auto-formatter, delimiter balancing engine, guided debugger, and interactive REPL console.
* **Full bilingual support:** Native support for both Spanish and English across all lessons, interface menus, and error messages.

## 3. Keyboard Shortcuts

| Shortcut | Category | Action |
| :--- | :--- | :--- |
| <kbd>NVDA+Ctrl+Shift+P</kbd> | Global | Open or focus add-on window. |
| <kbd>Ctrl+M</kbd> | Modes | Toggle between Tutor and Standalone Editor Mode. |
| <kbd>Ctrl+Enter</kbd> | Execution | Run code and verify challenge solution. |
| <kbd>F5</kbd> | Execution | Run active Python script. |
| <kbd>Alt+Right Arrow</kbd> | Navigation | Advance to next lesson step. |
| <kbd>Alt+Left Arrow</kbd> | Navigation | Return to previous lesson step. |
| <kbd>F3</kbd> | Tutor | Read active instruction without moving cursor. |
| <kbd>Ctrl+P</kbd> | Tutor | Request pedagogical hint. |
| <kbd>F1</kbd> | Tutor | Explain current line of code (offline local mode). |
| <kbd>Shift+F1</kbd> | Tutor | Query built-in documentation for symbol under cursor. |
| <kbd>Ctrl+R</kbd> | Tutor | Reset starter code for current exercise. |
| <kbd>Ctrl+1</kbd> | Tutor | Open chapter selector and view progress. |
| <kbd>Ctrl+J</kbd> | Tools | Open interactive REPL console. |
| <kbd>Ctrl+Shift+I</kbd> | Tools | Consult AI assistant (via Google Gemini API). |
| <kbd>F6</kbd> | Navigation | Switch focus between code editor and output console. |
| <kbd>Ctrl+4</kbd> | Navigation | Move focus to code editor. |
| <kbd>Ctrl+5</kbd> | Navigation | Move focus to console output. |
| <kbd>Ctrl+6</kbd> | Console | Read last output line. |
| <kbd>Ctrl+Shift+C</kbd> | Console | Read all accumulated console output. |
| <kbd>Ctrl+L</kbd> | Editing | Announce current line and column. |
| <kbd>Ctrl+N</kbd> | File | Create new script. |
| <kbd>Ctrl+O</kbd> | File | Open existing `.py` file. |
| <kbd>Ctrl+S</kbd> | File | Save current file. |
| <kbd>Ctrl+Shift+S</kbd> | File | Save as. |
| <kbd>Ctrl+F</kbd> | Editing | Find text in active file. |
| <kbd>Ctrl+G</kbd> | Editing | Go to specific line number. |
| <kbd>Ctrl+Space</kbd> | Editing | Accessible code autocompletion. |
| <kbd>Shift+Alt+F</kbd> | Editing | Format code with PEP 8. |
| <kbd>Ctrl+/</kbd> | Editing | Toggle line comment (`#`). |
| <kbd>Ctrl+D</kbd> | Editing | Duplicate current line. |
| <kbd>Ctrl+Shift+K</kbd> | Editing | Delete current line. |
| <kbd>Ctrl+Shift+R</kbd> | Refactor | Extract selection to new function. |
| <kbd>F2</kbd> | Refactor | Rename identifier across file. |
| <kbd>Ctrl+Shift+O</kbd> | Structure | List functions and classes in file. |
| <kbd>Alt+N</kbd> | Structure | Jump to next function or class header. |
| <kbd>Alt+P</kbd> | Structure | Jump to previous function or class header. |
| <kbd>F7</kbd> | Diagnostics | Check syntax and delimiter matching. |
| <kbd>F4</kbd> | Diagnostics | Move cursor directly to traceback error line. |
| <kbd>F9</kbd> | Debugging | Toggle breakpoint. |
| <kbd>F10</kbd> | Debugging | Start step-by-step interactive debugger. |
| <kbd>Ctrl+T</kbd> | Testing | Run automated unit test suite. |
| <kbd>Ctrl+Shift+P</kbd> | Environment | Manage Python interpreters and virtual environments. |
| <kbd>Ctrl+Shift+E</kbd> | Tools | Accessible project file explorer. |
| <kbd>F11</kbd> | Help | View keyboard shortcuts reference dialog. |
| <kbd>F12</kbd> | Help | Open this user documentation in web browser. |
| <kbd>Escape</kbd> | General | Close current dialog or window. |

## 4. Comprehensive Curriculum (40 Chapters)

### Phase 0: Computing Foundations (Chapters 1 to 5)
* **Chapter 1:** Computer architecture, binary numeral system, and RAM/CPU hierarchy.
* **Chapter 2:** Compilers, interpreters, bytecode, and Python execution flow.
* **Chapter 3:** Python history, design philosophy, and The Zen of Python.
* **Chapter 4:** Screen reader workflows and accessible coding practices with NVDA.
* **Chapter 5:** Computational thinking, algorithms, and non-visual debugging strategies.

### Phase 1: Output, Memory, and Variables (Chapters 6 to 9)
* **Chapter 6:** Standard output streams and the `print()` function.
* **Chapter 7:** Memory models, object references, and variable assignment.
* **Chapter 8:** Clean documentation standards and inline comments.
* **Chapter 9:** Dynamic retyping and variable lifecycle.

### Phase 2: Fundamental Types and User Interaction (Chapters 10 to 14)
* **Chapter 10:** Integer numbers (`int`) and fundamental arithmetic operators.
* **Chapter 11:** Floating-point numbers (`float`) and IEEE-754 precision.
* **Chapter 12:** Text strings (`str`), indexing, slicing, and escape sequences.
* **Chapter 13:** Modern string interpolation with f-strings.
* **Chapter 14:** Interactive user input with `input()` and typecasting.

### Phase 3: Boolean Logic and Control Flow (Chapters 15 to 19)
* **Chapter 15:** Boolean data type (`bool`) and relational comparison operators.
* **Chapter 16:** Logical connectors (`and`, `or`, `not`) and truth evaluation.
* **Chapter 17:** Conditional branches: `if` statement and PEP 8 indentation.
* **Chapter 18:** Mutual exclusivity: the `else` clause.
* **Chapter 19:** Multi-branch chaining: `elif` ladders.

### Phase 4: Loops and Iterations (Chapters 20 to 23)
* **Chapter 20:** Definite iteration: `for` loops and `range()` sequencing.
* **Chapter 21:** Indefinite iteration: `while` loops and condition testing.
* **Chapter 22:** Preventing infinite loops and defensive termination.
* **Chapter 23:** Loop control statements: `break`, `continue`, and loop `else`.

### Phase 5: Compound Data Structures (Chapters 24 to 28)
* **Chapter 24:** Mutable lists, indexing, slicing, and memory referencing.
* **Chapter 25:** List operations: `append()`, `insert()`, `remove()`, and `pop()`.
* **Chapter 26:** Indexed iteration using `enumerate()`.
* **Chapter 27:** Immutable tuples and sequence unpacking patterns.
* **Chapter 28:** Key-value mappings: Python dictionaries (`dict`).

### Phase 6: Modularity, Functions, and Exceptions (Chapters 29 to 32)
* **Chapter 29:** Subroutine definition with `def`, positional and keyword arguments.
* **Chapter 30:** Value return: `return` semantics vs console printing.
* **Chapter 31:** Variable scoping: local, global, and LEGB rule.
* **Chapter 32:** Robust error handling: `try`, `except`, `else`, and `finally`.

### Phase 7: Persistence and Object-Oriented Programming (Chapters 33 to 36)
* **Chapter 33:** Safe file I/O operations using context managers (`with open()`).
* **Chapter 34:** Data interchange and serialization with JSON.
* **Chapter 35:** Object-Oriented Programming: classes, blueprints, and instances.
* **Chapter 36:** Encapsulation, constructor `__init__`, and `self` reference.

### Phase 8: Standard Library and Capstone Project (Chapters 37 to 40)
* **Chapter 37:** Standard modules: `math`, `random`, and `datetime`.
* **Chapter 38:** Relational databases with embedded `sqlite3`.
* **Chapter 39:** Non-visual user interface design and software accessibility.
* **Chapter 40:** Capstone project: End-to-end accessible data management application.

## 5. Configuration

Configurable via **NVDA Menu > Preferences > Settings > Learning Python with NVDA**:

* **Interface language:** Automatic (follows NVDA), Spanish, or English.
* **Default mode on launch:** Choose between Tutor Mode or Standalone Editor Mode.
* **Auditory cues:** Toggle event chimes and PEP 8 acoustic indentation indicator.
* **Gemini API Key:** Optional key to enable the interactive AI assistant (<kbd>Ctrl+Shift+I</kbd>). Offline explanations (<kbd>F1</kbd>) function locally without requiring any key.

## 6. Changelog

### Version 1.0.0
* Initial official release.

## 7. Support

To report issues, ask questions, or contribute improvements:

* **Contact email:** [kevinvelasquezvargas@gmail.com](mailto:kevinvelasquezvargas@gmail.com)
* **Issue tracker:** [Official GitHub Issues](https://github.com/KevinVelasquezVargas/python_tutor/issues)

## 8. Collaboration and Donations

Learning Python with NVDA is a 100% free, accessible, non-profit community project built to guarantee equal access to computer science education. If this add-on aids your learning or professional development, voluntary donations help sustain its ongoing maintenance and the creation of new inclusive educational material:

* **Donate via PayPal:** [https://paypal.me/kevinvelasquezvargas](https://paypal.me/kevinvelasquezvargas)

---

Copyright © 2026 Kevin Andrés Velasquez Vargas. Released under the GNU General Public License v3.0 (GPLv3).
