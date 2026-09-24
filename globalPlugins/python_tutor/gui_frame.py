# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/gui_frame.py
# Propósito: Interfaz gráfica Action-First accesible y pedagógica para NVDA.
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
from .executor import ejecutar_codigo_seguro
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
            opciones.append(f"{icono}{cap['titulo']}")

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
        super(HintDialog, self).__init__(parent, title="Pista de Asistencia Pedagógica", size=(620, 380))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(panel, label=f"Pista disponible (Nivel {nivel_actual + 1} de {len(pistas)}):")
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        texto_pista = pistas[nivel_actual] if nivel_actual < len(pistas) else pistas[-1]
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
        super(WelcomeDialog, self).__init__(parent, title="Bienvenido a Aprendizaje de Python con NVDA", size=(700, 530))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        mensaje = (
            "¡Te damos la bienvenida al entorno accesible de Aprendizaje de Python con NVDA!\n\n"
            "Este complemento está diseñado para que cualquier persona aprenda a programar paso a paso, "
            "desde cero, mediante la práctica directa en el editor de código.\n\n"
            "Atajos de teclado esenciales:\n"
            "• Control + Enter: Ejecutar el código del editor y evaluar la misión.\n"
            "• Control + Flecha Derecha: Avanzar al siguiente paso del capítulo.\n"
            "• Control + Flecha Izquierda: Retroceder al paso anterior.\n"
            "• Control + P: Pedir una pista de asistencia pedagógica.\n"
            "• F1 (o Control + H): Traductor a Lenguaje Humano (explica la línea donde está el cursor).\n"
            "• F2: Consultar la lista completa de atajos de teclado.\n"
            "• Control + J: Abrir el Laboratorio Rápido (REPL) para pruebas de una línea.\n"
            "• Control + G: Abrir el Glosario de términos y funciones.\n"
            "• Control + 1: Abrir el Selector de Capítulos del temario.\n"
            "• Escape: Cerrar la ventana del tutor en cualquier momento.\n\n"
            "¡El cursor se posicionará en el editor para que comiences ahora mismo!"
        )

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(mensaje)
        txt.SetName("Mensaje de bienvenida y guía rápida")
        vbox.Add(txt, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        prog = ProgressManager.load_progress()
        self.chk_mostrar = wx.CheckBox(panel, label="Mostrar este diálogo de bienvenida al iniciar")
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
        super(ShortcutsDialog, self).__init__(parent, title="Guía de Atajos de Teclado", size=(680, 500))
        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        texto_atajos = (
            "Atajos de Teclado - Aprendizaje de Python con NVDA:\n\n"
            "• Control + Enter (o Control + E): Ejecutar código del editor y validar la solución.\n"
            "• Control + Flecha Derecha: Ir al paso siguiente.\n"
            "• Control + Flecha Izquierda: Ir al paso anterior.\n"
            "• Control + P: Pedir una pista escalonada.\n"
            "• F1 (o Control + H): Traductor a Lenguaje Humano (explica la línea del cursor).\n"
            "• F2: Mostrar esta lista de atajos.\n"
            "• Control + J: Abrir el Laboratorio Rápido (REPL).\n"
            "• Control + G: Abrir el Glosario de términos.\n"
            "• Control + 1: Abrir el Selector de Capítulos.\n"
            "• Control + R: Reiniciar el ejercicio actual a su código original.\n"
            "• Control + O: Abrir un archivo de script Python externo.\n"
            "• Control + S: Guardar el script actual en disco.\n"
            "• Control + 4: Llevar el foco directamente al Editor de código.\n"
            "• Control + 5: Llevar el foco directamente a la Consola de resultados.\n"
            "• Control + 6: Leer por voz la última línea emitida en consola.\n"
            "• Escape: Cerrar el tutor inmediatamente."
        )

        txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        txt.SetValue(texto_atajos)
        txt.SetName("Lista de atajos de teclado")
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
        super(GlossaryDialog, self).__init__(parent, title="Glosario Interactivo de Python", size=(720, 520))
        self.terminos = sorted(list(GLOSARIO.keys()))
        self.filtrados = list(self.terminos)

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Campo de búsqueda
        search_box = wx.BoxSizer(wx.HORIZONTAL)
        lbl = wx.StaticText(panel, label="Buscar término:")
        search_box.Add(lbl, flag=wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border=8)
        self.search_ctrl = wx.TextCtrl(panel)
        self.search_ctrl.SetName("Escribe aquí el comando o concepto para buscar.")
        search_box.Add(self.search_ctrl, proportion=1, flag=wx.EXPAND)
        main_sizer.Add(search_box, flag=wx.EXPAND | wx.ALL, border=10)

        # Contenido
        content_box = wx.BoxSizer(wx.HORIZONTAL)
        self.list_box = wx.ListBox(panel, choices=self.terminos)
        self.list_box.SetName("Términos disponibles.")
        content_box.Add(self.list_box, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=10)

        self.def_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.def_ctrl.SetName("Significado del término.")
        content_box.Add(self.def_ctrl, proportion=2, flag=wx.EXPAND)
        main_sizer.Add(content_box, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        btn_cerrar = wx.Button(panel, wx.ID_CANCEL, label="Cerrar Glosario")
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


class TutorFrame(wx.Frame):
    """
    Ventana principal del entorno interactivo Aprendizaje de Python con NVDA.
    Enfoca de entrada el editor de código, permitiendo aprender mediante la acción directa.
    """
    def __init__(self, parent):
        super(TutorFrame, self).__init__(parent, title="Aprendizaje de Python con NVDA", size=(980, 840))

        # Cargar estado de progreso del alumno y configuración
        prog = ProgressManager.load_progress()
        self.cap_idx = max(0, min(prog.get("current_chapter", 0), len(CURRICULUM) - 1))
        self.paso_idx = max(0, prog.get("current_step", 0))

        self.nivel_pista = 0
        self.linter_activo = prog.get("linter_enabled", True)
        self.sonidos_activos = prog.get("sound_enabled", True)
        self._last_linter_line = -1
        self._last_linter_indent = -1
        self.archivo_abierto = None

        self.crear_barra_menus()

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 1. Barra de Estado del Ejercicio
        self.lbl_estado = wx.StaticText(panel, label="")
        font_estado = self.lbl_estado.GetFont()
        font_estado.SetWeight(wx.FONTWEIGHT_BOLD)
        self.lbl_estado.SetFont(font_estado)
        vbox.Add(self.lbl_estado, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        # 2. Instrucción del Paso Activo
        self.mision_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size=(-1, 80))
        self.mision_ctrl.SetName("Instrucción del paso activo.")
        vbox.Add(self.mision_ctrl, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # 3. Editor de Código Fuente
        lbl_ed = wx.StaticText(panel, label="Editor de código:")
        vbox.Add(lbl_ed, flag=wx.LEFT | wx.TOP, border=12)

        self.edicion = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_PROCESS_TAB)
        self.edicion.SetName("Editor de código")
        vbox.Add(self.edicion, proportion=3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # 4. Consola de Resultados
        lbl_sal = wx.StaticText(panel, label="Consola de resultados y diagnóstico:")
        vbox.Add(lbl_sal, flag=wx.LEFT | wx.TOP, border=12)

        self.salida = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.salida.SetName("Consola de resultados.")
        vbox.Add(self.salida, proportion=2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # 5. Barra de Acciones
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_ejecutar = wx.Button(panel, label="Ejecutar (Ctrl+Enter)")
        self.btn_ejecutar.SetName("Botón Ejecutar Código")

        self.btn_pista = wx.Button(panel, label="Pedir pista (Ctrl+P)")
        self.btn_pista.SetName("Botón Pedir Pista")

        self.btn_traductor = wx.Button(panel, label="Traducir línea (F1)")
        self.btn_traductor.SetName("Botón Traductor a Lenguaje Humano")

        self.btn_anterior = wx.Button(panel, label="Paso anterior (Ctrl+Izquierda)")
        self.btn_anterior.SetName("Botón Paso Anterior")

        self.btn_siguiente = wx.Button(panel, label="Paso siguiente (Ctrl+Derecha)")
        self.btn_siguiente.SetName("Botón Paso Siguiente")

        self.btn_temario = wx.Button(panel, label="Temario (Ctrl+1)")
        self.btn_temario.SetName("Botón Selector de Capítulos")

        self.btn_cerrar = wx.Button(panel, wx.ID_CANCEL, label="Cerrar (Escape)")
        self.btn_cerrar.SetName("Botón Cerrar Tutor")

        hbox.Add(self.btn_ejecutar, flag=wx.RIGHT, border=6)
        hbox.Add(self.btn_pista, flag=wx.RIGHT, border=6)
        hbox.Add(self.btn_traductor, flag=wx.RIGHT, border=6)
        hbox.Add(self.btn_anterior, flag=wx.RIGHT, border=6)
        hbox.Add(self.btn_siguiente, flag=wx.RIGHT, border=6)
        hbox.Add(self.btn_temario, flag=wx.RIGHT, border=6)
        hbox.Add(self.btn_cerrar)

        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.ALL, border=12)
        panel.SetSizer(vbox)

        # Enlace de eventos
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

        # Sonido de inicio asegurado
        SoundManager.initialize()
        if self.sonidos_activos:
            SoundManager.play('inicio')

        self.Center()
        self.edicion.SetFocus()

        # Diálogo de bienvenida si está configurado
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

        # Archivo
        m_archivo = wx.Menu()
        item_abrir = m_archivo.Append(wx.ID_ANY, "Abrir archivo...\tCtrl+O", "Cargar un script externo")
        item_guardar = m_archivo.Append(wx.ID_ANY, "Guardar script\tCtrl+S", "Guardar el contenido del editor")
        item_guardar_como = m_archivo.Append(wx.ID_ANY, "Guardar como...", "Guardar con un nuevo nombre")
        m_archivo.AppendSeparator()
        item_salir = m_archivo.Append(wx.ID_EXIT, "Cerrar tutor\tAlt+F4", "Cierra el entorno de aprendizaje")

        self.Bind(wx.EVT_MENU, self.on_abrir_archivo, id=item_abrir.GetId())
        self.Bind(wx.EVT_MENU, self.on_guardar_archivo, id=item_guardar.GetId())
        self.Bind(wx.EVT_MENU, self.on_guardar_como, id=item_guardar_como.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.Close(), id=item_salir.GetId())

        # Herramientas
        m_herramientas = wx.Menu()
        item_traductor = m_herramientas.Append(wx.ID_ANY, "Traductor a Lenguaje Humano\tF1", "Explica la línea de código actual")
        item_repl = m_herramientas.Append(wx.ID_ANY, "Laboratorio Rápido (REPL)\tCtrl+J", "Consola interactiva de una línea")
        item_glosario = m_herramientas.Append(wx.ID_ANY, "Consultar Glosario\tCtrl+G", "Buscador de términos y funciones")
        item_temario = m_herramientas.Append(wx.ID_ANY, "Selector de Capítulos\tCtrl+1", "Ver el temario completo")
        item_reiniciar = m_herramientas.Append(wx.ID_ANY, "Reiniciar Ejercicio Actual\tCtrl+R", "Restablece el código original")

        self.Bind(wx.EVT_MENU, self.on_traducir_linea, id=item_traductor.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_repl, id=item_repl.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_glosario, id=item_glosario.GetId())
        self.Bind(wx.EVT_MENU, self.on_abrir_temario, id=item_temario.GetId())
        self.Bind(wx.EVT_MENU, self.on_reiniciar_codigo, id=item_reiniciar.GetId())

        # Configuración
        m_config = wx.Menu()
        self.item_linter = m_config.AppendCheckItem(wx.ID_ANY, "Linter Acústico de Sangría PEP 8", "Tonos al cambiar de sangría")
        self.item_sonidos = m_config.AppendCheckItem(wx.ID_ANY, "Señales Sonoras Interactivas", "Sonidos de inicio, éxito, error y pistas")
        self.item_linter.Check(self.linter_activo)
        self.item_sonidos.Check(self.sonidos_activos)

        self.Bind(wx.EVT_MENU, self.on_toggle_linter, id=self.item_linter.GetId())
        self.Bind(wx.EVT_MENU, self.on_toggle_sonidos, id=self.item_sonidos.GetId())

        # Ayuda
        m_ayuda = wx.Menu()
        item_doc = m_ayuda.Append(wx.ID_ANY, "Manual del Usuario (HTML)", "Abre el manual accesible en el navegador")
        item_atajos = m_ayuda.Append(wx.ID_ANY, "Atajos de Teclado\tF2", "Muestra la lista de combinaciones de teclas")
        item_bienvenida = m_ayuda.Append(wx.ID_ANY, "Mensaje de Bienvenida", "Vuelve a mostrar la guía inicial")
        m_ayuda.AppendSeparator()
        item_soporte = m_ayuda.Append(wx.ID_ANY, "Soporte y Contacto...", "Enviar correo de asistencia al autor")
        item_donacion = m_ayuda.Append(wx.ID_ANY, "Realizar una Donación...", "Apoyar el desarrollo libre del complemento")
        m_ayuda.AppendSeparator()
        item_acerca = m_ayuda.Append(wx.ID_ANY, "Acerca de Aprendizaje de Python con NVDA", "Créditos y versión")

        self.Bind(wx.EVT_MENU, self.on_abrir_doc, id=item_doc.GetId())
        self.Bind(wx.EVT_MENU, self.on_mostrar_atajos, id=item_atajos.GetId())
        self.Bind(wx.EVT_MENU, lambda e: self.mostrar_bienvenida(), id=item_bienvenida.GetId())
        self.Bind(wx.EVT_MENU, self.on_soporte, id=item_soporte.GetId())
        self.Bind(wx.EVT_MENU, self.on_donacion, id=item_donacion.GetId())
        self.Bind(wx.EVT_MENU, self.on_acerca, id=item_acerca.GetId())

        menu_bar.Append(m_archivo, "&Archivo")
        menu_bar.Append(m_herramientas, "&Herramientas")
        menu_bar.Append(m_config, "&Configuración")
        menu_bar.Append(m_ayuda, "A&yuda")
        self.SetMenuBar(menu_bar)

    def cargar_paso_actual(self, anunciar_voz=True):
        cap = CURRICULUM[self.cap_idx]
        total_pasos = len(cap["pasos"])
        if self.paso_idx >= total_pasos:
            self.paso_idx = total_pasos - 1

        paso = cap["pasos"][self.paso_idx]
        self.nivel_pista = 0
        self._last_linter_line = -1
        self._last_linter_indent = -1

        superado = ProgressManager.is_step_completed(self.cap_idx, self.paso_idx)
        marca_estado = "[Superado]" if superado else "[Pendiente]"

        texto_encabezado = f"{cap['titulo']} · Paso {self.paso_idx + 1} de {total_pasos}: {paso['titulo']} {marca_estado}"
        self.lbl_estado.SetLabel(texto_encabezado)

        self.mision_ctrl.SetValue(paso["instruccion"])
        self.edicion.SetValue(paso.get("codigo", ""))
        self.salida.SetValue("")

        if anunciar_voz and ui:
            ui.message(f"{paso['titulo']}. {paso['instruccion']}")

    def on_ejecutar(self, event=None):
        cap = CURRICULUM[self.cap_idx]
        paso = cap["pasos"][self.paso_idx]
        src = self.edicion.GetValue()

        res = ejecutar_codigo_seguro(src, timeout=3.0)

        aprobado = False
        reporte_pruebas = []

        if res.success:
            if "pruebas" in paso:
                todas_ok = True
                for p in paso["pruebas"]:
                    try:
                        ok = p["check"](src, res.output, res.local_ns)
                    except Exception:
                        ok = False
                    if ok:
                        reporte_pruebas.append(f"[✓] {p['nombre']}: Aprobada")
                    else:
                        reporte_pruebas.append(f"[✗] {p['nombre']}: No superada")
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
        lineas_reporte.append("=== SALIDA DE CONSOLA ===")
        lineas_reporte.append(res.output)
        lineas_reporte.append("")

        if reporte_pruebas:
            lineas_reporte.append("=== EVALUACIÓN DE PRUEBAS ===")
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
            if not res.success:
                lineas_reporte.append(f"Aviso de ejecución: {res.friendly_explanation}")
            else:
                lineas_reporte.append("La solución aún no cumple el objetivo del ejercicio. Pulsa Control + P para solicitar una pista.")

            self.salida.SetValue("\n".join(lineas_reporte))
            self.salida.SetFocus()

            if self.sonidos_activos:
                SoundManager.play('error')
            if ui:
                if not res.success:
                    ui.message(res.friendly_explanation)
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
        """Traduce la línea de código actual a lenguaje natural cotidiano."""
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

    def on_paso_siguiente(self, event=None):
        cap = CURRICULUM[self.cap_idx]
        if self.paso_idx < len(cap["pasos"]) - 1:
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
                "Puedes realizar una donación voluntaria para apoyar el proyecto en:\nhttps://www.paypal.me/kevinvelasquezvargas",
                "Realizar una Donación",
                wx.OK | wx.ICON_INFORMATION
            )

    def on_key_down_edicion(self, event):
        keycode = event.GetKeyCode()
        # Escape CIERRA la ventana del tutor inmediatamente
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

        # Tecla Escape en cualquier control de la ventana la cierra inmediatamente
        if keycode == wx.WXK_ESCAPE:
            self.Close()
            return

        # F1: Traductor a lenguaje humano
        if keycode == wx.WXK_F1:
            self.on_traducir_linea()
            return

        # F2: Atajos de teclado
        if keycode == wx.WXK_F2:
            self.on_mostrar_atajos()
            return

        if modifiers == wx.MOD_CONTROL:
            if keycode in (ord('C'), ord('V'), ord('X'), ord('Z'), ord('Y'), ord('A')):
                event.Skip()
                return

            if keycode in (wx.WXK_RETURN, ord('E')):
                self.on_ejecutar(None)
                return
            elif keycode == ord('P'):
                self.on_pista(None)
                return
            elif keycode == ord('H'):
                self.on_traducir_linea(None)
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
        else:
            if keycode == ord(':') and self.sonidos_activos:
                SoundManager.play('bloque')
            event.Skip()

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
            self, "Abrir script Python",
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
        estado = "activado" if self.linter_activo else "desactivado"
        if ui:
            ui.message(f"Linter acústico {estado}")

    def on_toggle_sonidos(self, event):
        self.sonidos_activos = self.item_sonidos.IsChecked()
        ProgressManager.set_setting("sound_enabled", self.sonidos_activos)
        estado = "activadas" if self.sonidos_activos else "desactivadas"
        if ui:
            ui.message(f"Señales sonoras {estado}")

    def on_abrir_doc(self, event=None):
        abierto = False
        if docHandler and hasattr(docHandler, 'openDoc'):
            try:
                abierto = docHandler.openDoc("readme.html")
            except Exception:
                abierto = False

        if not abierto:
            # Fallback manual buscando doc/es/readme.html
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            candidatos = [
                os.path.join(base_dir, "doc", "es", "readme.html"),
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
            ui.message("No fue posible abrir el manual de usuario en el navegador.")

    def on_acerca(self, event=None):
        info = (
            "Aprendizaje de Python con NVDA (Versión 2.0.0)\n\n"
            "Entorno de aprendizaje accesible diseñado para personas con discapacidad visual.\n"
            "Incorpora metodología práctica orientada a la acción, traductor a lenguaje humano,\n"
            "linter acústico de sangría PEP 8, laboratorio interactivo y temario estructurado.\n\n"
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
