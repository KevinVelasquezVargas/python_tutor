# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/__init__.py
# Complemento: Aprendizaje de Python con NVDA
# Versión: 2.0.0
# Autor: Kevin Andrés Velasquez Vargas <kevinvelasquezvargas@gmail.com>
# Licencia: GNU General Public License v3.0 (GPLv3)
# Compatibilidad: NVDA 2022.1.0 hasta 2026.3.0
# ============================================================================

import wx
import webbrowser

try:
    import globalPluginHandler
    import scriptHandler
    import ui
    import addonHandler
    try:
        addonHandler.initTranslation()
    except Exception:
        pass
except ImportError:
    globalPluginHandler = None
    scriptHandler = None
    ui = None

try:
    import gui
    from gui import SettingsPanel
    from gui.settingsDialogs import NVDASettingsDialog
except ImportError:
    gui = None
    SettingsPanel = None
    NVDASettingsDialog = None

from .audio_manager import SoundManager
from .gui_frame import TutorFrame
from .progress import ProgressManager

_BasePlugin = globalPluginHandler.GlobalPlugin if globalPluginHandler else object


class PythonTutorSettingsPanel(SettingsPanel):
    """Panel de configuración nativo integrado en el diálogo de opciones de NVDA."""
    title = "Aprendizaje de Python con NVDA"

    def makeSettings(self, settingsSizer):
        prog = ProgressManager.load_progress()

        self.chk_modo_editor = wx.CheckBox(self, label="Iniciar directamente en Modo Solo Editor profesional (ocultar misiones didácticas)")
        self.chk_modo_editor.SetValue(ProgressManager.get_editor_mode() == "editor")
        settingsSizer.Add(self.chk_modo_editor, flag=wx.ALL, border=6)

        self.chk_sonidos = wx.CheckBox(self, label="Activar señales sonoras y efectos auditivos")
        self.chk_sonidos.SetValue(prog.get("sound_enabled", True))
        settingsSizer.Add(self.chk_sonidos, flag=wx.ALL, border=6)

        self.chk_linter = wx.CheckBox(self, label="Activar linter acústico de sangría PEP 8 y sintaxis")
        self.chk_linter.SetValue(prog.get("linter_enabled", True))
        settingsSizer.Add(self.chk_linter, flag=wx.ALL, border=6)

        self.chk_bienvenida = wx.CheckBox(self, label="Mostrar diálogo de bienvenida al iniciar el complemento")
        self.chk_bienvenida.SetValue(prog.get("show_welcome", True))
        settingsSizer.Add(self.chk_bienvenida, flag=wx.ALL, border=6)

    def onSave(self):
        ProgressManager.set_editor_mode("editor" if self.chk_modo_editor.GetValue() else "learning")
        ProgressManager.set_setting("sound_enabled", self.chk_sonidos.GetValue())
        ProgressManager.set_setting("linter_enabled", self.chk_linter.GetValue())
        ProgressManager.set_setting("show_welcome", self.chk_bienvenida.GetValue())


class GlobalPlugin(_BasePlugin):
    """
    Plugin global principal de Aprendizaje de Python con NVDA.
    Gestiona el registro de gestos de entrada, la integración con el menú de herramientas,
    el panel de preferencias y el ciclo de vida del entorno pedagógico.
    """
    scriptCategory = "Aprendizaje de Python con NVDA"

    gestures = {
        "kb:NVDA+control+shift+p": "openPythonTutor",
    }

    def __init__(self, *args, **kwargs):
        if globalPluginHandler:
            super(GlobalPlugin, self).__init__(*args, **kwargs)
        self.gui_frame = None
        self._tools_menu = None
        self._menu_item_sub = None

        # Inicialización de señales sonoras
        SoundManager.initialize()

        # Registrar panel de preferencias en NVDA
        if NVDASettingsDialog and SettingsPanel:
            try:
                if PythonTutorSettingsPanel not in NVDASettingsDialog.categoryClasses:
                    NVDASettingsDialog.categoryClasses.append(PythonTutorSettingsPanel)
            except Exception:
                pass

        # Agregar menú en Herramientas de NVDA
        wx.CallAfter(self._crear_menu_herramientas)

    def _crear_menu_herramientas(self):
        try:
            if not gui or not hasattr(gui, 'mainFrame') or not gui.mainFrame:
                return
            sysTray = getattr(gui.mainFrame, 'sysTrayIcon', None)
            if not sysTray or not hasattr(sysTray, 'toolsMenu'):
                return

            self._tools_menu = sysTray.toolsMenu
            self._sub_menu = wx.Menu()

            item_abrir = self._sub_menu.Append(
                wx.ID_ANY,
                "Aprendizaje de Python con NVDA...",
                "Abre el entorno interactivo de aprendizaje"
            )
            gui.mainFrame.Bind(wx.EVT_MENU, lambda evt: wx.CallAfter(self._lanzar_interfaz), id=item_abrir.GetId())

            item_soporte = self._sub_menu.Append(
                wx.ID_ANY,
                "Soporte y contacto...",
                "Enviar un correo de consulta o soporte"
            )
            gui.mainFrame.Bind(wx.EVT_MENU, lambda evt: self._abrir_soporte(), id=item_soporte.GetId())

            item_donacion = self._sub_menu.Append(
                wx.ID_ANY,
                "Realizar una donación...",
                "Apoyar el desarrollo libre del complemento"
            )
            gui.mainFrame.Bind(wx.EVT_MENU, lambda evt: self._abrir_donacion(), id=item_donacion.GetId())

            self._menu_item_sub = self._tools_menu.AppendSubMenu(self._sub_menu, "Aprendizaje de Python con NVDA")
        except Exception:
            pass

    def _eliminar_menu_herramientas(self):
        try:
            if self._tools_menu and self._menu_item_sub:
                self._tools_menu.Remove(self._menu_item_sub.GetId())
        except Exception:
            pass

    def _abrir_soporte(self):
        url = "mailto:kevinvelasquezvargas@gmail.com?subject=Soporte%20-%20Aprendizaje%20de%20Python%20con%20NVDA"
        try:
            webbrowser.open(url)
            if ui:
                ui.message("Abriendo cliente de correo para soporte...")
        except Exception:
            pass

    def _abrir_donacion(self):
        url = "https://www.paypal.me/kevinvelasquezvargas"
        try:
            webbrowser.open(url)
            if ui:
                ui.message("Abriendo página de donaciones en el navegador...")
        except Exception:
            pass

    if scriptHandler and hasattr(scriptHandler, 'script'):
        @scriptHandler.script(
            description="Abre el entorno de Aprendizaje de Python con NVDA.",
            category="Aprendizaje de Python con NVDA",
            gesture="kb:NVDA+control+shift+p"
        )
        def script_openPythonTutor(self, gesture):
            wx.CallAfter(self._lanzar_interfaz)
    else:
        def script_openPythonTutor(self, gesture):
            wx.CallAfter(self._lanzar_interfaz)

    def _lanzar_interfaz(self):
        parent_window = None
        try:
            if gui and hasattr(gui, 'mainFrame') and gui.mainFrame:
                parent_window = gui.mainFrame
        except Exception:
            pass

        if not self.gui_frame:
            try:
                self.gui_frame = TutorFrame(parent_window)
                self.gui_frame.Bind(wx.EVT_WINDOW_DESTROY, self.on_frame_destroy)
            except Exception as e:
                if ui:
                    ui.message(f"Error al iniciar Aprendizaje de Python con NVDA: {e}")
                return

        try:
            self.gui_frame.Show()
            self.gui_frame.Raise()
            self.gui_frame.edicion.SetFocus()
        except Exception:
            try:
                self.gui_frame = TutorFrame(parent_window)
                self.gui_frame.Bind(wx.EVT_WINDOW_DESTROY, self.on_frame_destroy)
                self.gui_frame.Show()
                self.gui_frame.Raise()
                self.gui_frame.edicion.SetFocus()
            except Exception as e:
                if ui:
                    ui.message(f"No fue posible abrir la ventana del tutor: {e}")

    def on_frame_destroy(self, event):
        if event.GetEventObject() == self.gui_frame:
            self.gui_frame = None
        event.Skip()

    def terminate(self):
        """Libera de forma ordenada los recursos temporales y destruye ventanas activas."""
        try:
            self._eliminar_menu_herramientas()
        except Exception:
            pass

        if NVDASettingsDialog and SettingsPanel:
            try:
                if PythonTutorSettingsPanel in NVDASettingsDialog.categoryClasses:
                    NVDASettingsDialog.categoryClasses.remove(PythonTutorSettingsPanel)
            except Exception:
                pass

        try:
            if self.gui_frame:
                try:
                    self.gui_frame.Destroy()
                except Exception:
                    pass
                self.gui_frame = None
            SoundManager.cleanup()
        except Exception:
            pass

        if globalPluginHandler:
            super(GlobalPlugin, self).terminate()
