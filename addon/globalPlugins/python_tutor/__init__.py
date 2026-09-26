# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/__init__.py
# Complemento: Aprendizaje de Python con NVDA
# Versión: 2.0.0
# Autor: Kevin Andrés Velasquez Vargas
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

        self.chk_modo_editor = wx.CheckBox(self, label="Iniciar en Modo Editor autónomo (ocultar lecciones del tutor)")
        self.chk_modo_editor.SetValue(ProgressManager.get_editor_mode() == "editor")
        settingsSizer.Add(self.chk_modo_editor, flag=wx.ALL, border=6)

        self.chk_sonidos = wx.CheckBox(self, label="Efectos sonoros de confirmación y eventos")
        self.chk_sonidos.SetValue(prog.get("sound_enabled", True))
        settingsSizer.Add(self.chk_sonidos, flag=wx.ALL, border=6)

        self.chk_linter = wx.CheckBox(self, label="Avisos sonoros de sangría y estructura")
        self.chk_linter.SetValue(prog.get("linter_enabled", True))
        settingsSizer.Add(self.chk_linter, flag=wx.ALL, border=6)

        self.chk_bienvenida = wx.CheckBox(self, label="Mostrar diálogo de bienvenida al iniciar el complemento")
        self.chk_bienvenida.SetValue(prog.get("show_welcome", True))
        settingsSizer.Add(self.chk_bienvenida, flag=wx.ALL, border=6)

        # Botones de soporte y donaciones voluntarias
        btn_box = wx.BoxSizer(wx.HORIZONTAL)
        btn_soporte = wx.Button(self, label="Enviar mensaje de soporte")
        btn_donar = wx.Button(self, label="Realizar donación voluntaria")
        btn_box.Add(btn_soporte, flag=wx.RIGHT, border=8)
        btn_box.Add(btn_donar)
        settingsSizer.Add(btn_box, flag=wx.ALL, border=6)

        btn_soporte.Bind(wx.EVT_BUTTON, lambda e: webbrowser.open("mailto:kevinvelasquezvargas@gmail.com?subject=Soporte%20-%20Aprendizaje%20de%20Python%20con%20NVDA"))
        btn_donar.Bind(wx.EVT_BUTTON, lambda e: webbrowser.open("https://paypal.me/kevinvelasquezvargas"))

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
            item_donacion = self._sub_menu.Append(
                wx.ID_ANY,
                "Realizar una donación...",
                "Apoyar el desarrollo libre del complemento"
            )
            item_soporte = self._sub_menu.Append(
                wx.ID_ANY,
                "Soporte y contacto...",
                "Abrir canal de soporte por correo o incidencias"
            )

            # Vincular en sysTray, sub_menu y mainFrame para garantizar captura del evento
            cb_abrir = lambda evt: wx.CallAfter(self._lanzar_interfaz)
            cb_donacion = lambda evt: self._abrir_donacion()
            cb_soporte = lambda evt: self._abrir_soporte()

            sysTray.Bind(wx.EVT_MENU, cb_abrir, item_abrir)
            sysTray.Bind(wx.EVT_MENU, cb_donacion, item_donacion)
            sysTray.Bind(wx.EVT_MENU, cb_soporte, item_soporte)

            self._sub_menu.Bind(wx.EVT_MENU, cb_abrir, id=item_abrir.GetId())
            self._sub_menu.Bind(wx.EVT_MENU, cb_donacion, id=item_donacion.GetId())
            self._sub_menu.Bind(wx.EVT_MENU, cb_soporte, id=item_soporte.GetId())

            gui.mainFrame.Bind(wx.EVT_MENU, cb_abrir, id=item_abrir.GetId())
            gui.mainFrame.Bind(wx.EVT_MENU, cb_donacion, id=item_donacion.GetId())
            gui.mainFrame.Bind(wx.EVT_MENU, cb_soporte, id=item_soporte.GetId())

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
            try:
                webbrowser.open("https://github.com/KevinVelasquezVargas/python_tutor/issues")
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
        try:
            if self.gui_frame:
                try:
                    self.gui_frame.Show()
                    self.gui_frame.Raise()
                    self.gui_frame.edicion.SetFocus()
                    SoundManager.play('inicio')
                    return
                except Exception:
                    self.gui_frame = None

            self.gui_frame = TutorFrame(None)
            self.gui_frame.Bind(wx.EVT_WINDOW_DESTROY, self.on_frame_destroy)
            self.gui_frame.Show()
            self.gui_frame.Raise()
            self.gui_frame.edicion.SetFocus()
        except Exception as e:
            self.gui_frame = None
            if ui:
                ui.message(f"Error al iniciar Aprendizaje de Python con NVDA: {e}")

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
