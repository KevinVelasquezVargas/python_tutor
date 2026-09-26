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
        super(ChapterSelectDialog, self).__init__(parent, title="Selector de Capítulos del Temario", size=(650, 480))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(panel, label="Elige el capítulo al que deseas acceder:")
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.opciones = []
        self.cap_estados = []
        for i, cap in enumerate(CURRICULUM):
            total_pasos = len(cap.get("pasos", []))
            completado = ProgressManager.is_chapter_completed(i, total_pasos)
            desbloqueado = ProgressManager.is_chapter_unlocked(i)
            self.cap_estados.append((desbloqueado, completado))
            if completado:
                estado_str = "Superado, "
            elif desbloqueado:
                estado_str = "Disponible, "
            else:
                estado_str = "Bloqueado, "
            self.opciones.append(f"{estado_str}{cap.get('titulo', f'Capítulo {i+1}')}")

        self.list_box = wx.ListBox(panel, choices=self.opciones)
        self.list_box.SetName("Lista de capítulos. Presione Enter o haga clic para seleccionar.")
        if 0 <= current_idx < len(self.opciones):
            self.list_box.SetSelection(current_idx)
        vbox.Add(self.list_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_ok = wx.Button(panel, wx.ID_OK, label="Cargar Capítulo")
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label="Cancelar")
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
            desbloqueado, _ = self.cap_estados[sel]
            if not desbloqueado:
                msg = "Este capítulo está bloqueado. Debes completar todos los pasos del capítulo anterior para desbloquearlo."
                if ui:
                    ui.message(msg)
                wx.MessageBox(msg, "Capítulo bloqueado", wx.OK | wx.ICON_WARNING, self)
                return
        self.EndModal(wx.ID_OK)

    def get_selected_index(self):
        return self.list_box.GetSelection()


class HintDialog(wx.Dialog):
    """Diálogo accesible para el sistema escalonado de pistas pedagógicas."""
    def __init__(self, parent, pistas, nivel_actual=0):
        super(HintDialog, self).__init__(parent, title="Pista de Asistencia", size=(620, 380))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        total_pistas = max(1, len(pistas))
        lbl = wx.StaticText(panel, label=f"Pista disponible (Nivel {min(nivel_actual + 1, total_pistas)} de {total_pistas}):")
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        texto_pista = pistas[nivel_actual] if nivel_actual < len(pistas) else (pistas[-1] if pistas else "Revisa las instrucciones del ejercicio.")
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.text_ctrl.SetValue(texto_pista)
        self.text_ctrl.SetName("Contenido de la pista.")
        vbox.Add(self.text_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        btn_ok = wx.Button(panel, wx.ID_OK, label="Entendido")
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
        super(WelcomeDialog, self).__init__(parent, title="Bienvenido a Aprendizaje de Python con NVDA", size=(660, 440))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        mensaje = (
            "¡Te damos la bienvenida a Aprendizaje de Python con NVDA!\n\n"
            "Este complemento te guiará paso a paso en el aprendizaje de la programación en Python, "
            "comenzando desde los conceptos fundamentales y avanzando de manera progresiva a través "
            "de ejercicios prácticos diseñados para ser resueltos directamente en el editor.\n\n"
            "El entorno cuenta con dos modalidades de trabajo:\n"
            "Modo Aprendizaje: Ofrece lecciones guiadas, explicaciones teóricas y comprobación automática de soluciones.\n"
            "Modo Editor autónomo: Un editor despejado y accesible para escribir y ejecutar tus propios scripts.\n\n"
            "Puedes consultar la lista completa de atajos de teclado en cualquier momento pulsando F11 o desde el menú Ayuda, "
            "y obtener más detalles sobre el complemento en la opción Acerca de.\n\n"
            "Pulsa el botón Comenzar a aprender o pulsa Enter para empezar tu primera lección."
        )

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(mensaje)
        txt.SetName("Mensaje de bienvenida")
        vbox.Add(txt, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        prog = ProgressManager.load_progress()
        self.chk_mostrar = wx.CheckBox(panel, label="Mostrar esta guía de bienvenida al iniciar")
        self.chk_mostrar.SetValue(prog.get("show_welcome", True))
        vbox.Add(self.chk_mostrar, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM, border=12)

        btn_comenzar = wx.Button(panel, wx.ID_OK, label="Comenzar a aprender")
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
        super(ShortcutsDialog, self).__init__(parent, title="Guía de Atajos de Teclado", size=(700, 560))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        texto_atajos = (
            "Guía Completa de Atajos de Teclado:\n\n"
            "Modos y Aprendizaje:\n"
            "Control + Enter o Control + E: Ejecutar código y comprobar la solución.\n"
            "Control + M: Alternar entre Modo Aprendizaje y Modo Solo Editor profesional.\n"
            "F3 o Control + I: Leer la instrucción activa sin mover el foco del editor.\n"
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
            "Shift + Alt + F o Control + Shift + I: Formatear documento según PEP 8.\n"
            "Control + Shift + R: Extraer bloque de código seleccionado a una nueva función.\n"
            "Control + Espacio: Autocompletado inteligente con documentación.\n"
            "Control + Shift + O: Lista accesible de funciones y clases del script.\n"
            "Alt + N: Salto rápido a la cabecera de la siguiente función o clase.\n"
            "Alt + P: Salto rápido a la cabecera de la función o clase anterior.\n"
            "Control + / o Control + K: Comentar o descomentar la línea actual con '# '.\n"
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
            "F5: Ejecutar el código y verificar solución.\n"
            "F11: Abrir esta Guía de Atajos de Teclado.\n"
            "F12: Abrir la documentación de Acerca de en el navegador web.\n"
            "Escape: Cerrar la ventana del tutor inmediatamente desde cualquier control."
        )

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(texto_atajos)
        txt.SetName("Lista completa de atajos de teclado")
        vbox.Add(txt, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        btn_cerrar = wx.Button(panel, wx.ID_OK, label="Cerrar Guía")
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
        super(GlossaryDialog, self).__init__(parent, title="Diccionario de Términos de Python", size=(720, 520))
        self.terminos = sorted(list(GLOSARIO.keys()))
        self.filtrados = list(self.terminos)

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        search_box = wx.BoxSizer(wx.HORIZONTAL)
        lbl = wx.StaticText(panel, label="Buscar término:")
        search_box.Add(lbl, flag=wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border=8)
        self.search_ctrl = wx.TextCtrl(panel)
        self.search_ctrl.SetName("Escribe aquí el comando o concepto para buscar.")
        search_box.Add(self.search_ctrl, proportion=1, flag=wx.EXPAND)
        main_sizer.Add(search_box, flag=wx.EXPAND | wx.ALL, border=10)

        content_box = wx.BoxSizer(wx.HORIZONTAL)
        self.list_box = wx.ListBox(panel, choices=self.terminos)
        self.list_box.SetName("Términos disponibles.")
        content_box.Add(self.list_box, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=10)

        self.def_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.def_ctrl.SetName("Significado del término.")
        content_box.Add(self.def_ctrl, proportion=2, flag=wx.EXPAND)
        main_sizer.Add(content_box, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        btn_cerrar = wx.Button(panel, wx.ID_CANCEL, label="Cerrar Diccionario")
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
            self.def_ctrl.SetValue("No se encontraron coincidencias.")

    def on_select(self, event):
        sel = self.list_box.GetStringSelection()
        if sel in GLOSARIO:
            self.def_ctrl.SetValue(GLOSARIO[sel])
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
        super(AboutDialog, self).__init__(parent, title="Acerca de Aprendizaje de Python con NVDA", size=(780, 620))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        contenido = (
            "Aprendizaje de Python con NVDA\n"
            "Versión: 2.0.0\n"
            "Autor: Kevin Andrés Velasquez Vargas\n"
            "Correo de soporte: kevinvelasquezvargas@gmail.com\n"
            "Licencia: GNU General Public License v3.0 (GPLv3)\n"
            "Compatibilidad: NVDA 2022.1 hasta 2026.3\n"
            "Repositorio en GitHub: https://github.com/KevinVelasquezVargas/python_tutor\n"
            "Donaciones y apoyo voluntario: https://www.paypal.me/kevinvelasquezvargas\n\n"
            "======================================================================\n"
            "1. Visión General y Propósito del Complemento\n"
            "======================================================================\n\n"
            "Aprendizaje de Python con NVDA es un entorno formativo integral y un editor tiflotécnico "
            "de código adaptado para la programación en Python mediante NVDA. Proporciona una ruta de "
            "aprendizaje estructurada en 32 lecciones conceptuales y prácticas, complementada con un "
            "entorno de trabajo de doble modalidad: modo tutor guiado y modo editor autónomo.\n\n"
            "Integra navegación por elementos de código como funciones y clases, señales sonoras de sangría "
            "y estructura, verificación de delimitadores y simplificación de mensajes de error.\n\n"
            "El entorno ha sido diseñado para garantizar que cualquier persona ciega o con baja visión "
            "pueda formarse de manera 100% independiente, con retroalimentación en voz y braille.\n\n"
            "======================================================================\n"
            "2. Metodología Pedagógica: Ciclo de Aprendizaje en 4 Pasos\n"
            "======================================================================\n\n"
            "Cada capítulo implementa un ciclo pedagógico de cuatro fases progresivas:\n\n"
            "Paso 1: Fundamento Conceptual (Observar): Presenta la teoría en un lenguaje claro y "
            "cotidiano, acompañada de un script de demostración ejecutable con F5 o Control + Enter.\n\n"
            "Paso 2: Observación Guiada (Experimentar): Un fragmento de código funcional con una consigna "
            "específica para modificarlo y constatar la causa y efecto de los cambios.\n\n"
            "Paso 3: Reto Práctico (Desafío): El editor inicia completamente limpio para que el estudiante "
            "escriba su propio código. El tutor valida rigurosamente la solución sin aceptar respuestas vacías.\n\n"
            "Paso 4: Verificación Conceptual (Quiz): Pregunta formativa de opción múltiple (1, 2 o 3) para "
            "consolidar los conceptos aprendidos.\n\n"
            "======================================================================\n"
            "3. Doble Modalidad de Trabajo\n"
            "======================================================================\n\n"
            "Puedes alternar entre los dos modos en cualquier instante pulsando Control + M:\n\n"
            "Modo Aprendizaje Guiado: Muestra la instrucción del paso, el código, botones didácticos y "
            "el sistema de validación pedagógica.\n\n"
            "Modo Solo Editor (Profesional libre): Oculta todas las secciones de lecciones y maximiza el "
            "espacio para el editor y la consola de salida, permitiendo trabajar en proyectos propios con "
            "soporte para abrir y guardar archivos .py, verificación de delimitadores y navegación estructural.\n\n"
            "======================================================================\n"
            "4. Catálogo del Temario Pedagógico (32 Capítulos)\n"
            "======================================================================\n\n"
            "Fase 0: Pensamiento Computacional y Fundamentos (1 a 3)\n"
            "Capítulo 1: Pensamiento Computacional y Algoritmos Cotidianos\n"
            "Capítulo 2: Arquitectura Básica: Entrada, Proceso, Memoria y Salida\n"
            "Capítulo 3: Lógica Booleana: Verdadero, Falso y Decisiones\n\n"
            "Fase 1: Sintaxis Básica y Tipos de Datos (4 a 8)\n"
            "Capítulo 4: Nuestra Primera Instrucción: La Función print()\n"
            "Capítulo 5: Almacenamiento en Memoria: Variables y Asignación\n"
            "Capítulo 6: Tipos de Datos Primitivos: Números Enteros y Decimales\n"
            "Capítulo 7: Cadenas de Texto (Strings): Comillas y Concatenación\n"
            "Capítulo 8: Interacción con el Usuario: Entrada con input()\n\n"
            "Fase 2: Estructuras de Control de Flujo (9 a 15)\n"
            "Capítulo 9: Operadores de Comparación y Expresiones Condicionales\n"
            "Capítulo 10: Bifurcación Básica: Estructura if y Sangría PEP 8\n"
            "Capítulo 11: Alternativas Múltiples: Bloques elif y else\n"
            "Capítulo 12: Colecciones Ordenadas: Introducción a las Listas\n"
            "Capítulo 13: Métodos Fundamentales de Listas (append, remove, pop, len)\n"
            "Capítulo 14: Repetición y Automatización: El Bucle for y range()\n"
            "Capítulo 15: Repetición Condicional: El Bucle while\n\n"
            "Fase 3: Estructuras de Datos Complejas (16 a 17)\n"
            "Capítulo 16: Colecciones Clave-Valor: Diccionarios en Python\n"
            "Capítulo 17: Tuplas y Conjuntos (Sets): Inmutabilidad y Colecciones Únicas\n\n"
            "Fase 4: Modularidad y Funciones (18 a 19)\n"
            "Capítulo 18: Funciones Propias: Declaración con def y Parámetros\n"
            "Capítulo 19: Retorno de Resultados: La Sentencia return y Ámbito\n\n"
            "Fase 5: Manejo Profesional de Errores y Diagnóstico (20 a 21)\n"
            "Capítulo 20: Manejo Profesional de Errores: try, except y finally\n"
            "Capítulo 21: Decodificación de Tracebacks y Diagnóstico de Fallos\n\n"
            "Fase 6: Entrada/Salida de Archivos y Persistencia (22)\n"
            "Capítulo 22: Entrada y Salida de Archivos: with open() para Texto\n\n"
            "Fase 7: Programación Orientada a Objetos (23 a 27)\n"
            "Capítulo 23: Paradigma de Objetos: Clases, Instancias y Atributos\n"
            "Capítulo 24: El Constructor __init__ y el Parámetro self\n"
            "Capítulo 25: Métodos de Instancia y Encapsulamiento\n"
            "Capítulo 26: Herencia de Clases: Reutilización con super()\n"
            "Capítulo 27: Polimorfismo y Métodos Especiales (__str__)\n\n"
            "Fase 8: Ecosistema Profesional y Calidad (28 a 32)\n"
            "Capítulo 28: Módulos de la Biblioteca Estándar (math, random, datetime)\n"
            "Capítulo 29: Persistencia Estructurada: Formato JSON y Serialización\n"
            "Capítulo 30: Bases de Datos Relacionales con SQLite: Tablas y Consultas\n"
            "Capítulo 31: Consumo de Servicios Web: Peticiones HTTP y Respuestas JSON\n"
            "Capítulo 32: Calidad de Software: Pruebas Unitarias con unittest\n\n"
            "======================================================================\n"
            "5. Referencia Integral de Atajos de Teclado\n"
            "======================================================================\n\n"
            "F5 o Control + Enter: Ejecutar el código y comprobar la solución.\n"
            "Control + M: Alternar entre Modo Aprendizaje y Modo Solo Editor profesional.\n"
            "Alt + Flecha Derecha: Ir al paso siguiente.\n"
            "Alt + Flecha Izquierda: Ir al paso anterior.\n"
            "F1: Explicar la línea donde está el cursor con palabras sencillas.\n"
            "F2: Ver todos los atajos de teclado.\n"
            "F3 o Control + I: Leer la consigna activa sin mover el cursor del editor.\n"
            "F4: Situar el cursor directamente en la línea del error del Traceback.\n"
            "F6: Alternar el foco entre el editor de código y la consola.\n"
            "F7: Verificar sintaxis y balanceo de delimitadores/comillas.\n"
            "Control + P: Pedir una pista de asistencia.\n"
            "Control + 1: Selector de capítulos del temario.\n"
            "Control + J: Abrir la consola de pruebas rápidas (REPL).\n"
            "Control + Shift + O: Lista accesible de funciones y clases del script.\n"
            "Alt + N / Alt + P: Salto a la siguiente / anterior función o clase.\n"
            "Control + /: Comentar o descomentar la línea actual.\n"
            "Control + D: Duplicar línea abajo.\n"
            "Control + Shift + K: Eliminar línea actual.\n"
            "Control + L: Anunciar línea y columna actual.\n"
            "Control + F: Buscar texto en el editor.\n"
            "Control + G: Ir a número de línea.\n"
            "Control + N: Iniciar nuevo script limpio.\n"
            "Control + O / Control + S: Abrir / Guardar archivo.\n"
            "Control + Shift + S: Guardar como nuevo archivo.\n"
            "Control + 4 / Control + 5: Foco directo al editor / consola.\n"
            "Control + Shift + C: Verbalizar toda la salida de consola sin salir del editor.\n"
            "F12: Abrir esta documentación en Acerca de.\n"
            "Escape: Cerrar el tutor en cualquier momento.\n\n"
            "======================================================================\n"
            "6. Sistema de Retroalimentación Sonora\n"
            "======================================================================\n\n"
            "El entorno produce señales auditivas breves y diferenciadas:\n"
            "Inicio: Tono de confirmación al iniciar el entorno.\n"
            "Éxito: Tono agudo y gratificante al superar un ejercicio o ejecutar con éxito.\n"
            "Error: Tono grave al presentarse una excepción o fallo.\n"
            "Advertencia: Señal sonora ante delimitadores abiertos o avisos de sintaxis.\n"
            "Bloque: Tono sutil al tipear dos puntos (:) para indicar apertura de sangría.\n\n"
            "======================================================================\n"
            "7. Asistencia en la Depuración y Diagnóstico\n"
            "======================================================================\n\n"
            "El entorno asiste activamente en la detección temprana de fallos:\n"
            "Comprobación previa de comillas y delimitadores () [] {}.\n"
            "Salto automático con F4 a la línea del error del Traceback.\n"
            "Detección de caracteres confusos frecuentes como comas en flotantes o signos ¿¡.\n"
            "Traductor de sentencias con F1 a explicaciones humanas comprensibles.\n\n"
            "======================================================================\n"
            "8. Soporte, Contacto y Donaciones\n"
            "======================================================================\n\n"
            "Para soporte directo, sugerencias o consultas:\n"
            "Desarrollador: Kevin Andrés Velasquez Vargas\n"
            "Correo electrónico directo: kevinvelasquezvargas@gmail.com\n"
            "Asunto recomendado: Soporte - Aprendizaje de Python con NVDA\n"
            "Donaciones voluntarias por PayPal: https://www.paypal.me/kevinvelasquezvargas\n\n"
            "======================================================================\n"
            "9. Información Técnica y Licencia\n"
            "======================================================================\n\n"
            "Versión: 2.0.0\n"
            "Compatibilidad: NVDA 2022.1 hasta 2026.3\n"
            "Licencia: GNU General Public License v3.0 (GPLv3)\n"
            "Desarrollado para la comunidad de programadores usuarios de lectores de pantalla."
        )

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(contenido)
        txt.SetName("Documentación de Aprendizaje de Python con NVDA")
        vbox.Add(txt, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        btn_cerrar = wx.Button(panel, wx.ID_OK, label="Cerrar")
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
        super(TutorFrame, self).__init__(parent, title="Aprendizaje de Python con NVDA", size=(980, 840))

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
        item_nuevo = m_archivo.Append(wx.ID_ANY, "Nuevo script\tCtrl+N", "Inicia un nuevo script limpio en el editor")
        item_abrir = m_archivo.Append(wx.ID_ANY, "Abrir archivo...\tCtrl+O", "Carga un script de Python desde el disco")
        item_guardar = m_archivo.Append(wx.ID_ANY, "Guardar script\tCtrl+S", "Guarda el contenido del editor en el archivo")
        item_guardar_como = m_archivo.Append(wx.ID_ANY, "Guardar como...\tCtrl+Shift+S", "Guarda el código con un nuevo nombre o ubicación")
        m_archivo.AppendSeparator()
        item_salir = m_archivo.Append(wx.ID_EXIT, "Cerrar tutor\tAlt+F4", "Cierra el entorno de aprendizaje")

        self.Bind(wx.EVT_MENU, self.on_nuevo_archivo, id=item_nuevo.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_archivo, id=item_abrir.GetId())
        self.Bind(wx.EVT_MENU, self.on_guardar_archivo, id=item_guardar.GetId())
        self.Bind(wx.EVT_MENU, self.on_guardar_como, id=item_guardar_como.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.Close(), id=item_salir.GetId())

        # 2. Menú Edición
        m_edicion = wx.Menu()
        item_deshacer = m_edicion.Append(wx.ID_UNDO, "Deshacer\tCtrl+Z", "Revierte la última acción de edición")
        item_rehacer = m_edicion.Append(wx.ID_REDO, "Rehacer\tCtrl+Y", "Reaplica la acción deshecha")
        m_edicion.AppendSeparator()
        item_cortar = m_edicion.Append(wx.ID_CUT, "Cortar\tCtrl+X", "Corta el texto seleccionado al portapapeles")
        item_copiar = m_edicion.Append(wx.ID_COPY, "Copiar\tCtrl+C", "Copia el texto seleccionado al portapapeles")
        item_pegar = m_edicion.Append(wx.ID_PASTE, "Pegar\tCtrl+V", "Pega el contenido del portapapeles")
        item_sel_todo = m_edicion.Append(wx.ID_SELECTALL, "Seleccionar todo\tCtrl+A", "Selecciona todo el texto del editor")
        m_edicion.AppendSeparator()
        item_buscar = m_edicion.Append(wx.ID_ANY, "Buscar texto...\tCtrl+F", "Busca palabras o fragmentos de código")
        item_ir_linea = m_edicion.Append(wx.ID_ANY, "Ir a línea...\tCtrl+G", "Desplaza el cursor al número de línea indicado")
        m_edicion.AppendSeparator()
        item_pep8 = m_edicion.Append(wx.ID_ANY, "Formatear documento según PEP 8\tShift+Alt+F", "Ajusta la sangría a 4 espacios y los espacios de operadores")
        item_renombrar = m_edicion.Append(wx.ID_ANY, "Renombrar símbolo...\tF2", "Renombra la variable o función seleccionada en todo el script")
        item_extraer = m_edicion.Append(wx.ID_ANY, "Extraer a función...\tCtrl+Shift+R", "Convierte el bloque seleccionado en una nueva función")
        m_edicion.AppendSeparator()
        item_simbolos = m_edicion.Append(wx.ID_ANY, "Lista de funciones y clases...\tCtrl+Shift+O", "Abre la lista de funciones y clases del archivo")
        item_sig_def = m_edicion.Append(wx.ID_ANY, "Ir a siguiente función o clase\tAlt+N", "Salta a la cabecera de la siguiente función o clase")
        item_ant_def = m_edicion.Append(wx.ID_ANY, "Ir a anterior función o clase\tAlt+P", "Salta a la cabecera de la función o clase anterior")
        m_edicion.AppendSeparator()
        item_comentar = m_edicion.Append(wx.ID_ANY, "Comentar o descomentar línea\tCtrl+/", "Alterna el comentario '#' al inicio de la línea")
        item_duplicar = m_edicion.Append(wx.ID_ANY, "Duplicar línea abajo\tCtrl+D", "Duplica la línea actual en la siguiente")
        item_eliminar = m_edicion.Append(wx.ID_ANY, "Eliminar línea actual\tCtrl+Shift+K", "Elimina por completo la línea donde está el cursor")
        m_edicion.AppendSeparator()
        item_verificar = m_edicion.Append(wx.ID_ANY, "Verificar sintaxis y delimitadores\tF7", "Comprueba paréntesis, comillas y errores de sintaxis")
        item_posicion = m_edicion.Append(wx.ID_ANY, "Anunciar posición (Línea y columna)\tCtrl+L", "Informa en qué línea y columna se encuentra el cursor")

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
        item_alternar = m_herramientas.Append(wx.ID_ANY, "Alternar foco entre editor y consola\tF6", "Cambia el foco entre el editor de código y la salida")
        item_modo = m_herramientas.Append(wx.ID_ANY, "Alternar Modo Aprendizaje / Editor autónomo\tCtrl+M", "Conmuta entre el entorno didáctico y el editor limpio")
        item_breakpoint = m_herramientas.Append(wx.ID_ANY, "Alternar punto de interrupción\tF9", "Activa o desactiva un punto de parada en la línea actual")
        item_autocompletar = m_herramientas.Append(wx.ID_ANY, "Autocompletado con documentación\tCtrl+Space", "Muestra sugerencias de código con su descripción")
        item_repl = m_herramientas.Append(wx.ID_ANY, "Consola de pruebas rápidas (REPL)\tCtrl+J", "Ventana de pruebas inmediatas de una línea")
        item_depurar = m_herramientas.Append(wx.ID_ANY, "Depuración interactiva paso a paso...\tF10", "Ejecuta el script inspeccionando cada línea y sus variables")
        item_glosario = m_herramientas.Append(wx.ID_ANY, "Diccionario de términos de Python", "Buscador de términos y conceptos del lenguaje")
        item_doc_rapida = m_herramientas.Append(wx.ID_ANY, "Documentación rápida del símbolo\tShift+F1", "Lee la explicación de la función o palabra bajo el cursor")
        item_ejecutar = m_herramientas.Append(wx.ID_ANY, "Ejecutar código y verificar\tF5", "Ejecuta el script o valida la misión actual (F5 o Ctrl+Enter)")
        item_pruebas = m_herramientas.Append(wx.ID_ANY, "Ejecutar pruebas unitarias (Test Runner)...\tCtrl+T", "Ejecuta las pruebas unittest del script con reporte accesible")
        item_traductor = m_herramientas.Append(wx.ID_ANY, "Explicar línea de código\tF1", "Traduce la línea de código actual a palabras cotidianas")
        item_interprete = m_herramientas.Append(wx.ID_ANY, "Gestor de intérpretes y entornos virtuales...\tCtrl+Shift+P", "Selecciona el entorno de Python o virtualenv activo")
        item_error = m_herramientas.Append(wx.ID_ANY, "Ir a la línea del error del Traceback\tF4", "Mueve el cursor exactamente a la línea del fallo")
        item_temario = m_herramientas.Append(wx.ID_ANY, "Ir a un capítulo del temario...\tCtrl+1", "Ver el listado completo de capítulos")
        item_leer_inst = m_herramientas.Append(wx.ID_ANY, "Leer instrucción del paso activo\tF3", "Lee la consigna actual sin retirar el cursor del editor")
        item_leer_salida = m_herramientas.Append(wx.ID_ANY, "Leer toda la salida de consola\tCtrl+Shift+C", "Verbaliza todo el texto de la consola sin perder el foco")
        item_reiniciar = m_herramientas.Append(wx.ID_ANY, "Restablecer código del ejercicio\tCtrl+R", "Restaura el código original del paso")

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
        item_acerca = m_ayuda.Append(wx.ID_ANY, "Acerca de Aprendizaje de Python con NVDA...\tF12", "Documentación accesible completa en el navegador")
        item_donacion = m_ayuda.Append(wx.ID_ANY, "Colaborar con el proyecto...", "Realizar una donación voluntaria para apoyar el complemento")
        item_atajos = m_ayuda.Append(wx.ID_ANY, "Guía de atajos de teclado\tF11", "Muestra la lista de atajos rápidos")
        item_soporte = m_ayuda.Append(wx.ID_ANY, "Soporte y contacto...", "Canales de contacto directo por correo y asistencia")

        self.Bind(wx.EVT_MENU, self.on_acerca, id=item_acerca.GetId())
        self.Bind(wx.EVT_MENU, self.on_donacion, id=item_donacion.GetId())
        self.Bind(wx.EVT_MENU, self.on_mostrar_atajos, id=item_atajos.GetId())
        self.Bind(wx.EVT_MENU, self.on_soporte, id=item_soporte.GetId())

        menu_bar.Append(m_archivo, "&Archivo")
        menu_bar.Append(m_edicion, "&Edición")
        menu_bar.Append(m_herramientas, "&Herramientas")
        menu_bar.Append(m_ayuda, "A&yuda")
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

            self.lbl_ed.SetLabel("Editor de código (Modo autónomo):")

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

            self.SetTitle("Aprendizaje de Python con NVDA")
            self.panel.Layout()
            self.Layout()
            if anunciar:
                msg = "Modo Editor autónomo activado. Entorno limpio de trabajo sin lecciones."
                self.anunciar(msg)
        else:
            self.lbl_estado.Enable()
            self.lbl_estado.Show()
            self.vbox.Show(self.lbl_estado, True)

            self.mision_ctrl.Enable()
            self.mision_ctrl.Show()
            self.vbox.Show(self.mision_ctrl, True)

            self.lbl_ed.SetLabel("Editor de código:")

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

            self.SetTitle("Aprendizaje de Python con NVDA")
            self.panel.Layout()
            self.Layout()
            if anunciar:
                msg = "Modo Aprendizaje guiado activado. Lecciones y temario visibles."
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
        marca_estado = "Superado" if superado else "Pendiente"

        titulo_paso = paso.get("titulo", f"Paso {self.paso_idx + 1}")
        texto_encabezado = f"{cap.get('titulo', 'Capítulo')}, Paso {self.paso_idx + 1} de {total_pasos}: {titulo_paso}, {marca_estado}"
        self.lbl_estado.SetLabel(texto_encabezado)

        instruccion = paso.get("instruccion")
        if not instruccion:
            if paso.get("tipo") == "quiz":
                preg = paso.get("pregunta", "")
                opciones = paso.get("opciones", [])
                ops_txt = "\n".join(f"{i+1}. {op}" for i, op in enumerate(opciones))
                instruccion = f"Pregunta de verificación conceptual:\n\n{preg}\n\nOpciones:\n{ops_txt}\n\nEscribe el número de la respuesta correcta (1, 2 o 3) en el editor y pulsa Control + Enter."
            else:
                instruccion = "Sigue las instrucciones del ejercicio y ejecuta con Control + Enter."

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
            self.salida.SetValue(f"Aviso de delimitadores:\n{bal_err['mensaje']}\n\nPresiona F4 para situar el cursor en la línea del aviso.")
            if self.sonidos_activos:
                SoundManager.play('sintaxis_aviso')
            self.anunciar(f"Aviso de delimitadores: {bal_err['mensaje']}. Presiona F4 para ir a la línea.")
            return

        # 2. Comprobación de código vacío o solo comentarios
        lineas_codigo = [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
        if not lineas_codigo:
            if not self.modo_editor:
                cap = CURRICULUM[self.cap_idx]
                paso = cap["pasos"][self.paso_idx]
                tipo_paso = paso.get("tipo", "observar")
                if tipo_paso == "quiz":
                    msg = "No has indicado ninguna opción. Escribe el número 1, 2 o 3 en el editor y pulsa Control + Enter o F5."
                elif tipo_paso == "desafio":
                    msg = "El editor está vacío o solo contiene comentarios. Escribe tu código para resolver el reto práctico y pulsa Control + Enter o F5."
                elif tipo_paso == "experimentar":
                    msg = "No se detecta código ejecutable. Realiza la modificación indicada en la consigna y pulsa Control + Enter o F5."
                else:
                    msg = "El editor no contiene código para ejecutar."
            else:
                msg = "El editor está vacío. Escribe instrucciones de Python antes de ejecutar."

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
                salida_txt.append("Aviso de escritura:")
                salida_txt.append(res.keyboard_warning)
                salida_txt.append("")

            salida_txt.append("Salida:")
            salida_txt.append(res.output if res.output else "(Sin salida de consola)")

            if not res.success:
                self.ultimo_error_linea = res.error_line
                self.ultimo_error_msg = res.error_msg
                if res.friendly_explanation:
                    salida_txt.append("")
                    salida_txt.append(f"Aviso de ejecución: {res.friendly_explanation}")
                    salida_txt.append("Presiona F4 para posicionar el cursor en la línea del fallo.")
                if self.sonidos_activos:
                    SoundManager.play('error')
                msg_err = res.friendly_explanation or res.error_msg or "Error durante la ejecución"
                self.anunciar(f"Error: {msg_err}. Pulse F4 para ir al error.")
            else:
                self.ultimo_error_linea = None
                self.ultimo_error_msg = None
                if self.sonidos_activos:
                    SoundManager.play('exito')
                self.anunciar("Ejecución finalizada con éxito.")

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
                reporte_pruebas.append(f"Correcto: {paso.get('explicacion', 'Respuesta correcta.')}")
            else:
                aprobado = False
                reporte_pruebas.append("Pendiente: La opción seleccionada no es la correcta. Revisa las opciones en la instrucción e inténtalo de nuevo.")

            res_output = f"Opción enviada: {digits[0] if digits else val_clean}"
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
                            reporte_pruebas.append(f"Correcto: {p.get('nombre', 'Prueba')} superada")
                        else:
                            reporte_pruebas.append(f"Pendiente: {p.get('nombre', 'Prueba')} no superada")
                            todas_ok = False
                    aprobado = todas_ok
                elif "validar" in paso and callable(paso["validar"]):
                    try:
                        aprobado = bool(paso["validar"](src, res.output, res.local_ns))
                    except Exception:
                        aprobado = False
                    if not aprobado:
                        reporte_pruebas.append("Pendiente: El código se ejecutó sin errores de sintaxis, pero el resultado aún no cumple los requisitos específicos del reto.")
                else:
                    aprobado = (tipo_paso == "observar")

        lineas_reporte = []
        if tipo_paso != "quiz" and getattr(res, 'keyboard_warning', None):
            lineas_reporte.append("Aviso de escritura:")
            lineas_reporte.append(res.keyboard_warning)
            lineas_reporte.append("")

        lineas_reporte.append("Salida:")
        lineas_reporte.append(res_output if res_output else "(Sin salida de consola)")
        lineas_reporte.append("")

        if reporte_pruebas:
            lineas_reporte.append("Resultado de la comprobación:")
            lineas_reporte.extend(reporte_pruebas)
            lineas_reporte.append("")

        if aprobado:
            lineas_reporte.append("¡Misión superada con éxito! Puedes avanzar al siguiente paso con Alt + Flecha Derecha.")
            self.salida.SetValue("\n".join(lineas_reporte))
            wx.CallLater(100, self.salida.SetFocus)

            ProgressManager.mark_step_completed(self.cap_idx, self.paso_idx)

            if self.sonidos_activos:
                SoundManager.play('exito')
            self.anunciar("¡Misión superada! Pulsa Alt + Flecha Derecha para avanzar.")
        else:
            if paso.get("salida_esperada"):
                comp = generar_comparacion_salida(paso["salida_esperada"], res_output)
                lineas_reporte.append("Comparación con la salida esperada:")
                lineas_reporte.append(comp)
                lineas_reporte.append("")

            if friendly_err:
                lineas_reporte.append(f"Aviso de ejecución: {friendly_err}")
                lineas_reporte.append("Pulsa F4 para posicionar el cursor en la línea del fallo.")
            elif tipo_paso != "quiz":
                lineas_reporte.append("La solución no ha sido aprobada aún. Revisa la consigna o pulsa Control + P para solicitar una pista.")

            self.salida.SetValue("\n".join(lineas_reporte))
            wx.CallLater(100, self.salida.SetFocus)

            if self.sonidos_activos:
                SoundManager.play('error')
            if friendly_err:
                self.anunciar(f"{friendly_err}. Pulsa F4 para ir al error.")
            elif tipo_paso == "quiz":
                self.anunciar("Opción incorrecta. Revisa la pregunta y vuelve a intentarlo.")
            else:
                self.anunciar("Solución no superada. Pulsa Control + P para recibir una pista.")

    def on_pista(self, event=None):
        cap = CURRICULUM[self.cap_idx]
        paso = cap["pasos"][self.paso_idx]
        pistas = paso.get("pistas", ["Revisa el enunciado de la lección en la parte superior e intenta ejecutar nuevamente."])

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
            self.edicion.SetFocus()
        else:
            if self.cap_idx < len(CURRICULUM) - 1:
                if not ProgressManager.is_chapter_completed(self.cap_idx, total_pasos):
                    msg = "Para avanzar al siguiente capítulo, debes completar todos los pasos del capítulo actual."
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
                    ui.message("¡Felicidades! Has completado todos los capítulos del temario.")

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
        self.anunciar("Código del ejercicio restablecido a su estado inicial.")

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
                self.anunciar("Modo Editor autónomo activo.")
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
        """Abre la documentación de Acerca de en el navegador web predeterminado."""
        msg = "Abriendo la documentación de Acerca de en el navegador web."
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
