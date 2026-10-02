# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/gui_frame.py
# Propósito: Interfaz gráfica accesible, estructurada y con funciones avanzadas de edición.
# Autor: Kevin Andrés Velasquez Vargas
# Internacionalización (i18n): MisterK-Dev (desarrollado con Google Antigravity 2.0)
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================
import os
import re
import urllib.parse
import webbrowser
import wx

try:
    import addonHandler
    addonHandler.initTranslation()
except Exception:
    pass

try:
    _
except NameError:
    def _(msg):
        return msg

try:
    import ui
    import speech
except ImportError:
    ui = None
    speech = None

from .audio_manager import SoundManager
from .executor import (
    ejecutar_codigo_seguro,
    generar_comparacion_salida,
    detectar_errores_teclado_comunes,
    comprobar_balanceo_delimitadores
)
from .curriculum import CURRICULUM, GLOSARIO
from .progress import ProgressManager
from .repl_dialog import ReplDialog
from .translator import traducir_linea_codigo
from .ide_tools import (
    DOCS_PYTHON,
    obtener_documentacion_simbolo,
    formatear_codigo_pep8,
    AutoCompleteDialog,
    RenameSymbolDialog,
    ExtractFunctionDialog,
    StepDebuggerDialog,
    TestRunnerDialog,
    InterpreterManagerDialog
)

try:
    import docHandler
except ImportError:
    docHandler = None


class FindDialog(wx.Dialog):
    """Diálogo accesible para buscar texto dentro del editor de código."""
    def __init__(self, parent, text_ctrl):
        # Translators: Dialog title for text search.
        super(FindDialog, self).__init__(parent, title=_("Find in Editor"), size=(480, 240))
        self.text_ctrl = text_ctrl

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Translators: Label for search query text field.
        lbl = wx.StaticText(panel, label=_("Text to &find:"))
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.query_ctrl = wx.TextCtrl(panel)
        # Translators: Accessible name for search text field in Find dialog.
        self.query_ctrl.SetName(_("Search text"))
        vbox.Add(self.query_ctrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # Translators: Checkbox label for case-sensitive search.
        self.chk_case = wx.CheckBox(panel, label=_("Match &case"))
        vbox.Add(self.chk_case, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Button to find next occurrence.
        btn_find = wx.Button(panel, wx.ID_OK, label=_("&Find Next"))
        btn_find.SetDefault()
        # Translators: Button to close search dialog.
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label=_("&Close"))
        hbox.Add(btn_find, flag=wx.RIGHT, border=8)
        hbox.Add(btn_cancel)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.ALL, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        btn_find.Bind(wx.EVT_BUTTON, self.on_find)
        self.CenterOnParent()
        self.query_ctrl.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

    def on_find(self, event):
        q = self.query_ctrl.GetValue()
        if not q:
            if ui:
                # Translators: Speech announcement when user submits empty search field.
                ui.message(_("Enter text to search."))
            return

        full_text = self.text_ctrl.GetValue()
        match_case = self.chk_case.GetValue()
        search_in = full_text if match_case else full_text.lower()
        search_for = q if match_case else q.lower()

        current_pos = self.text_ctrl.GetInsertionPoint()
        idx = search_in.find(search_for, current_pos + 1)
        if idx == -1:
            idx = search_in.find(search_for, 0)

        if idx != -1:
            self.text_ctrl.SetSelection(idx, idx + len(q))
            self.text_ctrl.SetInsertionPoint(idx)
            row = full_text[:idx].count('\n') + 1
            # Translators: Speech notification when search query is found.
            msg = _("Found '{query}' on line {line}").format(query=q, line=row)
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
            self.EndModal(wx.ID_OK)
        else:
            # Translators: Speech notification when search query is not found.
            msg = _("'{query}' not found in code.").format(query=q)
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)


class GoToLineDialog(wx.Dialog):
    """Diálogo accesible para desplazarse a un número de línea específico."""
    def __init__(self, parent, text_ctrl):
        # Translators: Dialog title for jump to line number.
        super(GoToLineDialog, self).__init__(parent, title=_("Go to Line"), size=(420, 200))
        self.text_ctrl = text_ctrl
        total_lines = self.text_ctrl.GetNumberOfLines()
        if total_lines < 1:
            total_lines = self.text_ctrl.GetValue().count('\n') + 1

        self.total_lines = max(1, total_lines)

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Translators: Label indicating available line number range.
        lbl = wx.StaticText(panel, label=_("&Line number (1 - {total}):").format(total=self.total_lines))
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.line_ctrl = wx.TextCtrl(panel)
        # Translators: Accessible name for line number field in Go To Line dialog.
        self.line_ctrl.SetName(_("Line number"))
        vbox.Add(self.line_ctrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Button to execute line jump.
        btn_go = wx.Button(panel, wx.ID_OK, label=_("&Go to Line"))
        btn_go.SetDefault()
        # Translators: Button to cancel line jump dialog.
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label=_("&Cancel"))
        hbox.Add(btn_go, flag=wx.RIGHT, border=8)
        hbox.Add(btn_cancel)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.ALL, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        btn_go.Bind(wx.EVT_BUTTON, self.on_go)
        self.CenterOnParent()
        self.line_ctrl.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

    def on_go(self, event):
        val = self.line_ctrl.GetValue().strip()
        try:
            line_no = int(val)
        except ValueError:
            if ui:
                # Translators: Speech announcement for invalid line number entry.
                ui.message(_("Please enter a valid line number."))
            return

        if 1 <= line_no <= self.total_lines:
            src = self.text_ctrl.GetValue()
            lineas = src.split('\n')
            pt = len('\n'.join(lineas[:line_no - 1])) + 1 if line_no > 1 else 0
            self.text_ctrl.SetInsertionPoint(min(pt, len(src)))
            self.text_ctrl.SetFocus()
            # Translators: Speech notification confirming cursor positioned at line.
            msg = _("Cursor on line {line}").format(line=line_no)
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
            self.EndModal(wx.ID_OK)
        else:
            if ui:
                # Translators: Speech error announcement when line number is out of bounds.
                ui.message(_("The line must be between 1 and {total}.").format(total=self.total_lines))


class ChapterSelectDialog(wx.Dialog):
    """Diálogo accesible para saltar directamente a cualquier capítulo del temario."""
    def __init__(self, parent, current_idx):
        # Translators: Dialog title for selecting curriculum chapters.
        super(ChapterSelectDialog, self).__init__(parent, title=_("Curriculum Chapter Selector"), size=(650, 480))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Translators: Label for chapter selection list.
        lbl = wx.StaticText(panel, label=_("Choose the &chapter you want to access:"))
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.opciones = []
        self.cap_estados = []
        for i, cap in enumerate(CURRICULUM):
            total_pasos = len(cap.get("pasos", []))
            completado = ProgressManager.is_chapter_completed(i, total_pasos)
            desbloqueado = ProgressManager.is_chapter_unlocked(i)
            self.cap_estados.append((desbloqueado, completado))
            if completado:
                # Translators: Status prefix for completed chapter.
                estado_str = _("Completed, ")
            elif desbloqueado:
                # Translators: Status prefix for available chapter.
                estado_str = _("Available, ")
            else:
                # Translators: Status prefix for locked chapter.
                estado_str = _("Locked, ")
            # Translators: Fallback title format for chapter if not explicitly named.
            default_chapter_title = _("Chapter {num}").format(num=i+1)
            self.opciones.append(f"{estado_str}{cap.get('titulo', default_chapter_title)}")

        self.list_box = wx.ListBox(panel, choices=self.opciones)
        # Translators: Accessible name for chapter selection list.
        self.list_box.SetName(_("Chapter list. Press Enter or click to select."))
        if 0 <= current_idx < len(self.opciones):
            self.list_box.SetSelection(current_idx)
        vbox.Add(self.list_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Button to load chosen chapter.
        btn_ok = wx.Button(panel, wx.ID_OK, label=_("&Load Chapter"))
        # Translators: Button to cancel line jump dialog.
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label=_("&Cancel"))
        hbox.Add(btn_ok, flag=wx.RIGHT, border=8)
        hbox.Add(btn_cancel)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        btn_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        self.list_box.Bind(wx.EVT_LISTBOX_DCLICK, self.on_ok)
        self.CenterOnParent()
        self.list_box.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

    def on_ok(self, event):
        sel = self.list_box.GetSelection()
        if sel != wx.NOT_FOUND:
            desbloqueado, _completado = self.cap_estados[sel]
            if not desbloqueado:
                # Translators: Message explaining a chapter is locked.
                msg = _("This chapter is locked. You must complete all steps of the previous chapter to unlock it.")
                if ui:
                    ui.message(msg)
                # Translators: Message box title when chapter is locked.
                wx.MessageBox(msg, _("Chapter Locked"), wx.OK | wx.ICON_WARNING, self)
                return
        self.EndModal(wx.ID_OK)

    def get_selected_index(self):
        return self.list_box.GetSelection()


class HintDialog(wx.Dialog):
    """Diálogo accesible para el sistema escalonado de pistas pedagógicas."""
    def __init__(self, parent, pistas, nivel_actual=0):
        # Translators: Title for pedagogical assistance hint dialog.
        super(HintDialog, self).__init__(parent, title=_("Assistance Hint"), size=(620, 380))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        total_pistas = max(1, len(pistas))
        # Translators: Label indicating current hint tier level.
        lbl = wx.StaticText(panel, label=_("Available hint (Level {level} of {total}):").format(level=min(nivel_actual + 1, total_pistas), total=total_pistas))
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        # Translators: Fallback message when no hint text is defined.
        fallback_hint = _("Review the exercise instructions.")
        texto_pista = pistas[nivel_actual] if nivel_actual < len(pistas) else (pistas[-1] if pistas else fallback_hint)
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.text_ctrl.SetValue(texto_pista)
        # Translators: Accessible name for hint text box.
        self.text_ctrl.SetName(_("Hint content."))
        vbox.Add(self.text_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        # Translators: Confirmation button to dismiss hint.
        btn_ok = wx.Button(panel, wx.ID_OK, label=_("&Understood"))
        vbox.Add(btn_ok, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.CenterOnParent()
        self.text_ctrl.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()


class WelcomeDialog(wx.Dialog):
    """Diálogo accesible de bienvenida para orientar a nuevos estudiantes."""
    def __init__(self, parent):
        # Translators: Title for the first-launch welcome dialog.
        super(WelcomeDialog, self).__init__(parent, title=_("Welcome to Python Learning with NVDA"), size=(660, 440))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Translators: Welcome guide text displayed on first launch.
        mensaje = _(
            "Welcome to Python Learning with NVDA!\n\n"
            "This add-on will guide you step by step in learning Python programming, "
            "starting from fundamental concepts and advancing progressively through "
            "practical exercises designed to be solved directly in the editor.\n\n"
            "The environment features two working modes:\n"
            "Learning Mode: Provides guided lessons, theoretical explanations, and automatic solution verification.\n"
            "Standalone Editor Mode: A clutter-free, accessible editor to write and run your own scripts.\n\n"
            "You can consult the full list of keyboard shortcuts at any time by pressing F11 or from the Help menu, "
            "and learn more about the add-on in About.\n\n"
            "Press the Start learning button or press Enter to begin your first lesson."
        )

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(mensaje)
        # Translators: Accessible name for welcome text control.
        txt.SetName(_("Welcome message"))
        vbox.Add(txt, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        prog = ProgressManager.load_progress()
        # Translators: Checkbox to show welcome dialog on start.
        self.chk_mostrar = wx.CheckBox(panel, label=_("&Show this welcome guide on startup"))
        self.chk_mostrar.SetValue(prog.get("show_welcome", True))
        vbox.Add(self.chk_mostrar, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM, border=12)

        # Translators: Primary button to start learning curriculum.
        btn_comenzar = wx.Button(panel, wx.ID_OK, label=_("&Start learning"))
        btn_comenzar.SetDefault()
        vbox.Add(btn_comenzar, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.CenterOnParent()
        btn_comenzar.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.guardar_preferencia()
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

    def guardar_preferencia(self):
        ProgressManager.set_setting("show_welcome", self.chk_mostrar.GetValue())


class ShortcutsDialog(wx.Dialog):
    """Diálogo accesible que enumera todos los atajos de teclado del complemento."""
    def __init__(self, parent):
        # Translators: Dialog title for keyboard shortcuts guide.
        super(ShortcutsDialog, self).__init__(parent, title=_("Keyboard Shortcuts Guide"), size=(700, 560))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Translators: Complete keyboard shortcuts reference text.
        texto_atajos = _(
            "Complete Keyboard Shortcuts Guide:\n\n"
            "Modes and Learning:\n"
            "Control + Enter or Control + E: Run code and verify solution.\n"
            "Control + M: Toggle between Learning Mode and Professional Editor-Only Mode.\n"
            "F3 or Control + I: Read the active instruction without moving focus from the editor.\n"
            "F4: Place the cursor on the exact line of the Traceback error.\n"
            "F6: Toggle focus between the code editor and the output console.\n"
            "Alt + Right Arrow: Go to next step of the lesson.\n"
            "Alt + Left Arrow: Go to previous step of the lesson.\n"
            "Control + P: Request a graduated hint.\n"
            "F1: Explain current line in simple, everyday words.\n"
            "Shift + F1: Quick documentation for symbol under cursor.\n"
            "Control + R: Reset exercise initial code.\n"
            "Control + 1: Open Chapter Selector.\n"
            "Control + J: Open quick interactive playground (REPL).\n\n"
            "Editing and IDE Development Features:\n"
            "Control + N: Create a new blank script in editor.\n"
            "Control + F: Find text in code editor.\n"
            "Control + G: Go to a specific line number.\n"
            "F2: Rename identifier or variable across the file.\n"
            "Shift + Alt + F or Control + Shift + I: Format document with PEP 8.\n"
            "Control + Shift + R: Extract selected code block to a new function.\n"
            "Control + Space: Intelligent autocompletion with documentation.\n"
            "Control + Shift + O: Accessible list of functions and classes in script.\n"
            "Alt + N: Quick jump to header of next function or class.\n"
            "Alt + P: Quick jump to header of previous function or class.\n"
            "Control + / or Control + K: Comment or uncomment current line with '# '.\n"
            "Control + D: Duplicate current line downward.\n"
            "Control + Shift + K: Delete current line.\n"
            "F7: Check syntax, quotes, and delimiter balancing.\n"
            "Control + L: Announce cursor's current line and column.\n"
            "Control + 4: Focus Code Editor directly.\n"
            "Control + 5: Focus Output Console directly.\n"
            "Control + 6: Speak the last line of the console.\n"
            "Control + Shift + C: Speak the entire console output.\n\n"
            "Debugging, Testing, and Environments:\n"
            "F9: Toggle breakpoint on current line.\n"
            "F10: Start interactive step-by-step debugger.\n"
            "Control + T: Run unit tests (accessible Test Runner).\n"
            "Control + Shift + P: Python interpreters and virtual environments manager.\n\n"
            "Files, Help, and Documentation:\n"
            "Control + O: Open Python script (.py) from disk.\n"
            "Control + S: Save current script to disk.\n"
            "Control + Shift + S: Save script with a new name or location.\n"
            "F5: Run code and verify solution.\n"
            "F11: Open this Keyboard Shortcuts Guide.\n"
            "F12: Open About documentation in web browser.\n"
            "Escape: Close tutor window immediately from any control."
        )

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(texto_atajos)
        # Translators: Accessible name for keyboard shortcuts text box.
        txt.SetName(_("Full list of keyboard shortcuts"))
        vbox.Add(txt, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        # Translators: Button to close shortcuts guide.
        btn_cerrar = wx.Button(panel, wx.ID_OK, label=_("&Close Guide"))
        btn_cerrar.SetDefault()
        vbox.Add(btn_cerrar, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.CenterOnParent()
        btn_cerrar.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()


class GlossaryDialog(wx.Dialog):
    """Buscador rápido e interactivo de definiciones del lenguaje."""
    def __init__(self, parent):
        # Translators: Dialog title for Python terms glossary.
        super(GlossaryDialog, self).__init__(parent, title=_("Python Terms Dictionary"), size=(720, 520))
        self.terminos = sorted(list(GLOSARIO.keys()))
        self.filtrados = list(self.terminos)

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        search_box = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Label for glossary search input.
        lbl = wx.StaticText(panel, label=_("Search &term:"))
        search_box.Add(lbl, flag=wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border=8)
        self.search_ctrl = wx.TextCtrl(panel)
        # Translators: Accessible name for glossary search control.
        self.search_ctrl.SetName(_("Type command or concept here to search."))
        search_box.Add(self.search_ctrl, proportion=1, flag=wx.EXPAND)
        main_sizer.Add(search_box, flag=wx.EXPAND | wx.ALL, border=10)

        content_box = wx.BoxSizer(wx.HORIZONTAL)
        self.list_box = wx.ListBox(panel, choices=self.terminos)
        # Translators: Accessible name for available glossary terms list.
        self.list_box.SetName(_("Available terms."))
        content_box.Add(self.list_box, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=10)

        self.def_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        # Translators: Accessible name for term definition readout.
        self.def_ctrl.SetName(_("Meaning of the term."))
        content_box.Add(self.def_ctrl, proportion=2, flag=wx.EXPAND)
        main_sizer.Add(content_box, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        # Translators: Button to close glossary dictionary.
        btn_cerrar = wx.Button(panel, wx.ID_CANCEL, label=_("&Close Dictionary"))
        main_sizer.Add(btn_cerrar, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)

        panel.SetSizer(main_sizer)

        self.search_ctrl.Bind(wx.EVT_TEXT, self.on_search)
        self.list_box.Bind(wx.EVT_LISTBOX, self.on_select)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)

        if self.terminos:
            self.list_box.SetSelection(0)
            self.def_ctrl.SetValue(GLOSARIO[self.terminos[0]])

        self.CenterOnParent()
        self.search_ctrl.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

    def on_search(self, event):
        q = self.search_ctrl.GetValue().lower().strip()
        self.filtrados = [t for t in self.terminos if q in t.lower()]
        self.list_box.Set(self.filtrados)
        if self.filtrados:
            self.list_box.SetSelection(0)
            self.def_ctrl.SetValue(GLOSARIO.get(self.filtrados[0], ""))
        else:
            # Translators: Notice displayed when glossary search finds no matches.
            self.def_ctrl.SetValue(_("No matches found."))

    def on_select(self, event):
        sel = self.list_box.GetStringSelection()
        if sel in GLOSARIO:
            self.def_ctrl.SetValue(GLOSARIO[sel])
            if ui:
                ui.message(sel)


class SymbolsDialog(wx.Dialog):
    """Diálogo accesible que enumera todas las funciones y clases del script para navegación directa."""
    def __init__(self, parent, code_text):
        # Translators: Dialog title for symbols navigation.
        super(SymbolsDialog, self).__init__(parent, title=_("Code Structure: Functions and Classes"), size=(680, 480))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.simbolos = []
        lineas = code_text.splitlines(True)
        pos_acum = 0
        for num_linea, linea in enumerate(lineas, start=1):
            m = re.match(r'^(?:[ \t]*)(def|class)\s+([a-zA-Z_0-9]+)', linea)
            if m:
                # Translators: Label identifying symbol as Class or Function.
                tipo = _("Class") if m.group(1) == "class" else _("Function")
                nombre = m.group(2)
                self.simbolos.append((tipo, nombre, num_linea, pos_acum))
            pos_acum += len(linea)

        # Translators: Label for symbols selector list.
        lbl = wx.StaticText(panel, label=_("Select a &function or class to jump cursor directly to its header:"))
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        # Translators: Format for symbol entry in symbols list: [Type] Name (Line X).
        opciones = [
            _("[{type}] {name} (Line {line})").format(type=tipo, name=nombre, line=lin)
            for tipo, nombre, lin, _ in self.simbolos
        ]
        if not opciones:
            # Translators: Notice in symbols list when no definitions are present.
            opciones = [_("(No functions or classes found in current code)")]

        self.list_box = wx.ListBox(panel, choices=opciones)
        # Translators: Accessible name for symbols list box.
        self.list_box.SetName(_("List of functions and classes. Press Enter to jump to element."))
        if self.simbolos:
            self.list_box.SetSelection(0)
        vbox.Add(self.list_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Button to jump to selected symbol.
        btn_ir = wx.Button(panel, wx.ID_OK, label=_("&Go to Element"))
        # Translators: Button to cancel line jump dialog.
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label=_("&Cancel"))
        hbox.Add(btn_ir, flag=wx.RIGHT, border=8)
        hbox.Add(btn_cancel)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.list_box.Bind(wx.EVT_LISTBOX_DCLICK, lambda e: self.EndModal(wx.ID_OK))
        self.CenterOnParent()
        self.list_box.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

    def get_selected_symbol(self):
        sel = self.list_box.GetSelection()
        if 0 <= sel < len(self.simbolos):
            return self.simbolos[sel]
        return None



class SupportDialog(wx.Dialog):
    """Diálogo accesible para contactar con soporte técnico o realizar donaciones."""
    def __init__(self, parent):
        # Translators: Dialog title for technical support and contact.
        super(SupportDialog, self).__init__(parent, title=_("Support and Contact"), size=(640, 420))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Translators: Developer support and contact information text.
        info = _(
            "Developer Support and Contact:\n\n"
            "Author and Developer: Kevin Andrés Velasquez Vargas\n"
            "Support email: {email}\n"
            "Recommended subject: Support - Python Learning with NVDA\n\n"
            "You can send pedagogical inquiries about chapters, questions about solving "
            "exercises, improvement suggestions, or technical bug reports.\n\n"
            "Likewise, you can voluntarily support the project through donations to "
            "back ongoing maintenance and the creation of new accessible educational content."
        ).format(email="kevinvelasquezvargas@gmail.com")

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(info)
        # Translators: Accessible name for support info text control.
        txt.SetName(_("Support and contact information"))
        vbox.Add(txt, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Button to open default mail client for support.
        btn_mail = wx.Button(panel, label=_("&Send support email"))
        # Translators: Button to open donation page.
        btn_donar = wx.Button(panel, label=_("Make &donation (PayPal)"))
        # Translators: Button to close support dialog.
        btn_cerrar = wx.Button(panel, wx.ID_CANCEL, label=_("&Close"))

        hbox.Add(btn_mail, flag=wx.RIGHT, border=8)
        hbox.Add(btn_donar, flag=wx.RIGHT, border=8)
        hbox.Add(btn_cerrar)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        btn_mail.Bind(wx.EVT_BUTTON, self.on_enviar_correo)
        btn_donar.Bind(wx.EVT_BUTTON, self.on_donar)
        self.CenterOnParent()
        btn_mail.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

    def on_enviar_correo(self, event=None):
        # Translators: Subject line for support email.
        subj = urllib.parse.quote(_("Support - Python Learning with NVDA"))
        url = f"mailto:kevinvelasquezvargas@gmail.com?subject={subj}"
        try:
            webbrowser.open(url)
            if ui:
                # Translators: Speech announcement when opening email client.
                ui.message(_("Opening default email client..."))
        except Exception:
            if ui:
                # Translators: Speech announcement displaying contact email address.
                ui.message(_("Write to {email}").format(email="kevinvelasquezvargas@gmail.com"))

    def on_donar(self, event=None):
        url = "https://www.paypal.me/kevinvelasquezvargas"
        try:
            webbrowser.open(url)
            if ui:
                # Translators: Speech announcement when opening donations link.
                ui.message(_("Opening donations page..."))
        except Exception:
            pass


class AboutDialog(wx.Dialog):
    """Diálogo accesible que presenta la documentación completa y estructurada del complemento."""
    def __init__(self, parent):
        # Translators: Dialog title for About documentation.
        super(AboutDialog, self).__init__(parent, title=_("About Python Learning with NVDA"), size=(780, 620))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Translators: Full structured manual and about documentation text.
        contenido = _(
            "Python Learning with NVDA\n"
            "Version: 2.0.0\n"
            "Author: Kevin Andrés Velasquez Vargas\n"
            "Support email: {email}\n"
            "License: GNU General Public License v3.0 (GPLv3)\n"
            "Compatibility: NVDA 2022.1 up to 2026.3\n"
            "GitHub repository: {repo_url}\n"
            "Donations and voluntary support: {donate_url}\n\n"
            "======================================================================\n"
            "1. Overview and Purpose of the Add-on\n"
            "======================================================================\n\n"
            "Python Learning with NVDA is a comprehensive educational environment and an accessible "
            "code editor adapted for Python programming through NVDA. It provides a structured "
            "learning path across 32 conceptual and practical lessons, complemented by a dual-mode "
            "work environment: guided tutor mode and standalone editor mode.\n\n"
            "It integrates structural navigation through code elements such as functions and classes, "
            "audio cues for indentation and structure, delimiter balancing checks, and simplified error messages.\n\n"
            "The environment has been designed to ensure that any blind or low-vision user "
            "can learn 100% independently, with speech and braille feedback.\n\n"
            "======================================================================\n"
            "2. Pedagogical Methodology: 4-Step Learning Cycle\n"
            "======================================================================\n\n"
            "Each chapter implements a four-phase progressive pedagogical cycle:\n\n"
            "Step 1: Conceptual Foundation (Observe): Presents theory in clear, everyday language, "
            "accompanied by a demonstration script runnable with F5 or Control + Enter.\n\n"
            "Step 2: Guided Observation (Experiment): A functional code snippet with a specific task "
            "to modify it and observe the cause and effect of changes.\n\n"
            "Step 3: Practical Challenge (Challenge): The editor starts completely blank so the student "
            "writes their own code. The tutor rigorously validates the solution without accepting empty answers.\n\n"
            "Step 4: Conceptual Verification (Quiz): A formative multiple-choice question (1, 2, or 3) "
            "to consolidate learned concepts.\n\n"
            "======================================================================\n"
            "3. Dual Working Modes\n"
            "======================================================================\n\n"
            "You can toggle between the two modes at any moment by pressing Control + M:\n\n"
            "Guided Learning Mode: Displays the step instruction, code, didactic buttons, and "
            "the pedagogical validation system.\n\n"
            "Standalone Editor Mode (Free Professional): Hides all lesson sections and maximizes "
            "workspace for the editor and output console, allowing work on personal projects with "
            "support for opening and saving .py files, delimiter checking, and structural navigation.\n\n"
            "======================================================================\n"
            "4. Pedagogical Curriculum Catalog (32 Chapters)\n"
            "======================================================================\n\n"
            "Phase 0: Computational Thinking and Fundamentals (1 to 3)\n"
            "Chapter 1: Computational Thinking and Everyday Algorithms\n"
            "Chapter 2: Basic Architecture: Input, Process, Memory, and Output\n"
            "Chapter 3: Boolean Logic: True, False, and Decisions\n\n"
            "Phase 1: Basic Syntax and Data Types (4 to 8)\n"
            "Chapter 4: Our First Instruction: The print() Function\n"
            "Chapter 5: Memory Storage: Variables and Assignment\n"
            "Chapter 6: Primitive Data Types: Integers and Floats\n"
            "Chapter 7: Text Strings: Quotes and Concatenation\n"
            "Chapter 8: User Interaction: Input with input()\n\n"
            "Phase 2: Flow Control Structures (9 to 15)\n"
            "Chapter 9: Comparison Operators and Conditional Expressions\n"
            "Chapter 10: Basic Branching: The if Statement and PEP 8 Indentation\n"
            "Chapter 11: Multiple Alternatives: elif and else Blocks\n"
            "Chapter 12: Ordered Collections: Introduction to Lists\n"
            "Chapter 13: Fundamental List Methods (append, remove, pop, len)\n"
            "Chapter 14: Repetition and Automation: The for Loop and range()\n"
            "Chapter 15: Conditional Repetition: The while Loop\n\n"
            "Phase 3: Complex Data Structures (16 to 17)\n"
            "Chapter 16: Key-Value Collections: Dictionaries in Python\n"
            "Chapter 17: Tuples and Sets: Immutability and Unique Collections\n\n"
            "Phase 4: Modularity and Functions (18 to 19)\n"
            "Chapter 18: Custom Functions: Declaration with def and Parameters\n"
            "Chapter 19: Returning Results: The return Statement and Scope\n\n"
            "Phase 5: Professional Error Handling and Diagnostics (20 to 21)\n"
            "Chapter 20: Professional Error Handling: try, except, and finally\n"
            "Chapter 21: Decoding Tracebacks and Fault Diagnostics\n\n"
            "Phase 6: File Input/Output and Persistence (22)\n"
            "Chapter 22: File Input and Output: with open() for Text\n\n"
            "Phase 7: Object-Oriented Programming (23 to 27)\n"
            "Chapter 23: Object Paradigm: Classes, Instances, and Attributes\n"
            "Chapter 24: The __init__ Constructor and the self Parameter\n"
            "Chapter 25: Instance Methods and Encapsulation\n"
            "Chapter 26: Class Inheritance: Reuse with super()\n"
            "Chapter 27: Polymorphism and Special Methods (__str__)\n\n"
            "Phase 8: Professional Ecosystem and Quality (28 to 32)\n"
            "Chapter 28: Standard Library Modules (math, random, datetime)\n"
            "Chapter 29: Structured Persistence: JSON Format and Serialization\n"
            "Chapter 30: Relational Databases with SQLite: Tables and Queries\n"
            "Chapter 31: Consuming Web Services: HTTP Requests and JSON Responses\n"
            "Chapter 32: Software Quality: Unit Testing with unittest\n\n"
            "======================================================================\n"
            "5. Comprehensive Keyboard Shortcuts Reference\n"
            "======================================================================\n\n"
            "F5 or Control + Enter: Run code and check solution.\n"
            "Control + M: Toggle between Learning Mode and Professional Editor-Only Mode.\n"
            "Alt + Right Arrow: Go to next step.\n"
            "Alt + Left Arrow: Go to previous step.\n"
            "F1: Explain line where cursor is located in simple words.\n"
            "F2: Rename symbol across file.\n"
            "F3 or Control + I: Read active mission prompt without moving cursor from editor.\n"
            "F4: Place cursor directly on Traceback error line.\n"
            "F6: Toggle focus between code editor and console.\n"
            "F7: Check syntax and balance of delimiters/quotes.\n"
            "Control + P: Request assistance hint.\n"
            "Control + 1: Curriculum chapter selector.\n"
            "Control + J: Open quick test console (REPL).\n"
            "Control + Shift + O: Accessible list of functions and classes in script.\n"
            "Alt + N / Alt + P: Jump to next / previous function or class.\n"
            "Control + /: Comment or uncomment current line.\n"
            "Control + D: Duplicate line downward.\n"
            "Control + Shift + K: Delete current line.\n"
            "Control + L: Announce current line and column.\n"
            "Control + F: Find text in editor.\n"
            "Control + G: Go to line number.\n"
            "Control + N: Start new blank script.\n"
            "Control + O / Control + S: Open / Save file.\n"
            "Control + Shift + S: Save as new file.\n"
            "Control + 4 / Control + 5: Direct focus to editor / console.\n"
            "Control + Shift + C: Speak all console output without leaving editor.\n"
            "F12: Open this documentation in About.\n"
            "Escape: Close tutor at any time.\n\n"
            "======================================================================\n"
            "6. Acoustic Feedback System\n"
            "======================================================================\n\n"
            "The environment produces brief, distinct audio cues:\n"
            "Startup: Confirmation tone when starting the environment.\n"
            "Success: High, rewarding tone when passing an exercise or executing successfully.\n"
            "Error: Low tone when an exception or failure occurs.\n"
            "Warning: Sound cue on unclosed delimiters or syntax notices.\n"
            "Block: Subtle tone when typing a colon (:) to indicate opening indentation.\n\n"
            "======================================================================\n"
            "7. Debugging and Diagnostic Assistance\n"
            "======================================================================\n\n"
            "The environment actively assists in early fault detection:\n"
            "Pre-check of quotes and delimiters () [] {}.\n"
            "Automatic jump with F4 to Traceback error line.\n"
            "Detection of confusing characters such as commas in floats or punctuation signs.\n"
            "Statement translator with F1 to understandable human explanations.\n\n"
            "======================================================================\n"
            "8. Support, Contact, and Donations\n"
            "======================================================================\n\n"
            "For direct support, suggestions, or inquiries:\n"
            "Developer: Kevin Andrés Velasquez Vargas\n"
            "Direct email: {email}\n"
            "Recommended subject: Support - Python Learning with NVDA\n"
            "Voluntary donations via PayPal: {donate_url}\n\n"
            "======================================================================\n"
            "9. Technical Information and License\n"
            "======================================================================\n\n"
            "Version: 2.0.0\n"
            "Compatibility: NVDA 2022.1 up to 2026.3\n"
            "License: GNU General Public License v3.0 (GPLv3)\n"
            "Developed for the screen reader programmer community."
        ).format(
            email="kevinvelasquezvargas@gmail.com",
            repo_url="https://github.com/KevinVelasquezVargas/python_tutor",
            donate_url="https://www.paypal.me/kevinvelasquezvargas"
        )

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(contenido)
        # Translators: Accessible name for about documentation text control.
        txt.SetName(_("Python Learning with NVDA Documentation"))
        vbox.Add(txt, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        # Translators: Button to close about dialog.
        btn_cerrar = wx.Button(panel, wx.ID_OK, label=_("&Close"))
        btn_cerrar.SetDefault()
        vbox.Add(btn_cerrar, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.CenterOnParent()
        btn_cerrar.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()


class TutorFrame(wx.Frame):
    """
    Ventana principal del entorno interactivo Aprendizaje de Python con NVDA.
    """
    PALABRAS_CLAVE = [
        "print", "input", "def", "return", "if", "elif", "else", "for", "while",
        "in", "range", "len", "try", "except", "finally", "import", "from",
        "True", "False", "None", "break", "continue", "pass", "int", "float",
        "str", "list", "dict", "append", "remove", "pop"
    ]

    def __init__(self, parent):
        # Translators: Main application window title.
        super(TutorFrame, self).__init__(parent, title=_("Python Learning with NVDA"), size=(980, 840))

        prog = ProgressManager.load_progress()
        self.cap_idx = max(0, min(prog.get("current_chapter", 0), len(CURRICULUM) - 1))
        self.paso_idx = max(0, prog.get("current_step", 0))

        self.nivel_pista = 0
        self.linter_activo = prog.get("linter_enabled", True)
        self.sonidos_activos = prog.get("sound_enabled", True)
        self.modo_editor = ProgressManager.get_editor_mode() == "editor"
        self.ultimo_error_linea = None
        self.ultimo_error_msg = ""
        self._last_linter_line = -1
        self._last_linter_indent = -1
        self.archivo_abierto = None
        self._codigo_leccion = ""
        self._codigo_editor_usuario = ""
        self.breakpoints = set()

        self.crear_barra_menus()

        self.panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        # 1. Estado del paso
        self.lbl_estado = wx.StaticText(self.panel, label="")
        font_estado = self.lbl_estado.GetFont()
        font_estado.SetWeight(wx.FONTWEIGHT_BOLD)
        self.lbl_estado.SetFont(font_estado)
        self.vbox.Add(self.lbl_estado, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        # 2. Instrucción del paso
        self.mision_ctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size=(-1, 130))
        # Translators: Accessible name for active step instruction control.
        self.mision_ctrl.SetName(_("Active step instruction."))
        self.vbox.Add(self.mision_ctrl, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # 3. Editor de código
        # Translators: Label for the code editor area.
        self.lbl_ed = wx.StaticText(self.panel, label=_("Code editor:"))
        self.vbox.Add(self.lbl_ed, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.edicion = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_PROCESS_TAB)
        # Translators: Accessible name for the code editor text control.
        self.edicion.SetName(_("Code editor"))
        self.vbox.Add(self.edicion, proportion=3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # 4. Consola de resultados
        # Translators: Label for results output and diagnostic console.
        self.lbl_sal = wx.StaticText(self.panel, label=_("Results and diagnostic console:"))
        self.vbox.Add(self.lbl_sal, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.salida = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        # Translators: Accessible name for the results output console control.
        self.salida.SetName(_("Results console."))
        self.vbox.Add(self.salida, proportion=2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # 5. Barra de botones
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        # Translators: Toolbar button to run script or check exercise.
        self.btn_ejecutar = wx.Button(self.panel, label=_("&Run (F5 or Ctrl+Enter)"))
        # Translators: Accessible name for run code button.
        self.btn_ejecutar.SetName(_("Run Code Button"))

        # Translators: Toolbar button to request hint.
        self.btn_pista = wx.Button(self.panel, label=_("Get &Hint (Ctrl+P)"))
        # Translators: Accessible name for hint button.
        self.btn_pista.SetName(_("Get Hint Button"))

        # Translators: Toolbar button to explain current code line.
        self.btn_traductor = wx.Button(self.panel, label=_("Explain &Line (F1)"))
        # Translators: Accessible name for explain line button.
        self.btn_traductor.SetName(_("Explain Line Button"))

        # Translators: Toolbar button to go to previous step.
        self.btn_anterior = wx.Button(self.panel, label=_("&Previous Step (Alt+Left)"))
        # Translators: Accessible name for previous step button.
        self.btn_anterior.SetName(_("Previous Step Button"))

        # Translators: Toolbar button to go to next step.
        self.btn_siguiente = wx.Button(self.panel, label=_("&Next Step (Alt+Right)"))
        # Translators: Accessible name for next step button.
        self.btn_siguiente.SetName(_("Next Step Button"))

        # Translators: Toolbar button to open curriculum chapter selector.
        self.btn_temario = wx.Button(self.panel, label=_("&Curriculum (Ctrl+1)"))
        # Translators: Accessible name for chapter selector button.
        self.btn_temario.SetName(_("Chapter Selector Button"))

        # Translators: Toolbar button to close application.
        self.btn_cerrar = wx.Button(self.panel, wx.ID_CANCEL, label=_("&Close (Escape)"))
        # Translators: Accessible name for close button.
        self.btn_cerrar.SetName(_("Close Button"))

        self.hbox.Add(self.btn_ejecutar, flag=wx.RIGHT, border=6)
        self.hbox.Add(self.btn_pista, flag=wx.RIGHT, border=6)
        self.hbox.Add(self.btn_traductor, flag=wx.RIGHT, border=6)
        self.hbox.Add(self.btn_anterior, flag=wx.RIGHT, border=6)
        self.hbox.Add(self.btn_siguiente, flag=wx.RIGHT, border=6)
        self.hbox.Add(self.btn_temario, flag=wx.RIGHT, border=6)
        self.hbox.Add(self.btn_cerrar)

        self.vbox.Add(self.hbox, flag=wx.ALIGN_CENTER | wx.ALL, border=12)
        self.panel.SetSizer(self.vbox)

        # Eventos
        self.btn_ejecutar.Bind(wx.EVT_BUTTON, self.on_ejecutar)
        self.btn_pista.Bind(wx.EVT_BUTTON, self.on_pista)
        self.btn_traductor.Bind(wx.EVT_BUTTON, self.on_traducir_linea)
        self.btn_anterior.Bind(wx.EVT_BUTTON, self.on_paso_anterior)
        self.btn_siguiente.Bind(wx.EVT_BUTTON, self.on_paso_siguiente)
        self.btn_temario.Bind(wx.EVT_BUTTON, self.on_abrir_temario)
        self.btn_cerrar.Bind(wx.EVT_BUTTON, lambda e: self.Close())

        self.edicion.Bind(wx.EVT_KEY_DOWN, self.on_key_down_edicion)
        self.edicion.Bind(wx.EVT_KEY_UP, self.on_key_up_edicion)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook_global)
        self.Bind(wx.EVT_CLOSE, self.on_close)

        # Cargar paso actual
        self.cargar_paso_actual(anunciar_voz=False)
        self.aplicar_modo_trabajo(anunciar=False)

        # Reproducir señal de inicio
        SoundManager.initialize()
        if self.sonidos_activos:
            SoundManager.play('inicio')

        self.Center()
        self.edicion.SetFocus()

        if prog.get("show_welcome", True):
            wx.CallAfter(self.mostrar_bienvenida)

    def mostrar_bienvenida(self):
        dlg = WelcomeDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.guardar_preferencia()
        dlg.Destroy()
        self.edicion.SetFocus()

    def anunciar(self, msg, delay=180, cancelar_previo=True):
        """
        Verbaliza un mensaje de forma accesible mediante NVDA (speech y ui.message).
        Utiliza un retardo asíncrono para que cuando el menú se cierre y el editor
        de código recupere el foco, el lector de pantalla no interrumpa ni
        cancele la verbalización de la función ejecutada.
        """
        if not msg:
            return

        def _do_anuncio():
            try:
                if cancelar_previo and speech and hasattr(speech, 'cancelSpeech'):
                    speech.cancelSpeech()
                if speech and hasattr(speech, 'speakMessage'):
                    speech.speakMessage(msg)
                if ui:
                    ui.message(msg)
            except Exception:
                pass

        wx.CallLater(delay, _do_anuncio)

    def crear_barra_menus(self):
        menu_bar = wx.MenuBar()

        # 1. Menú Archivo
        m_archivo = wx.Menu()
        item_nuevo = m_archivo.Append(wx.ID_ANY, _("&New script\tCtrl+N"), _("Starts a new blank script in the editor"))
        item_abrir = m_archivo.Append(wx.ID_ANY, _("&Open file...\tCtrl+O"), _("Loads a Python script from disk"))
        item_guardar = m_archivo.Append(wx.ID_ANY, _("&Save script\tCtrl+S"), _("Saves editor content to file"))
        item_guardar_como = m_archivo.Append(wx.ID_ANY, _("Save &as...\tCtrl+Shift+S"), _("Saves code with a new name or location"))
        m_archivo.AppendSeparator()
        item_salir = m_archivo.Append(wx.ID_EXIT, _("&Close tutor\tAlt+F4"), _("Closes the learning environment"))

        self.Bind(wx.EVT_MENU, self.on_nuevo_archivo, id=item_nuevo.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_archivo, id=item_abrir.GetId())
        self.Bind(wx.EVT_MENU, self.on_guardar_archivo, id=item_guardar.GetId())
        self.Bind(wx.EVT_MENU, self.on_guardar_como, id=item_guardar_como.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.Close(), id=item_salir.GetId())

        # 2. Menú Edición
        m_edicion = wx.Menu()
        item_deshacer = m_edicion.Append(wx.ID_UNDO, _("&Undo\tCtrl+Z"), _("Reverts the last editing action"))
        item_rehacer = m_edicion.Append(wx.ID_REDO, _("&Redo\tCtrl+Y"), _("Reapplies undone action"))
        m_edicion.AppendSeparator()
        item_cortar = m_edicion.Append(wx.ID_CUT, _("Cu&t\tCtrl+X"), _("Cuts selected text to clipboard"))
        item_copiar = m_edicion.Append(wx.ID_COPY, _("&Copy\tCtrl+C"), _("Copies selected text to clipboard"))
        item_pegar = m_edicion.Append(wx.ID_PASTE, _("&Paste\tCtrl+V"), _("Pastes clipboard content"))
        item_sel_todo = m_edicion.Append(wx.ID_SELECTALL, _("Select &all\tCtrl+A"), _("Selects all text in editor"))
        m_edicion.AppendSeparator()
        item_buscar = m_edicion.Append(wx.ID_ANY, _("&Find text...\tCtrl+F"), _("Searches for words or code snippets"))
        item_ir_linea = m_edicion.Append(wx.ID_ANY, _("&Go to line...\tCtrl+G"), _("Moves cursor to specified line number"))
        m_edicion.AppendSeparator()
        item_pep8 = m_edicion.Append(wx.ID_ANY, _("Format document by &PEP 8\tShift+Alt+F"), _("Adjusts indentation to 4 spaces and formats operator spacing"))
        item_renombrar = m_edicion.Append(wx.ID_ANY, _("&Rename symbol...\tF2"), _("Renames selected variable or function across script"))
        item_extraer = m_edicion.Append(wx.ID_ANY, _("E&xtract to function...\tCtrl+Shift+R"), _("Converts selected block into a new function"))
        m_edicion.AppendSeparator()
        item_simbolos = m_edicion.Append(wx.ID_ANY, _("List of &functions and classes...\tCtrl+Shift+O"), _("Opens list of functions and classes in file"))
        item_sig_def = m_edicion.Append(wx.ID_ANY, _("&Next function or class\tAlt+N"), _("Jumps to next function or class header"))
        item_ant_def = m_edicion.Append(wx.ID_ANY, _("&Previous function or class\tAlt+P"), _("Jumps to previous function or class header"))
        m_edicion.AppendSeparator()
        item_comentar = m_edicion.Append(wx.ID_ANY, _("Toggle &comment on line\tCtrl+/"), _("Toggles '#' comment prefix on current line"))
        item_duplicar = m_edicion.Append(wx.ID_ANY, _("&Duplicate line below\tCtrl+D"), _("Duplicates current line below"))
        item_eliminar = m_edicion.Append(wx.ID_ANY, _("D&elete current line\tCtrl+Shift+K"), _("Completely deletes the line at cursor"))
        m_edicion.AppendSeparator()
        item_verificar = m_edicion.Append(wx.ID_ANY, _("Check s&yntax and delimiters\tF7"), _("Checks parentheses, quotes, and syntax errors"))
        item_posicion = m_edicion.Append(wx.ID_ANY, _("Announce &position (Line and column)\tCtrl+L"), _("Reports line and column cursor position"))

        self.Bind(wx.EVT_MENU, lambda e: self.edicion.Undo(), id=item_deshacer.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.edicion.Redo(), id=item_rehacer.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.edicion.Cut(), id=item_cortar.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.edicion.Copy(), id=item_copiar.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.edicion.Paste(), id=item_pegar.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.edicion.SelectAll(), id=item_sel_todo.GetId())
        self.Bind(wx.EVT_MENU, self.on_buscar, id=item_buscar.GetId())
        self.Bind(wx.EVT_MENU, self.on_ir_a_linea, id=item_ir_linea.GetId())
        self.Bind(wx.EVT_MENU, self.on_formatear_pep8, id=item_pep8.GetId())
        self.Bind(wx.EVT_MENU, self.on_renombrar_simbolo, id=item_renombrar.GetId())
        self.Bind(wx.EVT_MENU, self.on_extraer_funcion, id=item_extraer.GetId())
        self.Bind(wx.EVT_MENU, self.on_mostrar_simbolos, id=item_simbolos.GetId())
        self.Bind(wx.EVT_MENU, self.on_siguiente_definicion, id=item_sig_def.GetId())
        self.Bind(wx.EVT_MENU, self.on_anterior_definicion, id=item_ant_def.GetId())
        self.Bind(wx.EVT_MENU, self.on_comentar_descomentar, id=item_comentar.GetId())
        self.Bind(wx.EVT_MENU, self.on_duplicar_linea, id=item_duplicar.GetId())
        self.Bind(wx.EVT_MENU, self.on_eliminar_linea, id=item_eliminar.GetId())
        self.Bind(wx.EVT_MENU, self.on_verificar_sintaxis, id=item_verificar.GetId())
        self.Bind(wx.EVT_MENU, self.on_anunciar_posicion, id=item_posicion.GetId())

        # 3. Menú Herramientas (organizado estrictamente por orden alfabético)
        m_herramientas = wx.Menu()
        item_alternar = m_herramientas.Append(wx.ID_ANY, _("Toggle &focus between editor and console\tF6"), _("Switches focus between editor and output"))
        item_modo = m_herramientas.Append(wx.ID_ANY, _("Toggle &Learning / Standalone Mode\tCtrl+M"), _("Toggles between didactic guide and standalone editor"))
        item_breakpoint = m_herramientas.Append(wx.ID_ANY, _("Toggle &breakpoint\tF9"), _("Toggles a breakpoint on current line"))
        item_autocompletar = m_herramientas.Append(wx.ID_ANY, _("&Autocomplete with documentation\tCtrl+Space"), _("Shows code suggestions with description"))
        item_repl = m_herramientas.Append(wx.ID_ANY, _("Quick test console (&REPL)\tCtrl+J"), _("Instant one-line interactive test window"))
        item_depurar = m_herramientas.Append(wx.ID_ANY, _("&Step-by-step interactive debugger...\tF10"), _("Runs script inspecting each line and its variables"))
        item_glosario = m_herramientas.Append(wx.ID_ANY, _("Python terms &dictionary"), _("Search terms and language concepts"))
        item_doc_rapida = m_herramientas.Append(wx.ID_ANY, _("&Quick documentation of symbol\tShift+F1"), _("Reads explanation of function or keyword under cursor"))
        item_ejecutar = m_herramientas.Append(wx.ID_ANY, _("&Run code and verify\tF5"), _("Executes script or validates current mission (F5 or Ctrl+Enter)"))
        item_pruebas = m_herramientas.Append(wx.ID_ANY, _("Run unit &tests (Test Runner)...\tCtrl+T"), _("Runs unittest suite with accessible report"))
        item_traductor = m_herramientas.Append(wx.ID_ANY, _("&Explain line of code\tF1"), _("Translates current code line to plain words"))
        item_interprete = m_herramientas.Append(wx.ID_ANY, _("&Interpreter and virtual environment manager...\tCtrl+Shift+P"), _("Selects active Python interpreter or virtual environment"))
        item_error = m_herramientas.Append(wx.ID_ANY, _("&Go to Traceback error line\tF4"), _("Moves cursor directly to the error line"))
        item_temario = m_herramientas.Append(wx.ID_ANY, _("Go to curriculum &chapter...\tCtrl+1"), _("View the complete list of chapters"))
        item_leer_inst = m_herramientas.Append(wx.ID_ANY, _("Read active step &instruction\tF3"), _("Reads current mission prompt without moving editor cursor"))
        item_leer_salida = m_herramientas.Append(wx.ID_ANY, _("Read &all console output\tCtrl+Shift+C"), _("Speaks all console output without losing focus"))
        item_reiniciar = m_herramientas.Append(wx.ID_ANY, _("Reset exercise &code\tCtrl+R"), _("Restores initial exercise code"))

        self.Bind(wx.EVT_MENU, self.on_alternar_foco, id=item_alternar.GetId())
        self.Bind(wx.EVT_MENU, self.on_alternar_modo_trabajo, id=item_modo.GetId())
        self.Bind(wx.EVT_MENU, self.on_toggle_breakpoint, id=item_breakpoint.GetId())
        self.Bind(wx.EVT_MENU, self.on_autocompletar, id=item_autocompletar.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_repl, id=item_repl.GetId())
        self.Bind(wx.EVT_MENU, self.on_depurar_paso_a_paso, id=item_depurar.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_glosario, id=item_glosario.GetId())
        self.Bind(wx.EVT_MENU, self.on_doc_rapida, id=item_doc_rapida.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.on_ejecutar(None), id=item_ejecutar.GetId())
        self.Bind(wx.EVT_MENU, self.on_ejecutar_pruebas, id=item_pruebas.GetId())
        self.Bind(wx.EVT_MENU, self.on_traducir_linea, id=item_traductor.GetId())
        self.Bind(wx.EVT_MENU, self.on_gestor_interpretes, id=item_interprete.GetId())
        self.Bind(wx.EVT_MENU, self.on_ir_al_error, id=item_error.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_temario, id=item_temario.GetId())
        self.Bind(wx.EVT_MENU, self.on_leer_instruccion_actual, id=item_leer_inst.GetId())
        self.Bind(wx.EVT_MENU, self.on_leer_toda_la_salida, id=item_leer_salida.GetId())
        self.Bind(wx.EVT_MENU, self.on_reiniciar_codigo, id=item_reiniciar.GetId())

        # 4. Menú Ayuda (organizado alfabéticamente)
        m_ayuda = wx.Menu()
        item_acerca = m_ayuda.Append(wx.ID_ANY, _("&About Python Learning with NVDA...\tF12"), _("Complete accessible documentation in web browser"))
        item_donacion = m_ayuda.Append(wx.ID_ANY, _("&Donate to project..."), _("Make a voluntary donation to support the add-on"))
        item_atajos = m_ayuda.Append(wx.ID_ANY, _("Keyboard shortcuts &guide\tF11"), _("Displays quick shortcuts reference"))
        item_soporte = m_ayuda.Append(wx.ID_ANY, _("&Support and contact..."), _("Direct email and technical assistance channels"))

        self.Bind(wx.EVT_MENU, self.on_acerca, id=item_acerca.GetId())
        self.Bind(wx.EVT_MENU, self.on_donacion, id=item_donacion.GetId())
        self.Bind(wx.EVT_MENU, self.on_mostrar_atajos, id=item_atajos.GetId())
        self.Bind(wx.EVT_MENU, self.on_soporte, id=item_soporte.GetId())

        # Translators: Top-level menu title for File operations.
        menu_bar.Append(m_archivo, _("&File"))
        # Translators: Top-level menu title for Edit operations.
        menu_bar.Append(m_edicion, _("&Edit"))
        # Translators: Top-level menu title for Tools.
        menu_bar.Append(m_herramientas, _("&Tools"))
        # Translators: Top-level menu title for Help.
        menu_bar.Append(m_ayuda, _("&Help"))
        self.SetMenuBar(menu_bar)

    def aplicar_modo_trabajo(self, anunciar=False):
        """Aplica la configuración visual y de navegación según el modo de trabajo."""
        if self.modo_editor:
            self.lbl_estado.Hide()
            self.lbl_estado.Disable()
            self.vbox.Show(self.lbl_estado, False)

            self.mision_ctrl.Hide()
            self.mision_ctrl.Disable()
            self.vbox.Show(self.mision_ctrl, False)

            # Translators: Label for editor in standalone mode.
            self.lbl_ed.SetLabel(_("Code editor (Standalone mode):"))

            self.btn_pista.Hide()
            self.btn_pista.Disable()
            self.hbox.Show(self.btn_pista, False)

            self.btn_traductor.Hide()
            self.btn_traductor.Disable()
            self.hbox.Show(self.btn_traductor, False)

            self.btn_anterior.Hide()
            self.btn_anterior.Disable()
            self.hbox.Show(self.btn_anterior, False)

            self.btn_siguiente.Hide()
            self.btn_siguiente.Disable()
            self.hbox.Show(self.btn_siguiente, False)

            self.btn_temario.Hide()
            self.btn_temario.Disable()
            self.hbox.Show(self.btn_temario, False)

            # Translators: Main application window title.
            self.SetTitle(_("Python Learning with NVDA"))
            self.panel.Layout()
            self.Layout()
            if anunciar:
                # Translators: Speech announcement when switching to standalone editor mode.
                msg = _("Standalone Editor mode activated. Clean workspace without lessons.")
                self.anunciar(msg)
        else:
            self.lbl_estado.Enable()
            self.lbl_estado.Show()
            self.vbox.Show(self.lbl_estado, True)

            self.mision_ctrl.Enable()
            self.mision_ctrl.Show()
            self.vbox.Show(self.mision_ctrl, True)

            # Translators: Label for the code editor area.
            self.lbl_ed.SetLabel(_("Code editor:"))

            self.btn_pista.Enable()
            self.btn_pista.Show()
            self.hbox.Show(self.btn_pista, True)

            self.btn_traductor.Enable()
            self.btn_traductor.Show()
            self.hbox.Show(self.btn_traductor, True)

            self.btn_anterior.Enable()
            self.btn_anterior.Show()
            self.hbox.Show(self.btn_anterior, True)

            self.btn_siguiente.Enable()
            self.btn_siguiente.Show()
            self.hbox.Show(self.btn_siguiente, True)

            self.btn_temario.Enable()
            self.btn_temario.Show()
            self.hbox.Show(self.btn_temario, True)

            # Translators: Main application window title.
            self.SetTitle(_("Python Learning with NVDA"))
            self.panel.Layout()
            self.Layout()
            if anunciar:
                # Translators: Speech announcement when switching to guided learning mode.
                msg = _("Guided Learning mode activated. Lessons and curriculum visible.")
                self.anunciar(msg)

    def on_alternar_modo_trabajo(self, event=None):
        """Alterna entre el Modo Aprendizaje y el Modo Solo Editor (Ctrl+M)."""
        self.modo_editor = not self.modo_editor
        ProgressManager.set_editor_mode("editor" if self.modo_editor else "learning")

        if self.modo_editor:
            # Al entrar en Modo Solo Editor: guardar el código de la lección y limpiar el lienzo
            self._codigo_leccion = self.edicion.GetValue()
            self.edicion.SetValue(self._codigo_editor_usuario)
            if self.sonidos_activos:
                SoundManager.play('modo_editor')
        else:
            # Al regresar a Modo Aprendizaje: guardar el script del usuario y restaurar la lección
            self._codigo_editor_usuario = self.edicion.GetValue()
            if self._codigo_leccion:
                self.edicion.SetValue(self._codigo_leccion)
            else:
                cap = CURRICULUM[self.cap_idx]
                paso = cap["pasos"][self.paso_idx]
                self.edicion.SetValue(paso.get("codigo", ""))
            if self.sonidos_activos:
                SoundManager.play('modo_aprendizaje')

        self.aplicar_modo_trabajo(anunciar=True)
        self.edicion.SetFocus()

    def cargar_paso_actual(self, anunciar_voz=True):
        """Carga el paso activo asegurando que no ocurran excepciones por claves ausentes."""
        if not (0 <= self.cap_idx < len(CURRICULUM)):
            self.cap_idx = 0

        cap = CURRICULUM[self.cap_idx]
        total_pasos = len(cap.get("pasos", []))
        if total_pasos == 0:
            return

        if self.paso_idx >= total_pasos:
            self.paso_idx = total_pasos - 1
        elif self.paso_idx < 0:
            self.paso_idx = 0

        paso = cap["pasos"][self.paso_idx]
        self.nivel_pista = 0
        self._last_linter_line = -1
        self._last_linter_indent = -1

        superado = ProgressManager.is_step_completed(self.cap_idx, self.paso_idx)
        # Translators: Step status label: Passed / Completed.
        # Translators: Step status label: Pending.
        marca_estado = _("Completed") if superado else _("Pending")

        # Translators: Default step title format if not named.
        titulo_paso = paso.get("titulo", _("Step {step}").format(step=self.paso_idx + 1))
        # Translators: Header format for current step: Chapter, Step X of Y: Step Title, Status
        cap_tit = cap.get('titulo', _("Chapter"))
        texto_encabezado = _("{chapter}, Step {step} of {total}: {title}, {status}").format(
            chapter=cap_tit,
            step=self.paso_idx + 1,
            total=total_pasos,
            title=titulo_paso,
            status=marca_estado
        )
        self.lbl_estado.SetLabel(texto_encabezado)

        instruccion = paso.get("instruccion")
        if not instruccion:
            if paso.get("tipo") == "quiz":
                preg = paso.get("pregunta", "")
                opciones = paso.get("opciones", [])
                ops_txt = "\n".join(f"{i+1}. {op}" for i, op in enumerate(opciones))
                # Translators: Instruction template for conceptual quiz lessons.
                instruccion = _(
                    "Conceptual verification question:\n\n{question}\n\nOptions:\n{options}\n\n"
                    "Type the number of the correct answer (1, 2 or 3) in the editor and press Control + Enter."
                ).format(question=preg, options=ops_txt)
            else:
                # Translators: Default instruction fallback for lessons.
                instruccion = _("Follow the instructions for the exercise and run with Control + Enter.")

        instruccion_limpia = instruccion.replace("\r\n", "\n")
        self.mision_ctrl.SetValue(instruccion_limpia)

        if not self.modo_editor:
            self.edicion.SetValue(paso.get("codigo", ""))
        self.salida.SetValue("")

        if anunciar_voz and ui:
            ui.message(f"{titulo_paso}. {instruccion_limpia}")

    def on_ejecutar(self, event=None):
        src = self.edicion.GetValue()

        # 1. Comprobación temprana de balanceo de delimitadores
        bal_err = comprobar_balanceo_delimitadores(src)
        if bal_err:
            self.ultimo_error_linea = bal_err.get("linea")
            self.ultimo_error_msg = bal_err.get("mensaje")
            # Translators: Output console warning for unclosed delimiters.
            self.salida.SetValue(_("Delimiter Notice:\n{message}\n\nPress F4 to place cursor on notice line.").format(message=bal_err["mensaje"]))
            if self.sonidos_activos:
                SoundManager.play('sintaxis_aviso')
            # Translators: Speech announcement for unclosed delimiters.
            self.anunciar(_("Delimiter notice: {message}. Press F4 to go to line.").format(message=bal_err["mensaje"]))
            return

        # 2. Comprobación de código vacío o solo comentarios
        lineas_codigo = [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
        if not lineas_codigo:
            if not self.modo_editor:
                cap = CURRICULUM[self.cap_idx]
                paso = cap["pasos"][self.paso_idx]
                tipo_paso = paso.get("tipo", "observar")
                if tipo_paso == "quiz":
                    # Translators: Notice when quiz answer is missing.
                    msg = _("No option selected. Type number 1, 2, or 3 in the editor and press Control + Enter or F5.")
                elif tipo_paso == "desafio":
                    # Translators: Notice when challenge editor is empty.
                    msg = _("The editor is empty or only contains comments. Write your code to solve the challenge and press Control + Enter or F5.")
                elif tipo_paso == "experimentar":
                    # Translators: Notice when experimentation step has no executable code.
                    msg = _("No executable code detected. Make the modification indicated in the prompt and press Control + Enter or F5.")
                else:
                    # Translators: Generic notice for empty editor.
                    msg = _("The editor contains no code to run.")
            else:
                # Translators: Notice in standalone mode when trying to run empty editor.
                msg = _("The editor is empty. Write Python instructions before executing.")

            self.salida.SetValue(msg)
            if self.sonidos_activos:
                SoundManager.play('error')
            self.anunciar(msg)
            return

        # 3. Flujo en Modo Solo Editor Profesional
        if self.modo_editor:
            res = ejecutar_codigo_seguro(src, timeout=5.0)
            salida_txt = []
            if getattr(res, 'keyboard_warning', None):
                salida_txt.append(_("Typing Notice:"))
                salida_txt.append(res.keyboard_warning)
                salida_txt.append("")

            salida_txt.append(_("Output:"))
            salida_txt.append(res.output if res.output else _("(No console output)"))

            if not res.success:
                self.ultimo_error_linea = res.error_line
                self.ultimo_error_msg = res.error_msg
                if res.friendly_explanation:
                    salida_txt.append("")
                    salida_txt.append(_("Execution notice: {message}").format(message=res.friendly_explanation))
                    salida_txt.append(_("Press F4 to position cursor on error line."))
                if self.sonidos_activos:
                    SoundManager.play('error')
                fallback_err = _("Error during execution")
                msg_err = res.friendly_explanation or res.error_msg or fallback_err
                # Translators: Speech announcement on execution error.
                self.anunciar(_("Error: {error}. Press F4 to go to error.").format(error=msg_err))
            else:
                self.ultimo_error_linea = None
                self.ultimo_error_msg = None
                if self.sonidos_activos:
                    SoundManager.play('exito')
                # Translators: Speech announcement on successful standalone execution.
                self.anunciar(_("Execution finished successfully."))

            self.salida.SetValue("\n".join(salida_txt))
            wx.CallLater(100, self.salida.SetFocus)
            return

        # 4. Flujo en Modo Aprendizaje Guiado
        cap = CURRICULUM[self.cap_idx]
        paso = cap["pasos"][self.paso_idx]
        tipo_paso = paso.get("tipo", "observar")
        reporte_pruebas = []
        aprobado = False
        res_output = ""
        friendly_err = ""

        if tipo_paso == "quiz":
            cor = str(paso.get("correcta", 0) + 1)
            val_clean = "".join(lineas_codigo).strip()
            digits = re.findall(r'\d+', val_clean)
            if len(digits) == 1 and digits[0] == cor:
                aprobado = True
                correct_exp = paso.get("explicacion", _("Correct answer."))
                reporte_pruebas.append(_("Correct: {explanation}").format(explanation=correct_exp))
            else:
                aprobado = False
                # Translators: Notice when quiz answer is incorrect.
                reporte_pruebas.append(_("Pending: Selected option is incorrect. Review options in instruction and try again."))

            submitted_opt = digits[0] if digits else val_clean
            res_output = _("Option submitted: {option}").format(option=submitted_opt)
            self.ultimo_error_linea = None
            self.ultimo_error_msg = None
        else:
            res = ejecutar_codigo_seguro(src, timeout=4.0)
            res_output = res.output
            friendly_err = res.friendly_explanation

            if not res.success:
                self.ultimo_error_linea = res.error_line
                self.ultimo_error_msg = res.error_msg or friendly_err
                aprobado = False
            else:
                self.ultimo_error_linea = None
                self.ultimo_error_msg = None
                if "pruebas" in paso:
                    todas_ok = True
                    for p in paso["pruebas"]:
                        try:
                            ok = p["check"](src, res.output, res.local_ns)
                        except Exception:
                            ok = False
                        if ok:
                            test_name = p.get("nombre", _("Test"))
                            reporte_pruebas.append(_("Correct: {test_name} passed").format(test_name=test_name))
                        else:
                            test_name = p.get("nombre", _("Test"))
                            reporte_pruebas.append(_("Pending: {test_name} not passed").format(test_name=test_name))
                            todas_ok = False
                    aprobado = todas_ok
                elif "validar" in paso and callable(paso["validar"]):
                    try:
                        aprobado = bool(paso["validar"](src, res.output, res.local_ns))
                    except Exception:
                        aprobado = False
                    if not aprobado:
                        # Translators: Feedback when challenge execution does not satisfy validator.
                        reporte_pruebas.append(_("Pending: Code ran without syntax errors, but output does not yet meet challenge requirements."))
                else:
                    aprobado = (tipo_paso == "observar")

        lineas_reporte = []
        if tipo_paso != "quiz" and getattr(res, 'keyboard_warning', None):
            lineas_reporte.append(_("Typing Notice:"))
            lineas_reporte.append(res.keyboard_warning)
            lineas_reporte.append("")

        lineas_reporte.append(_("Output:"))
        lineas_reporte.append(res_output if res_output else _("(No console output)"))
        lineas_reporte.append("")

        if reporte_pruebas:
            lineas_reporte.append(_("Check Results:"))
            lineas_reporte.extend(reporte_pruebas)
            lineas_reporte.append("")

        if aprobado:
            lineas_reporte.append(_("Mission passed successfully! You can advance to next step with Alt + Right Arrow."))
            self.salida.SetValue("\n".join(lineas_reporte))
            wx.CallLater(100, self.salida.SetFocus)

            ProgressManager.mark_step_completed(self.cap_idx, self.paso_idx)

            if self.sonidos_activos:
                SoundManager.play('exito')
            # Translators: Speech announcement on mission completion.
            self.anunciar(_("Mission accomplished! Press Alt + Right Arrow to advance."))
        else:
            if paso.get("salida_esperada"):
                comp = generar_comparacion_salida(paso["salida_esperada"], res_output)
                lineas_reporte.append(_("Comparison with expected output:"))
                lineas_reporte.append(comp)
                lineas_reporte.append("")

            if friendly_err:
                lineas_reporte.append(_("Execution notice: {message}").format(message=friendly_err))
                lineas_reporte.append(_("Press F4 to position cursor on error line."))
            elif tipo_paso != "quiz":
                lineas_reporte.append(_("Solution not yet approved. Review prompt or press Control + P to request a hint."))

            self.salida.SetValue("\n".join(lineas_reporte))
            wx.CallLater(100, self.salida.SetFocus)

            if self.sonidos_activos:
                SoundManager.play('error')
            if friendly_err:
                self.anunciar(_("{error}. Press F4 to go to error.").format(error=friendly_err))
            elif tipo_paso == "quiz":
                self.anunciar(_("Incorrect option. Review question and try again."))
            else:
                self.anunciar(_("Solution not passed. Press Control + P to receive a hint."))

    def on_pista(self, event=None):
        cap = CURRICULUM[self.cap_idx]
        paso = cap["pasos"][self.paso_idx]
        # Translators: Default fallback hint if no hints are defined in the step.
        default_hint = _("Review the lesson description at the top and try running again.")
        pistas = paso.get("pistas", [default_hint])

        if self.sonidos_activos:
            SoundManager.play('pista')

        dlg = HintDialog(self, pistas, self.nivel_pista)
        dlg.ShowModal()
        dlg.Destroy()

        if self.nivel_pista < len(pistas) - 1:
            self.nivel_pista += 1

    def on_traducir_linea(self, event=None):
        """Explica la línea de código actual con palabras cotidianas."""
        try:
            pt = self.edicion.GetInsertionPoint()
            txt = self.edicion.GetValue()
            row = txt[:pt].count('\n')
            linea = self.edicion.GetLineText(row)
        except Exception:
            linea = ""

        traduccion = traducir_linea_codigo(linea)
        self.anunciar(traduccion)

    # ===    # Herramientas del Editor (Productividad estilo IDE)
    # ===
    def on_nuevo_archivo(self, event=None):
        """Crea un nuevo script en blanco tras confirmación si hay texto."""
        if self.edicion.GetValue().strip():
            # Translators: Confirmation prompt before creating a new blank script.
            msg = _("Do you want to start a new blank script? Current text in the editor will be cleared.")
            # Translators: Title for new script confirmation dialog.
            title = _("New Script")
            res = wx.MessageBox(
                msg,
                title,
                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION,
                self
            )
            if res != wx.YES:
                return
        self.edicion.SetValue("")
        self.salida.SetValue("")
        self.archivo_abierto = None
        self.ultimo_error_linea = None
        self.ultimo_error_msg = None
        self.edicion.SetFocus()
        # Translators: Speech announcement when a new blank script is created.
        self.anunciar(_("New blank script started."))

    def on_buscar(self, event=None):
        """Abre el diálogo accesible de búsqueda en el editor (Ctrl+F)."""
        dlg = FindDialog(self, self.edicion)
        dlg.ShowModal()
        dlg.Destroy()
        self.edicion.SetFocus()

    def on_ir_a_linea(self, event=None):
        """Abre el diálogo accesible para desplazarse a una línea (Ctrl+G)."""
        dlg = GoToLineDialog(self, self.edicion)
        dlg.ShowModal()
        dlg.Destroy()
        self.edicion.SetFocus()

    def on_comentar_descomentar(self, event=None):
        """Alterna el comentario '#' al inicio de la línea donde está el cursor."""
        try:
            pt = self.edicion.GetInsertionPoint()
            txt = self.edicion.GetValue()
            row = txt[:pt].count('\n')
            linea = self.edicion.GetLineText(row)

            lineas = txt.split('\n')
            if linea.lstrip().startswith('#'):
                if linea.startswith('# '):
                    lineas[row] = linea[2:]
                elif linea.startswith('#'):
                    lineas[row] = linea[1:]
                else:
                    idx = linea.find('#')
                    if idx != -1:
                        resto = linea[idx+1:]
                        if resto.startswith(' '):
                            resto = resto[1:]
                        lineas[row] = linea[:idx] + resto
                # Translators: Speech announcement when code line is uncommented.
                msg = _("Line uncommented")
            else:
                lineas[row] = '# ' + linea
                # Translators: Speech announcement when code line is commented.
                msg = _("Line commented")

            nueva_txt = '\n'.join(lineas)
            self.edicion.SetValue(nueva_txt)
            self.edicion.SetInsertionPoint(min(pt, len(nueva_txt)))

            self.anunciar(msg)
        except Exception:
            pass

    def on_duplicar_linea(self, event=None):
        """Duplica la línea actual debajo de la misma (Ctrl+D)."""
        try:
            pt = self.edicion.GetInsertionPoint()
            txt = self.edicion.GetValue()
            row = txt[:pt].count('\n')
            lineas = txt.split('\n')
            lineas.insert(row + 1, lineas[row])
            self.edicion.SetValue('\n'.join(lineas))

            nuevo_pt = len('\n'.join(lineas[:row + 1])) + 1
            self.edicion.SetInsertionPoint(min(nuevo_pt, len(self.edicion.GetValue())))
            # Translators: Speech announcement when code line is duplicated.
            self.anunciar(_("Line duplicated"))
        except Exception:
            pass

    def on_eliminar_linea(self, event=None):
        """Elimina por completo la línea actual (Ctrl+Shift+K)."""
        try:
            pt = self.edicion.GetInsertionPoint()
            txt = self.edicion.GetValue()
            row = txt[:pt].count('\n')
            lineas = txt.split('\n')
            if len(lineas) > 1:
                del lineas[row]
                self.edicion.SetValue('\n'.join(lineas))
                nuevo_pt = len('\n'.join(lineas[:row])) if row < len(lineas) else len(self.edicion.GetValue())
                self.edicion.SetInsertionPoint(min(nuevo_pt, len(self.edicion.GetValue())))
            else:
                self.edicion.SetValue("")

            # Translators: Speech announcement when code line is deleted.
            self.anunciar(_("Line deleted"))
        except Exception:
            pass

    def on_verificar_sintaxis(self, event=None):
        """Analiza la sintaxis y el balanceo de delimitadores del código sin ejecutarlo (F7)."""
        src = self.edicion.GetValue()

        bal_err = comprobar_balanceo_delimitadores(src)
        if bal_err:
            linea_err = bal_err.get("linea", 1)
            # Translators: Speech announcement for delimiter syntax warning.
            msg = _("Delimiter notice on line {line}: {message}").format(
                line=linea_err, message=bal_err['mensaje']
            )
            self.ultimo_error_linea = linea_err
            self.ultimo_error_msg = bal_err['mensaje']
            if self.sonidos_activos:
                SoundManager.play('sintaxis_aviso')
            try:
                lineas = src.split('\n')
                pt = len('\n'.join(lineas[:linea_err - 1])) + 1 if linea_err > 1 else 0
                self.edicion.SetInsertionPoint(min(pt, len(src)))
            except Exception:
                pass
            self.anunciar(msg)
            return

        try:
            compile(src, "<string>", "exec")
            self.ultimo_error_linea = None
            self.ultimo_error_msg = None
            # Translators: Speech announcement when code syntax check passes with no errors.
            msg = _("Syntax and delimiters correct. No structural errors detected in code.")
            if self.sonidos_activos:
                SoundManager.play('exito')
        except SyntaxError as e:
            linea_err = e.lineno or 1
            self.ultimo_error_linea = linea_err
            self.ultimo_error_msg = e.msg
            # Translators: Speech announcement when a SyntaxError is detected.
            msg = _("Syntax error on line {line}: {error}.").format(line=linea_err, error=e.msg)
            if self.sonidos_activos:
                SoundManager.play('sintaxis_aviso')
            try:
                lineas = src.split('\n')
                pt = len('\n'.join(lineas[:linea_err - 1])) + 1 if linea_err > 1 else 0
                self.edicion.SetInsertionPoint(min(pt, len(src)))
            except Exception:
                pass
        except Exception as e:
            # Translators: Speech announcement for compilation notice.
            msg = _("Compilation notice: {error}.").format(error=e)

        self.anunciar(msg)

    def on_ir_al_error(self, event=None):
        """Mueve el cursor exactamente a la línea del último error detectado (F4)."""
        if self.ultimo_error_linea is None:
            # Translators: Speech announcement when pressing F4 but no error is recorded.
            self.anunciar(_("No recent execution or syntax errors recorded."))
            return

        src = self.edicion.GetValue()
        lineas = src.split('\n')
        linea_num = max(1, min(self.ultimo_error_linea, len(lineas)))
        pt = len('\n'.join(lineas[:linea_num - 1])) + 1 if linea_num > 1 else 0
        self.edicion.SetInsertionPoint(min(pt, len(src)))
        self.edicion.SetFocus()

        # Translators: Fallback error detail if not specifically recorded.
        detalle = self.ultimo_error_msg or _("error detected")
        # Translators: Speech announcement after jumping cursor to error line.
        msg = _("Cursor on line {line}: {detail}").format(line=linea_num, detail=detalle)
        self.anunciar(msg)

    def on_mostrar_simbolos(self, event=None):
        """Abre el diálogo accesible de navegación estructural por funciones y clases (Ctrl+Shift+O)."""
        dlg = SymbolsDialog(self, self.edicion.GetValue())
        if dlg.ShowModal() == wx.ID_OK:
            simbolo = dlg.get_selected_symbol()
            if simbolo:
                tipo, nombre, num_linea, pos_char = simbolo
                self.edicion.SetInsertionPoint(min(pos_char, len(self.edicion.GetValue())))
                self.edicion.SetFocus()
                # Translators: Speech announcement after jumping to symbol header.
                msg = _("Cursor on {type} {name}, line {line}").format(type=tipo.lower(), name=nombre, line=num_linea)
                self.anunciar(msg)
        dlg.Destroy()

    def on_siguiente_definicion(self, event=None):
        """Salta a la cabecera de la siguiente función o clase en el código (Alt+N)."""
        src = self.edicion.GetValue()
        pt = self.edicion.GetInsertionPoint()
        lineas = src.splitlines(True)
        pos_acum = 0
        linea_actual = src[:pt].count('\n') + 1
        siguiente = None

        for num_linea, linea in enumerate(lineas, start=1):
            if num_linea > linea_actual:
                m = re.match(r'^(?:[ \t]*)(def|class)\s+([a-zA-Z_0-9]+)', linea)
                if m:
                    siguiente = (m.group(1), m.group(2), num_linea, pos_acum)
                    break
            pos_acum += len(linea)

        if siguiente:
            tipo, nombre, num_linea, pos_char = siguiente
            self.edicion.SetInsertionPoint(min(pos_char, len(src)))
            self.edicion.SetFocus()
            # Translators: Label for Class in definition jump announcement.
            # Translators: Label for Function in definition jump announcement.
            desc = _("Class") if tipo == "class" else _("Function")
            # Translators: Speech announcement when jumping to definition: [Class/Function] Name, line X.
            msg = _("{kind} {name}, line {line}").format(kind=desc, name=nombre, line=num_linea)
            self.anunciar(msg)
        else:
            # Translators: Speech announcement when Alt+N finds no further definitions.
            self.anunciar(_("No more definitions ahead."))

    def on_anterior_definicion(self, event=None):
        """Salta a la cabecera de la función o clase anterior en el código (Alt+P)."""
        src = self.edicion.GetValue()
        pt = self.edicion.GetInsertionPoint()
        lineas = src.splitlines(True)
        linea_actual = src[:pt].count('\n') + 1
        anterior = None

        pos_acum = 0
        for num_linea, linea in enumerate(lineas, start=1):
            if num_linea < linea_actual:
                m = re.match(r'^(?:[ \t]*)(def|class)\s+([a-zA-Z_0-9]+)', linea)
                if m:
                    anterior = (m.group(1), m.group(2), num_linea, pos_acum)
            pos_acum += len(linea)

        if anterior:
            tipo, nombre, num_linea, pos_char = anterior
            self.edicion.SetInsertionPoint(min(pos_char, len(src)))
            self.edicion.SetFocus()
            # Translators: Label for Class in definition jump announcement.
            # Translators: Label for Function in definition jump announcement.
            desc = _("Class") if tipo == "class" else _("Function")
            # Translators: Speech announcement when jumping to definition: [Class/Function] Name, line X.
            msg = _("{kind} {name}, line {line}").format(kind=desc, name=nombre, line=num_linea)
            self.anunciar(msg)
        else:
            # Translators: Speech announcement when Alt+P finds no earlier definitions.
            self.anunciar(_("No previous definitions."))

    def on_leer_toda_la_salida(self, event=None):
        """Verbaliza por voz todo el contenido de la consola sin retirar el foco del editor (Ctrl+Shift+C)."""
        txt = self.salida.GetValue().strip()
        if not txt:
            # Translators: Speech announcement when reading console output but it is empty.
            self.anunciar(_("Console empty."))
            return
        self.anunciar(txt)

    def on_anunciar_posicion(self, event=None):
        """Informa verbalmente la línea y columna actual del cursor (Ctrl+L)."""
        pt = self.edicion.GetInsertionPoint()
        txt = self.edicion.GetValue()
        row = txt[:pt].count('\n') + 1
        last_nl = txt[:pt].rfind('\n')
        col = (pt - last_nl) if last_nl != -1 else (pt + 1)
        total_lineas = txt.count('\n') + 1

        # Translators: Speech announcement reporting cursor line and column.
        msg = _("Line {row} of {total}, column {col}.").format(row=row, total=total_lineas, col=col)
        self.anunciar(msg)

    def on_autocompletar(self, event=None):
        """Asistente de autocompletado inteligente con previsualización de documentación (Ctrl+Espacio)."""
        try:
            pt = self.edicion.GetInsertionPoint()
            txt = self.edicion.GetValue()
            prefijo = txt[:pt].split()[-1] if txt[:pt].split() else ""
            prefijo = re.sub(r'[^a-zA-Z0-9_]', '', prefijo)

            simbolos_locales = set(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', txt))
            palabras_candidatas = sorted(list(set(self.PALABRAS_CLAVE) | set(DOCS_PYTHON.keys()) | simbolos_locales))

            if not prefijo:
                coincidencias = sorted(list(set(self.PALABRAS_CLAVE) | set(DOCS_PYTHON.keys())))[:25]
            else:
                coincidencias = [p for p in palabras_candidatas if p.startswith(prefijo) and p != prefijo]

            if not coincidencias:
                if ui:
                    # Translators: Speech announcement when autocomplete finds no suggestions.
                    ui.message(_("No suggestions for '{prefix}'.").format(prefix=prefijo))
                return

            if len(coincidencias) == 1:
                eleccion = coincidencias[0]
                resto = eleccion[len(prefijo):]
                self.edicion.WriteText(resto)
                # Translators: Announcement when autocompletion completes a word.
                msg = _("Completed: {choice}").format(choice=eleccion)
                if speech and hasattr(speech, 'speakMessage'):
                    speech.speakMessage(msg)
                if ui:
                    ui.message(msg)
            else:
                dlg = AutoCompleteDialog(self, prefijo, coincidencias)
                if dlg.ShowModal() == wx.ID_OK and dlg.seleccion:
                    eleccion = dlg.seleccion
                    resto = eleccion[len(prefijo):]
                    self.edicion.WriteText(resto)
                    # Translators: Announcement when autocompletion inserts a word.
                    msg = _("Inserted: {choice}").format(choice=eleccion)
                    if speech and hasattr(speech, 'speakMessage'):
                        speech.speakMessage(msg)
                    if ui:
                        ui.message(msg)
                dlg.Destroy()
                self.edicion.SetFocus()
        except Exception:
            pass

    def on_doc_rapida(self, event=None):
        """Muestra la documentación rápida del símbolo bajo el cursor (Shift+F1)."""
        try:
            pt = self.edicion.GetInsertionPoint()
            txt = self.edicion.GetValue()
            palabra = ""
            izq = pt
            while izq > 0 and (txt[izq - 1].isalnum() or txt[izq - 1] == '_'):
                izq -= 1
            der = pt
            while der < len(txt) and (txt[der].isalnum() or txt[der] == '_'):
                der += 1
            palabra = txt[izq:der]

            if not palabra:
                sel = self.edicion.GetStringSelection().strip()
                if sel:
                    palabra = sel

            if not palabra:
                # Translators: Speech announcement when Shift+F1 is pressed on empty space.
                self.anunciar(_("Place cursor over a function or keyword to view documentation."))
                return

            doc = obtener_documentacion_simbolo(palabra)
            self.anunciar(doc)
        except Exception:
            pass

    def on_formatear_pep8(self, event=None):
        """Formatea el documento activo según el estándar PEP 8 (Shift+Alt+F o Ctrl+Shift+I)."""
        codigo_actual = self.edicion.GetValue()
        nuevo_codigo, reporte = formatear_codigo_pep8(codigo_actual)
        if nuevo_codigo != codigo_actual:
            pt = self.edicion.GetInsertionPoint()
            self.edicion.SetValue(nuevo_codigo)
            self.edicion.SetInsertionPoint(min(pt, len(nuevo_codigo)))
        self.anunciar(reporte)

    def on_renombrar_simbolo(self, event=None):
        """Renombra un identificador o variable en todo el script (F2)."""
        pt = self.edicion.GetInsertionPoint()
        txt = self.edicion.GetValue()
        palabra = self.edicion.GetStringSelection().strip()
        if not palabra:
            izq = pt
            while izq > 0 and (txt[izq - 1].isalnum() or txt[izq - 1] == '_'):
                izq -= 1
            der = pt
            while der < len(txt) and (txt[der].isalnum() or txt[der] == '_'):
                der += 1
            palabra = txt[izq:der]

        if not palabra:
            palabra = "mi_variable"

        dlg = RenameSymbolDialog(self, palabra)
        if dlg.ShowModal() == wx.ID_OK and dlg.nuevo_nombre and dlg.nuevo_nombre != palabra:
            patron = r'\b' + re.escape(palabra) + r'\b'
            nuevo_txt, total = re.subn(patron, dlg.nuevo_nombre, txt)
            self.edicion.SetValue(nuevo_txt)
            self.edicion.SetInsertionPoint(min(pt, len(nuevo_txt)))
            # Translators: Speech announcement after renaming an identifier across script.
            msg = _("Renamed {count} occurrences of {old} to {new}.").format(
                count=total, old=palabra, new=dlg.nuevo_nombre
            )
            self.anunciar(msg)
        dlg.Destroy()
        self.edicion.SetFocus()

    def on_extraer_funcion(self, event=None):
        """Extrae el bloque seleccionado a una nueva función (Ctrl+Shift+R)."""
        sel = self.edicion.GetStringSelection()
        if not sel.strip():
            # Translators: Speech announcement when extracting function without active selection.
            self.anunciar(_("First select the code block you want to extract into a function."))
            return

        dlg = ExtractFunctionDialog(self)
        if dlg.ShowModal() == wx.ID_OK and dlg.nombre_funcion:
            nombre = dlg.nombre_funcion
            lineas_sel = [f"    {l}" for l in sel.strip().splitlines()]
            cuerpo_fn = "\n".join(lineas_sel)
            nueva_def = f"\ndef {nombre}():\n{cuerpo_fn}\n\n"

            inicio, fin = self.edicion.GetSelection()
            txt_completo = self.edicion.GetValue()

            nuevo_codigo = nueva_def + txt_completo[:inicio] + f"{nombre}()" + txt_completo[fin:]
            self.edicion.SetValue(nuevo_codigo)
            # Translators: Speech announcement after extracting code into a function.
            msg = _("Function '{name}' extracted successfully.").format(name=nombre)
            self.anunciar(msg)
        dlg.Destroy()
        self.edicion.SetFocus()

    def on_toggle_breakpoint(self, event=None):
        """Alterna un punto de interrupción en la línea actual (F9)."""
        pt = self.edicion.GetInsertionPoint()
        txt = self.edicion.GetValue()
        row = txt[:pt].count('\n') + 1

        if row in self.breakpoints:
            self.breakpoints.remove(row)
            # Translators: Speech announcement when a breakpoint is removed.
            msg = _("Breakpoint removed on line {line}.").format(line=row)
        else:
            self.breakpoints.add(row)
            # Translators: Speech announcement when a breakpoint is set.
            msg = _("Breakpoint set on line {line}.").format(line=row)
            if self.sonidos_activos:
                SoundManager.play('bloque')

        self.anunciar(msg)

    def on_depurar_paso_a_paso(self, event=None):
        """Inicia el depurador interactivo paso a paso (F10)."""
        codigo = self.edicion.GetValue()
        if not codigo.strip():
            # Translators: Speech announcement when launching debugger on empty code.
            self.anunciar(_("The editor is empty. Write code before starting debugging."))
            return

        dlg = StepDebuggerDialog(self, codigo, self.breakpoints)
        dlg.ShowModal()
        dlg.Destroy()
        self.edicion.SetFocus()

    def on_ejecutar_pruebas(self, event=None):
        """Ejecuta las pruebas unitarias del script con reporte accesible (Ctrl+T)."""
        dlg = TestRunnerDialog(self, self.edicion.GetValue())
        dlg.ShowModal()
        dlg.Destroy()
        self.edicion.SetFocus()

    def on_gestor_interpretes(self, event=None):
        """Abre el gestor de intérpretes de Python y entornos virtuales (Ctrl+Shift+P)."""
        dlg = InterpreterManagerDialog(self)
        dlg.ShowModal()
        dlg.Destroy()
        self.edicion.SetFocus()

    # ===    # Navegación entre pasos
    # ===
    def on_paso_siguiente(self, event=None):
        cap = CURRICULUM[self.cap_idx]
        total_pasos = len(cap.get("pasos", []))
        if self.paso_idx < total_pasos - 1:
            self.paso_idx += 1
            if self.sonidos_activos:
                SoundManager.play('paso')
            self.cargar_paso_actual(anunciar_voz=True)
            self.edicion.SetFocus()
        else:
            if self.cap_idx < len(CURRICULUM) - 1:
                if not ProgressManager.is_chapter_completed(self.cap_idx, total_pasos):
                    msg = _("To advance to next chapter, you must complete all steps of current chapter.")
                    if speech and hasattr(speech, 'speakMessage'):
                        speech.speakMessage(msg)
                    if ui:
                        ui.message(msg)
                    return
                self.cap_idx += 1
                self.paso_idx = 0
                if self.sonidos_activos:
                    SoundManager.play('paso')
                self.cargar_paso_actual(anunciar_voz=True)
                self.edicion.SetFocus()
            else:
                if ui:
                    ui.message(_("Congratulations! You have completed all chapters in curriculum."))

    def on_paso_anterior(self, event=None):
        if self.paso_idx > 0:
            self.paso_idx -= 1
            if self.sonidos_activos:
                SoundManager.play('paso')
            self.cargar_paso_actual(anunciar_voz=True)
            self.edicion.SetFocus()
        elif self.cap_idx > 0:
            self.cap_idx -= 1
            self.paso_idx = len(CURRICULUM[self.cap_idx]["pasos"]) - 1
            if self.sonidos_activos:
                SoundManager.play('paso')
            self.cargar_paso_actual(anunciar_voz=True)
            self.edicion.SetFocus()

    def on_abrir_repl(self, event=None):
        dlg = ReplDialog(self)
        dlg.ShowModal()
        dlg.Destroy()
        self.edicion.SetFocus()

    def on_abrir_glosario(self, event=None):
        dlg = GlossaryDialog(self)
        dlg.ShowModal()
        dlg.Destroy()
        self.edicion.SetFocus()

    def on_abrir_temario(self, event=None):
        dlg = ChapterSelectDialog(self, self.cap_idx)
        if dlg.ShowModal() == wx.ID_OK:
            sel = dlg.get_selected_index()
            if sel != wx.NOT_FOUND:
                self.cap_idx = sel
                self.paso_idx = 0
                self.cargar_paso_actual(anunciar_voz=True)
                self.edicion.SetFocus()
        dlg.Destroy()

    def on_reiniciar_codigo(self, event=None):
        cap = CURRICULUM[self.cap_idx]
        paso = cap["pasos"][self.paso_idx]
        self.edicion.SetValue(paso.get("codigo", ""))
        self.salida.SetValue("")
        self.edicion.SetFocus()
        # Translators: Speech announcement when code is reset.
        self.anunciar(_("Exercise code reset to its initial state."))

    def on_mostrar_atajos(self, event=None):
        dlg = ShortcutsDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def on_donacion(self, event=None):
        url = "https://www.paypal.me/kevinvelasquezvargas"
        try:
            webbrowser.open(url)
            if ui:
                # Translators: Speech announcement when opening donation page in browser.
                ui.message(_("Opening donation page in web browser..."))
        except Exception:
            # Translators: Dialog message showing donation link.
            msg = _(
                "You can make a voluntary contribution to support the project at:\n"
                "{url}"
            ).format(url=url)
            # Translators: Title for donation dialog.
            title = _("Make a Donation")
            wx.MessageBox(
                msg,
                title,
                wx.OK | wx.ICON_INFORMATION,
                self
            )

    def on_key_down_edicion(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ESCAPE:
            self.Close()
            return
        elif keycode == wx.WXK_TAB:
            if event.ShiftDown():
                if not self.modo_editor and self.mision_ctrl.IsShown():
                    self.mision_ctrl.SetFocus()
                else:
                    self.btn_cerrar.SetFocus()
            else:
                self.edicion.WriteText("    ")
            return
        elif keycode == wx.WXK_RETURN:
            if self.linter_activo:
                pt = self.edicion.GetInsertionPoint()
                txt = self.edicion.GetValue()
                row = txt[:pt].count('\n')
                linea = self.edicion.GetLineText(row).strip()

                palabras_bloque = ("def ", "if ", "elif ", "while ", "for ", "class ", "try:", "except")
                if any(linea.startswith(p) for p in palabras_bloque) and not linea.endswith(":"):
                    if self.sonidos_activos:
                        SoundManager.play('sintaxis_aviso')
            event.Skip()
            return
        event.Skip()

    def on_key_up_edicion(self, event):
        self.ejecutar_linter_acustico()
        event.Skip()

    def ejecutar_linter_acustico(self):
        if not self.linter_activo or not self.sonidos_activos:
            return
        try:
            pt = self.edicion.GetInsertionPoint()
            txt = self.edicion.GetValue()
            row = txt[:pt].count('\n')

            linea_txt = self.edicion.GetLineText(row)
            espacios = len(linea_txt) - len(linea_txt.lstrip(' '))

            if espacios >= 12:
                nivel = 12
            elif espacios >= 8:
                nivel = 8
            elif espacios >= 4:
                nivel = 4
            else:
                nivel = 0

            if row != self._last_linter_line or nivel != self._last_linter_indent:
                self._last_linter_line = row
                self._last_linter_indent = nivel

                if nivel == 0:
                    SoundManager.play('indent0')
                elif nivel == 4:
                    SoundManager.play('indent4')
                elif nivel == 8:
                    SoundManager.play('indent8')
                elif nivel >= 12:
                    SoundManager.play('indent12')
        except Exception:
            pass

    def on_char_hook_global(self, event):
        keycode = event.GetKeyCode()
        modifiers = event.GetModifiers()

        if keycode == wx.WXK_ESCAPE:
            self.Close()
            return

        if keycode == wx.WXK_F1:
            if event.ShiftDown():
                self.on_doc_rapida()
            else:
                self.on_traducir_linea()
            return

        if keycode == wx.WXK_F2:
            self.on_renombrar_simbolo()
            return

        if keycode == wx.WXK_F3:
            self.on_leer_instruccion_actual()
            return

        if keycode == wx.WXK_F4:
            self.on_ir_al_error()
            return

        if keycode == wx.WXK_F5:
            self.on_ejecutar(None)
            return

        if keycode == wx.WXK_F6:
            self.on_alternar_foco()
            return

        if keycode == wx.WXK_F7:
            self.on_verificar_sintaxis()
            return

        if keycode == wx.WXK_F9:
            self.on_toggle_breakpoint()
            return

        if keycode == wx.WXK_F10:
            self.on_depurar_paso_a_paso()
            return

        if keycode == wx.WXK_F11:
            self.on_mostrar_atajos()
            return

        if keycode == wx.WXK_F12:
            self.on_acerca()
            return

        # Atajos con Alt
        is_alt = event.AltDown() or bool(modifiers & wx.MOD_ALT)
        if is_alt:
            if event.ShiftDown() and keycode in (ord('F'), ord('f')):
                self.on_formatear_pep8()
                return
            if not event.ControlDown() and not event.ShiftDown():
                if keycode == wx.WXK_RIGHT:
                    self.on_paso_siguiente()
                    return
                elif keycode == wx.WXK_LEFT:
                    self.on_paso_anterior()
                    return
                elif keycode in (ord('N'), ord('n')):
                    self.on_siguiente_definicion()
                    return
                elif keycode in (ord('P'), ord('p')):
                    self.on_anterior_definicion()
                    return

        if modifiers == wx.MOD_CONTROL:
            # Permitir navegación y selección estándar en controles de texto
            if keycode in (ord('C'), ord('V'), ord('X'), ord('Z'), ord('Y'), ord('A'),
                           wx.WXK_LEFT, wx.WXK_RIGHT, wx.WXK_UP, wx.WXK_DOWN,
                           wx.WXK_HOME, wx.WXK_END, wx.WXK_PAGEUP, wx.WXK_PAGEDOWN):
                event.Skip()
                return

            if keycode in (wx.WXK_RETURN, ord('E')):
                self.on_ejecutar(None)
                return
            elif keycode == ord('M'):
                self.on_alternar_modo_trabajo()
                return
            elif keycode == ord('N'):
                self.on_nuevo_archivo(None)
                return
            elif keycode == ord('F'):
                self.on_buscar(None)
                return
            elif keycode == ord('G'):
                self.on_ir_a_linea(None)
                return
            elif keycode == ord('I'):
                self.on_leer_instruccion_actual()
                return
            elif keycode == ord('P'):
                self.on_pista(None)
                return
            elif keycode in (ord('/'), ord('K')):
                self.on_comentar_descomentar(None)
                return
            elif keycode == ord('D'):
                self.on_duplicar_linea(None)
                return
            elif keycode == ord('L'):
                self.on_anunciar_posicion(None)
                return
            elif keycode == wx.WXK_SPACE:
                self.on_autocompletar(None)
                return
            elif keycode == ord('T'):
                self.on_ejecutar_pruebas(None)
                return
            elif keycode == ord('J'):
                self.on_abrir_repl(None)
                return
            elif keycode == ord('1'):
                self.on_abrir_temario(None)
                return
            elif keycode == ord('R'):
                self.on_reiniciar_codigo(None)
                return
            elif keycode == ord('O'):
                self.on_abrir_archivo(None)
                return
            elif keycode == ord('S'):
                self.on_guardar_archivo(None)
                return
            elif keycode == ord('4'):
                self.edicion.SetFocus()
                return
            elif keycode == ord('5'):
                self.salida.SetFocus()
                return
            elif keycode == ord('6'):
                self.leer_ultima_salida()
                return
            else:
                event.Skip()
        elif modifiers == (wx.MOD_CONTROL | wx.MOD_SHIFT):
            # Permitir selección de texto por bloques / palabras
            if keycode in (wx.WXK_LEFT, wx.WXK_RIGHT, wx.WXK_UP, wx.WXK_DOWN,
                           wx.WXK_HOME, wx.WXK_END, wx.WXK_PAGEUP, wx.WXK_PAGEDOWN):
                event.Skip()
                return

            if keycode == ord('K'):
                self.on_eliminar_linea(None)
                return
            elif keycode == ord('O'):
                self.on_mostrar_simbolos()
                return
            elif keycode == ord('C'):
                self.on_leer_toda_la_salida()
                return
            elif keycode == ord('S'):
                self.on_guardar_como(None)
                return
            elif keycode == ord('P'):
                self.on_gestor_interpretes(None)
                return
            elif keycode == ord('R'):
                self.on_extraer_funcion(None)
                return
            elif keycode == ord('I'):
                self.on_formatear_pep8(None)
                return
            event.Skip()
        else:
            if keycode == ord(':') and self.sonidos_activos:
                SoundManager.play('bloque')
            event.Skip()

    def on_leer_instruccion_actual(self, event=None):
        """Lee la consigna del paso actual por voz y braille sin retirar el foco del editor de código."""
        try:
            if self.modo_editor:
                # Translators: Speech announcement when reading instruction in standalone editor mode.
                self.anunciar(_("Standalone Editor mode active."))
                return

            cap = CURRICULUM[self.cap_idx]
            paso = cap["pasos"][self.paso_idx]
            num_paso = self.paso_idx + 1
            total_pasos = len(cap["pasos"])
            instruccion = paso.get("instruccion", "")
            if not instruccion:
                instruccion = self.mision_ctrl.GetValue().strip()
            # Translators: Speech announcement when reading current lesson instruction.
            msg = _("Step {step} of {total}: {instruction}").format(
                step=num_paso, total=total_pasos, instruction=instruccion
            )
            self.anunciar(msg)
        except Exception:
            pass

    def on_alternar_foco(self, event=None):
        """Alterna el foco entre el editor de código y la consola de resultados (F6)."""
        foco_actual = wx.Window.FindFocus()
        if foco_actual == self.salida:
            def _ir_edicion():
                self.edicion.SetFocus()
                # Translators: Speech announcement when switching focus to code editor.
                self.anunciar(_("Focus on code editor"), delay=50)
            wx.CallLater(100, _ir_edicion)
        else:
            def _ir_salida():
                self.salida.SetFocus()
                # Translators: Speech announcement when switching focus to results console.
                self.anunciar(_("Focus on results console"), delay=50)
            wx.CallLater(100, _ir_salida)

    def leer_ultima_salida(self):
        txt = self.salida.GetValue().strip()
        if not txt:
            if ui:
                # Translators: Speech announcement when reading last console line but it is empty.
                ui.message(_("Console empty."))
            return
        lineas = [l.strip() for l in txt.splitlines() if l.strip()]
        if lineas:
            ultima = lineas[-1]
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(ultima)
            if ui:
                ui.message(ultima)

    def on_abrir_archivo(self, event=None):
        dlg = wx.FileDialog(
            self, _("Open Python script"),
            wildcard=_("Python Files (*.py)|*.py|All Files (*.*)|*.*"),
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    self.edicion.SetValue(f.read())
                self.archivo_abierto = path
                if ui:
                    ui.message(_("File loaded: {filename}").format(filename=os.path.basename(path)))
                self.edicion.SetFocus()
            except Exception as e:
                wx.MessageBox(_("Error opening file: {error}").format(error=e), _("Error"), wx.OK | wx.ICON_ERROR, self)
        dlg.Destroy()

    def on_guardar_archivo(self, event=None):
        if self.archivo_abierto:
            try:
                with open(self.archivo_abierto, "w", encoding="utf-8") as f:
                    f.write(self.edicion.GetValue())
                if ui:
                    ui.message(_("Saved to {filename}").format(filename=os.path.basename(self.archivo_abierto)))
            except Exception as e:
                wx.MessageBox(_("Error saving file: {error}").format(error=e), _("Error"), wx.OK | wx.ICON_ERROR, self)
        else:
            self.on_guardar_como(event)

    def on_guardar_como(self, event=None):
        dlg = wx.FileDialog(
            self, _("Save script as"),
            wildcard=_("Python Files (*.py)|*.py"),
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(self.edicion.GetValue())
                self.archivo_abierto = path
                if ui:
                    ui.message(_("Saved as {filename}").format(filename=os.path.basename(path)))
            except Exception as e:
                wx.MessageBox(_("Error saving file: {error}").format(error=e), _("Error"), wx.OK | wx.ICON_ERROR, self)
        dlg.Destroy()

    def on_abrir_doc(self, event=None):
        abierto = False
        if docHandler and hasattr(docHandler, 'openDoc'):
            try:
                abierto = docHandler.openDoc("readme.html")
            except Exception:
                abierto = False

        if not abierto:
            cur_lang = "en"
            try:
                import languageHandler
                cur_lang = languageHandler.getLanguage().split("_")[0]
            except Exception:
                cur_lang = "es"

            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            candidatos = [
                os.path.join(base_dir, "doc", cur_lang, "readme.html"),
                os.path.join(base_dir, "addon", "doc", cur_lang, "readme.html"),
                os.path.join(base_dir, "doc", "es", "readme.html"),
                os.path.join(base_dir, "addon", "doc", "es", "readme.html"),
                os.path.join(base_dir, "doc", "en", "readme.html"),
                os.path.join(base_dir, "addon", "doc", "en", "readme.html"),
                os.path.join(base_dir, "doc", "readme.html"),
                os.path.join(base_dir, "readme.html")
            ]
            for cand in candidatos:
                if os.path.isfile(cand):
                    try:
                        os.startfile(cand)
                        abierto = True
                        break
                    except Exception:
                        try:
                            webbrowser.open(f"file:///{cand.replace(os.sep, '/')}")
                            abierto = True
                            break
                        except Exception:
                            pass

        if not abierto and ui:
            ui.message(_("Could not open documentation in web browser."))

    def on_soporte(self, event=None):
        """Abre el diálogo accesible de soporte técnico y donaciones."""
        dlg = SupportDialog(self)
        dlg.ShowModal()
        dlg.Destroy()
        self.edicion.SetFocus()

    def on_acerca(self, event=None):
        """Abre la documentación de Acerca de en el navegador web predeterminado."""
        # Translators: Speech announcement when opening About documentation.
        msg = _("Opening About documentation in web browser.")
        if speech and hasattr(speech, 'speakMessage'):
            speech.speakMessage(msg)
        if ui:
            ui.message(msg)
        self.on_abrir_doc(event)

    def on_close(self, event):
        prog = ProgressManager.load_progress()
        prog["current_chapter"] = self.cap_idx
        prog["current_step"] = self.paso_idx
        ProgressManager.save_progress(prog)
        self.Destroy()
