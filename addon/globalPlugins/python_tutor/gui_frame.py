# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/gui_frame.py
# Propósito: Interfaz gráfica accesible, estructurada y con funciones avanzadas de edición.
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

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

try:
    import docHandler
except ImportError:
    docHandler = None


class ChapterSelectDialog(wx.Dialog):
    """Diálogo accesible para saltar directamente a cualquier capítulo del temario."""
    def __init__(self, parent, current_idx):
        super(ChapterSelectDialog, self).__init__(parent, title="Selector de Capítulos del Temario", size=(650, 480))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(panel, label="Elige el capítulo al que deseas acceder:")
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        opciones = []
        for i, cap in enumerate(CURRICULUM):
            completado = ProgressManager.is_step_completed(i, len(cap["pasos"]) - 1)
            icono = "[Superado] " if completado else ""
            opciones.append(f"{icono}{cap.get('titulo', f'Capítulo {i+1}')}")

        self.list_box = wx.ListBox(panel, choices=opciones)
        self.list_box.SetName("Lista de capítulos. Presione Enter o haga clic para seleccionar.")
        if 0 <= current_idx < len(opciones):
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
        self.list_box.Bind(wx.EVT_LISTBOX_DCLICK, lambda e: self.EndModal(wx.ID_OK))
        self.CenterOnParent()
        self.list_box.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

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
        super(WelcomeDialog, self).__init__(parent, title="Bienvenido a Aprendizaje de Python con NVDA", size=(700, 540))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        mensaje = (
            "¡Te damos la bienvenida al entorno accesible de Aprendizaje de Python con NVDA!\n\n"
            "Este complemento está diseñado para que cualquier persona aprenda a programar paso a paso, "
            "desde cero, mediante la práctica directa en el editor de código.\n\n"
            "Atajos de teclado esenciales:\n"
            "• Control + Enter: Ejecutar el código y comprobar la solución.\n"
            "• Control + M: Alternar entre Modo Aprendizaje y Modo Solo Editor profesional.\n"
            "• F3 o Control + I: Leer la instrucción activa sin mover el cursor del editor.\n"
            "• F4: Situar el cursor directamente en la línea del error del Traceback.\n"
            "• F6: Alternar el foco entre el editor de código y la consola.\n"
            "• F7: Verificar sintaxis y balanceo de delimitadores/comillas.\n"
            "• Control + Shift + O: Lista accesible de funciones y clases del script.\n"
            "• Alt + N / Alt + P: Salto a la siguiente / anterior función o clase.\n"
            "• Control + Shift + C: Verbalizar toda la salida de consola sin salir del editor.\n"
            "• Control + Flecha Derecha: Ir al paso siguiente.\n"
            "• Control + Flecha Izquierda: Ir al paso anterior.\n"
            "• Control + P: Pedir una pista de asistencia.\n"
            "• F1: Explicar la línea de código donde está el cursor con palabras sencillas.\n"
            "• F2: Ver todos los atajos de teclado.\n"
            "• Control + /: Comentar o descomentar la línea actual.\n"
            "• Control + L: Anunciar la línea y columna actual.\n"
            "• Control + J: Abrir la consola de pruebas rápidas (REPL).\n"
            "• Control + G: Abrir el diccionario de términos de Python.\n"
            "• Control + 1: Selector de capítulos del temario.\n"
            "• Escape: Cerrar el tutor en cualquier momento.\n\n"
            "¡El cursor se posicionará en el editor para comenzar ahora mismo!"
        )

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(mensaje)
        txt.SetName("Mensaje de bienvenida y guía rápida")
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
        super(ShortcutsDialog, self).__init__(parent, title="Guía de Atajos de Teclado", size=(700, 540))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        texto_atajos = (
            "Guía Completa de Atajos de Teclado:\n\n"
            "Modos y Aprendizaje:\n"
            "• Control + M: Alternar entre Modo Aprendizaje y Modo Solo Editor profesional.\n"
            "• Control + Enter (o Control + E): Ejecutar código y validar ejercicio.\n"
            "• F3 (o Control + I): Leer la instrucción activa sin mover el foco del editor.\n"
            "• F4: Situar el cursor en la línea exacta del error del Traceback.\n"
            "• F6: Alternar el foco entre el editor de código y la consola de resultados.\n"
            "• Control + Flecha Derecha: Ir al paso siguiente.\n"
            "• Control + Flecha Izquierda: Ir al paso anterior.\n"
            "• Control + P: Pedir una pista escalonada.\n"
            "• F1: Explicar la línea actual con palabras sencillas.\n"
            "• Control + R: Restablecer el código original del ejercicio.\n"
            "• Control + 1: Abrir el Selector de Capítulos del temario.\n"
            "• Control + J: Abrir la consola de pruebas rápidas (REPL).\n"
            "• Control + G: Abrir el diccionario de términos de Python.\n\n"
            "Navegación Estructural y Edición tipo Visual Studio:\n"
            "• Control + Shift + O: Lista accesible de funciones y clases del script.\n"
            "• Alt + N: Salto rápido a la cabecera de la siguiente función o clase.\n"
            "• Alt + P: Salto rápido a la cabecera de la función o clase anterior.\n"
            "• Control + / (o Control + K): Comentar o descomentar la línea actual con '# '.\n"
            "• Control + D: Duplicar la línea actual hacia abajo.\n"
            "• Control + Shift + K: Eliminar la línea actual.\n"
            "• F7: Verificar sintaxis, comillas y balanceo de delimitadores () [] {}.\n"
            "• Control + L: Anunciar la línea y columna actual del cursor.\n"
            "• Control + Espacio: Autocompletar la palabra actual con palabras clave de Python.\n"
            "• Control + 4: Llevar el foco directamente al Editor de código.\n"
            "• Control + 5: Llevar el foco directamente a la Consola de resultados.\n"
            "• Control + 6: Leer por voz la última línea de la consola.\n"
            "• Control + Shift + C: Leer por voz todo el contenido de la consola.\n\n"
            "Archivos y Sistema:\n"
            "• Control + O: Abrir script de Python (.py) externo.\n"
            "• Control + S: Guardar script actual en disco.\n"
            "• F12: Abrir manual de usuario en el navegador web.\n"
            "• Escape: Cerrar el tutor inmediatamente desde cualquier control."
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
        self.mision_ctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size=(-1, 85))
        self.mision_ctrl.SetName("Instrucción del paso activo.")
        self.vbox.Add(self.mision_ctrl, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # 3. Editor de código
        self.lbl_ed = wx.StaticText(self.panel, label="Editor de código:")
        self.vbox.Add(self.lbl_ed, flag=wx.LEFT | wx.TOP, border=12)

        self.edicion = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_PROCESS_TAB)
        self.edicion.SetName("Editor de código")
        self.vbox.Add(self.edicion, proportion=3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # 4. Consola de resultados
        self.lbl_sal = wx.StaticText(self.panel, label="Consola de resultados y diagnóstico:")
        self.vbox.Add(self.lbl_sal, flag=wx.LEFT | wx.TOP, border=12)

        self.salida = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.salida.SetName("Consola de resultados.")
        self.vbox.Add(self.salida, proportion=2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # 5. Barra de botones
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_ejecutar = wx.Button(self.panel, label="Ejecutar (Ctrl+Enter)")
        self.btn_ejecutar.SetName("Botón Ejecutar Código")

        self.btn_pista = wx.Button(self.panel, label="Pedir pista (Ctrl+P)")
        self.btn_pista.SetName("Botón Pedir Pista")

        self.btn_traductor = wx.Button(self.panel, label="Explicar línea (F1)")
        self.btn_traductor.SetName("Botón Explicar Línea")

        self.btn_anterior = wx.Button(self.panel, label="Paso anterior (Ctrl+Izquierda)")
        self.btn_anterior.SetName("Botón Paso Anterior")

        self.btn_siguiente = wx.Button(self.panel, label="Paso siguiente (Ctrl+Derecha)")
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

        # Cargar paso actual con protección total
        self.cargar_paso_actual(anunciar_voz=False)
        self.aplicar_modo_trabajo(anunciar=False)

        # Reproducir señal de inicio de forma confiable
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

    def crear_barra_menus(self):
        menu_bar = wx.MenuBar()

        # 1. Menú Archivo
        m_archivo = wx.Menu()
        item_abrir = m_archivo.Append(wx.ID_ANY, "Abrir archivo...\tCtrl+O", "Carga un script de Python desde el disco")
        item_guardar = m_archivo.Append(wx.ID_ANY, "Guardar script\tCtrl+S", "Guarda el contenido del editor en el archivo")
        item_guardar_como = m_archivo.Append(wx.ID_ANY, "Guardar como...", "Guarda el código con un nuevo nombre")
        m_archivo.AppendSeparator()
        item_salir = m_archivo.Append(wx.ID_EXIT, "Cerrar tutor\tAlt+F4", "Cierra el entorno de aprendizaje")

        self.Bind(wx.EVT_MENU, self.on_abrir_archivo, id=item_abrir.GetId())
        self.Bind(wx.EVT_MENU, self.on_guardar_archivo, id=item_guardar.GetId())
        self.Bind(wx.EVT_MENU, self.on_guardar_como, id=item_guardar_como.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.Close(), id=item_salir.GetId())

        # 2. Menú Edición (Productividad tipo Visual Studio)
        m_edicion = wx.Menu()
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

        self.Bind(wx.EVT_MENU, self.on_mostrar_simbolos, id=item_simbolos.GetId())
        self.Bind(wx.EVT_MENU, self.on_siguiente_definicion, id=item_sig_def.GetId())
        self.Bind(wx.EVT_MENU, self.on_anterior_definicion, id=item_ant_def.GetId())
        self.Bind(wx.EVT_MENU, self.on_comentar_descomentar, id=item_comentar.GetId())
        self.Bind(wx.EVT_MENU, self.on_duplicar_linea, id=item_duplicar.GetId())
        self.Bind(wx.EVT_MENU, self.on_eliminar_linea, id=item_eliminar.GetId())
        self.Bind(wx.EVT_MENU, self.on_verificar_sintaxis, id=item_verificar.GetId())
        self.Bind(wx.EVT_MENU, self.on_anunciar_posicion, id=item_posicion.GetId())

        # 3. Menú Herramientas
        m_herramientas = wx.Menu()
        item_modo = m_herramientas.Append(wx.ID_ANY, "Alternar Modo Aprendizaje / Solo Editor\tCtrl+M", "Conmuta entre el entorno con lecciones y el editor limpio")
        item_error = m_herramientas.Append(wx.ID_ANY, "Ir a la línea del error del Traceback\tF4", "Mueve el cursor exactamente a la línea del fallo")
        item_leer_inst = m_herramientas.Append(wx.ID_ANY, "Leer instrucción del paso activo\tF3", "Lee la consigna actual sin retirar el cursor del editor")
        item_alternar = m_herramientas.Append(wx.ID_ANY, "Alternar foco entre editor y consola\tF6", "Cambia el foco entre el editor de código y la salida")
        item_leer_salida = m_herramientas.Append(wx.ID_ANY, "Leer toda la salida de consola\tCtrl+Shift+C", "Verbaliza todo el texto de la consola sin perder el foco")
        m_herramientas.AppendSeparator()
        item_traductor = m_herramientas.Append(wx.ID_ANY, "Explicar línea de código\tF1", "Traduce la línea de código actual a palabras cotidianas")
        item_repl = m_herramientas.Append(wx.ID_ANY, "Consola de pruebas rápidas (REPL)\tCtrl+J", "Ventana de pruebas inmediatas de una línea")
        item_glosario = m_herramientas.Append(wx.ID_ANY, "Diccionario de términos de Python\tCtrl+G", "Buscador de términos y funciones del lenguaje")
        item_temario = m_herramientas.Append(wx.ID_ANY, "Ir a un capítulo del temario...\tCtrl+1", "Ver el listado completo de capítulos")
        item_reiniciar = m_herramientas.Append(wx.ID_ANY, "Restablecer código del ejercicio\tCtrl+R", "Restaura el código original del paso")

        self.Bind(wx.EVT_MENU, self.on_alternar_modo_trabajo, id=item_modo.GetId())
        self.Bind(wx.EVT_MENU, self.on_ir_al_error, id=item_error.GetId())
        self.Bind(wx.EVT_MENU, self.on_leer_instruccion_actual, id=item_leer_inst.GetId())
        self.Bind(wx.EVT_MENU, self.on_alternar_foco, id=item_alternar.GetId())
        self.Bind(wx.EVT_MENU, self.on_leer_toda_la_salida, id=item_leer_salida.GetId())
        self.Bind(wx.EVT_MENU, self.on_traducir_linea, id=item_traductor.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_repl, id=item_repl.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_glosario, id=item_glosario.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_temario, id=item_temario.GetId())
        self.Bind(wx.EVT_MENU, self.on_reiniciar_codigo, id=item_reiniciar.GetId())

        # 4. Menú Configuración
        m_config = wx.Menu()
        self.item_modo_editor = m_config.AppendCheckItem(wx.ID_ANY, "Modo Solo Editor profesional (ocultar misiones)", "Entorno de edición limpio sin secciones didácticas")
        self.item_linter = m_config.AppendCheckItem(wx.ID_ANY, "Señales sonoras al escribir espacios de sangría", "Emite tonos al cambiar de nivel de sangría PEP 8")
        self.item_sonidos = m_config.AppendCheckItem(wx.ID_ANY, "Sonidos de confirmación, pistas y errores", "Efectos auditivos durante el aprendizaje")
        self.item_modo_editor.Check(self.modo_editor)
        self.item_linter.Check(self.linter_activo)
        self.item_sonidos.Check(self.sonidos_activos)

        self.Bind(wx.EVT_MENU, self.on_toggle_modo_editor_menu, id=self.item_modo_editor.GetId())
        self.Bind(wx.EVT_MENU, self.on_toggle_linter, id=self.item_linter.GetId())
        self.Bind(wx.EVT_MENU, self.on_toggle_sonidos, id=self.item_sonidos.GetId())

        # 5. Menú Ayuda
        m_ayuda = wx.Menu()
        item_doc = m_ayuda.Append(wx.ID_ANY, "Manual de usuario en el navegador\tF12", "Abre la documentación accesible en formato HTML")
        item_atajos = m_ayuda.Append(wx.ID_ANY, "Guía de atajos de teclado\tF2", "Muestra la lista de atajos rápidos")
        item_bienvenida = m_ayuda.Append(wx.ID_ANY, "Mostrar guía de inicio rápido", "Vuelve a abrir la ventana de bienvenida")
        m_ayuda.AppendSeparator()
        item_soporte = m_ayuda.Append(wx.ID_ANY, "Contactar por correo electrónico...", "Escribir al desarrollador para dudas o soporte")
        item_donacion = m_ayuda.Append(wx.ID_ANY, "Colaborar con el proyecto...", "Realizar una donación voluntaria para apoyar el complemento")
        m_ayuda.AppendSeparator()
        item_acerca = m_ayuda.Append(wx.ID_ANY, "Acerca de Aprendizaje de Python con NVDA...", "Información sobre el autor, versión y licencia")

        self.Bind(wx.EVT_MENU, self.on_abrir_doc, id=item_doc.GetId())
        self.Bind(wx.EVT_MENU, self.on_mostrar_atajos, id=item_atajos.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.mostrar_bienvenida(), id=item_bienvenida.GetId())
        self.Bind(wx.EVT_MENU, self.on_soporte, id=item_soporte.GetId())
        self.Bind(wx.EVT_MENU, self.on_donacion, id=item_donacion.GetId())
        self.Bind(wx.EVT_MENU, self.on_acerca, id=item_acerca.GetId())

        menu_bar.Append(m_archivo, "&Archivo")
        menu_bar.Append(m_edicion, "&Edición")
        menu_bar.Append(m_herramientas, "&Herramientas")
        menu_bar.Append(m_config, "&Configuración")
        menu_bar.Append(m_ayuda, "A&yuda")
        self.SetMenuBar(menu_bar)

    def aplicar_modo_trabajo(self, anunciar=False):
        """Aplica la configuración visual según el modo de trabajo (Aprendizaje o Solo Editor)."""
        if self.modo_editor:
            self.lbl_estado.Hide()
            self.mision_ctrl.Hide()
            self.btn_pista.Hide()
            self.btn_traductor.Hide()
            self.btn_anterior.Hide()
            self.btn_siguiente.Hide()
            self.btn_temario.Hide()
            if hasattr(self, 'item_modo_editor'):
                self.item_modo_editor.Check(True)
            self.SetTitle("Aprendizaje de Python con NVDA - [Modo Solo Editor Profesional]")
            self.panel.Layout()
            self.Layout()
            if anunciar:
                msg = "Modo Solo Editor activado. Entorno limpio de edición sin misiones didácticas."
                if speech and hasattr(speech, 'speakMessage'):
                    speech.speakMessage(msg)
                if ui:
                    ui.message(msg)
        else:
            self.lbl_estado.Show()
            self.mision_ctrl.Show()
            self.btn_pista.Show()
            self.btn_traductor.Show()
            self.btn_anterior.Show()
            self.btn_siguiente.Show()
            self.btn_temario.Show()
            if hasattr(self, 'item_modo_editor'):
                self.item_modo_editor.Check(False)
            self.SetTitle("Aprendizaje de Python con NVDA - Entorno Interactivo")
            self.panel.Layout()
            self.Layout()
            if anunciar:
                msg = "Modo Aprendizaje guiado activado. Misiones y temario visibles."
                if speech and hasattr(speech, 'speakMessage'):
                    speech.speakMessage(msg)
                if ui:
                    ui.message(msg)

    def on_alternar_modo_trabajo(self, event=None):
        """Alterna entre el Modo Aprendizaje y el Modo Solo Editor (Ctrl+M)."""
        self.modo_editor = not self.modo_editor
        ProgressManager.set_editor_mode("editor" if self.modo_editor else "learning")
        self.aplicar_modo_trabajo(anunciar=True)
        self.edicion.SetFocus()

    def on_toggle_modo_editor_menu(self, event=None):
        """Manejador para la opción del menú de configuración."""
        if hasattr(self, 'item_modo_editor'):
            self.modo_editor = self.item_modo_editor.IsChecked()
        else:
            self.modo_editor = not self.modo_editor
        ProgressManager.set_editor_mode("editor" if self.modo_editor else "learning")
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
        marca_estado = "[Superado]" if superado else "[Pendiente]"

        titulo_paso = paso.get("titulo", f"Paso {self.paso_idx + 1}")
        texto_encabezado = f"{cap.get('titulo', 'Capítulo')} · Paso {self.paso_idx + 1} de {total_pasos}: {titulo_paso} {marca_estado}"
        self.lbl_estado.SetLabel(texto_encabezado)

        # Construcción segura de la instrucción
        instruccion = paso.get("instruccion")
        if not instruccion:
            if paso.get("tipo") == "quiz":
                preg = paso.get("pregunta", "")
                opciones = paso.get("opciones", [])
                ops_txt = "\n".join(f"{i+1}. {op}" for i, op in enumerate(opciones))
                instruccion = f"Pregunta de verificación conceptual:\n{preg}\n\nOpciones:\n{ops_txt}\n\nEscribe el número de la respuesta correcta (1, 2 o 3) en el editor y pulsa Control + Enter."
            else:
                instruccion = "Sigue las instrucciones del ejercicio y ejecuta con Control + Enter."

        self.mision_ctrl.SetValue(instruccion)
        self.edicion.SetValue(paso.get("codigo", ""))
        self.salida.SetValue("")

        if anunciar_voz and ui:
            ui.message(f"{titulo_paso}. {instruccion}")

    def on_ejecutar(self, event=None):
        src = self.edicion.GetValue()

        # Si estamos en Modo Solo Editor profesional: ejecución libre sin misiones
        if self.modo_editor:
            bal_err = comprobar_balanceo_delimitadores(src)
            if bal_err:
                self.ultimo_error_linea = bal_err.get("linea")
                self.ultimo_error_msg = bal_err.get("mensaje")
                self.salida.SetValue(f"=== AVISO DE SINTAXIS ===\n{bal_err['mensaje']}\n\nPresione F4 para ir a la línea del error.")
                if self.sonidos_activos:
                    SoundManager.play('sintaxis_aviso')
                if ui:
                    ui.message(f"Error de delimitador: {bal_err['mensaje']}. Presione F4 para ir a la línea.")
                return

            res = ejecutar_codigo_seguro(src, timeout=5.0)
            salida_txt = []
            if getattr(res, 'keyboard_warning', None):
                salida_txt.append("=== AVISO DE ESCRITURA ===")
                salida_txt.append(res.keyboard_warning)
                salida_txt.append("")

            salida_txt.append("=== SALIDA DE EJECUCIÓN ===")
            salida_txt.append(res.output if res.output else "(Sin salida de consola)")

            if not res.success:
                self.ultimo_error_linea = res.error_line
                self.ultimo_error_msg = res.error_msg
                if res.friendly_explanation:
                    salida_txt.append("")
                    salida_txt.append(f"Aviso de ejecución: {res.friendly_explanation}")
                    salida_txt.append("Presione F4 para posicionar el cursor en la línea del fallo.")
                if self.sonidos_activos:
                    SoundManager.play('error')
                if ui:
                    msg_err = res.friendly_explanation or res.error_msg or "Error durante la ejecución"
                    ui.message(f"Error: {msg_err}. Pulse F4 para ir al error.")
            else:
                self.ultimo_error_linea = None
                self.ultimo_error_msg = None
                if self.sonidos_activos:
                    SoundManager.play('exito')
                if ui:
                    ui.message("Ejecución finalizada con éxito.")

            self.salida.SetValue("\n".join(salida_txt))
            self.salida.SetFocus()
            return

        # Modo Aprendizaje Guiado
        cap = CURRICULUM[self.cap_idx]
        paso = cap["pasos"][self.paso_idx]

        tipo_paso = paso.get("tipo", "observar")
        reporte_pruebas = []
        aprobado = False

        if tipo_paso == "quiz":
            cor = str(paso.get("correcta", 0) + 1)
            lineas_resp = [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")]
            res_val = "".join(lineas_resp)
            if cor in res_val:
                aprobado = True
                reporte_pruebas.append(f"[✓] Respuesta correcta. {paso.get('explicacion', '')}")
            else:
                aprobado = False
                reporte_pruebas.append("[✗] La opción seleccionada no es la correcta. Revisa las opciones en la instrucción e inténtalo de nuevo.")

            res_output = f"Opción enviada: {res_val if res_val else '(vacía)'}"
            friendly_err = ""
            self.ultimo_error_linea = None
            self.ultimo_error_msg = None
        else:
            # Comprobar delimitadores antes de ejecutar
            bal_err = comprobar_balanceo_delimitadores(src)
            if bal_err:
                self.ultimo_error_linea = bal_err.get("linea")
                self.ultimo_error_msg = bal_err.get("mensaje")

            res = ejecutar_codigo_seguro(src, timeout=3.0)
            res_output = res.output
            friendly_err = res.friendly_explanation

            if not res.success:
                self.ultimo_error_linea = res.error_line
                self.ultimo_error_msg = res.error_msg or friendly_err

            if res.success:
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
                            reporte_pruebas.append(f"[✓] {p.get('nombre', 'Prueba')}: Aprobada")
                        else:
                            reporte_pruebas.append(f"[✗] {p.get('nombre', 'Prueba')}: No superada")
                            todas_ok = False
                    aprobado = todas_ok
                elif "validar" in paso and callable(paso["validar"]):
                    try:
                        aprobado = paso["validar"](src, res.output, res.local_ns)
                    except Exception:
                        aprobado = False
                else:
                    aprobado = True
            else:
                aprobado = False

        lineas_reporte = []
        if tipo_paso != "quiz" and getattr(res, 'keyboard_warning', None):
            lineas_reporte.append("=== AVISO DE ESCRITURA ===")
            lineas_reporte.append(res.keyboard_warning)
            lineas_reporte.append("")

        lineas_reporte.append("=== SALIDA DE CONSOLA ===")
        lineas_reporte.append(res_output)
        lineas_reporte.append("")

        if reporte_pruebas:
            lineas_reporte.append("=== EVALUACIÓN ===")
            lineas_reporte.extend(reporte_pruebas)
            lineas_reporte.append("")

        if aprobado:
            lineas_reporte.append("¡Misión superada con éxito! Puedes avanzar al siguiente paso con Control + Flecha Derecha.")
            self.salida.SetValue("\n".join(lineas_reporte))
            self.salida.SetFocus()

            ProgressManager.mark_step_completed(self.cap_idx, self.paso_idx)

            if self.sonidos_activos:
                SoundManager.play('exito')
            if ui:
                ui.message("¡Misión superada! Pulsa Control + Flecha Derecha para avanzar.")
        else:
            if paso.get("salida_esperada"):
                comp = generar_comparacion_salida(paso["salida_esperada"], res_output)
                lineas_reporte.append("=== COMPARACIÓN FORMATIVA ===")
                lineas_reporte.append(comp)
                lineas_reporte.append("")

            if friendly_err:
                lineas_reporte.append(f"Aviso de ejecución: {friendly_err}")
                lineas_reporte.append("Pulsa F4 para posicionar el cursor en la línea del fallo.")
            else:
                lineas_reporte.append("La solución aún no cumple el objetivo del ejercicio. Pulsa Control + P para solicitar una pista.")

            self.salida.SetValue("\n".join(lineas_reporte))
            self.salida.SetFocus()

            if self.sonidos_activos:
                SoundManager.play('error')
            if ui:
                if tipo_paso != "quiz" and getattr(res, 'keyboard_warning', None):
                    ui.message(res.keyboard_warning)
                elif friendly_err:
                    ui.message(f"{friendly_err}. Pulsa F4 para ir al error.")
                else:
                    ui.message("Solución incompleta. Pulsa Control + P para recibir una pista.")

    def on_pista(self, event=None):
        cap = CURRICULUM[self.cap_idx]
        paso = cap["pasos"][self.paso_idx]
        pistas = paso.get("pistas", ["Revisa el enunciado de la misión en la parte superior e intenta ejecutar nuevamente."])

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

        if speech and hasattr(speech, 'speakMessage'):
            speech.speakMessage(traduccion)
        if ui:
            ui.message(traduccion)

    # =========================================================================
    # Herramientas del Editor (Productividad estilo Visual Studio / IDE)
    # =========================================================================

    def on_comentar_descomentar(self, event=None):
        """Alterna el comentario '#' al inicio de la línea donde está el cursor."""
        try:
            pt = self.edicion.GetInsertionPoint()
            txt = self.edicion.GetValue()
            row = txt[:pt].count('\n')
            linea = self.edicion.GetLineText(row)

            lineas = txt.split('\n')
            if linea.lstrip().startswith('#'):
                # Descomentar
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
                # Comentar
                lineas[row] = '# ' + linea
                msg = "Línea comentada"

            nueva_txt = '\n'.join(lineas)
            self.edicion.SetValue(nueva_txt)
            self.edicion.SetInsertionPoint(min(pt, len(nueva_txt)))

            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
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

            # Posicionar en la nueva línea
            nuevo_pt = len('\n'.join(lineas[:row + 1])) + 1
            self.edicion.SetInsertionPoint(min(nuevo_pt, len(self.edicion.GetValue())))

            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage("Línea duplicada")
            if ui:
                ui.message("Línea duplicada")
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

            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage("Línea eliminada")
            if ui:
                ui.message("Línea eliminada")
        except Exception:
            pass

    def on_verificar_sintaxis(self, event=None):
        """Analiza la sintaxis y el balanceo de delimitadores del código sin ejecutarlo (F7)."""
        src = self.edicion.GetValue()

        # 1. Comprobación de delimitadores (paréntesis, corchetes, llaves y comillas)
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
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
            return

        # 2. Compilación en memoria para sintaxis general de Python
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

        if speech and hasattr(speech, 'speakMessage'):
            speech.speakMessage(msg)
        if ui:
            ui.message(msg)

    def on_ir_al_error(self, event=None):
        """Mueve el cursor exactamente a la línea del último error detectado (F4)."""
        if self.ultimo_error_linea is None:
            msg = "No hay registro de errores recientes de ejecución o sintaxis."
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
            return

        src = self.edicion.GetValue()
        lineas = src.split('\n')
        linea_num = max(1, min(self.ultimo_error_linea, len(lineas)))
        pt = len('\n'.join(lineas[:linea_num - 1])) + 1 if linea_num > 1 else 0
        self.edicion.SetInsertionPoint(min(pt, len(src)))
        self.edicion.SetFocus()

        detalle = self.ultimo_error_msg or "error detectado"
        msg = f"Cursor en línea {linea_num}: {detalle}"
        if speech and hasattr(speech, 'speakMessage'):
            speech.speakMessage(msg)
        if ui:
            ui.message(msg)

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
                if speech and hasattr(speech, 'speakMessage'):
                    speech.speakMessage(msg)
                if ui:
                    ui.message(msg)
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
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
        else:
            msg = "No hay más definiciones adelante."
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)

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
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
        else:
            msg = "No hay definiciones anteriores."
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)

    def on_leer_toda_la_salida(self, event=None):
        """Verbaliza por voz todo el contenido de la consola sin retirar el foco del editor (Ctrl+Shift+C)."""
        txt = self.salida.GetValue().strip()
        if not txt:
            msg = "Consola vacía."
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
            return

        if speech and hasattr(speech, 'speakMessage'):
            speech.speakMessage(txt)
        if ui:
            ui.message(txt)

    def on_anunciar_posicion(self, event=None):
        """Informa verbalmente la línea y columna actual del cursor (Ctrl+L)."""
        pt = self.edicion.GetInsertionPoint()
        txt = self.edicion.GetValue()
        row = txt[:pt].count('\n') + 1
        last_nl = txt[:pt].rfind('\n')
        col = (pt - last_nl) if last_nl != -1 else (pt + 1)
        total_lineas = txt.count('\n') + 1

        msg = f"Línea {row} de {total_lineas}, columna {col}."
        if speech and hasattr(speech, 'speakMessage'):
            speech.speakMessage(msg)
        if ui:
            ui.message(msg)

    def on_autocompletar(self, event=None):
        """Asistente de autocompletado accesible (Ctrl+Espacio)."""
        try:
            pt = self.edicion.GetInsertionPoint()
            txt = self.edicion.GetValue()
            prefijo = txt[:pt].split()[-1] if txt[:pt].split() else ""
            prefijo = re.sub(r'[^a-zA-Z0-9_]', '', prefijo)

            if not prefijo:
                if ui:
                    ui.message("Escribe al menos una letra para autocompletar.")
                return

            coincidencias = [p for p in self.PALABRAS_CLAVE if p.startswith(prefijo) and p != prefijo]
            if not coincidencias:
                if ui:
                    ui.message(f"Sin sugerencias para '{prefijo}'.")
                return

            if len(coincidencias) == 1:
                eleccion = coincidencias[0]
                resto = eleccion[len(prefijo):]
                self.edicion.WriteText(resto)
                if speech and hasattr(speech, 'speakMessage'):
                    speech.speakMessage(eleccion)
                if ui:
                    ui.message(f"Completado: {eleccion}")
            else:
                sugerencias_txt = ", ".join(coincidencias[:6])
                if speech and hasattr(speech, 'speakMessage'):
                    speech.speakMessage(sugerencias_txt)
                if ui:
                    ui.message(f"Sugerencias: {sugerencias_txt}")
        except Exception:
            pass

    # =========================================================================
    # Navegación entre pasos
    # =========================================================================

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
        if ui:
            ui.message("Código del ejercicio restablecido a su estado inicial.")

    def on_mostrar_atajos(self, event=None):
        dlg = ShortcutsDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def on_soporte(self, event=None):
        url = "mailto:kevinvelasquezvargas@gmail.com?subject=Soporte%20-%20Aprendizaje%20de%20Python%20con%20NVDA"
        try:
            webbrowser.open(url)
            if ui:
                ui.message("Abriendo cliente de correo para contactar con soporte...")
        except Exception:
            wx.MessageBox(
                "Para recibir soporte o enviar sugerencias, por favor escribe a:\nkevinvelasquezvargas@gmail.com",
                "Soporte y Contacto",
                wx.OK | wx.ICON_INFORMATION
            )

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
                wx.OK | wx.ICON_INFORMATION
            )

    def on_key_down_edicion(self, event):
        keycode = event.GetKeyCode()
        # Escape CIERRA inmediatamente la ventana
        if keycode == wx.WXK_ESCAPE:
            self.Close()
            return
        elif keycode == wx.WXK_TAB:
            if event.ShiftDown():
                self.mision_ctrl.SetFocus()
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

        # Tecla Escape cierra la aplicación desde cualquier parte
        if keycode == wx.WXK_ESCAPE:
            self.Close()
            return

        # F1: Explicar línea de código
        if keycode == wx.WXK_F1:
            self.on_traducir_linea()
            return

        # F2: Atajos de teclado
        if keycode == wx.WXK_F2:
            self.on_mostrar_atajos()
            return

        # F3: Leer instrucción activa sin mover foco
        if keycode == wx.WXK_F3:
            self.on_leer_instruccion_actual()
            return

        # F4: Ir a la línea del error del Traceback
        if keycode == wx.WXK_F4:
            self.on_ir_al_error()
            return

        # F6: Alternar foco entre editor y consola
        if keycode == wx.WXK_F6:
            self.on_alternar_foco()
            return

        # F7: Verificar sintaxis y delimitadores
        if keycode == wx.WXK_F7:
            self.on_verificar_sintaxis()
            return

        # F12: Manual en navegador
        if keycode == wx.WXK_F12:
            self.on_abrir_doc()
            return

        # Atajos con Alt (Navegación estructural)
        if event.AltDown() and not event.ControlDown() and not event.ShiftDown():
            if keycode in (ord('N'), ord('n')):
                self.on_siguiente_definicion()
                return
            elif keycode in (ord('P'), ord('p')):
                self.on_anterior_definicion()
                return

        if modifiers == wx.MOD_CONTROL:
            if keycode in (ord('C'), ord('V'), ord('X'), ord('Z'), ord('Y'), ord('A')):
                event.Skip()
                return

            if keycode in (wx.WXK_RETURN, ord('E')):
                self.on_ejecutar(None)
                return
            elif keycode == ord('M'):
                self.on_alternar_modo_trabajo()
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
            elif keycode == ord('J'):
                self.on_abrir_repl(None)
                return
            elif keycode == ord('G'):
                self.on_abrir_glosario(None)
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
            elif keycode == wx.WXK_RIGHT:
                self.on_paso_siguiente(None)
                return
            elif keycode == wx.WXK_LEFT:
                self.on_paso_anterior(None)
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
            if keycode == ord('K'):
                self.on_eliminar_linea(None)
                return
            elif keycode == ord('O'):
                self.on_mostrar_simbolos()
                return
            elif keycode == ord('C'):
                self.on_leer_toda_la_salida()
                return
            event.Skip()
        else:
            if keycode == ord(':') and self.sonidos_activos:
                SoundManager.play('bloque')
            event.Skip()

    def on_leer_instruccion_actual(self, event=None):
        """Lee la consigna del paso actual por voz y braille sin retirar el foco del editor de código."""
        try:
            cap = CURRICULUM[self.cap_idx]
            paso = cap["pasos"][self.paso_idx]
            num_paso = self.paso_idx + 1
            total_pasos = len(cap["pasos"])
            instruccion = paso.get("instruccion", "")
            if not instruccion:
                instruccion = self.mision_ctrl.GetValue().strip()
            msg = f"Paso {num_paso} de {total_pasos}: {instruccion}"
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
        except Exception:
            pass

    def on_alternar_foco(self, event=None):
        """Alterna el foco entre el editor de código y la consola de resultados (F6)."""
        foco_actual = wx.Window.FindFocus()
        if foco_actual == self.salida:
            self.edicion.SetFocus()
            if ui:
                ui.message("Foco en el editor de código")
        else:
            self.salida.SetFocus()
            if ui:
                ui.message("Foco en la consola de resultados")

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
                wx.MessageBox(f"Error al abrir archivo: {e}", "Error", wx.OK | wx.ICON_ERROR)
        dlg.Destroy()

    def on_guardar_archivo(self, event=None):
        if self.archivo_abierto:
            try:
                with open(self.archivo_abierto, "w", encoding="utf-8") as f:
                    f.write(self.edicion.GetValue())
                if ui:
                    ui.message(f"Guardado en {os.path.basename(self.archivo_abierto)}")
            except Exception as e:
                wx.MessageBox(f"Error al guardar: {e}", "Error", wx.OK | wx.ICON_ERROR)
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
                wx.MessageBox(f"Error al guardar: {e}", "Error", wx.OK | wx.ICON_ERROR)
        dlg.Destroy()

    def on_toggle_linter(self, event):
        self.linter_activo = self.item_linter.IsChecked()
        ProgressManager.set_setting("linter_enabled", self.linter_activo)
        estado = "activadas" if self.linter_activo else "desactivadas"
        if ui:
            ui.message(f"Señales de sangría {estado}")

    def on_toggle_sonidos(self, event):
        self.sonidos_activos = self.item_sonidos.IsChecked()
        ProgressManager.set_setting("sound_enabled", self.sonidos_activos)
        estado = "activados" if self.sonidos_activos else "desactivados"
        if ui:
            ui.message(f"Efectos de sonido {estado}")

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
            ui.message("No fue posible abrir el manual de usuario en el navegador.")

    def on_acerca(self, event=None):
        info = (
            "Aprendizaje de Python con NVDA (Versión 2.0.0)\n\n"
            "Entorno de aprendizaje accesible diseñado para personas con discapacidad visual.\n"
            "Incorpora metodología práctica, explicación de código en palabras cotidianas,\n"
            "linter acústico de sangría PEP 8, herramientas de edición de código y temario completo.\n\n"
            "Autor: Kevin Andrés Velasquez Vargas\n"
            "Contacto: kevinvelasquezvargas@gmail.com\n"
            "Donaciones: https://www.paypal.me/kevinvelasquezvargas\n"
            "Licencia: GNU General Public License v3.0 (GPLv3)\n"
            "Compatibilidad: NVDA 2022.1.0 hasta 2026.3.0"
        )
        wx.MessageBox(info, "Acerca de Aprendizaje de Python con NVDA", wx.OK | wx.ICON_INFORMATION)

    def on_close(self, event):
        prog = ProgressManager.load_progress()
        prog["current_chapter"] = self.cap_idx
        prog["current_step"] = self.paso_idx
        ProgressManager.save_progress(prog)
        self.Destroy()
