# -*- coding: utf-8 -*-
# Módulo: gui.py
import wx
import os
import io
import sys
import ast
import re
import traceback
import webbrowser
from .data import LECCIONES, GLOSARIO_RAPIDO, ATAJOS_TEXTO, PLANTILLAS_BASE
from .sound import SoundManager

# Importación segura de módulos de NVDA
try:
    import speech
    import ui
except ImportError:
    speech = None
    ui = None

class AccessibleManualDialog(wx.Dialog):
    def __init__(self, parent, title, text):
        super(AccessibleManualDialog, self).__init__(parent, title=title, size=(650, 520))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.text_ctrl.SetValue(text)
        self.text_ctrl.SetName("Contenido del Manual de Atajos. Navegue por este texto con sus flechas de direccion.")
        btn_ok = wx.Button(panel, wx.ID_OK, label="Cerrar Manual")
        btn_ok.SetName("Boton Cerrar Ventana")
        vbox.Add(self.text_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=15)
        vbox.Add(btn_ok, proportion=0, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=15)
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.text_ctrl.SetFocus()
    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE: self.EndModal(wx.ID_CANCEL)
        else: event.Skip()

class AccessibleAboutDialog(wx.Dialog):
    def __init__(self, parent, title, text):
        super(AccessibleAboutDialog, self).__init__(parent, title=title, size=(650, 520))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.text_ctrl.SetValue(text)
        self.text_ctrl.SetName("Contenido Informativo del Complemento. Navegue por este texto con sus flechas de direccion.")
        btn_ok = wx.Button(panel, wx.ID_OK, label="Cerrar Acerca de")
        btn_ok.SetName("Boton Cerrar Ventana")
        vbox.Add(self.text_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=15)
        vbox.Add(btn_ok, proportion=0, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=15)
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.text_ctrl.SetFocus()
    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE: self.EndModal(wx.ID_CANCEL)
        else: event.Skip()

class GlossaryDialog(wx.Dialog):
    def __init__(self, parent, glosario_dict):
        super(GlossaryDialog, self).__init__(parent, title="Glosario Interactivo de Conceptos", size=(750, 550))
        self.glosario = glosario_dict
        self.terminos_ordenados = sorted(list(glosario_dict.keys()))
        self.filtrados = list(self.terminos_ordenados)
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        search_box = wx.BoxSizer(wx.HORIZONTAL)
        search_box.Add(wx.StaticText(panel, label="Buscador de terminos:"), flag=wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border=5)
        self.search_ctrl = wx.TextCtrl(panel)
        self.search_ctrl.SetName("Escribe aqui la palabra para filtrar el glosario.")
        search_box.Add(self.search_ctrl, proportion=1, flag=wx.EXPAND)
        main_sizer.Add(search_box, flag=wx.EXPAND | wx.ALL, border=10)
        content_sizer = wx.BoxSizer(wx.HORIZONTAL)
        list_sizer = wx.BoxSizer(wx.VERTICAL)
        list_sizer.Add(wx.StaticText(panel, label="Terminos disponibles:"), flag=wx.BOTTOM, border=5)
        self.list_box = wx.ListBox(panel, choices=self.terminos_ordenados)
        self.list_box.SetName("Lista de terminos. Presione flechas abajo o arriba para seleccionar.")
        list_sizer.Add(self.list_box, proportion=1, flag=wx.EXPAND)
        content_sizer.Add(list_sizer, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=10)
        def_sizer = wx.BoxSizer(wx.VERTICAL)
        def_sizer.Add(wx.StaticText(panel, label="Significado:"), flag=wx.BOTTOM, border=5)
        self.def_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.def_ctrl.SetName("Significado del termino seleccionado. Presione tabulador para acceder y leer.")
        def_sizer.Add(self.def_ctrl, proportion=1, flag=wx.EXPAND)
        content_sizer.Add(def_sizer, proportion=2, flag=wx.EXPAND)
        main_sizer.Add(content_sizer, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_cerrar = wx.Button(panel, label="Cerrar Glosario")
        self.btn_cerrar.SetName("Boton cerrar glosario")
        btn_sizer.Add(self.btn_cerrar)
        main_sizer.Add(btn_sizer, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)
        panel.SetSizer(main_sizer)
        self.search_ctrl.Bind(wx.EVT_TEXT, self.on_search_change)
        self.list_box.Bind(wx.EVT_LISTBOX, self.on_list_select)
        self.btn_cerrar.Bind(wx.EVT_BUTTON, lambda e: self.Close())
        self.search_ctrl.Bind(wx.EVT_KEY_DOWN, self.on_search_key_down)
        self.list_box.Bind(wx.EVT_KEY_DOWN, self.on_list_key_down)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        if self.terminos_ordenados:
            self.list_box.SetSelection(0)
            self.actualizar_definicion()
        self.search_ctrl.SetFocus()
    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE: self.EndModal(wx.ID_CANCEL)
        else: event.Skip()
    def on_search_change(self, event):
        query = self.search_ctrl.GetValue().lower().strip()
        self.filtrados = [t for t in self.terminos_ordenados if query in t]
        self.list_box.Set(self.filtrados)
        if self.filtrados: self.list_box.SetSelection(0)
        self.actualizar_definicion()
    def on_list_select(self, event): self.actualizar_definicion()
    def actualizar_definicion(self):
        sel = self.list_box.GetStringSelection()
        if sel and sel in self.glosario:
            self.def_ctrl.SetValue(self.glosario[sel])
            if ui: ui.message(sel)
        else: self.def_ctrl.SetValue("")
    def on_search_key_down(self, event):
        if event.GetKeyCode() == wx.WXK_DOWN: self.list_box.SetFocus()
        else: event.Skip()
    def on_list_key_down(self, event):
        if event.GetKeyCode() == wx.WXK_UP and self.list_box.GetSelection() == 0: self.search_ctrl.SetFocus()
        else: event.Skip()

class TutorFrame(wx.Frame):
    def __init__(self, parent):
        super(TutorFrame, self).__init__(parent, title="Python Tutor", size=(950, 850))
        self.linter_activo, self.exito_activo, self.error_activo = True, True, True
        self.historial_anterior, self.archivo_actual = "", None 
        self.crear_barra_menus()
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(wx.StaticText(panel, label="1. Selector de Capitulos (Ctrl + 1):"), flag=wx.LEFT|wx.TOP, border=10)
        self.lista_capitulos = wx.ListBox(panel, choices=[l["titulo"] for l in LECCIONES])
        vbox.Add(self.lista_capitulos, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        vbox.Add(wx.StaticText(panel, label="2. Panel de Teoria (Ctrl + 2):"), flag=wx.LEFT|wx.TOP, border=10)
        self.teoria = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)
        vbox.Add(self.teoria, proportion=3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        vbox.Add(wx.StaticText(panel, label="3. Actividad Practica (Ctrl + 3):"), flag=wx.LEFT|wx.TOP, border=10)
        self.practica = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)
        vbox.Add(self.practica, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        vbox.Add(wx.StaticText(panel, label="4. Editor de Codigo (Ctrl + 4):"), flag=wx.LEFT|wx.TOP, border=10)
        self.edicion = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_PROCESS_TAB)
        vbox.Add(self.edicion, proportion=3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        vbox.Add(wx.StaticText(panel, label="5. Consola (Ctrl + 5):"), flag=wx.LEFT|wx.TOP, border=10)
        self.salida = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)
        vbox.Add(self.salida, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_ejecutar = wx.Button(panel, label="Ejecutar (Ctrl + E)")
        self.btn_reiniciar = wx.Button(panel, label="Reiniciar (Ctrl + R)")
        self.btn_limpiar = wx.Button(panel, label="Limpiar (Ctrl + L)")
        self.btn_cerrar = wx.Button(panel, label="Cerrar")
        hbox.Add(self.btn_ejecutar, flag=wx.RIGHT, border=5)
        hbox.Add(self.btn_reiniciar, flag=wx.RIGHT, border=5)
        hbox.Add(self.btn_limpiar, flag=wx.RIGHT, border=5)
        hbox.Add(self.btn_cerrar)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER|wx.ALL, border=15)
        panel.SetSizer(vbox)
        self.lista_capitulos.Bind(wx.EVT_LISTBOX, self.on_seleccionar_capitulo)
        self.edicion.Bind(wx.EVT_KEY_DOWN, self.on_key_down_edicion)
        self.edicion.Bind(wx.EVT_KEY_UP, self.on_key_up_edicion)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook_global)
        self.btn_ejecutar.Bind(wx.EVT_BUTTON, self.on_ejecutar)
        self.btn_reiniciar.Bind(wx.EVT_BUTTON, self.on_reiniciar_acertijo)
        self.btn_limpiar.Bind(wx.EVT_BUTTON, self.on_limpiar_consola)
        self.btn_cerrar.Bind(wx.EVT_BUTTON, lambda e: self.Close())
        self.teoria.SetValue("Navega al Selector de Capitulos (Ctrl + 1) para comenzar.")
        SoundManager.play('inicio')

    def crear_barra_menus(self):
        menu_bar = wx.MenuBar()
        menu_archivo = wx.Menu()
        item_abrir = menu_archivo.Append(wx.ID_ANY, "Abrir...	Ctrl+O")
        item_guardar = menu_archivo.Append(wx.ID_ANY, "Guardar	Ctrl+S")
        self.Bind(wx.EVT_MENU, self.on_abrir_archivo, id=item_abrir.GetId())
        self.Bind(wx.EVT_MENU, self.on_guardar_archivo, id=item_guardar.GetId())
        menu_ajustes = wx.Menu()
        self.item_linter = menu_ajustes.AppendCheckItem(wx.ID_ANY, "Linter Acústico")
        self.item_linter.Check(True)
        menu_glosario = wx.Menu()
        item_glosario = menu_glosario.Append(wx.ID_ANY, "Glosario...	Ctrl+G")
        self.Bind(wx.EVT_MENU, self.on_abrir_glosario_dialog, id=item_glosario.GetId())
        menu_ayuda = wx.Menu()
        item_atajos = menu_ayuda.Append(wx.ID_ANY, "Manual de Atajos")
        self.Bind(wx.EVT_MENU, self.on_ver_atajos, id=item_atajos.GetId())
        menu_bar.Append(menu_archivo, "&Archivo")
        menu_bar.Append(menu_ajustes, "&Configuración")
        menu_bar.Append(menu_glosario, "&Glosario")
        menu_bar.Append(menu_ayuda, "&Ayuda")
        self.SetMenuBar(menu_bar)

    def on_abrir_archivo(self, event=None):
        dlg = wx.FileDialog(self, "Abrir archivo Python", wildcard="*.py", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            with open(path, 'r', encoding='utf-8', errors='ignore') as f: self.edicion.SetValue(f.read())
            self.archivo_actual = path
            if ui: ui.message(f"Abierto: {os.path.basename(path)}")
        dlg.Destroy()

    def on_guardar_archivo(self, event=None):
        if not self.archivo_actual:
            dlg = wx.FileDialog(self, "Guardar como", wildcard="*.py", style=wx.FD_SAVE)
            if dlg.ShowModal() == wx.ID_OK: self.archivo_actual = dlg.GetPath()
            dlg.Destroy()
        if self.archivo_actual:
            with open(self.archivo_actual, 'w', encoding='utf-8') as f: f.write(self.edicion.GetValue())
            if ui: ui.message("Guardado.")

    def on_abrir_glosario_dialog(self, event=None): GlossaryDialog(self, GLOSARIO_RAPIDO).ShowModal()
    def on_ver_atajos(self, event): AccessibleManualDialog(self, "Atajos", ATAJOS_TEXTO).ShowModal()

    def on_seleccionar_capitulo(self, event):
        idx = self.lista_capitulos.GetSelection()
        if idx != wx.NOT_FOUND:
            lec = LECCIONES[idx]
            self.teoria.SetValue(lec["teoria"])
            self.practica.SetValue(lec["practica"])
            self.edicion.SetValue(lec["codigo"])
            self.salida.SetValue("")
            if ui: ui.message(f"Cargado: {lec['titulo']}")

    def on_char_hook_global(self, event):
        keycode, modifiers = event.GetKeyCode(), event.GetModifiers()
        if keycode == wx.WXK_ESCAPE:
            self.Close()
            return
        if modifiers == wx.MOD_CONTROL:
            if keycode == ord('1'): self.lista_capitulos.SetFocus()
            elif keycode == ord('2'): self.teoria.SetFocus()
            elif keycode == ord('3'): self.practica.SetFocus()
            elif keycode == ord('4'): self.edicion.SetFocus()
            elif keycode == ord('5'): self.salida.SetFocus()
            elif keycode == ord('E'): self.on_ejecutar()
            elif keycode == ord('G'): self.on_abrir_glosario_dialog()
            elif keycode == ord('T'): self.insertar_plantilla()
            else: event.Skip()
        else: event.Skip()

    def on_key_down_edicion(self, event):
        if event.GetKeyCode() == wx.WXK_TAB: self.edicion.WriteText("    ")
        else: event.Skip()

    def on_key_up_edicion(self, event):
        if self.item_linter.IsChecked():
            pt = self.edicion.GetInsertionPoint()
            row = self.edicion.GetValue()[:pt].count('\n')
            espacios = len(self.edicion.GetLineText(row)) - len(self.edicion.GetLineText(row).lstrip())
            if espacios == 0: SoundManager.play('indent0')
            elif espacios == 4: SoundManager.play('indent4')
            elif espacios == 8: SoundManager.play('indent8')
        event.Skip()

    def insertar_plantilla(self):
        idx = self.lista_capitulos.GetSelection()
        if idx+1 in PLANTILLAS_BASE:
            self.edicion.SetValue(PLANTILLAS_BASE[idx+1])
            if ui: ui.message("Plantilla cargada.")

    def on_limpiar_consola(self, event=None): self.salida.SetValue(""); ui.message("Limpio.")

    def on_ejecutar(self, event=None):
        src = self.edicion.GetValue()
        buf = io.StringIO()
        sys.stdout, sys.stderr = buf, buf
        try:
            exec(src, {}, {})
            res = buf.getvalue() or "Ejecutado."
            SoundManager.play('exito')
        except Exception:
            res = traceback.format_exc()
            SoundManager.play('error')
        finally:
            sys.stdout, sys.stderr = sys.__stdout__, sys.__stderr__
        self.salida.SetValue(res)
        self.salida.SetFocus()
        if ui: ui.message("Fin de ejecucion.")

    def on_reiniciar_acertijo(self, event=None):
        idx = self.lista_capitulos.GetSelection()
        if idx != wx.NOT_FOUND: self.edicion.SetValue(LECCIONES[idx]["codigo"])

    def on_close(self, event): self.Destroy()
