# -*- coding: utf-8 -*-
# ======# Módulo: globalPlugins/python_tutor/gui_frame.py
# Propósito: Interfaz gráfica accesible, estructurada y con funciones avanzadas de edición.
# Autor: Kevin Andrés Velasquez Vargas
# Licencia: GNU General Public License v3.0 (GPLv3)
# ======
import os
import re
import webbrowser
import wx

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
from .curriculum import CURRICULUM, GLOSARIO, obtener_glosario
from .progress import ProgressManager
from .repl_dialog import ReplDialog
from .translator import traducir_linea_codigo
from .ai_assistant import AIConfigDialog, AIConsultDialog, obtener_config_ia
from .i18n import _t, obtener_idioma_actual, establecer_idioma
from .project_manager import ProjectManagerDialog
from .braille_helper import anunciar_braille, formatear_linea_para_braille
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
        super(FindDialog, self).__init__(parent, title="Buscar en el Editor", size=(480, 240))
        self.text_ctrl = text_ctrl

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(panel, label="Texto a buscar:")
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.query_ctrl = wx.TextCtrl(panel)
        self.query_ctrl.SetName("Texto a buscar")
        vbox.Add(self.query_ctrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        self.chk_case = wx.CheckBox(panel, label="Coincidir mayúsculas y minúsculas")
        vbox.Add(self.chk_case, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_find = wx.Button(panel, wx.ID_OK, label="Buscar siguiente")
        btn_find.SetDefault()
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label="Cerrar")
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
                ui.message("Escribe un texto para buscar.")
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
            msg = f"Encontrado '{q}' en la línea {row}"
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
            self.EndModal(wx.ID_OK)
        else:
            msg = f"No se encontró '{q}' en el código."
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)


class GoToLineDialog(wx.Dialog):
    """Diálogo accesible para desplazarse a un número de línea específico."""
    def __init__(self, parent, text_ctrl):
        super(GoToLineDialog, self).__init__(parent, title="Ir a la Línea", size=(420, 200))
        self.text_ctrl = text_ctrl
        total_lines = self.text_ctrl.GetNumberOfLines()
        if total_lines < 1:
            total_lines = self.text_ctrl.GetValue().count('\n') + 1

        self.total_lines = max(1, total_lines)

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(panel, label=f"Número de línea (1 - {self.total_lines}):")
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.line_ctrl = wx.TextCtrl(panel)
        self.line_ctrl.SetName("Número de línea")
        vbox.Add(self.line_ctrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_go = wx.Button(panel, wx.ID_OK, label="Ir a línea")
        btn_go.SetDefault()
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label="Cancelar")
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
                ui.message("Por favor introduce un número de línea válido.")
            return

        if 1 <= line_no <= self.total_lines:
            src = self.text_ctrl.GetValue()
            lineas = src.split('\n')
            pt = len('\n'.join(lineas[:line_no - 1])) + 1 if line_no > 1 else 0
            self.text_ctrl.SetInsertionPoint(min(pt, len(src)))
            self.text_ctrl.SetFocus()
            msg = f"Cursor en línea {line_no}"
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
            self.EndModal(wx.ID_OK)
        else:
            if ui:
                ui.message(f"La línea debe estar entre 1 y {self.total_lines}.")


class ChapterSelectDialog(wx.Dialog):
    """Diálogo accesible para saltar directamente a cualquier capítulo del temario."""
    def __init__(self, parent, current_idx):
        is_en = (obtener_idioma_actual() == "en")
        title = "Syllabus - Chapter Selector" if is_en else "Selector de Capítulos del Temario"
        super(ChapterSelectDialog, self).__init__(parent, title=title, size=(650, 480))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl_text = "Select the chapter you wish to navigate to:" if is_en else "Elige el capítulo al que deseas acceder:"
        lbl = wx.StaticText(panel, label=lbl_text)
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.opciones = []
        self.cap_estados = []
        for i, cap in enumerate(CURRICULUM):
            total_pasos = len(cap.get("pasos", []))
            completado = ProgressManager.is_chapter_completed(i, total_pasos)
            desbloqueado = ProgressManager.is_chapter_unlocked(i)
            self.cap_estados.append((desbloqueado, completado))
            if completado:
                estado_str = "Passed, " if is_en else "Superado, "
            elif desbloqueado:
                estado_str = "Available, " if is_en else "Disponible, "
            else:
                estado_str = "Locked, " if is_en else "Bloqueado, "
            cap_title = cap.get("titulo_en" if is_en and "titulo_en" in cap else "titulo", f"Chapter {i+1}" if is_en else f"Capítulo {i+1}")
            self.opciones.append(f"{estado_str}{cap_title}")

        self.list_box = wx.ListBox(panel, choices=self.opciones)
        list_acc_name = "Chapter list. Press Enter or click to select." if is_en else "Lista de capítulos. Presione Enter o haga clic para seleccionar."
        self.list_box.SetName(list_acc_name)
        if 0 <= current_idx < len(self.opciones):
            self.list_box.SetSelection(current_idx)
        vbox.Add(self.list_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_ok = wx.Button(panel, wx.ID_OK, label="Load Chapter" if is_en else "Cargar Capítulo")
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label="Cancel" if is_en else "Cancelar")
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
        is_en = (obtener_idioma_actual() == "en")
        if sel != wx.NOT_FOUND:
            desbloqueado, _ = self.cap_estados[sel]
            if not desbloqueado:
                msg = (
                    "This chapter is locked. You must complete all steps of the previous chapter to unlock it."
                    if is_en else
                    "Este capítulo está bloqueado. Debes completar todos los pasos del capítulo anterior para desbloquearlo."
                )
                box_title = "Chapter Locked" if is_en else "Capítulo bloqueado"
                if ui:
                    ui.message(msg)
                wx.MessageBox(msg, box_title, wx.OK | wx.ICON_WARNING, self)
                return
        self.EndModal(wx.ID_OK)

    def get_selected_index(self):
        return self.list_box.GetSelection()


class HintDialog(wx.Dialog):
    """Diálogo accesible para el sistema escalonado de pistas pedagógicas."""
    def __init__(self, parent, pistas, nivel_actual=0):
        is_en = (obtener_idioma_actual() == "en")
        title = "Assistance Hint" if is_en else "Pista de Asistencia"
        super(HintDialog, self).__init__(parent, title=title, size=(620, 380))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        total_pistas = max(1, len(pistas))
        cur_num = min(nivel_actual + 1, total_pistas)
        lbl_text = (
            f"Available hint (Level {cur_num} of {total_pistas}):"
            if is_en else
            f"Pista disponible (Nivel {cur_num} de {total_pistas}):"
        )
        lbl = wx.StaticText(panel, label=lbl_text)
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        default_txt = "Review the lesson instructions." if is_en else "Revisa las instrucciones del ejercicio."
        texto_pista = pistas[nivel_actual] if nivel_actual < len(pistas) else (pistas[-1] if pistas else default_txt)
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.text_ctrl.SetValue(texto_pista)
        self.text_ctrl.SetName("Hint content." if is_en else "Contenido de la pista.")
        vbox.Add(self.text_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        btn_ok = wx.Button(panel, wx.ID_OK, label="Understood" if is_en else "Entendido")
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
        is_en = (obtener_idioma_actual() == "en")
        title = "Welcome to Learning Python with NVDA" if is_en else "Bienvenido a Aprendizaje de Python con NVDA"
        super(WelcomeDialog, self).__init__(parent, title=title, size=(660, 440))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        if is_en:
            mensaje = (
                "Welcome to Learning Python with NVDA!\n\n"
                "This add-on guides you step-by-step through learning Python programming, "
                "beginning with fundamental computer concepts and progressing through practical "
                "coding exercises solved directly inside the editor.\n\n"
                "The environment features two operating modes:\n"
                "- Learning Mode: guided lessons, theoretical foundations, and automatic solution verification.\n"
                "- Standalone Editor Mode: a clean, accessible programming editor to write and run your own scripts.\n\n"
                "You can inspect keyboard shortcuts at any time by pressing F11 or via the Help menu, "
                "and access full documentation in your web browser by pressing F12."
            )
            chk_label = "Show this welcome guide on startup"
            btn_label = "Start"
            acc_name = "Welcome message"
        else:
            mensaje = (
                "¡Te damos la bienvenida a Aprendizaje de Python con NVDA!\n\n"
                "Este complemento te guiará paso a paso en el aprendizaje de la programación en Python, "
                "comenzando desde los conceptos fundamentales y avanzando de manera progresiva a través "
                "de ejercicios prácticos diseñados para ser resueltos directamente en el editor.\n\n"
                "El entorno cuenta con dos modalidades de trabajo:\n"
                "- Modo Aprendizaje: lecciones guiadas, explicaciones teóricas y comprobación automática de soluciones.\n"
                "- Modo Editor autónomo: un editor despejado y accesible para escribir y ejecutar tus propios scripts.\n\n"
                "Puedes consultar la lista de atajos de teclado en cualquier momento pulsando F11 o desde el menú Ayuda, "
                "y acceder a la documentación completa en el navegador web pulsando F12."
            )
            chk_label = "Mostrar esta bienvenida al iniciar"
            btn_label = "Comenzar"
            acc_name = "Mensaje de bienvenida"

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(mensaje)
        txt.SetName(acc_name)
        vbox.Add(txt, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        prog = ProgressManager.load_progress()
        self.chk_mostrar = wx.CheckBox(panel, label=chk_label)
        self.chk_mostrar.SetValue(prog.get("show_welcome", True))
        vbox.Add(self.chk_mostrar, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM, border=12)

        btn_comenzar = wx.Button(panel, wx.ID_OK, label=btn_label)
        btn_comenzar.SetDefault()
        vbox.Add(btn_comenzar, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.CenterOnParent()
        btn_comenzar.SetFocus()

        def _leer_auto_bienvenida():
            try:
                if speech and hasattr(speech, 'speakMessage'):
                    speech.speakMessage(mensaje)
                elif ui and hasattr(ui, 'message'):
                    ui.message(mensaje)
            except Exception:
                pass
        wx.CallLater(150, _leer_auto_bienvenida)

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.guardar_preferencia()
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

    def guardar_preferencia(self):
        ProgressManager.set_setting("show_welcome", self.chk_mostrar.GetValue())


class DonationPromptDialog(wx.Dialog):
    """Diálogo accesible para fomentar las donaciones voluntarias y el soporte continuo del proyecto."""
    def __init__(self, parent):
        is_en = (obtener_idioma_actual() == "en")
        title = "Support the Project & Voluntary Donations" if is_en else "Apoyo al Proyecto y Donaciones Voluntarias"
        super(DonationPromptDialog, self).__init__(parent, title=title, size=(660, 420))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        if is_en:
            mensaje = (
                "Project Support and Voluntary Donations\n\n"
                "This educational platform is an independent, 100% free, and accessible initiative "
                "created to empower blind and visually impaired individuals in programming.\n\n"
                "Maintaining this 40-chapter curriculum, the custom accessible code editor, "
                "and ensuring compatibility with NVDA requires ongoing research and dedication.\n\n"
                "If this project is helpful to your journey, please consider making a voluntary donation. "
                "Your contribution helps keep the platform actively maintained and free for everyone."
            )
            btn_donar_lbl = "Donate"
            btn_continuar_lbl = "Not now"
            acc_name = "Donation and project support message"
        else:
            mensaje = (
                "Apoyo al Proyecto y Donaciones Voluntarias\n\n"
                "Este complemento es un proyecto 100% libre, gratuito y accesible, desarrollado "
                "para facilitar el aprendizaje de la programación en la comunidad de personas con discapacidad visual.\n\n"
                "El mantenimiento continuo del curso de 40 capítulos, el editor adaptado "
                "y la compatibilidad técnica con las versiones más recientes de NVDA requieren tiempo y recursos constantes.\n\n"
                "Si esta iniciativa te resulta de utilidad, te invitamos a respaldarla "
                "con una donación voluntaria. Cualquier aporte ayuda a garantizar su continuidad libre para todos."
            )
            btn_donar_lbl = "Donar"
            btn_continuar_lbl = "Ahora no"
            acc_name = "Mensaje de donación y apoyo al proyecto"

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(mensaje)
        txt.SetName(acc_name)
        vbox.Add(txt, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_donar = wx.Button(panel, label=btn_donar_lbl)
        self.btn_continuar = wx.Button(panel, wx.ID_OK, label=btn_continuar_lbl)
        self.btn_continuar.SetDefault()

        hbox.Add(self.btn_donar, flag=wx.RIGHT, border=10)
        hbox.Add(self.btn_continuar)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.btn_donar.Bind(wx.EVT_BUTTON, self.on_donar)
        self.btn_continuar.Bind(wx.EVT_BUTTON, lambda e: self.EndModal(wx.ID_OK))
        self.CenterOnParent()
        self.btn_continuar.SetFocus()

        def _leer_auto_donacion():
            try:
                if speech and hasattr(speech, 'speakMessage'):
                    speech.speakMessage(mensaje)
                elif ui and hasattr(ui, 'message'):
                    ui.message(mensaje)
            except Exception:
                pass
        wx.CallLater(150, _leer_auto_donacion)

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

    def on_donar(self, event=None):
        url = "https://www.paypal.me/kevinvelasquezvargas"
        try:
            webbrowser.open(url)
            is_en = (obtener_idioma_actual() == "en")
            msg = "Opening PayPal donation page in web browser..." if is_en else "Abriendo página de donaciones en el navegador web..."
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
        except Exception:
            pass


class ShortcutsDialog(wx.Dialog):
    """Diálogo accesible que enumera todos los atajos de teclado del complemento."""
    def __init__(self, parent):
        is_en = (obtener_idioma_actual() == "en")
        title = "Keyboard Shortcuts Guide" if is_en else "Guía de Atajos de Teclado"
        super(ShortcutsDialog, self).__init__(parent, title=title, size=(700, 560))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        if is_en:
            texto_atajos = (
                "Complete Keyboard Shortcuts Guide:\n\n"
                "Modes and Learning:\n"
                "Control + Enter: Run code and verify challenge solution.\n"
                "Control + M: Toggle between Guided Learning Mode and Standalone Editor Mode.\n"
                "F3: Read active lesson instruction without moving cursor focus.\n"
                "F4: Place editor cursor on exact line of Traceback error.\n"
                "F6: Switch focus between code editor and output console.\n"
                "Alt + Right Arrow: Advance to next step in lesson.\n"
                "Alt + Left Arrow: Go to previous step in lesson.\n"
                "Control + P: Request assistance hint.\n"
                "F1: Explain current line in plain language (local & private by default).\n"
                "Shift + F1: Quick documentation for symbol under cursor.\n"
                "Control + R: Reset exercise starter code.\n"
                "Control + 1: Open Syllabus chapter selector.\n"
                "Control + J: Open interactive Python REPL console.\n\n"
                "Editing and IDE Development Features:\n"
                "Control + N: New clean script in editor.\n"
                "Control + F: Find text in code editor.\n"
                "Control + G: Go to specific line number.\n"
                "F2: Rename identifier or variable across file.\n"
                "Shift + Alt + F: Format document according to PEP 8.\n"
                "Control + Shift + I: Consult Google Gemini Educational AI Assistant.\n"
                "Control + Shift + R: Extract selected code block to new function.\n"
                "Control + Space: Intelligent auto-completion with documentation.\n"
                "Control + Shift + O: Accessible list of script functions and classes.\n"
                "Alt + N: Jump to next function or class header.\n"
                "Alt + P: Jump to previous function or class header.\n"
                "Control + /: Toggle comment on current line with '# '.\n"
                "Control + D: Duplicate current line downward.\n"
                "Control + Shift + K: Delete current line.\n"
                "F7: Verify syntax, quote matching, and delimiter balancing.\n"
                "Control + L: Announce current line and column of cursor.\n"
                "Control + 4: Focus Code Editor directly.\n"
                "Control + 5: Focus Output Console directly.\n"
                "Control + 6: Announce last line of output console.\n"
                "Control + Shift + C: Announce entire output console content.\n\n"
                "Debugging, Testing, and Environments:\n"
                "F9: Toggle breakpoint on current line.\n"
                "F10: Launch step-by-step interactive debugger.\n"
                "Control + T: Run automated unit tests (Accessible Test Runner).\n"
                "Control + Shift + P: Manage Python interpreters and virtual environments.\n\n"
                "File Operations and General:\n"
                "Control + O: Open Python script (.py) from disk.\n"
                "Control + S: Save current script to disk.\n"
                "Control + Shift + S: Save script as new file.\n"
                "F5: Run active script in editor.\n"
                "F11: Open this Keyboard Shortcuts Guide.\n"
                "F12: Open full documentation in web browser.\n"
                "Escape: Close window immediately from any control."
            )
            btn_close_label = "Close Guide"
            acc_name = "Complete list of keyboard shortcuts"
        else:
            texto_atajos = (
                "Guía Completa de Atajos de Teclado:\n\n"
                "Modos y Aprendizaje:\n"
                "Control + Enter: Ejecutar código y comprobar la solución del reto.\n"
                "Control + M: Alternar entre Modo Aprendizaje y Modo Solo Editor profesional.\n"
                "F3: Leer la instrucción activa sin mover el foco del editor.\n"
                "F4: Situar el cursor en la línea exacta del error del Traceback.\n"
                "F6: Alternar el foco entre el editor de código y la consola de resultados.\n"
                "Alt + Flecha Derecha: Ir al paso siguiente de la lección.\n"
                "Alt + Flecha Izquierda: Ir al paso anterior de la lección.\n"
                "Control + P: Pedir una pista escalonada de asistencia.\n"
                "F1: Explicar la línea actual con palabras sencillas y cotidianas.\n"
                "Shift + F1: Documentación rápida del símbolo bajo el cursor.\n"
                "Control + R: Restablecer el código inicial del ejercicio.\n"
                "Control + 1: Abrir el Selector de Capítulos del temario.\n"
                "Control + J: Abrir la consola de pruebas rápidas (REPL).\n\n"
                "Edición y Funciones de Desarrollo (IDE):\n"
                "Control + N: Crear un nuevo script limpio en el editor.\n"
                "Control + F: Buscar texto en el editor de código.\n"
                "Control + G: Desplazarse a un número de línea específico.\n"
                "F2: Renombrar identificador o variable en todo el archivo.\n"
                "Shift + Alt + F: Formatear documento según el estándar PEP 8.\n"
                "Control + Shift + I: Consultar al Asistente pedagógico de IA (Google Gemini).\n"
                "Control + Shift + R: Extraer bloque de código seleccionado a una nueva función.\n"
                "Control + Espacio: Autocompletado inteligente con documentación.\n"
                "Control + Shift + O: Lista accesible de funciones y clases del script.\n"
                "Alt + N: Salto rápido a la cabecera de la siguiente función o clase.\n"
                "Alt + P: Salto rápido a la cabecera de la función o clase anterior.\n"
                "Control + /: Comentar o descomentar la línea actual con '# '.\n"
                "Control + D: Duplicar la línea actual hacia abajo.\n"
                "Control + Shift + K: Eliminar la línea actual.\n"
                "F7: Verificar sintaxis, comillas y balanceo de delimitadores.\n"
                "Control + L: Anunciar la línea y columna actual del cursor.\n"
                "Control + 4: Llevar el foco directamente al Editor de código.\n"
                "Control + 5: Llevar el foco directamente a la Consola de resultados.\n"
                "Control + 6: Leer por voz la última línea de la consola.\n"
                "Control + Shift + C: Leer por voz todo el contenido de la consola.\n\n"
                "Depuración, Pruebas y Entornos:\n"
                "F9: Alternar punto de interrupción (breakpoint) en la línea actual.\n"
                "F10: Iniciar depurador interactivo paso a paso.\n"
                "Control + T: Ejecutar pruebas unitarias (Test Runner accesible).\n"
                "Control + Shift + P: Gestor de intérpretes de Python y entornos virtuales.\n\n"
                "Archivos, Ayuda y Documentación:\n"
                "Control + O: Abrir script de Python (.py) desde disco.\n"
                "Control + S: Guardar script actual en disco.\n"
                "Control + Shift + S: Guardar script con un nuevo nombre o ubicación.\n"
                "F5: Ejecutar script activo en el editor.\n"
                "F11: Abrir esta Guía de Atajos de Teclado.\n"
                "F12: Abrir la documentación de Acerca de en el navegador web.\n"
                "Escape: Cerrar la ventana del tutor inmediatamente desde cualquier control."
            )
            btn_close_label = "Cerrar Guía"
            acc_name = "Lista completa de atajos de teclado"

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(texto_atajos)
        txt.SetName(acc_name)
        vbox.Add(txt, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        btn_cerrar = wx.Button(panel, wx.ID_OK, label=btn_close_label)
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
        is_en = (obtener_idioma_actual() == "en")
        title = "Python Technical Glossary" if is_en else "Diccionario de Términos de Python"
        super(GlossaryDialog, self).__init__(parent, title=title, size=(720, 520))
        self.glosario = obtener_glosario(obtener_idioma_actual())
        self.terminos = sorted(list(self.glosario.keys()))
        self.filtrados = list(self.terminos)

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        search_box = wx.BoxSizer(wx.HORIZONTAL)
        lbl_text = "Search concept or keyword:" if is_en else "Buscar término:"
        lbl = wx.StaticText(panel, label=lbl_text)
        search_box.Add(lbl, flag=wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border=8)
        self.search_ctrl = wx.TextCtrl(panel)
        s_acc = "Type a Python keyword, function, or concept to search." if is_en else "Escribe aquí el comando o concepto para buscar."
        self.search_ctrl.SetName(s_acc)
        search_box.Add(self.search_ctrl, proportion=1, flag=wx.EXPAND)
        main_sizer.Add(search_box, flag=wx.EXPAND | wx.ALL, border=10)

        content_box = wx.BoxSizer(wx.HORIZONTAL)
        self.list_box = wx.ListBox(panel, choices=self.terminos)
        self.list_box.SetName("Available terms." if is_en else "Términos disponibles.")
        content_box.Add(self.list_box, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=10)

        self.def_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.def_ctrl.SetName("Definition." if is_en else "Significado del término.")
        content_box.Add(self.def_ctrl, proportion=2, flag=wx.EXPAND)
        main_sizer.Add(content_box, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        btn_close_lbl = "Close Glossary" if is_en else "Cerrar Diccionario"
        btn_cerrar = wx.Button(panel, wx.ID_CANCEL, label=btn_close_lbl)
        main_sizer.Add(btn_cerrar, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)

        panel.SetSizer(main_sizer)

        self.search_ctrl.Bind(wx.EVT_TEXT, self.on_search)
        self.list_box.Bind(wx.EVT_LISTBOX, self.on_select)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)

        if self.terminos:
            self.list_box.SetSelection(0)
            self.def_ctrl.SetValue(self.glosario[self.terminos[0]])

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
        is_en = (obtener_idioma_actual() == "en")
        if self.filtrados:
            self.list_box.SetSelection(0)
            self.def_ctrl.SetValue(self.glosario.get(self.filtrados[0], ""))
        else:
            not_found = "No matches found." if is_en else "No se encontraron coincidencias."
            self.def_ctrl.SetValue(not_found)

    def on_select(self, event):
        sel = self.list_box.GetStringSelection()
        if sel in self.glosario:
            self.def_ctrl.SetValue(self.glosario[sel])
            if ui:
                ui.message(sel)


class SymbolsDialog(wx.Dialog):
    """Diálogo accesible que enumera todas las funciones y clases del script para navegación directa."""
    def __init__(self, parent, code_text):
        super(SymbolsDialog, self).__init__(parent, title="Estructura del Código: Funciones y Clases", size=(680, 480))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.simbolos = []
        lineas = code_text.splitlines(True)
        pos_acum = 0
        for num_linea, linea in enumerate(lineas, start=1):
            m = re.match(r'^(?:[ \t]*)(def|class)\s+([a-zA-Z_0-9]+)', linea)
            if m:
                tipo = "Clase" if m.group(1) == "class" else "Función"
                nombre = m.group(2)
                self.simbolos.append((tipo, nombre, num_linea, pos_acum))
            pos_acum += len(linea)

        lbl = wx.StaticText(panel, label="Selecciona una función o clase para desplazar el cursor directamente a su cabecera:")
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        opciones = [f"[{tipo}] {nombre} (Línea {lin})" for tipo, nombre, lin, _ in self.simbolos]
        if not opciones:
            opciones = ["(No se encontraron funciones ni clases en el código actual)"]

        self.list_box = wx.ListBox(panel, choices=opciones)
        self.list_box.SetName("Lista de funciones y clases. Presione Enter para ir al elemento.")
        if self.simbolos:
            self.list_box.SetSelection(0)
        vbox.Add(self.list_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_ir = wx.Button(panel, wx.ID_OK, label="Ir al elemento")
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label="Cancelar")
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
        super(SupportDialog, self).__init__(parent, title="Soporte y Contacto", size=(640, 420))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        info = (
            "Soporte y Contacto con el Desarrollador:\n\n"
            "Autor y Desarrollador: Kevin Andrés Velasquez Vargas\n"
            "Correo electrónico de soporte: kevinvelasquezvargas@gmail.com\n"
            "Asunto recomendado: Soporte - Aprendizaje de Python con NVDA\n\n"
            "Puedes enviar consultas pedagógicas sobre los capítulos, dudas sobre la resolución "
            "de ejercicios, sugerencias de mejora o reportes de errores técnicos.\n\n"
            "Asimismo, puedes colaborar voluntariamente con el proyecto mediante donaciones para "
            "respaldar el mantenimiento continuo y la creación de nuevos contenidos formativos accesibles."
        )

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(info)
        txt.SetName("Información de soporte y contacto")
        vbox.Add(txt, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_mail = wx.Button(panel, label="Enviar correo de soporte")
        btn_donar = wx.Button(panel, label="Realizar donación (PayPal)")
        btn_cerrar = wx.Button(panel, wx.ID_CANCEL, label="Cerrar")

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
        url = "mailto:kevinvelasquezvargas@gmail.com?subject=Soporte%20-%20Aprendizaje%20de%20Python%20con%20NVDA"
        try:
            webbrowser.open(url)
            if ui:
                ui.message("Abriendo cliente de correo predeterminado...")
        except Exception:
            if ui:
                ui.message("Escribe a kevinvelasquezvargas@gmail.com")

    def on_donar(self, event=None):
        url = "https://www.paypal.me/kevinvelasquezvargas"
        try:
            webbrowser.open(url)
            if ui:
                ui.message("Abriendo página de donaciones...")
        except Exception:
            pass


class AboutDialog(wx.Dialog):
    """Diálogo accesible que presenta la documentación completa y estructurada del complemento."""
    def __init__(self, parent):
        is_en = (obtener_idioma_actual() == "en")
        title = "About Learning Python with NVDA" if is_en else "Acerca de Aprendizaje de Python con NVDA"
        super(AboutDialog, self).__init__(parent, title=title, size=(780, 620))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        if is_en:
            contenido = (
                "Learning Python with NVDA\n"
                "Version: 1.0.0\n"
                "Author: Kevin Andrés Velasquez Vargas\n"
                "Support Email: kevinvelasquezvargas@gmail.com\n"
                "License: GNU General Public License v3.0 (GPLv3)\n"
                "Compatibility: NVDA 2022.1 to 2026.2\n"
                "GitHub Repository: https://github.com/KevinVelasquezVargas/python_tutor\n"
                "Donations & Support: https://www.paypal.me/kevinvelasquezvargas\n\n"
                "======================================================================\n"
                "1. Overview and Mission\n"
                "======================================================================\n\n"
                "Learning Python with NVDA is a comprehensive, fully accessible educational platform and "
                "screen-reader-optimized Python code editor designed specifically for blind and visually impaired students.\n\n"
                "It features a structured 40-chapter curriculum spanning from fundamental computer science concepts "
                "(hardware architecture, binary logic, interpreters, NVDA navigation workflows) through intermediate "
                "data structures, object-oriented programming, and standard library modules (sqlite3, json, math, winsound).\n\n"
                "Dual-mode workflow:\n"
                "- Guided Learning Mode: Step-by-step conceptual walkthroughs, quizzes, and coding workshops.\n"
                "- Standalone Editor Mode: Distraction-free coding environment for independent software projects.\n\n"
                "======================================================================\n"
                "2. Pedagogical Progression (40 Chapters)\n"
                "======================================================================\n\n"
                "Module 0: Foundations of Computer Science (Chapters 1 to 5)\n"
                "Chapter 1: Computer Architecture: Binary System, CPU, and RAM\n"
                "Chapter 2: Compilers, Interpreters, and How Code Runs\n"
                "Chapter 3: History of Python, Philosophy, and the Zen of Python\n"
                "Chapter 4: Screen Readers and Accessible Programming with NVDA\n"
                "Chapter 5: Algorithmic Thinking and Debugging Psychology\n\n"
                "Module 1: Output, Memory, and Variables (Chapters 6 to 9)\n"
                "Chapter 6: First Contact: print() and Standard Output Streams\n"
                "Chapter 7: Variables and Dynamic Memory Allocation\n"
                "Chapter 8: Code Documentation: Comments and Clean Code Practices\n"
                "Chapter 9: Variable Reassignment and Memory States\n\n"
                "Module 2: Fundamental Data Types and Input (Chapters 10 to 14)\n"
                "Chapter 10: Numeric Types: Integers (int)\n"
                "Chapter 11: Floating-Point Numbers (float) and Precise Division\n"
                "Chapter 12: Text Strings (str) and Escape Sequences\n"
                "Chapter 13: String Formatting with Modern F-Strings\n"
                "Chapter 14: User Interaction: input() and Type Casting\n\n"
                "Module 3: Logical Operators and Branching (Chapters 15 to 19)\n"
                "Chapter 15: Boolean Type (bool) and Relational Operators\n"
                "Chapter 16: Logical Operators: and, or, not\n"
                "Chapter 17: Conditional Execution: if and Indentation Blocks\n"
                "Chapter 18: Alternative Execution: The else Clause\n"
                "Chapter 19: Multi-branch Decisions: elif Ladders\n\n"
                "Module 4: Loops and Iterations (Chapters 20 to 23)\n"
                "Chapter 20: Definite Loops: for and the range() Generator\n"
                "Chapter 21: Indefinite Loops: The while Statement\n"
                "Chapter 22: Infinite Loops and Timeout Protection\n"
                "Chapter 23: Loop Flow Control: break, continue, and else\n\n"
                "Module 5: Data Structures and Collections (Chapters 24 to 28)\n"
                "Chapter 24: Ordered Sequences: Introduction to Lists\n"
                "Chapter 25: List Modification: append, insert, remove, pop\n"
                "Chapter 26: List Traversal: Iteration and enumerate()\n"
                "Chapter 27: Immutable Sequences: Tuples (tuple)\n"
                "Chapter 28: Key-Value Mapping: Dictionaries (dict)\n\n"
                "Module 6: Functions, Scope, and Error Handling (Chapters 29 to 32)\n"
                "Chapter 29: Modular Code: Declaring Functions with def\n"
                "Chapter 30: Function Output: return vs print\n"
                "Chapter 31: Scope Rules: Local vs Global Variables\n"
                "Chapter 32: Exception Handling: try, except, finally\n\n"
                "Module 7: Persistence and Object-Oriented Programming (Chapters 33 to 36)\n"
                "Chapter 33: File Input/Output: with open() for Text Files\n"
                "Chapter 34: Structured Persistence: Serializing with JSON\n"
                "Chapter 35: Object-Oriented Programming: Classes and Instances\n"
                "Chapter 36: Methods and State: __init__ and self\n\n"
                "Module 8: Standard Library and Capstone Project (Chapters 37 to 40)\n"
                "Chapter 37: Standard Library Modules: math, random, datetime\n"
                "Chapter 38: Relational Databases: sqlite3 Foundations\n"
                "Chapter 39: Assistive Software Design: Audio and Accessible Feedback\n"
                "Chapter 40: Capstone Project: Accessible Information and Task Management Engine\n\n"
                "======================================================================\n"
                "3. Keyboard Shortcuts Reference\n"
                "======================================================================\n\n"
                "Control + Enter: Run code and verify challenge solution\n"
                "F5: Run active script in editor\n"
                "Control + M: Toggle between Guided Learning and Standalone Editor Mode\n"
                "Alt + Right Arrow: Next lesson step\n"
                "Alt + Left Arrow: Previous lesson step\n"
                "F1: Explain current line in plain language\n"
                "F2: Rename symbol across editor\n"
                "F3: Read active instruction aloud without moving editor cursor\n"
                "F4: Jump cursor directly to error line from Traceback\n"
                "F6: Switch focus between code editor and output console\n"
                "F7: Check syntax and delimiter balancing\n"
                "Control + P: Request hint for current challenge\n"
                "Control + 1: Open Chapter Selector (Syllabus)\n"
                "Control + J: Launch Python REPL test console\n"
                "Control + Shift + O: Accessible outline of functions and classes\n"
                "Control + Shift + E: Multi-file project explorer\n"
                "Control + Shift + I: Consult Google Gemini AI Assistant\n"
                "Control + F / Control + G: Find text / Go to line\n"
                "Control + N / O / S: New script / Open file / Save script\n"
                "F12: Open full documentation in web browser\n"
                "Escape: Close tutor or active dialog"
            )
        else:
            contenido = (
                "Aprendizaje de Python con NVDA\n"
                "Versión: 1.0.0\n"
                "Autor: Kevin Andrés Velasquez Vargas\n"
                "Correo de soporte: kevinvelasquezvargas@gmail.com\n"
                "Licencia: GNU General Public License v3.0 (GPLv3)\n"
                "Compatibilidad: NVDA 2022.1 hasta 2026.2\n"
                "Repositorio en GitHub: https://github.com/KevinVelasquezVargas/python_tutor\n"
                "Donaciones y apoyo voluntario: https://www.paypal.me/kevinvelasquezvargas\n\n"
                "======================================================================\n"
                "1. Visión General y Propósito del Complemento\n"
                "======================================================================\n\n"
                "Aprendizaje de Python con NVDA es un entorno formativo integral y un editor tiflotécnico "
                "de código adaptado para la programación accesible mediante NVDA. Proporciona una ruta de "
                "aprendizaje estructurada en 40 capítulos progresivos que abarcan desde conceptos computacionales "
                "básicos (arquitectura de ordenadores, binario, intérpretes y flujo tiflotécnico) hasta estructuras "
                "avanzadas, programación orientada a objetos, bases de datos SQLite y persistencia JSON.\n\n"
                "Doble modalidad de trabajo:\n"
                "- Modo Aprendizaje Guiado: Ciclo formativo con lectura conceptual, preguntas y talleres prácticos.\n"
                "- Modo Solo Editor: Espacio de trabajo libre y sin distracciones para el desarrollo autónomo.\n\n"
                "======================================================================\n"
                "2. Catálogo del Temario Pedagógico (40 Capítulos)\n"
                "======================================================================\n\n"
                "Módulo 0: Fundamentos y Pensamiento Computacional (Capítulos 1 a 5)\n"
                "Capítulo 1: Arquitectura del Ordenador: El Sistema Binario, la CPU y la Memoria RAM\n"
                "Capítulo 2: Compiladores e Intérpretes: Cómo se Ejecuta el Código\n"
                "Capítulo 3: Historia de Python, Filosofía y el Zen de Python\n"
                "Capítulo 4: Lectores de Pantalla y Programación Accesible con NVDA\n"
                "Capítulo 5: Pensamiento Algorítmico y Psicología de la Depuración\n\n"
                "Módulo 1: Salida, Memoria y Variables (Capítulos 6 a 9)\n"
                "Capítulo 6: Primer Contacto: La Función print() y los Flujos de Salida\n"
                "Capítulo 7: Almacenamiento en Memoria: Variables y Asignación\n"
                "Capítulo 8: Documentación del Código: Comentarios y Buenas Prácticas\n"
                "Capítulo 9: Reasignación de Variables y Estados de Memoria\n\n"
                "Módulo 2: Tipos de Datos Fundamentales y Entrada (Capítulos 10 a 14)\n"
                "Capítulo 10: Tipos Numéricos: Números Enteros (int)\n"
                "Capítulo 11: Números Decimales (float) y la Precisión en División\n"
                "Capítulo 12: Cadenas de Texto (str) y Secuencias de Escape\n"
                "Capítulo 13: Formateo Moderno de Cadenas con F-Strings\n"
                "Capítulo 14: Entrada de Datos con input() y Conversión de Tipos (Casting)\n\n"
                "Módulo 3: Lógica Proposicional y Control de Flujo (Capítulos 15 a 19)\n"
                "Capítulo 15: Tipo Booleano (bool) y Operadores Relacionales\n"
                "Capítulo 16: Conectores Lógicos: and, or y not\n"
                "Capítulo 17: Bifurcación Condicional: Sentencia if y Sangría de Bloque\n"
                "Capítulo 18: Caminos Alternativos: La Cláusula else\n"
                "Capítulo 19: Decisiones Múltiples: Estructura elif\n\n"
                "Módulo 4: Bucles e Iteraciones (Capítulos 20 a 23)\n"
                "Capítulo 20: Bucles Determinados: Bucle for y el Generador range()\n"
                "Capítulo 21: Bucles Indeterminados: Bucle while\n"
                "Capítulo 22: Bucles Infinitos y Protección por Tiempo de Espera (Timeout)\n"
                "Capítulo 23: Control de Bucles: break, continue y la Cláusula else\n\n"
                "Módulo 5: Estructuras de Datos y Colecciones (Capítulos 24 a 28)\n"
                "Capítulo 24: Listas en Python: Secuencias Mutables y Ordenadas\n"
                "Capítulo 25: Métodos de Listas: append, insert, remove y pop\n"
                "Capítulo 26: Recorrido de Listas: Iteración con for y enumerate()\n"
                "Capítulo 27: Tuplas (tuple): Inmutabilidad y Protección de Datos\n"
                "Capítulo 28: Diccionarios (dict): Pares Clave-Valor\n\n"
                "Módulo 6: Modularidad, Funciones y Manejo de Errores (Capítulos 29 a 32)\n"
                "Capítulo 29: Declaración de Funciones Propias con def y Parámetros\n"
                "Capítulo 30: Retorno de Datos: La Sentencia return frente a print()\n"
                "Capítulo 31: Ámbito de Variables: Variables Locales y Globales\n"
                "Capítulo 32: Manejo Profesional de Excepciones: try, except y finally\n\n"
                "Módulo 7: Persistencia y Programación Orientada a Objetos (Capítulos 33 a 36)\n"
                "Capítulo 33: Entrada/Salida de Archivos: with open() y Codificación UTF-8\n"
                "Capítulo 34: Persistencia Estructurada: Serialización con JSON\n"
                "Capítulo 35: Paradigma Orientado a Objetos: Clases e Instancias\n"
                "Capítulo 36: Métodos y Estado Interno: __init__ y el Parámetro self\n\n"
                "Módulo 8: Biblioteca Estándar y Proyecto Final (Capítulos 37 a 40)\n"
                "Capítulo 37: Módulos Nativos de la Biblioteca Estándar: math, random y datetime\n"
                "Capítulo 38: Bases de Datos Relacionales Embebidas: sqlite3 y Consultas Parametrizadas\n"
                "Capítulo 39: Tiflotecnología y Accesibilidad: Señales Acústicas y Retroalimentación por Voz\n"
                "Capítulo 40: Proyecto Integrador Final: Creación de un Gestor Accesible de Información y Tareas\n\n"
                "======================================================================\n"
                "3. Referencia Integral de Atajos de Teclado\n"
                "======================================================================\n\n"
                "Control + Enter: Ejecutar el código y comprobar la solución del reto.\n"
                "F5: Ejecutar el script activo en el editor.\n"
                "Control + M: Alternar entre Modo Aprendizaje y Modo Solo Editor profesional.\n"
                "Alt + Flecha Derecha: Ir al paso siguiente.\n"
                "Alt + Flecha Izquierda: Ir al paso anterior.\n"
                "F1: Explicar la línea donde está el cursor con palabras sencillas.\n"
                "F2: Renombrar símbolo en todo el script.\n"
                "F3: Leer la consigna activa sin mover el cursor del editor.\n"
                "F4: Situar el cursor directamente en la línea del error del Traceback.\n"
                "F6: Alternar el foco entre el editor de código y la consola.\n"
                "F7: Verificar sintaxis y balanceo de delimitadores/comillas.\n"
                "Control + P: Pedir una pista de asistencia.\n"
                "Control + 1: Selector de capítulos del temario.\n"
                "Control + J: Abrir la consola de pruebas rápidas (REPL).\n"
                "Control + Shift + O: Lista accesible de funciones y clases del script.\n"
                "Control + Shift + E: Explorador de proyectos multi-archivo.\n"
                "Control + Shift + I: Consultar al Asistente de IA (Google Gemini).\n"
                "Control + F / Control + G: Buscar texto / Ir a número de línea.\n"
                "Control + N / O / S: Nuevo script / Abrir archivo / Guardar script.\n"
                "F12: Abrir la documentación completa en el navegador web.\n"
                "Escape: Cerrar el tutor en cualquier momento."
            )

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(contenido)
        txt_acc = "Learning Python with NVDA Documentation" if is_en else "Documentación de Aprendizaje de Python con NVDA"
        txt.SetName(txt_acc)
        vbox.Add(txt, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        btn_lbl = "Close" if is_en else "Cerrar"
        btn_cerrar = wx.Button(panel, wx.ID_OK, label=btn_lbl)
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
        frame_title = "Learning Python with NVDA" if obtener_idioma_actual() == "en" else "Aprendizaje de Python con NVDA"
        super(TutorFrame, self).__init__(parent, title=frame_title, size=(980, 840))

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
        self.mision_ctrl.SetName("Instrucción del paso activo.")
        self.vbox.Add(self.mision_ctrl, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # Panel accesible de Pregunta de Opción Múltiple (Quiz)
        self.quiz_panel = wx.Panel(self.panel, style=wx.TAB_TRAVERSAL)
        self.quiz_vbox = wx.BoxSizer(wx.VERTICAL)
        self.lbl_quiz_pregunta = wx.StaticText(self.quiz_panel, label="")
        font_quiz = self.lbl_quiz_pregunta.GetFont()
        font_quiz.SetWeight(wx.FONTWEIGHT_BOLD)
        self.lbl_quiz_pregunta.SetFont(font_quiz)
        self.quiz_vbox.Add(self.lbl_quiz_pregunta, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=8)

        self.quiz_list = wx.ListBox(self.quiz_panel, style=wx.LB_SINGLE)
        self.quiz_list.SetName("Opciones de respuesta del quiz")
        self.quiz_vbox.Add(self.quiz_list, proportion=1, flag=wx.EXPAND | wx.ALL, border=8)

        self.hbox_quiz_btns = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_comprobar_quiz = wx.Button(self.quiz_panel, label="Comprobar respuesta (Enter)")
        self.btn_comprobar_quiz.SetName("Botón Comprobar Respuesta")
        self.hbox_quiz_btns.Add(self.btn_comprobar_quiz, flag=wx.RIGHT, border=8)

        self.lbl_quiz_feedback = wx.StaticText(self.quiz_panel, label="")
        self.hbox_quiz_btns.Add(self.lbl_quiz_feedback, flag=wx.ALIGN_CENTER_VERTICAL)
        self.quiz_vbox.Add(self.hbox_quiz_btns, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM, border=8)

        self.quiz_panel.SetSizer(self.quiz_vbox)
        self.vbox.Add(self.quiz_panel, proportion=3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)
        self.quiz_panel.Hide()

        # 3. Editor de código
        self.lbl_ed = wx.StaticText(self.panel, label="Editor de código:")
        self.vbox.Add(self.lbl_ed, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.edicion = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_PROCESS_TAB)
        self.edicion.SetName("Editor de código")
        self.vbox.Add(self.edicion, proportion=3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # 4. Consola de resultados
        self.lbl_sal = wx.StaticText(self.panel, label="Consola de resultados y diagnóstico:")
        self.vbox.Add(self.lbl_sal, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.salida = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.salida.SetName("Consola de resultados.")
        self.vbox.Add(self.salida, proportion=2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # 5. Barra de botones
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_continuar_concepto = wx.Button(self.panel, label="Continuar al siguiente paso (Enter)")
        self.btn_continuar_concepto.SetName("Botón Continuar al Siguiente Paso")
        self.btn_continuar_concepto.Hide()

        self.btn_ejecutar = wx.Button(self.panel, label="Ejecutar (F5 o Ctrl+Enter)")
        self.btn_ejecutar.SetName("Botón Ejecutar Código")

        self.btn_pista = wx.Button(self.panel, label="Pedir pista (Ctrl+P)")
        self.btn_pista.SetName("Botón Pedir Pista")

        self.btn_traductor = wx.Button(self.panel, label="Explicar línea (F1)")
        self.btn_traductor.SetName("Botón Explicar Línea")

        self.btn_anterior = wx.Button(self.panel, label="Paso anterior (Alt+Izquierda)")
        self.btn_anterior.SetName("Botón Paso Anterior")

        self.btn_siguiente = wx.Button(self.panel, label="Paso siguiente (Alt+Derecha)")
        self.btn_siguiente.SetName("Botón Paso Siguiente")

        self.btn_temario = wx.Button(self.panel, label="Temario (Ctrl+1)")
        self.btn_temario.SetName("Botón Selector de Capítulos")

        self.btn_cerrar = wx.Button(self.panel, wx.ID_CANCEL, label="Cerrar (Escape)")
        self.btn_cerrar.SetName("Botón Cerrar")

        self.hbox.Add(self.btn_continuar_concepto, flag=wx.RIGHT, border=6)
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
        self.btn_continuar_concepto.Bind(wx.EVT_BUTTON, self.on_paso_siguiente)
        self.btn_comprobar_quiz.Bind(wx.EVT_BUTTON, self.on_comprobar_quiz)
        self.quiz_list.Bind(wx.EVT_LISTBOX_DCLICK, self.on_comprobar_quiz)
        self.quiz_list.Bind(wx.EVT_KEY_DOWN, self.on_key_down_quiz)
        self.mision_ctrl.Bind(wx.EVT_KEY_DOWN, self.on_key_down_mision)
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

        # Aplicar textos e idioma
        self.actualizar_textos_interfaz()

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
        res = dlg.ShowModal()
        if res == wx.ID_OK:
            dlg.guardar_preferencia()
            dlg.Destroy()
            don_dlg = DonationPromptDialog(self)
            don_dlg.ShowModal()
            don_dlg.Destroy()
            self.dar_foco_adecuado()
        else:
            dlg.Destroy()
            self.Close()

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

    def actualizar_textos_interfaz(self):
        """Actualiza los títulos y botones de la ventana principal según el idioma activo."""
        is_en = (obtener_idioma_actual() == "en")
        title = "Learning Python with NVDA" if is_en else "Aprendizaje de Python con NVDA"
        self.SetTitle(title)

        if self.modo_editor:
            self.lbl_ed.SetLabel("Python Code Editor (Standalone Mode):" if is_en else "Editor de código (Modo autónomo):")
        else:
            self.lbl_ed.SetLabel("Python Code Editor:" if is_en else "Editor de código:")

        self.lbl_sal.SetLabel("Output Console and Diagnostics:" if is_en else "Consola de resultados y diagnóstico:")

        self.btn_ejecutar.SetLabel("Run (F5 or Ctrl+Enter)" if is_en else "Ejecutar (F5 o Ctrl+Enter)")
        self.btn_pista.SetLabel("Hint (Ctrl+P)" if is_en else "Pedir pista (Ctrl+P)")
        self.btn_traductor.SetLabel("Explain Line (F1)" if is_en else "Explicar línea (F1)")
        self.btn_anterior.SetLabel("Previous Step (Alt+Left)" if is_en else "Paso anterior (Alt+Izquierda)")
        self.btn_siguiente.SetLabel("Next Step (Alt+Right)" if is_en else "Paso siguiente (Alt+Derecha)")
        self.btn_temario.SetLabel("Syllabus (Ctrl+1)" if is_en else "Temario (Ctrl+1)")
        self.btn_cerrar.SetLabel("Close (Escape)" if is_en else "Cerrar (Escape)")

        if hasattr(self, 'btn_continuar_concepto'):
            self.btn_continuar_concepto.SetLabel("Continue to Next Step (Enter)" if is_en else "Continuar al siguiente paso (Enter)")
        if hasattr(self, 'btn_comprobar_quiz'):
            self.btn_comprobar_quiz.SetLabel("Check Answer (Enter)" if is_en else "Comprobar respuesta (Enter)")
        if hasattr(self, 'quiz_list'):
            self.quiz_list.SetName("Quiz answer options" if is_en else "Opciones de respuesta del quiz")

    def crear_barra_menus(self):
        is_en = (obtener_idioma_actual() == "en")
        menu_bar = wx.MenuBar()

        # 1. Menú Archivo / File
        m_archivo = wx.Menu()
        item_nuevo = m_archivo.Append(
            wx.ID_ANY,
            "New Script\tCtrl+N" if is_en else "Nuevo script\tCtrl+N",
            "Starts a fresh, clean script in the editor" if is_en else "Inicia un nuevo script limpio en el editor"
        )
        item_abrir = m_archivo.Append(
            wx.ID_ANY,
            "Open File...\tCtrl+O" if is_en else "Abrir archivo...\tCtrl+O",
            "Loads a Python script from disk" if is_en else "Carga un script de Python desde el disco"
        )
        item_guardar = m_archivo.Append(
            wx.ID_ANY,
            "Save Script\tCtrl+S" if is_en else "Guardar script\tCtrl+S",
            "Saves current editor content to file" if is_en else "Guarda el contenido del editor en el archivo"
        )
        item_guardar_como = m_archivo.Append(
            wx.ID_ANY,
            "Save As...\tCtrl+Shift+S" if is_en else "Guardar como...\tCtrl+Shift+S",
            "Saves code with a new name or location" if is_en else "Guarda el código con un nuevo nombre o ubicación"
        )
        m_archivo.AppendSeparator()
        item_salir = m_archivo.Append(
            wx.ID_EXIT,
            "Close Tutor\tAlt+F4" if is_en else "Cerrar tutor\tAlt+F4",
            "Exits the learning environment" if is_en else "Cierra el entorno de aprendizaje"
        )

        self.Bind(wx.EVT_MENU, self.on_nuevo_archivo, id=item_nuevo.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_archivo, id=item_abrir.GetId())
        self.Bind(wx.EVT_MENU, self.on_guardar_archivo, id=item_guardar.GetId())
        self.Bind(wx.EVT_MENU, self.on_guardar_como, id=item_guardar_como.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.Close(), id=item_salir.GetId())

        # 2. Menú Edición / Edit
        m_edicion = wx.Menu()
        item_deshacer = m_edicion.Append(wx.ID_UNDO, "Undo\tCtrl+Z" if is_en else "Deshacer\tCtrl+Z", "Reverts last edit" if is_en else "Revierte la última acción de edición")
        item_rehacer = m_edicion.Append(wx.ID_REDO, "Redo\tCtrl+Y" if is_en else "Rehacer\tCtrl+Y", "Reapplies undone action" if is_en else "Reaplica la acción deshecha")
        m_edicion.AppendSeparator()
        item_cortar = m_edicion.Append(wx.ID_CUT, "Cut\tCtrl+X" if is_en else "Cortar\tCtrl+X", "Cuts selection to clipboard" if is_en else "Corta el texto seleccionado al portapapeles")
        item_copiar = m_edicion.Append(wx.ID_COPY, "Copy\tCtrl+C" if is_en else "Copiar\tCtrl+C", "Copies selection to clipboard" if is_en else "Copia el texto seleccionado al portapapeles")
        item_pegar = m_edicion.Append(wx.ID_PASTE, "Paste\tCtrl+V" if is_en else "Pegar\tCtrl+V", "Pastes clipboard content" if is_en else "Pega el contenido del portapapeles")
        item_sel_todo = m_edicion.Append(wx.ID_SELECTALL, "Select All\tCtrl+A" if is_en else "Seleccionar todo\tCtrl+A", "Selects all text in editor" if is_en else "Selecciona todo el texto del editor")
        m_edicion.AppendSeparator()
        item_buscar = m_edicion.Append(wx.ID_ANY, "Find Text...\tCtrl+F" if is_en else "Buscar texto...\tCtrl+F", "Searches for words or code snippets" if is_en else "Busca palabras o fragmentos de código")
        item_ir_linea = m_edicion.Append(wx.ID_ANY, "Go to Line...\tCtrl+G" if is_en else "Ir a línea...\tCtrl+G", "Moves cursor to specified line number" if is_en else "Desplaza el cursor al número de línea indicado")
        m_edicion.AppendSeparator()
        item_pep8 = m_edicion.Append(wx.ID_ANY, "Format Document (PEP 8)\tShift+Alt+F" if is_en else "Formatear documento según PEP 8\tShift+Alt+F", "Adjusts indentation to 4 spaces and operator spacing" if is_en else "Ajusta la sangría a 4 espacios y los espacios de operadores")
        item_renombrar = m_edicion.Append(wx.ID_ANY, "Rename Symbol...\tF2" if is_en else "Renombrar símbolo...\tF2", "Renames selected variable or function across script" if is_en else "Renombra la variable o función seleccionada en todo el script")
        item_extraer = m_edicion.Append(wx.ID_ANY, "Extract Function...\tCtrl+Shift+R" if is_en else "Extraer a función...\tCtrl+Shift+R", "Converts selected block into a new function" if is_en else "Convierte el bloque seleccionado en una nueva función")
        m_edicion.AppendSeparator()
        item_simbolos = m_edicion.Append(wx.ID_ANY, "Functions & Classes List...\tCtrl+Shift+O" if is_en else "Lista de funciones y clases...\tCtrl+Shift+O", "Opens list of all functions and classes in script" if is_en else "Abre la lista de funciones y clases del archivo")
        item_sig_def = m_edicion.Append(wx.ID_ANY, "Go to Next Function or Class\tAlt+N" if is_en else "Ir a siguiente función o clase\tAlt+N", "Jumps to header of next function or class" if is_en else "Salta a la cabecera de la siguiente función o clase")
        item_ant_def = m_edicion.Append(wx.ID_ANY, "Go to Previous Function or Class\tAlt+P" if is_en else "Ir a anterior función o clase\tAlt+P", "Jumps to header of previous function or class" if is_en else "Salta a la cabecera de la función o clase anterior")
        m_edicion.AppendSeparator()
        item_comentar = m_edicion.Append(wx.ID_ANY, "Toggle Line Comment\tCtrl+/" if is_en else "Comentar o descomentar línea\tCtrl+/", "Toggles '#' at beginning of line" if is_en else "Alterna el comentario '#' al inicio de la línea")
        item_duplicar = m_edicion.Append(wx.ID_ANY, "Duplicate Line Down\tCtrl+D" if is_en else "Duplicar línea abajo\tCtrl+D", "Duplicates current line below" if is_en else "Duplica la línea actual en la siguiente")
        item_eliminar = m_edicion.Append(wx.ID_ANY, "Delete Line\tCtrl+Shift+K" if is_en else "Eliminar línea actual\tCtrl+Shift+K", "Deletes entire line where cursor is located" if is_en else "Elimina por completo la línea donde está el cursor")
        m_edicion.AppendSeparator()
        item_verificar = m_edicion.Append(wx.ID_ANY, "Verify Syntax & Delimiters\tF7" if is_en else "Verificar sintaxis y delimitadores\tF7", "Checks brackets, quotes, and syntax errors" if is_en else "Comprueba paréntesis, comillas y errores de sintaxis")
        item_posicion = m_edicion.Append(wx.ID_ANY, "Announce Position (Line & Column)\tCtrl+L" if is_en else "Anunciar posición (Línea y columna)\tCtrl+L", "Speaks current line and column of cursor" if is_en else "Informa en qué línea y columna se encuentra el cursor")

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

        # 3. Menú Herramientas / Tools
        m_herramientas = wx.Menu()
        item_alternar = m_herramientas.Append(
            wx.ID_ANY,
            "Toggle Focus between Editor and Console\tF6" if is_en else "Alternar foco entre editor y consola\tF6",
            "Switches keyboard focus between code editor and output" if is_en else "Cambia el foco entre el editor de código y la salida"
        )
        item_modo = m_herramientas.Append(
            wx.ID_ANY,
            "Toggle Learning Mode / Standalone Editor\tCtrl+M" if is_en else "Alternar Modo Aprendizaje / Editor autónomo\tCtrl+M",
            "Switches between pedagogical tutor and clean code editor" if is_en else "Conmuta entre el entorno didáctico y el editor limpio"
        )
        item_autocompletar = m_herramientas.Append(
            wx.ID_ANY,
            "Autocomplete with Documentation\tCtrl+Space" if is_en else "Autocompletado con documentación\tCtrl+Space",
            "Shows intelligent code suggestions with descriptions" if is_en else "Muestra sugerencias de código con su descripción"
        )
        item_ai_config = m_herramientas.Append(
            wx.ID_ANY,
            "Educational Assistant Settings..." if is_en else "Configuración del Asistente pedagógico...",
            "Configure educational AI assistant options" if is_en else "Configura las opciones del asistente pedagógico"
        )
        item_repl = m_herramientas.Append(
            wx.ID_ANY,
            "Interactive Python REPL\tCtrl+J" if is_en else "Consola interactiva de pruebas (REPL)\tCtrl+J",
            "Quick single-line Python experimentation console" if is_en else "Ventana de pruebas inmediatas de una línea"
        )
        item_ai_consult = m_herramientas.Append(
            wx.ID_ANY,
            "Ask Educational Assistant...\tCtrl+Shift+I" if is_en else "Consultar al Asistente pedagógico...\tCtrl+Shift+I",
            "Ask pedagogical assistant about code or concepts" if is_en else "Consulta dudas sobre el código o conceptos pedagógicos"
        )
        item_depurar = m_herramientas.Append(
            wx.ID_ANY,
            "Step-by-Step Interactive Debugger...\tF10" if is_en else "Depuración interactiva paso a paso...\tF10",
            "Runs script step-by-step inspecting variables" if is_en else "Ejecuta el script inspeccionando cada línea y sus variables"
        )
        item_glosario = m_herramientas.Append(
            wx.ID_ANY,
            "Python Technical Glossary" if is_en else "Diccionario de términos de Python",
            "Searchable dictionary of programming terms and concepts" if is_en else "Buscador de términos y conceptos del lenguaje"
        )
        item_doc_rapida = m_herramientas.Append(
            wx.ID_ANY,
            "Quick Symbol Documentation\tShift+F1" if is_en else "Documentación rápida del símbolo\tShift+F1",
            "Speaks documentation for function or keyword under cursor" if is_en else "Lee la explicación de la función o palabra bajo el cursor"
        )
        item_ejecutar = m_herramientas.Append(
            wx.ID_ANY,
            "Run Code & Verify\tF5" if is_en else "Ejecutar código y verificar\tF5",
            "Executes script or validates current mission (F5 or Ctrl+Enter)" if is_en else "Ejecuta el script o valida la misión actual (F5 o Ctrl+Enter)"
        )
        item_pruebas = m_herramientas.Append(
            wx.ID_ANY,
            "Run Unit Tests (Test Runner)...\tCtrl+T" if is_en else "Ejecutar pruebas unitarias (Test Runner)...\tCtrl+T",
            "Runs script unittests with accessible reporting" if is_en else "Ejecuta las pruebas unittest del script con reporte accesible"
        )
        item_traductor = m_herramientas.Append(
            wx.ID_ANY,
            "Explain Code Line\tF1" if is_en else "Explicar línea de código\tF1",
            "Explains current code line in plain natural language (offline)" if is_en else "Traduce la línea de código actual a palabras cotidianas"
        )
        item_proyectos = m_herramientas.Append(
            wx.ID_ANY,
            "Project Explorer...\tCtrl+Shift+E" if is_en else "Explorador de proyectos...\tCtrl+Shift+E",
            "Manage, create and navigate between project modules" if is_en else "Gestiona, crea y navega entre los módulos del proyecto"
        )
        item_interprete = m_herramientas.Append(
            wx.ID_ANY,
            "Manage Interpreters & Virtualenvs...\tCtrl+Shift+P" if is_en else "Gestor de intérpretes y entornos virtuales...\tCtrl+Shift+P",
            "Selects Python environment or active virtualenv" if is_en else "Selecciona el entorno de Python o virtualenv activo"
        )
        item_error = m_herramientas.Append(
            wx.ID_ANY,
            "Go to Traceback Error Line\tF4" if is_en else "Ir a la línea del error del Traceback\tF4",
            "Moves cursor directly to line where error occurred" if is_en else "Mueve el cursor exactamente a la línea del fallo"
        )
        item_leer_inst = m_herramientas.Append(
            wx.ID_ANY,
            "Read Active Step Instruction\tF3" if is_en else "Leer instrucción del paso activo\tF3",
            "Reads current mission without moving cursor away from editor" if is_en else "Lee la consigna actual sin retirar el cursor del editor"
        )
        item_leer_salida = m_herramientas.Append(
            wx.ID_ANY,
            "Read Full Console Output\tCtrl+Shift+C" if is_en else "Leer toda la salida de consola\tCtrl+Shift+C",
            "Speaks entire console output without leaving editor" if is_en else "Verbaliza todo el texto de la consola sin perder el foco"
        )
        item_breakpoint = m_herramientas.Append(
            wx.ID_ANY,
            "Toggle Breakpoint\tF9" if is_en else "Punto de interrupción (Breakpoint)\tF9",
            "Sets or clears a debug breakpoint on current line" if is_en else "Activa o desactiva un punto de parada en la línea actual"
        )
        item_reiniciar = m_herramientas.Append(
            wx.ID_ANY,
            "Reset Lesson Code\tCtrl+R" if is_en else "Restablecer código del ejercicio\tCtrl+R",
            "Restores original initial code of current step" if is_en else "Restaura el código original del paso"
        )
        item_temario = m_herramientas.Append(
            wx.ID_ANY,
            "Browse Chapter Syllabus...\tCtrl+1" if is_en else "Selector de capítulos del temario...\tCtrl+1",
            "View and select from complete list of chapters" if is_en else "Ver el listado completo de capítulos"
        )

        self.Bind(wx.EVT_MENU, self.on_alternar_foco, id=item_alternar.GetId())
        self.Bind(wx.EVT_MENU, self.on_alternar_modo_trabajo, id=item_modo.GetId())
        self.Bind(wx.EVT_MENU, self.on_autocompletar, id=item_autocompletar.GetId())
        self.Bind(wx.EVT_MENU, self.on_configurar_ia, id=item_ai_config.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_repl, id=item_repl.GetId())
        self.Bind(wx.EVT_MENU, self.on_consultar_ia, id=item_ai_consult.GetId())
        self.Bind(wx.EVT_MENU, self.on_depurar_paso_a_paso, id=item_depurar.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_glosario, id=item_glosario.GetId())
        self.Bind(wx.EVT_MENU, self.on_doc_rapida, id=item_doc_rapida.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.on_ejecutar(None), id=item_ejecutar.GetId())
        self.Bind(wx.EVT_MENU, self.on_ejecutar_pruebas, id=item_pruebas.GetId())
        self.Bind(wx.EVT_MENU, self.on_traducir_linea, id=item_traductor.GetId())
        self.Bind(wx.EVT_MENU, self.on_explorador_proyectos, id=item_proyectos.GetId())
        self.Bind(wx.EVT_MENU, self.on_gestor_interpretes, id=item_interprete.GetId())
        self.Bind(wx.EVT_MENU, self.on_ir_al_error, id=item_error.GetId())
        self.Bind(wx.EVT_MENU, self.on_leer_instruccion_actual, id=item_leer_inst.GetId())
        self.Bind(wx.EVT_MENU, self.on_leer_toda_la_salida, id=item_leer_salida.GetId())
        self.Bind(wx.EVT_MENU, self.on_toggle_breakpoint, id=item_breakpoint.GetId())
        self.Bind(wx.EVT_MENU, self.on_reiniciar_codigo, id=item_reiniciar.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_temario, id=item_temario.GetId())

        # 4. Menú Ayuda / Help
        m_ayuda = wx.Menu()
        item_acerca = m_ayuda.Append(
            wx.ID_ANY,
            "About Learning Python with NVDA...\tF12" if is_en else "Acerca de Aprendizaje de Python con NVDA...\tF12",
            "Complete accessible documentation and guide" if is_en else "Documentación accesible completa en el navegador"
        )
        item_donacion = m_ayuda.Append(
            wx.ID_ANY,
            "Support Project (Donate)..." if is_en else "Colaborar con el proyecto...",
            "Make a voluntary donation to support free development" if is_en else "Realizar una donación voluntaria para apoyar el complemento"
        )
        item_atajos = m_ayuda.Append(
            wx.ID_ANY,
            "Keyboard Shortcuts Guide\tF11" if is_en else "Guía de atajos de teclado\tF11",
            "Displays quick keyboard shortcuts reference" if is_en else "Muestra la lista de atajos rápidos"
        )
        item_soporte = m_ayuda.Append(
            wx.ID_ANY,
            "Support and Contact..." if is_en else "Soporte y contacto...",
            "Direct contact channels for email and assistance" if is_en else "Canales de contacto directo por correo y asistencia"
        )

        self.Bind(wx.EVT_MENU, self.on_acerca, id=item_acerca.GetId())
        self.Bind(wx.EVT_MENU, self.on_donacion, id=item_donacion.GetId())
        self.Bind(wx.EVT_MENU, self.on_mostrar_atajos, id=item_atajos.GetId())
        self.Bind(wx.EVT_MENU, self.on_soporte, id=item_soporte.GetId())

        menu_bar.Append(m_archivo, "&File" if is_en else "&Archivo")
        menu_bar.Append(m_edicion, "&Edit" if is_en else "&Edición")
        menu_bar.Append(m_herramientas, "&Tools" if is_en else "&Herramientas")
        menu_bar.Append(m_ayuda, "&Help" if is_en else "A&yuda")
        self.SetMenuBar(menu_bar)

    def aplicar_modo_trabajo(self, anunciar=False):
        """Aplica la configuración visual y de navegación según el modo de trabajo."""
        is_en = (obtener_idioma_actual() == "en")
        if self.modo_editor:
            self.lbl_estado.Hide()
            self.lbl_estado.Disable()
            self.vbox.Show(self.lbl_estado, False)

            self.mision_ctrl.Hide()
            self.mision_ctrl.Disable()
            self.vbox.Show(self.mision_ctrl, False)

            if hasattr(self, 'quiz_panel'):
                self.quiz_panel.Hide()
            if hasattr(self, 'btn_continuar_concepto'):
                self.btn_continuar_concepto.Hide()

            self.lbl_ed.Show()
            self.lbl_ed.Enable()
            self.edicion.Show()
            self.edicion.Enable()
            self.lbl_sal.Show()
            self.lbl_sal.Enable()
            self.salida.Show()
            self.salida.Enable()

            self.vbox.GetItem(self.edicion).SetProportion(3)
            self.vbox.GetItem(self.salida).SetProportion(2)

            self.btn_ejecutar.Show()
            self.btn_ejecutar.Enable()
            self.hbox.Show(self.btn_ejecutar, True)

            self.lbl_ed.SetLabel("Python Code Editor (Standalone Mode):" if is_en else "Editor de código (Modo autónomo):")

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

            app_title = "Learning Python with NVDA" if is_en else "Aprendizaje de Python con NVDA"
            self.SetTitle(app_title)
            self.panel.Layout()
            self.Layout()
            if anunciar:
                msg = "Standalone editor mode" if is_en else "Modo editor autónomo"
                self.anunciar(msg)
        else:
            self.lbl_estado.Enable()
            self.lbl_estado.Show()
            self.vbox.Show(self.lbl_estado, True)

            self.mision_ctrl.Enable()
            self.mision_ctrl.Show()
            self.vbox.Show(self.mision_ctrl, True)

            self.btn_anterior.Enable()
            self.btn_anterior.Show()
            self.hbox.Show(self.btn_anterior, True)

            self.btn_siguiente.Enable()
            self.btn_siguiente.Show()
            self.hbox.Show(self.btn_siguiente, True)

            self.btn_temario.Enable()
            self.btn_temario.Show()
            self.hbox.Show(self.btn_temario, True)

            self.lbl_ed.SetLabel("Python Code Editor:" if is_en else "Editor de código:")
            self.lbl_sal.SetLabel("Console Output & Diagnostics:" if is_en else "Consola de resultados y diagnóstico:")

            app_title = "Learning Python with NVDA" if is_en else "Aprendizaje de Python con NVDA"
            self.SetTitle(app_title)

            # Cargar paso actual para adaptar visibilidad específica del tipo de paso
            self.cargar_paso_actual(anunciar_voz=False)

            self.panel.Layout()
            self.Layout()
            if anunciar:
                msg = "Learning mode" if is_en else "Modo aprendizaje"
                self.anunciar(msg)

    def on_alternar_modo_trabajo(self, event=None):
        """Alterna entre el Modo Aprendizaje y el Modo Solo Editor (Ctrl+M)."""
        is_en = (obtener_idioma_actual() == "en")
        self.modo_editor = not self.modo_editor
        ProgressManager.set_editor_mode("editor" if self.modo_editor else "learning")

        if self.modo_editor:
            self._codigo_leccion = self.edicion.GetValue()
            self.edicion.SetValue(self._codigo_editor_usuario)
            if self.sonidos_activos:
                SoundManager.play('modo_editor')
        else:
            self._codigo_editor_usuario = self.edicion.GetValue()
            if self._codigo_leccion:
                self.edicion.SetValue(self._codigo_leccion)
            else:
                cap = CURRICULUM[self.cap_idx]
                paso = cap["pasos"][self.paso_idx]
                cod = paso.get("codigo_en" if is_en and "codigo_en" in paso else "codigo", "")
                self.edicion.SetValue(cod)
            if self.sonidos_activos:
                SoundManager.play('modo_aprendizaje')

        self.aplicar_modo_trabajo(anunciar=True)
        self.dar_foco_adecuado()

        try:
            pt = self.edicion.GetInsertionPoint()
            txt = self.edicion.GetValue()
            row = txt[:pt].count('\n')
            linea_txt = self.edicion.GetLineText(row)
            espacios = len(linea_txt) - len(linea_txt.lstrip(' '))
            self._last_linter_line = row
            self._last_linter_indent = 12 if espacios >= 12 else (8 if espacios >= 8 else (4 if espacios >= 4 else 0))
        except Exception:
            pass

    def dar_foco_adecuado(self):
        """Asigna el foco accesible al control correspondiente según el modo y tipo de paso."""
        if self.modo_editor:
            self.edicion.SetFocus()
            return
        if not (0 <= self.cap_idx < len(CURRICULUM)):
            self.edicion.SetFocus()
            return
        cap = CURRICULUM[self.cap_idx]
        pasos = cap.get("pasos", [])
        if not (0 <= self.paso_idx < len(pasos)):
            self.edicion.SetFocus()
            return
        paso = pasos[self.paso_idx]
        tipo = paso.get("tipo", "observar")
        if tipo in ("concepto", "lectura", "teoria"):
            self.mision_ctrl.SetFocus()
        elif tipo == "quiz":
            self.quiz_list.SetFocus()
        else:
            self.edicion.SetFocus()

    def cargar_paso_actual(self, anunciar_voz=True):
        """Carga el paso activo asegurando que no ocurran excepciones y adaptando la interfaz."""
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
        tipo = paso.get("tipo", "observar")
        self.nivel_pista = 0
        self._last_linter_line = -1
        self._last_linter_indent = -1
        self._quiz_superado = False

        if tipo in ("concepto", "lectura", "teoria"):
            ProgressManager.mark_step_completed(self.cap_idx, self.paso_idx)

        superado = ProgressManager.is_step_completed(self.cap_idx, self.paso_idx)
        self._quiz_superado = superado if tipo == "quiz" else False
        is_en = (obtener_idioma_actual() == "en")
        marca_estado = ("Passed" if superado else "Pending") if is_en else ("Superado" if superado else "Pendiente")

        titulo_paso = paso.get("titulo_en" if is_en and "titulo_en" in paso else "titulo", f"Step {self.paso_idx + 1}" if is_en else f"Paso {self.paso_idx + 1}")
        titulo_cap = cap.get("titulo_en" if is_en and "titulo_en" in cap else "titulo", "Chapter" if is_en else "Capítulo")

        texto_encabezado = (
            f"{titulo_cap}, Step {self.paso_idx + 1} of {total_pasos}: {titulo_paso}, {marca_estado}"
            if is_en else
            f"{titulo_cap}, Paso {self.paso_idx + 1} de {total_pasos}: {titulo_paso}, {marca_estado}"
        )
        self.lbl_estado.SetLabel(texto_encabezado)

        instruccion = paso.get("instruccion_en" if is_en and "instruccion_en" in paso else "instruccion", "")
        if not instruccion and tipo == "quiz":
            instruccion = paso.get("pregunta_en" if is_en and "pregunta_en" in paso else "pregunta", "")

        instruccion_limpia = instruccion.replace("\r\n", "\n")
        self.mision_ctrl.SetValue(instruccion_limpia)

        if not self.modo_editor:
            cod = paso.get("codigo_en" if is_en and "codigo_en" in paso else "codigo", "")
            self.edicion.SetValue(cod)
        self.salida.SetValue("")

        if not self.modo_editor:
            if tipo in ("concepto", "lectura", "teoria"):
                self.quiz_panel.Hide()
                self.lbl_ed.Hide()
                self.edicion.Hide()
                self.lbl_sal.Hide()
                self.salida.Hide()
                self.btn_ejecutar.Hide()
                self.btn_pista.Hide()
                self.btn_traductor.Hide()
                self.btn_continuar_concepto.Show()
                self.vbox.GetItem(self.mision_ctrl).SetProportion(1)
                self.panel.Layout()
                if anunciar_voz and ui:
                    msg_voz = f"{titulo_paso}. {instruccion_limpia}. {'Press Enter to continue.' if is_en else 'Presione Enter para continuar.'}"
                    ui.message(msg_voz)
                wx.CallAfter(self.dar_foco_adecuado)
                return

            elif tipo == "quiz":
                self.lbl_ed.Hide()
                self.edicion.Hide()
                self.lbl_sal.Hide()
                self.salida.Hide()
                self.btn_ejecutar.Hide()
                self.btn_pista.Hide()
                self.btn_traductor.Hide()
                self.btn_continuar_concepto.Hide()

                preg = paso.get("pregunta_en" if is_en and "pregunta_en" in paso else "pregunta", "")
                opciones = paso.get("opciones_en" if is_en and "opciones_en" in paso else "opciones", [])

                self.lbl_quiz_pregunta.SetLabel(preg)
                self.quiz_list.Clear()
                for i, op in enumerate(opciones):
                    self.quiz_list.Append(f"{i + 1}. {op}")
                if opciones:
                    self.quiz_list.SetSelection(0)

                if superado:
                    fb = "Passed: You previously answered this check correctly." if is_en else "Superado: Ya has respondido correctamente a esta pregunta."
                    self.lbl_quiz_feedback.SetLabel(fb)
                else:
                    self.lbl_quiz_feedback.SetLabel("")

                self.vbox.GetItem(self.mision_ctrl).SetProportion(0)
                self.vbox.GetItem(self.quiz_panel).SetProportion(1)
                self.quiz_panel.Show()
                self.panel.Layout()
                if anunciar_voz and ui:
                    ui.message(f"{titulo_paso}. {preg}")
                wx.CallAfter(self.dar_foco_adecuado)
                return

            else:
                self.quiz_panel.Hide()
                self.btn_continuar_concepto.Hide()
                self.lbl_ed.Show()
                self.edicion.Show()
                self.lbl_sal.Show()
                self.salida.Show()
                self.btn_ejecutar.Show()
                self.btn_pista.Show()
                self.btn_traductor.Show()
                self.vbox.GetItem(self.mision_ctrl).SetProportion(0)
                self.vbox.GetItem(self.edicion).SetProportion(3)
                self.vbox.GetItem(self.salida).SetProportion(2)
                self.panel.Layout()
                if anunciar_voz and ui:
                    ui.message(f"{titulo_paso}. {instruccion_limpia}")
                wx.CallAfter(self.dar_foco_adecuado)
                return

    def on_comprobar_quiz(self, event=None):
        """Comprueba la respuesta seleccionada en el cuestionario accesible."""
        if not (0 <= self.cap_idx < len(CURRICULUM)):
            return
        cap = CURRICULUM[self.cap_idx]
        paso = cap["pasos"][self.paso_idx]
        if paso.get("tipo") != "quiz":
            return

        is_en = (obtener_idioma_actual() == "en")
        sel = self.quiz_list.GetSelection()
        if sel == wx.NOT_FOUND:
            msg = "Please select an answer option from the list." if is_en else "Por favor seleccione una opción de la lista."
            self.anunciar(msg)
            return

        correcta = paso.get("correcta", 0)
        explicacion = paso.get("explicacion_en" if is_en and "explicacion_en" in paso else "explicacion", "")

        if sel == correcta:
            self._quiz_superado = True
            ProgressManager.mark_step_completed(self.cap_idx, self.paso_idx)
            if self.sonidos_activos:
                SoundManager.play('exito')

            fb_txt = f"{'Correct!' if is_en else '¡Correcto!'} {explicacion}"
            self.lbl_quiz_feedback.SetLabel(fb_txt)

            lbl_cur = self.lbl_estado.GetLabel()
            if "Pending" in lbl_cur:
                self.lbl_estado.SetLabel(lbl_cur.replace("Pending", "Passed"))
            elif "Pendiente" in lbl_cur:
                self.lbl_estado.SetLabel(lbl_cur.replace("Pendiente", "Superado"))

            anuncio = (
                f"Correct! {explicacion} Press Enter or Alt + Right Arrow to advance to the next step."
                if is_en else
                f"¡Correcto! {explicacion} Presiona Enter o Alt + Flecha Derecha para avanzar al siguiente paso."
            )
            self.anunciar(anuncio)
        else:
            if self.sonidos_activos:
                SoundManager.play('error')
            fb_txt = (
                "Incorrect answer. Review the concept and try selecting another option."
                if is_en else
                "Respuesta incorrecta. Revisa el concepto e inténtalo seleccionando otra opción."
            )
            self.lbl_quiz_feedback.SetLabel(fb_txt)
            self.anunciar(fb_txt)
            self.quiz_list.SetFocus()

    def on_key_down_quiz(self, event):
        """Maneja el teclado en la lista de opciones del quiz."""
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN:
            if getattr(self, '_quiz_superado', False):
                self.on_paso_siguiente()
            else:
                self.on_comprobar_quiz()
            return
        event.Skip()

    def on_key_down_mision(self, event):
        """Permite avanzar con Enter desde la instrucción en pasos conceptuales."""
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN:
            if not self.modo_editor and (0 <= self.cap_idx < len(CURRICULUM)):
                cap = CURRICULUM[self.cap_idx]
                paso = cap["pasos"][self.paso_idx]
                if paso.get("tipo") in ("concepto", "lectura", "teoria"):
                    self.on_paso_siguiente()
                    return
        event.Skip()

    def on_ejecutar(self, event=None):
        if not self.modo_editor and (0 <= self.cap_idx < len(CURRICULUM)):
            cap = CURRICULUM[self.cap_idx]
            paso = cap["pasos"][self.paso_idx]
            tipo = paso.get("tipo", "observar")
            if tipo == "quiz":
                self.on_comprobar_quiz()
                return
            elif tipo in ("concepto", "lectura", "teoria"):
                self.on_paso_siguiente()
                return

        src = self.edicion.GetValue()

        is_en = (obtener_idioma_actual() == "en")

        # 1. Comprobación temprana de balanceo de delimitadores
        bal_err = comprobar_balanceo_delimitadores(src)
        if bal_err:
            self.ultimo_error_linea = bal_err.get("linea")
            self.ultimo_error_msg = bal_err.get("mensaje")
            aviso_del = (
                f"Delimiter warning:\n{bal_err['mensaje']}\n\nPress F4 to place cursor on warning line."
                if is_en else
                f"Aviso de delimitadores:\n{bal_err['mensaje']}\n\nPresiona F4 para situar el cursor en la línea del aviso."
            )
            self.salida.SetValue(aviso_del)
            if self.sonidos_activos:
                SoundManager.play('sintaxis_aviso')
            anuncio_del = (
                f"Delimiter warning: {bal_err['mensaje']}. Press F4 to go to line."
                if is_en else
                f"Aviso de delimitadores: {bal_err['mensaje']}. Presiona F4 para ir a la línea."
            )
            self.anunciar(anuncio_del)
            return

        # 2. Comprobación de código vacío o solo comentarios
        lineas_codigo = [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
        if not lineas_codigo:
            if not self.modo_editor:
                cap = CURRICULUM[self.cap_idx]
                paso = cap["pasos"][self.paso_idx]
                tipo_paso = paso.get("tipo", "observar")
                if tipo_paso == "quiz":
                    msg = (
                        "No option selected. Type number 1, 2, or 3 into the editor and press Control + Enter or F5."
                        if is_en else
                        "No has indicado ninguna opción. Escribe el número 1, 2 o 3 en el editor y pulsa Control + Enter o F5."
                    )
                elif tipo_paso == "desafio":
                    msg = (
                        "The editor is empty or only contains comments. Write your solution code and press Control + Enter or F5."
                        if is_en else
                        "El editor está vacío o solo contiene comentarios. Escribe tu código para resolver el reto práctico y pulsa Control + Enter o F5."
                    )
                elif tipo_paso == "experimentar":
                    msg = (
                        "No executable code detected. Make the change requested in the instructions and press Control + Enter or F5."
                        if is_en else
                        "No se detecta código ejecutable. Realiza la modificación indicada en la consigna y pulsa Control + Enter o F5."
                    )
                else:
                    msg = "The editor does not contain code to execute." if is_en else "El editor no contiene código para ejecutar."
            else:
                msg = "The editor is empty. Write Python instructions before running." if is_en else "El editor está vacío. Escribe instrucciones de Python antes de ejecutar."

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
                salida_txt.append("Keyboard warning:" if is_en else "Aviso de escritura:")
                salida_txt.append(res.keyboard_warning)
                salida_txt.append("")

            salida_txt.append("Output:" if is_en else "Salida:")
            no_out = "(No console output)" if is_en else "(Sin salida de consola)"
            salida_txt.append(res.output if res.output else no_out)

            if not res.success:
                self.ultimo_error_linea = res.error_line
                self.ultimo_error_msg = res.error_msg
                if res.friendly_explanation:
                    salida_txt.append("")
                    salida_txt.append(f"{'Runtime diagnostic:' if is_en else 'Aviso de ejecución:'} {res.friendly_explanation}")
                    salida_txt.append("Press F4 to place cursor on error line." if is_en else "Presiona F4 para posicionar el cursor en la línea del fallo.")
                if self.sonidos_activos:
                    SoundManager.play('error')
                msg_err = res.friendly_explanation or res.error_msg or ("Error during execution" if is_en else "Error durante la ejecución")
                self.anunciar(f"{'Error:' if is_en else 'Error:'} {msg_err}. {'Press F4 to go to error.' if is_en else 'Pulse F4 para ir al error.'}")
            else:
                self.ultimo_error_linea = None
                self.ultimo_error_msg = None
                if self.sonidos_activos:
                    SoundManager.play('exito')
                self.anunciar("Execution completed successfully." if is_en else "Ejecución finalizada con éxito.")

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
                exp_txt = paso.get("explicacion_en" if is_en and "explicacion_en" in paso else "explicacion", "Correct answer." if is_en else "Respuesta correcta.")
                reporte_pruebas.append(f"{'Correct:' if is_en else 'Correcto:'} {exp_txt}")
            else:
                aprobado = False
                reporte_pruebas.append(
                    "Pending: The selected option is not correct. Review the options in the instructions and try again."
                    if is_en else
                    "Pendiente: La opción seleccionada no es la correcta. Revisa las opciones en la instrucción e inténtalo de nuevo."
                )

            res_output = f"{'Submitted option:' if is_en else 'Opción enviada:'} {digits[0] if digits else val_clean}"
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
                        p_nom = p.get("nombre_en" if is_en and "nombre_en" in p else "nombre", "Test" if is_en else "Prueba")
                        if ok:
                            reporte_pruebas.append(f"{'Passed:' if is_en else 'Correcto:'} {p_nom} {'passed' if is_en else 'superada'}")
                        else:
                            reporte_pruebas.append(f"{'Pending:' if is_en else 'Pendiente:'} {p_nom} {'not passed' if is_en else 'no superada'}")
                            todas_ok = False
                    aprobado = todas_ok
                elif "validar" in paso and callable(paso["validar"]):
                    try:
                        aprobado = bool(paso["validar"](src, res.output, res.local_ns))
                    except Exception:
                        aprobado = False
                    if not aprobado:
                        reporte_pruebas.append(
                            "Pending: The code executed without syntax errors, but the output does not yet meet the challenge criteria."
                            if is_en else
                            "Pendiente: El código se ejecutó sin errores de sintaxis, pero el resultado aún no cumple los requisitos específicos del reto."
                        )
                else:
                    aprobado = (tipo_paso == "observar")

        lineas_reporte = []
        if tipo_paso != "quiz" and getattr(res, 'keyboard_warning', None):
            lineas_reporte.append("Keyboard warning:" if is_en else "Aviso de escritura:")
            lineas_reporte.append(res.keyboard_warning)
            lineas_reporte.append("")

        lineas_reporte.append("Output:" if is_en else "Salida:")
        no_out = "(No console output)" if is_en else "(Sin salida de consola)"
        lineas_reporte.append(res_output if res_output else no_out)
        lineas_reporte.append("")

        if reporte_pruebas:
            lineas_reporte.append("Verification results:" if is_en else "Resultado de la comprobación:")
            lineas_reporte.extend(reporte_pruebas)
            lineas_reporte.append("")

        if aprobado:
            succ_msg = (
                "Challenge completed successfully! You can advance to the next step with Alt + Right Arrow."
                if is_en else
                "¡Misión superada con éxito! Puedes avanzar al siguiente paso con Alt + Flecha Derecha."
            )
            lineas_reporte.append(succ_msg)
            self.salida.SetValue("\n".join(lineas_reporte))
            wx.CallLater(100, self.salida.SetFocus)

            ProgressManager.mark_step_completed(self.cap_idx, self.paso_idx)

            if self.sonidos_activos:
                SoundManager.play('exito')
            anuncio_succ = "Challenge completed! Press Alt + Right Arrow to advance." if is_en else "¡Misión superada! Pulsa Alt + Flecha Derecha para avanzar."
            self.anunciar(anuncio_succ)
        else:
            if paso.get("salida_esperada"):
                comp = generar_comparacion_salida(paso["salida_esperada"], res_output)
                lineas_reporte.append("Comparison with expected output:" if is_en else "Comparación con la salida esperada:")
                lineas_reporte.append(comp)
                lineas_reporte.append("")

            if friendly_err:
                lineas_reporte.append(f"{'Runtime diagnostic:' if is_en else 'Aviso de ejecución:'} {friendly_err}")
                lineas_reporte.append("Press F4 to place cursor on error line." if is_en else "Pulsa F4 para posicionar el cursor en la línea del fallo.")
            elif tipo_paso != "quiz":
                lineas_reporte.append(
                    "The solution has not passed yet. Review the instructions or press Control + P for a hint."
                    if is_en else
                    "La solución no ha sido aprobada aún. Revisa la consigna o pulsa Control + P para solicitar una pista."
                )

            self.salida.SetValue("\n".join(lineas_reporte))
            wx.CallLater(100, self.salida.SetFocus)

            if self.sonidos_activos:
                SoundManager.play('error')
            if friendly_err:
                self.anunciar(f"{friendly_err}. {'Press F4 to go to error.' if is_en else 'Pulsa F4 para ir al error.'}")
            elif tipo_paso == "quiz":
                self.anunciar("Incorrect option. Review the question and try again." if is_en else "Opción incorrecta. Revisa la pregunta y vuelve a intentarlo.")
            else:
                self.anunciar("Solution not passed. Press Control + P for a hint." if is_en else "Solución no superada. Pulsa Control + P para recibir una pista.")

    def on_pista(self, event=None):
        is_en = (obtener_idioma_actual() == "en")
        cap = CURRICULUM[self.cap_idx]
        paso = cap["pasos"][self.paso_idx]
        def_hint = ["Review the lesson instructions above and try running the code again."] if is_en else ["Revisa el enunciado de la lección en la parte superior e intenta ejecutar nuevamente."]
        pistas = paso.get("pistas_en" if is_en and "pistas_en" in paso else "pistas", def_hint)

        if self.sonidos_activos:
            SoundManager.play('pista')

        dlg = HintDialog(self, pistas, self.nivel_pista)
        dlg.ShowModal()
        dlg.Destroy()

        if self.nivel_pista < len(pistas) - 1:
            self.nivel_pista += 1

    def on_traducir_linea(self, event=None):
        """Explica la línea de código actual con palabras cotidianas (100% local y privado por defecto)."""
        try:
            pt = self.edicion.GetInsertionPoint()
            txt = self.edicion.GetValue()
            row = txt[:pt].count('\n')
            linea = self.edicion.GetLineText(row)
        except Exception:
            linea = ""
            txt = ""

        f1_mode = ProgressManager.get_setting("f1_mode", "local")
        config_ia = obtener_config_ia()
        if f1_mode == "ai" and config_ia.get("activa") and config_ia.get("api_key"):
            self.on_consultar_ia()
            return

        traduccion = traducir_linea_codigo(linea, lang=obtener_idioma_actual())
        anunciar_braille(formatear_linea_para_braille(linea))
        self.anunciar(traduccion)

    def on_consultar_ia(self, event=None):
        """Abre el diálogo accesible del Asistente de IA (Ctrl+Shift+I)."""
        try:
            pt = self.edicion.GetInsertionPoint()
            txt = self.edicion.GetValue()
            row = txt[:pt].count('\n')
            linea = self.edicion.GetLineText(row)
        except Exception:
            linea = ""
            txt = ""

        error = getattr(self, "ultimo_error_msg", "") or ""
        dlg = AIConsultDialog(self, codigo_actual=txt, linea_actual=linea, error_reciente=error)
        dlg.ShowModal()
        dlg.Destroy()

    def on_configurar_ia(self, event=None):
        """Abre la configuración del Asistente de IA."""
        dlg = AIConfigDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def on_explorador_proyectos(self, event=None):
        """Abre el explorador de proyectos multi-archivo (Ctrl+Shift+E)."""
        dlg = ProjectManagerDialog(
            self,
            archivo_activo=self.archivo_abierto,
            on_abrir_archivo=self._cargar_archivo_directo
        )
        dlg.ShowModal()
        dlg.Destroy()

    def _cargar_archivo_directo(self, ruta):
        """Carga un archivo directamente desde el gestor de proyectos."""
        try:
            with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
                codigo = f.read()
            self.edicion.SetValue(codigo)
            self.archivo_abierto = ruta
            self.anunciar(f"Módulo cargado: {os.path.basename(ruta)}")
            self.edicion.SetFocus()
        except Exception as e:
            wx.MessageBox(f"Error al cargar el archivo: {e}", "Error", wx.ICON_ERROR, self)

    def on_cambiar_idioma(self, event=None):
        """Alterna el idioma del tutor entre Español e Inglés y actualiza la interfaz al instante."""
        actual = obtener_idioma_actual()
        nuevo = "en" if actual == "es" else "es"
        establecer_idioma(nuevo)
        nombre_idioma = "English" if nuevo == "en" else "Español"
        self.crear_barra_menus()
        self.actualizar_textos_interfaz()
        self.cargar_paso_actual(anunciar_voz=False)
        self.anunciar(f"Idioma cambiado a: {nombre_idioma}. Language switched to {nombre_idioma}.")

    # ========================================================================
    # Herramientas del Editor (Productividad estilo IDE)
    # ========================================================================
    def on_nuevo_archivo(self, event=None):
        """Crea un nuevo script en blanco tras confirmación si hay texto."""
        if self.edicion.GetValue().strip():
            res = wx.MessageBox(
                "¿Deseas iniciar un nuevo script en blanco? Se limpiará el texto actual del editor.",
                "Nuevo script",
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
        self.anunciar("Nuevo script iniciado.")

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
                msg = "Línea descomentada"
            else:
                lineas[row] = '# ' + linea
                msg = "Línea comentada"

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
            self.anunciar("Línea duplicada")
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

            self.anunciar("Línea eliminada")
        except Exception:
            pass

    def on_verificar_sintaxis(self, event=None):
        """Analiza la sintaxis y el balanceo de delimitadores del código sin ejecutarlo (F7)."""
        src = self.edicion.GetValue()

        bal_err = comprobar_balanceo_delimitadores(src)
        if bal_err:
            linea_err = bal_err.get("linea", 1)
            msg = f"Aviso de delimitador en línea {linea_err}: {bal_err['mensaje']}"
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
            msg = "Sintaxis y delimitadores correctos. No se detectaron errores de estructura en el código."
            if self.sonidos_activos:
                SoundManager.play('exito')
        except SyntaxError as e:
            linea_err = e.lineno or 1
            self.ultimo_error_linea = linea_err
            self.ultimo_error_msg = e.msg
            msg = f"Error de sintaxis en la línea {linea_err}: {e.msg}."
            if self.sonidos_activos:
                SoundManager.play('sintaxis_aviso')
            try:
                lineas = src.split('\n')
                pt = len('\n'.join(lineas[:linea_err - 1])) + 1 if linea_err > 1 else 0
                self.edicion.SetInsertionPoint(min(pt, len(src)))
            except Exception:
                pass
        except Exception as e:
            msg = f"Aviso de compilación: {e}."

        self.anunciar(msg)

    def on_ir_al_error(self, event=None):
        """Mueve el cursor exactamente a la línea del último error detectado (F4)."""
        if self.ultimo_error_linea is None:
            self.anunciar("No hay registro de errores recientes de ejecución o sintaxis.")
            return

        src = self.edicion.GetValue()
        lineas = src.split('\n')
        linea_num = max(1, min(self.ultimo_error_linea, len(lineas)))
        pt = len('\n'.join(lineas[:linea_num - 1])) + 1 if linea_num > 1 else 0
        self.edicion.SetInsertionPoint(min(pt, len(src)))
        self.edicion.SetFocus()

        detalle = self.ultimo_error_msg or "error detectado"
        msg = f"Cursor en línea {linea_num}: {detalle}"
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
                msg = f"Cursor en {tipo.lower()} {nombre}, línea {num_linea}"
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
            desc = "Clase" if tipo == "class" else "Función"
            msg = f"{desc} {nombre}, línea {num_linea}"
            self.anunciar(msg)
        else:
            self.anunciar("No hay más definiciones adelante.")

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
            desc = "Clase" if tipo == "class" else "Función"
            msg = f"{desc} {nombre}, línea {num_linea}"
            self.anunciar(msg)
        else:
            self.anunciar("No hay definiciones anteriores.")

    def on_leer_toda_la_salida(self, event=None):
        """Verbaliza por voz todo el contenido de la consola sin retirar el foco del editor (Ctrl+Shift+C)."""
        txt = self.salida.GetValue().strip()
        if not txt:
            self.anunciar("Consola vacía.")
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

        msg = f"Línea {row} de {total_lineas}, columna {col}."
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
                    ui.message(f"Sin sugerencias para '{prefijo}'.")
                return

            if len(coincidencias) == 1:
                eleccion = coincidencias[0]
                resto = eleccion[len(prefijo):]
                self.edicion.WriteText(resto)
                if speech and hasattr(speech, 'speakMessage'):
                    speech.speakMessage(f"Completado: {eleccion}")
                if ui:
                    ui.message(f"Completado: {eleccion}")
            else:
                dlg = AutoCompleteDialog(self, prefijo, coincidencias)
                if dlg.ShowModal() == wx.ID_OK and dlg.seleccion:
                    eleccion = dlg.seleccion
                    resto = eleccion[len(prefijo):]
                    self.edicion.WriteText(resto)
                    if speech and hasattr(speech, 'speakMessage'):
                        speech.speakMessage(f"Insertado: {eleccion}")
                    if ui:
                        ui.message(f"Insertado: {eleccion}")
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
                self.anunciar("Sitúa el cursor sobre una función o palabra para ver su documentación.")
                return

            doc = obtener_documentacion_simbolo(palabra)
            self.anunciar(doc)
        except Exception:
            pass

    def on_formatear_pep8(self, event=None):
        """Formatea el documento activo según el estándar PEP 8 (Shift+Alt+F)."""
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
            msg = f"Se renombraron {total} apariciones de {palabra} por {dlg.nuevo_nombre}."
            self.anunciar(msg)
        dlg.Destroy()
        self.edicion.SetFocus()

    def on_extraer_funcion(self, event=None):
        """Extrae el bloque seleccionado a una nueva función (Ctrl+Shift+R)."""
        sel = self.edicion.GetStringSelection()
        if not sel.strip():
            self.anunciar("Selecciona primero el bloque de código que deseas extraer a una función.")
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
            msg = f"Función '{nombre}' extraída correctamente."
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
            msg = f"Punto de interrupción eliminado en la línea {row}."
        else:
            self.breakpoints.add(row)
            msg = f"Punto de interrupción activado en la línea {row}."
            if self.sonidos_activos:
                SoundManager.play('bloque')

        self.anunciar(msg)

    def on_depurar_paso_a_paso(self, event=None):
        """Inicia el depurador interactivo paso a paso (F10)."""
        codigo = self.edicion.GetValue()
        if not codigo.strip():
            self.anunciar("El editor está vacío. Escribe código antes de iniciar la depuración.")
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
            self.dar_foco_adecuado()
        else:
            if self.cap_idx < len(CURRICULUM) - 1:
                if not ProgressManager.is_chapter_completed(self.cap_idx, total_pasos):
                    is_en = (obtener_idioma_actual() == "en")
                    msg = (
                        "To advance to the next chapter, you must complete all steps of the current chapter."
                        if is_en else
                        "Para avanzar al siguiente capítulo, debes completar todos los pasos del capítulo actual."
                    )
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
                self.dar_foco_adecuado()
            else:
                is_en = (obtener_idioma_actual() == "en")
                msg_done = (
                    "Congratulations! You have completed all chapters of the curriculum."
                    if is_en else
                    "¡Felicidades! Has completado todos los capítulos del temario."
                )
                if ui:
                    ui.message(msg_done)

    def on_paso_anterior(self, event=None):
        if self.paso_idx > 0:
            self.paso_idx -= 1
            if self.sonidos_activos:
                SoundManager.play('paso')
            self.cargar_paso_actual(anunciar_voz=True)
            self.dar_foco_adecuado()
        elif self.cap_idx > 0:
            self.cap_idx -= 1
            self.paso_idx = len(CURRICULUM[self.cap_idx]["pasos"]) - 1
            if self.sonidos_activos:
                SoundManager.play('paso')
            self.cargar_paso_actual(anunciar_voz=True)
            self.dar_foco_adecuado()

    def on_abrir_repl(self, event=None):
        dlg = ReplDialog(self)
        dlg.ShowModal()
        dlg.Destroy()
        self.dar_foco_adecuado()

    def on_abrir_glosario(self, event=None):
        dlg = GlossaryDialog(self)
        dlg.ShowModal()
        dlg.Destroy()
        self.dar_foco_adecuado()

    def on_abrir_temario(self, event=None):
        dlg = ChapterSelectDialog(self, self.cap_idx)
        if dlg.ShowModal() == wx.ID_OK:
            sel = dlg.get_selected_index()
            if sel != wx.NOT_FOUND:
                self.cap_idx = sel
                self.paso_idx = 0
                self.cargar_paso_actual(anunciar_voz=True)
                self.dar_foco_adecuado()
        dlg.Destroy()

    def on_reiniciar_codigo(self, event=None):
        cap = CURRICULUM[self.cap_idx]
        paso = cap["pasos"][self.paso_idx]
        is_en = (obtener_idioma_actual() == "en")
        cod = paso.get("codigo_en" if is_en and "codigo_en" in paso else "codigo", "")
        self.edicion.SetValue(cod)
        self.salida.SetValue("")
        self.edicion.SetFocus()
        msg = "Exercise starter code reset to initial state." if is_en else "Código del ejercicio restablecido a su estado inicial."
        self.anunciar(msg)

    def on_mostrar_atajos(self, event=None):
        dlg = ShortcutsDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def on_donacion(self, event=None):
        url = "https://www.paypal.me/kevinvelasquezvargas"
        try:
            webbrowser.open(url)
            if ui:
                ui.message("Abriendo página de donaciones en el navegador...")
        except Exception:
            wx.MessageBox(
                "Puedes realizar una contribución voluntaria para apoyar el proyecto en:\nhttps://www.paypal.me/kevinvelasquezvargas",
                "Realizar una Donación",
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
        keycode = event.GetKeyCode()
        if keycode in (wx.WXK_CONTROL, wx.WXK_SHIFT, wx.WXK_ALT, ord('M'), ord('m')):
            event.Skip()
            return
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
        is_ctrl = event.ControlDown() or bool(modifiers & wx.MOD_CONTROL)
        is_shift = event.ShiftDown() or bool(modifiers & wx.MOD_SHIFT)
        is_alt = event.AltDown() or bool(modifiers & wx.MOD_ALT)

        if is_alt and not is_ctrl:
            if is_shift and keycode in (ord('F'), ord('f')):
                self.on_formatear_pep8()
                return
            if not is_shift:
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

        if is_ctrl and is_shift and not is_alt:
            # Permitir selección de texto por bloques / palabras
            if keycode in (wx.WXK_LEFT, wx.WXK_RIGHT, wx.WXK_UP, wx.WXK_DOWN,
                           wx.WXK_HOME, wx.WXK_END, wx.WXK_PAGEUP, wx.WXK_PAGEDOWN):
                event.Skip()
                return

            if keycode in (ord('K'), ord('k')):
                self.on_eliminar_linea(None)
                return
            elif keycode in (ord('O'), ord('o')):
                self.on_mostrar_simbolos()
                return
            elif keycode in (ord('C'), ord('c')):
                self.on_leer_toda_la_salida()
                return
            elif keycode in (ord('S'), ord('s')):
                self.on_guardar_como(None)
                return
            elif keycode in (ord('P'), ord('p')):
                self.on_gestor_interpretes(None)
                return
            elif keycode in (ord('R'), ord('r')):
                self.on_extraer_funcion(None)
                return
            elif keycode in (ord('I'), ord('i')):
                self.on_consultar_ia(None)
                return
            elif keycode in (ord('E'), ord('e')):
                self.on_explorador_proyectos(None)
                return
            event.Skip()
            return

        if is_ctrl and not is_shift and not is_alt:
            # Permitir navegación y selección estándar en controles de texto
            if keycode in (ord('C'), ord('c'), ord('V'), ord('v'), ord('X'), ord('x'),
                           ord('Z'), ord('z'), ord('Y'), ord('y'), ord('A'), ord('a'),
                           wx.WXK_LEFT, wx.WXK_RIGHT, wx.WXK_UP, wx.WXK_DOWN,
                           wx.WXK_HOME, wx.WXK_END, wx.WXK_PAGEUP, wx.WXK_PAGEDOWN):
                event.Skip()
                return

            if keycode == wx.WXK_RETURN:
                self.on_ejecutar(None)
                return
            elif keycode in (ord('M'), ord('m')):
                self.on_alternar_modo_trabajo()
                return
            elif keycode in (ord('N'), ord('n')):
                self.on_nuevo_archivo(None)
                return
            elif keycode in (ord('F'), ord('f')):
                self.on_buscar(None)
                return
            elif keycode in (ord('G'), ord('g')):
                self.on_ir_a_linea(None)
                return
            elif keycode in (ord('P'), ord('p')):
                self.on_pista(None)
                return
            elif keycode == ord('/'):
                self.on_comentar_descomentar(None)
                return
            elif keycode in (ord('D'), ord('d')):
                self.on_duplicar_linea(None)
                return
            elif keycode in (ord('L'), ord('l')):
                self.on_anunciar_posicion(None)
                return
            elif keycode == wx.WXK_SPACE:
                self.on_autocompletar(None)
                return
            elif keycode in (ord('T'), ord('t')):
                self.on_ejecutar_pruebas(None)
                return
            elif keycode in (ord('J'), ord('j')):
                self.on_abrir_repl(None)
                return
            elif keycode == ord('1'):
                self.on_abrir_temario(None)
                return
            elif keycode in (ord('R'), ord('r')):
                self.on_reiniciar_codigo(None)
                return
            elif keycode in (ord('O'), ord('o')):
                self.on_abrir_archivo(None)
                return
            elif keycode in (ord('S'), ord('s')):
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
                return
        else:
            if keycode == ord(':') and self.sonidos_activos:
                SoundManager.play('bloque')
            event.Skip()

    def on_leer_instruccion_actual(self, event=None):
        """Lee la consigna del paso actual por voz y braille sin retirar el foco del editor de código."""
        try:
            if self.modo_editor:
                is_en = (obtener_idioma_actual() == "en")
                self.anunciar("Standalone editor mode" if is_en else "Modo editor autónomo")
                return

            cap = CURRICULUM[self.cap_idx]
            paso = cap["pasos"][self.paso_idx]
            num_paso = self.paso_idx + 1
            total_pasos = len(cap["pasos"])
            instruccion = paso.get("instruccion", "")
            if not instruccion:
                instruccion = self.mision_ctrl.GetValue().strip()
            msg = f"Paso {num_paso} de {total_pasos}: {instruccion}"
            self.anunciar(msg)
        except Exception:
            pass

    def on_alternar_foco(self, event=None):
        """Alterna el foco entre el editor de código y la consola de resultados (F6)."""
        foco_actual = wx.Window.FindFocus()
        if foco_actual == self.salida:
            def _ir_edicion():
                self.edicion.SetFocus()
                self.anunciar("Foco en el editor de código", delay=50)
            wx.CallLater(100, _ir_edicion)
        else:
            def _ir_salida():
                self.salida.SetFocus()
                self.anunciar("Foco en la consola de resultados", delay=50)
            wx.CallLater(100, _ir_salida)

    def leer_ultima_salida(self):
        txt = self.salida.GetValue().strip()
        if not txt:
            if ui:
                ui.message("Consola vacía.")
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
            self, "Abrir script de Python",
            wildcard="Archivos Python (*.py)|*.py|Todos los archivos (*.*)|*.*",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    self.edicion.SetValue(f.read())
                self.archivo_abierto = path
                if ui:
                    ui.message(f"Archivo cargado: {os.path.basename(path)}")
                self.edicion.SetFocus()
            except Exception as e:
                wx.MessageBox(f"Error al abrir archivo: {e}", "Error", wx.OK | wx.ICON_ERROR, self)
        dlg.Destroy()

    def on_guardar_archivo(self, event=None):
        if self.archivo_abierto:
            try:
                with open(self.archivo_abierto, "w", encoding="utf-8") as f:
                    f.write(self.edicion.GetValue())
                if ui:
                    ui.message(f"Guardado en {os.path.basename(self.archivo_abierto)}")
            except Exception as e:
                wx.MessageBox(f"Error al guardar: {e}", "Error", wx.OK | wx.ICON_ERROR, self)
        else:
            self.on_guardar_como(event)

    def on_guardar_como(self, event=None):
        dlg = wx.FileDialog(
            self, "Guardar script como",
            wildcard="Archivos Python (*.py)|*.py",
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(self.edicion.GetValue())
                self.archivo_abierto = path
                if ui:
                    ui.message(f"Guardado como {os.path.basename(path)}")
            except Exception as e:
                wx.MessageBox(f"Error al guardar: {e}", "Error", wx.OK | wx.ICON_ERROR, self)
        dlg.Destroy()

    def on_abrir_doc(self, event=None):
        abierto = False
        if docHandler and hasattr(docHandler, 'openDoc'):
            try:
                abierto = docHandler.openDoc("readme.html")
            except Exception:
                abierto = False

        if not abierto:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            candidatos = [
                os.path.join(base_dir, "doc", "es", "readme.html"),
                os.path.join(base_dir, "doc", "readme.html"),
                os.path.join(base_dir, "readme.html"),
                os.path.join(base_dir, "addon", "doc", "es", "readme.html")
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
            ui.message("No fue posible abrir la documentación en el navegador.")

    def on_soporte(self, event=None):
        """Abre el diálogo accesible de soporte técnico y donaciones."""
        dlg = SupportDialog(self)
        dlg.ShowModal()
        dlg.Destroy()
        self.edicion.SetFocus()

    def on_acerca(self, event=None):
        """Abre la documentación accesible de Acerca de en el navegador web según el idioma activo."""
        is_en = (obtener_idioma_actual() == "en")
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            idioma = "en" if is_en else "es"
            doc_file = os.path.join(base_dir, "doc", idioma, "readme.html")
            if not os.path.isfile(doc_file):
                doc_file = os.path.join(base_dir, "doc", "readme.html")

            if os.path.isfile(doc_file):
                try:
                    os.startfile(doc_file)
                except Exception:
                    webbrowser.open(f"file:///{os.path.abspath(doc_file).replace(os.sep, '/')}")
                msg = "Opening documentation in web browser..." if is_en else "Abriendo documentación en el navegador web..."
                self.anunciar(msg)
                return
        except Exception:
            pass

        try:
            from ...docHandler import openDoc
            if openDoc():
                return
        except Exception:
            try:
                import docHandler
                if docHandler.openDoc():
                    return
            except Exception:
                pass

        msg = "Documentation file not found." if is_en else "Archivo de documentación no encontrado."
        self.anunciar(msg)

    def on_close(self, event):
        prog = ProgressManager.load_progress()
        prog["current_chapter"] = self.cap_idx
        prog["current_step"] = self.paso_idx
        ProgressManager.save_progress(prog)
        self.Destroy()
