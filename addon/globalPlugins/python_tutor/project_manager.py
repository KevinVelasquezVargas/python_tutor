# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/project_manager.py
# Propósito: Gestor accesible de proyectos multi-archivo y módulos Python.
# Autor: Kevin Andrés Velasquez Vargas
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import os
import wx

try:
    import ui
except ImportError:
    ui = None


class ProjectManagerDialog(wx.Dialog):
    """
    Diálogo accesible para explorar, crear y alternar entre los archivos y módulos
    de un proyecto en Python (Control + Shift + E).
    """
    def __init__(self, parent, carpeta_proyecto=None, archivo_activo=None, on_abrir_archivo=None):
        super(ProjectManagerDialog, self).__init__(
            parent,
            title="Explorador de Archivos del Proyecto (Multi-archivo)",
            size=(520, 420)
        )
        self.parent = parent
        self.carpeta_proyecto = carpeta_proyecto or os.path.join(os.path.expanduser("~"), "Documents", "PythonTutorProjects")
        self.archivo_activo = archivo_activo
        self.on_abrir_archivo = on_abrir_archivo

        if not os.path.exists(self.carpeta_proyecto):
            try:
                os.makedirs(self.carpeta_proyecto)
            except Exception:
                pass

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl_carpeta = wx.StaticText(panel, label=f"Carpeta del Proyecto: {self.carpeta_proyecto}")
        vbox.Add(lbl_carpeta, flag=wx.ALL, border=10)

        lbl_lista = wx.StaticText(panel, label="Archivos del proyecto (presiona Enter o Espacio para abrir):")
        vbox.Add(lbl_lista, flag=wx.LEFT | wx.RIGHT, border=10)

        self.lista_archivos = wx.ListBox(panel, style=wx.LB_SINGLE)
        vbox.Add(self.lista_archivos, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)

        hbox_btns = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_abrir = wx.Button(panel, label="Abrir en Editor")
        self.btn_nuevo = wx.Button(panel, label="Nuevo Módulo (.py)...")
        self.btn_carpeta = wx.Button(panel, label="Cambiar Carpeta...")
        self.btn_cerrar = wx.Button(panel, wx.ID_CANCEL, label="Cerrar")

        hbox_btns.Add(self.btn_abrir, flag=wx.RIGHT, border=6)
        hbox_btns.Add(self.btn_nuevo, flag=wx.RIGHT, border=6)
        hbox_btns.Add(self.btn_carpeta, flag=wx.RIGHT, border=6)
        hbox_btns.Add(self.btn_cerrar)
        vbox.Add(hbox_btns, flag=wx.ALL | wx.ALIGN_RIGHT, border=10)

        panel.SetSizer(vbox)

        self.btn_abrir.Bind(wx.EVT_BUTTON, self.on_abrir)
        self.btn_nuevo.Bind(wx.EVT_BUTTON, self.on_nuevo)
        self.btn_carpeta.Bind(wx.EVT_BUTTON, self.on_cambiar_carpeta)
        self.lista_archivos.Bind(wx.EVT_LISTBOX_DCLICK, self.on_abrir)
        self.lista_archivos.Bind(wx.EVT_KEY_DOWN, self.on_key_lista)

        self.refrescar_lista()
        self.CentreOnParent()

    def refrescar_lista(self):
        """Lista todos los archivos .py presentes en la carpeta del proyecto."""
        self.lista_archivos.Clear()
        if not os.path.exists(self.carpeta_proyecto):
            return

        archivos = sorted([
            f for f in os.listdir(self.carpeta_proyecto)
            if f.endswith(".py")
        ])

        if not archivos:
            self.lista_archivos.Append("(No hay archivos Python en este proyecto)")
            return

        for f in archivos:
            indicador = " [Activo]" if self.archivo_activo and os.path.basename(self.archivo_activo) == f else ""
            self.lista_archivos.Append(f"{f}{indicador}")

        if archivos:
            self.lista_archivos.SetSelection(0)

    def on_key_lista(self, event):
        if event.GetKeyCode() == wx.WXK_RETURN:
            self.on_abrir(event)
        else:
            event.Skip()

    def on_abrir(self, event=None):
        sel = self.lista_archivos.GetSelection()
        if sel == wx.NOT_FOUND:
            return
        nombre = self.lista_archivos.GetString(sel).replace(" [Activo]", "").strip()
        if nombre.startswith("("):
            return

        ruta_completa = os.path.join(self.carpeta_proyecto, nombre)
        if self.on_abrir_archivo and os.path.exists(ruta_completa):
            self.on_abrir_archivo(ruta_completa)
            if ui: ui.message(f"Abierto en el editor: {nombre}")
            self.EndModal(wx.ID_OK)

    def on_nuevo(self, event=None):
        dlg = wx.TextEntryDialog(
            self,
            "Introduce el nombre del nuevo módulo (ejemplo: utilidades o calculos.py):",
            "Nuevo Módulo Python"
        )
        if dlg.ShowModal() == wx.ID_OK:
            nombre = dlg.GetValue().strip()
            if nombre:
                if not nombre.endswith(".py"):
                    nombre += ".py"
                ruta = os.path.join(self.carpeta_proyecto, nombre)
                if os.path.exists(ruta):
                    if ui: ui.message("Ese archivo ya existe.")
                else:
                    try:
                        with open(ruta, "w", encoding="utf-8") as f:
                            f.write(f"# -*- coding: utf-8 -*-\n# Módulo: {nombre}\n\n")
                        self.refrescar_lista()
                        if self.on_abrir_archivo:
                            self.on_abrir_archivo(ruta)
                            if ui: ui.message(f"Módulo creado y abierto: {nombre}")
                            self.EndModal(wx.ID_OK)
                    except Exception as e:
                        wx.MessageBox(f"Error al crear el archivo: {e}", "Error", wx.ICON_ERROR, self)
        dlg.Destroy()

    def on_cambiar_carpeta(self, event=None):
        dlg = wx.DirDialog(
            self,
            "Selecciona la carpeta del proyecto Python:",
            defaultPath=self.carpeta_proyecto
        )
        if dlg.ShowModal() == wx.ID_OK:
            self.carpeta_proyecto = dlg.GetPath()
            self.refrescar_lista()
            if ui: ui.message(f"Proyecto cambiado a: {os.path.basename(self.carpeta_proyecto)}")
        dlg.Destroy()
