# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/__init__.py
# Complemento: Aprendizaje de Python con NVDA
# Versión: 2.0.0
# Autor: Kevin Andrés Velasquez Vargas
# Licencia: GNU General Public License v3.0 (GPLv3)
# Compatibilidad: NVDA 2022.1.0 hasta 2026.3.0
# ============================================================================

import os
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
    import gettext
    _loc = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "locale")
    try:
        _t = gettext.translation("nvda", localedir=_loc, languages=["es"])
        _ = _t.gettext
    except Exception:
        def _(msg):
            return msg

try:
    import globalPluginHandler
    import scriptHandler
    import ui
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
_BaseSettingsPanel = SettingsPanel if SettingsPanel else object


class PythonTutorSettingsPanel(_BaseSettingsPanel):
    """Panel de configuración nativo integrado en el diálogo de opciones de NVDA."""
    title = _("Python Learning with NVDA")

    def makeSettings(self, settingsSizer):
        prog = ProgressManager.load_progress()

        self.chk_modo_editor = wx.CheckBox(self, label=_("Start in standalone Editor Mode (hide tutor lessons)"))
        self.chk_modo_editor.SetValue(ProgressManager.get_editor_mode() == "editor")
        settingsSizer.Add(self.chk_modo_editor, flag=wx.ALL, border=6)

        self.chk_sonidos = wx.CheckBox(self, label=_("Confirmation and event sound effects"))
        self.chk_sonidos.SetValue(prog.get("sound_enabled", True))
        settingsSizer.Add(self.chk_sonidos, flag=wx.ALL, border=6)

        self.chk_linter = wx.CheckBox(self, label=_("Indentation and structure sound alerts"))
        self.chk_linter.SetValue(prog.get("linter_enabled", True))
        settingsSizer.Add(self.chk_linter, flag=wx.ALL, border=6)

        self.chk_bienvenida = wx.CheckBox(self, label=_("Show welcome dialog when addon starts"))
        self.chk_bienvenida.SetValue(prog.get("show_welcome", True))
        settingsSizer.Add(self.chk_bienvenida, flag=wx.ALL, border=6)

        # Botones de soporte y donaciones voluntarias
        btn_box = wx.BoxSizer(wx.HORIZONTAL)
        btn_soporte = wx.Button(self, label=_("Send support message"))
        btn_donar = wx.Button(self, label=_("Make voluntary donation"))
        btn_box.Add(btn_soporte, flag=wx.RIGHT, border=8)
        btn_box.Add(btn_donar)
        settingsSizer.Add(btn_box, flag=wx.ALL, border=6)

        subject = _("Support - Python Learning with NVDA")
        mail_url = f"mailto:kevinvelasquezvargas@gmail.com?subject={urllib.parse.quote(subject)}"
        btn_soporte.Bind(wx.EVT_BUTTON, lambda e: webbrowser.open(mail_url))
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
    scriptCategory = _("Python Learning with NVDA")

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
                _("Python Learning with NVDA..."),
                _("Opens the interactive learning environment")
            )
            item_donacion = self._sub_menu.Append(
                wx.ID_ANY,
                _("Make a donation..."),
                _("Support free addon development")
            )
            item_soporte = self._sub_menu.Append(
                wx.ID_ANY,
                _("Support and contact..."),
                _("Open support channel via email or issues")
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

            self._menu_item_sub = self._tools_menu.AppendSubMenu(self._sub_menu, _("Python Learning with NVDA"))
        except Exception:
            pass

    def _eliminar_menu_herramientas(self):
        try:
            if self._tools_menu and self._menu_item_sub:
                self._tools_menu.Remove(self._menu_item_sub.GetId())
        except Exception:
            pass

    def _abrir_soporte(self):
        subject = _("Support - Python Learning with NVDA")
        url = f"mailto:kevinvelasquezvargas@gmail.com?subject={urllib.parse.quote(subject)}"
        try:
            webbrowser.open(url)
            if ui:
                ui.message(_("Opening email client for support..."))
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
                ui.message(_("Opening donations page in browser..."))
        except Exception:
            pass

    if scriptHandler and hasattr(scriptHandler, 'script'):
        @scriptHandler.script(
            description=_("Opens the Python Learning with NVDA environment."),
            category=_("Python Learning with NVDA"),
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
                # Translators: Error message when Python Tutor interface fails to launch. {error} is the error message.
                ui.message(_("Error launching Python Learning with NVDA: {error}").format(error=e))

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
