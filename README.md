# Python Learning with NVDA

[![Version](https://img.shields.io/github/v/release/KevinVelasquezVargas/python_tutor?label=Version&color=blue)](https://github.com/KevinVelasquezVargas/python_tutor/releases/latest)
[![NVDA Compatibility](https://img.shields.io/badge/NVDA-2022.1%20to%202026.2-005a9c)](https://github.com/KevinVelasquezVargas/python_tutor)
[![License](https://img.shields.io/badge/License-GPL%20v3-green)](COPYING.txt)
[![Unit Tests](https://github.com/KevinVelasquezVargas/python_tutor/actions/workflows/unitTests.yml/badge.svg)](https://github.com/KevinVelasquezVargas/python_tutor/actions)
[![Downloads](https://img.shields.io/github/downloads/KevinVelasquezVargas/python_tutor/total?label=Downloads&color=orange)](https://github.com/KevinVelasquezVargas/python_tutor/releases)

> 🌐 **Language / Idioma:** [English](README.md) | [Español](README.es.md)  
> 📥 **Direct Download of the Official Installer:**  
> [**Download python_tutor-2.0.0.nvda-addon (980 KB)**](https://github.com/KevinVelasquezVargas/python_tutor/releases/download/v2.0.0/python_tutor-2.0.0.nvda-addon)  
> *(Ready to install in NVDA simply by opening the file or pressing Enter on it)*

Training tool and accessible code editor designed for Python programming using the NVDA screen reader. It provides a structured learning curriculum across 32 conceptual and practical chapters (128 lessons), complemented by a dual-mode workspace: a guided tutor mode and a standalone editor mode. Features code structure navigation across functions and classes, acoustic indentation and structure cues, real-time delimiter verification, and simplified error diagnostic messages.

* **Version:** 2.0.0
* **Author:** Kevin Andrés Velasquez Vargas
* **Compatibility:** NVDA 2022.1.0 to 2026.2.0
* **License:** GNU General Public License v3.0 (GPLv3)
* **Repository:** [Visit the official GitHub repository](https://github.com/KevinVelasquezVargas/python_tutor)

---

## Table of Contents
* [1. Introduction](#1-introduction)
* [2. Launching the Add-on](#2-launching-the-add-on)
* [3. Dual Usage Modes](#3-dual-usage-modes)
* [4. Navigation and Editor Tools](#4-navigation-and-editor-tools)
* [5. Learning Curriculum (32 Chapters and 128 Lessons)](#5-learning-curriculum)
* [6. Configuration and Preferences](#6-configuration-and-preferences)
* [7. Changelog](#7-changelog)
* [8. Support](#8-support)
* [9. Donations](#9-donations)

---

## 1. Introduction
Python Learning with NVDA is a comprehensive add-on designed to eliminate the accessibility barriers experienced by blind and visually impaired users when learning and writing Python code.

It combines an active non-visual pedagogy ("Concepts First", micro-challenges, conceptual quizzes, and everyday real-world analogies) with a professional, focused, distraction-free accessible code editor.

## 2. Launching the Add-on
* **Global Shortcut:** `NVDA + Control + Shift + P`
* **NVDA Menu:** NVDA Menu (`NVDA + N`) > Tools > Python Learning with NVDA > Python Learning with NVDA...

## 3. Dual Usage Modes
Pressing `Control + M` (or via the Tools menu) toggles at any time between:

* **Learning Mode:** Step-by-step guided environment with educational instructions, layered hints, and automated exercise assessment.
* **Standalone Editor Mode:** Pure editing environment without pedagogical panels. Maximizes workspace for writing, debugging, and running custom scripts with all accessibility tools active and fluent tab navigation.

## 4. Navigation and Editor Tools

### Lesson Navigation
* `Alt + Right Arrow`: Go to next lesson step.
* `Alt + Left Arrow`: Go to previous lesson step.

### Direct Structural Navigation
* `Alt + N` / `Alt + P`: Jump to next / previous function (`def`) or class (`class`).
* `Control + Shift + O`: Accessible symbol dialog to list all functions and classes and jump to them instantly.

### Search and Navigation
* `Control + F`: Accessible search dialog to find text in the editor.
* `Control + G`: Accessible go-to-line dialog.

### File Management
* `Control + N`: Create a new empty script in the editor.
* `Control + O`: Open an existing Python (`.py`) file.
* `Control + S`: Save current script.
* `Control + Shift + S`: Save script with a new name or location.

### Execution and Diagnostics
* `F5` or `Control + Enter`: Run current script in the integrated console.
* `F4`: Immediate jump to the exact Traceback error line with accessible diagnostic explanation.
* `F7`: Real-time delimiter balance checker `()`, `[]`, `{}` and unclosed string quotes.

### Non-Invasive Console Reading
* `Control + Shift + C`: Speak entire console output without moving focus from the editor.
* `Control + 6`: Speak the last emitted line in the console.
* `F6`: Toggle physical focus between editor and output console.

### Code Assistance and Acoustic Signals
* `F1` (Human-Language Translator): Explains the line of code at the cursor in simple, natural language.
* **PEP 8 Acoustic Indentation Cues:** Real-time audio tones indicating indentation depth (0, 4, 8, 12 spaces) and block opening after colons (`:`).

### Efficient Editing
* `Control + /` (or `Control + K`): Comment or uncomment current line.
* `Control + D`: Duplicate current line downward.
* `Control + Shift + K`: Delete current line.
* `Control + L`: Announce current line and column of the cursor.
* `Control + Space`: Autocomplete Python keywords and identifiers.

### Advanced IDE Tools
* `F9`: Interactive Step Debugger for step-by-step code inspection.
* `Control + Shift + T`: Test Runner dialog for executing `unittest` test suites.
* `Control + Shift + I`: Python Interpreter Manager dialog to configure local Python environments.
* `Control + Shift + F`: PEP 8 code auto-formatter.
* `Control + Shift + X`: Extract Function refactoring assistant.
* `F2` (in editor): Rename Symbol refactoring dialog.

### Support and Utility
* `Control + J`: Open quick testing console (REPL).
* `Control + 1`: Chapter selector dialog (with progressive unlocking system).
* `Control + R`: Reset starter code for the current exercise.
* `F2` (general): Full keyboard shortcuts guide dialog.
* `F12`: Open accessible user manual in default web browser.
* `Escape`: Close Python Tutor window immediately from any control.

## 5. Learning Curriculum
* **Phase 0: Conceptual Foundations:** Computational thinking, everyday algorithms, CPU and memory architecture, elementary boolean logic (Chapters 1 to 3).
* **Phase 1: Basic Syntax and Elementary Types:** First print, variables, integers and floats, strings (`str`), user input with `input` (Chapters 4 to 8).
* **Phase 2: Control Flow and Collections:** Relational conditions, `if` and PEP 8 indentation, `elif`/`else`, lists, mutable methods, `for`/`range` loops, `while`, key-value dictionaries (Chapters 9 to 16).
* **Phase 3: Modularity, Robustness, and Files:** Tuples and sets (`set`), functions with `def`, `return` and scope, exception handling (`try`/`except`), accessible Traceback reading, file management with `with open` (Chapters 17 to 22).
* **Phase 4: Object-Oriented Programming (OOP):** Classes and attributes, `__init__` constructor and `self` parameter, instance methods, inheritance with `super()`, string representation with `__str__` (Chapters 23 to 27).
* **Phase 5: Professional Development and Testing:** Standard libraries (`math`, `random`, `datetime`), JSON data exchange, local databases with SQLite3, REST API consumption, unit testing with `unittest` (Chapters 28 to 32).

## 6. Configuration and Preferences
To customize add-on behavior, go to **NVDA Menu > Preferences > Settings > Python Learning with NVDA**:

* **Start in standalone Editor Mode:** Directly opens pure editing workspace, hiding tutor lesson sections.
* **Confirmation and event sound effects:** Toggles sound alerts when evaluating exercises or changing states.
* **Indentation and structure sound alerts:** Controls acoustic feedback for indentation spaces and block openings.
* **Show welcome dialog:** Configures whether to display the welcome dialog when launching the add-on.
* **Support and Donations:** Quick buttons to send support emails or make voluntary contributions.

## 7. Changelog

### Version 2.0.0
* **Dual Usage Modes:** Switch instantly with `Control + M` between guided Learning Mode and standalone Editor Mode for distraction-free coding.
* **Comprehensive Curriculum Expansion:** Expanded to 32 chapters and 128 practical lessons, covering computational thinking, OOP, SQLite3, REST APIs, and unit tests with `unittest`.
* **Advanced Structural Navigation:** Jump directly across functions and classes (`Alt + N` / `Alt + P`) and open symbol picker (`Control + Shift + O`).
* **Real-time Diagnostics and Error Jumping:** Delimiter and quote balance checker (`F7`) and instant jump to Traceback error lines (`F4`).
* **Non-invasive Console Review:** Speech-based console review shortcuts (`Control + Shift + C` and `Control + 6`).
* **Professional IDE Tools:** Added Step Debugger (`F9`), Unit Test Runner (`Control + Shift + T`), Interpreter Manager (`Control + Shift + I`), PEP 8 Formatter (`Control + Shift + F`), and Refactoring Dialogs (`F2` / `Control + Shift + X`).
* **Internationalization (i18n):** Complete bilingual support in English and Spanish compliant with official NVDA Add-on Store standards.
* **Updated Compatibility Engine:** Extended support for modern NVDA versions (from NVDA 2022.1.0 to 2026.2.0).

### Version 1.0.0
* Initial release with foundational programming curriculum and interactive execution in NVDA.

## 8. Support
If you wish to report a bug, request a new feature, share pedagogical feedback, or need assistance, contact us through:

* **Email:** [Send a support email message](mailto:kevinvelasquezvargas@gmail.com?subject=Support%20-%20Python%20Learning%20with%20NVDA)
* **Issue Tracker:** [Open an issue on GitHub](https://github.com/KevinVelasquezVargas/python_tutor/issues)

## 9. Donations
This project is distributed completely free of charge under the open-source philosophy, dedicated to ensuring equitable access to computer science education for blind and visually impaired individuals.

If this add-on has helped you in your learning or teaching journey and you would like to support its ongoing development and maintenance:

* **Direct Link:** [Make a voluntary donation via PayPal](https://paypal.me/kevinvelasquezvargas)

---

Copyright © 2026 Kevin Andrés Velasquez Vargas.
