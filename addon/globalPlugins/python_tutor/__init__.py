# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/__init__.py
# Complemento: Aprendizaje de Python con NVDA
# Versión: 1.0.0
# Autor: Kevin Andrés Velasquez Vargas
# Licencia: GNU General Public License v3.0 (GPLv3)
# Compatibilidad: NVDA 2022.1.0 hasta 2026.2.0
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
    from gui import settingsDialogs
    SettingsPanel = getattr(settingsDialogs, 'SettingsPanel', getattr(gui, 'SettingsPanel', None))
    NVDASettingsDialog = getattr(settingsDialogs, 'NVDASettingsDialog', None)
except Exception:
    gui = None
    SettingsPanel = None
    NVDASettingsDialog = None

from .audio_manager import SoundManager
from .gui_frame import TutorFrame
from .progress import ProgressManager
from .i18n import _t, _, detectar_idioma_preferido, establecer_idioma, obtener_idioma_actual
from .ai_assistant import obtener_config_ia, guardar_config_ia

_BasePlugin = globalPluginHandler.GlobalPlugin if globalPluginHandler else object
_BaseSettingsPanel = SettingsPanel if SettingsPanel else object


class _SettingsPanelMeta(type(_BaseSettingsPanel)):
    @property
    def title(cls):
        return "Learning Python with NVDA" if obtener_idioma_actual() == "en" else "Aprendizaje de Python con NVDA"

    @title.setter
    def title(cls, value):
        pass


class PythonTutorSettingsPanel(_BaseSettingsPanel, metaclass=_SettingsPanelMeta):
    """Panel de configuración nativo integrado en el diálogo de opciones de NVDA."""

    @property
    def title(self):
        return "Learning Python with NVDA" if obtener_idioma_actual() == "en" else "Aprendizaje de Python con NVDA"

    def makeSettings(self, settingsSizer):
        prog = ProgressManager.load_progress()
        cfg_ia = obtener_config_ia()
        is_en = (obtener_idioma_actual() == "en")

        # 1. Selector de Idioma (Language)
        lbl_lang = wx.StaticText(
            self,
            label="Interface and curriculum language:" if is_en else "Idioma de la interfaz y lecciones:"
        )
        settingsSizer.Add(lbl_lang, flag=wx.LEFT | wx.TOP, border=6)

        lang_choices = [
            "Automatic (follows NVDA language)" if is_en else "Automático (según el idioma de NVDA)",
            "Español (Spanish)",
            "English"
        ]
        self.choice_lang = wx.Choice(self, choices=lang_choices)
        saved_lang = ProgressManager.get_setting("language", "auto")
        if saved_lang == "es":
            self.choice_lang.SetSelection(1)
        elif saved_lang == "en":
            self.choice_lang.SetSelection(2)
        else:
            self.choice_lang.SetSelection(0)
        settingsSizer.Add(self.choice_lang, flag=wx.ALL, border=6)

        # 2. Modo de inicio
        lbl_modo = "Start directly in Standalone Editor Mode (hide tutor lessons)" if is_en else "Iniciar en Modo Editor autónomo (ocultar lecciones del tutor)"
        self.chk_modo_editor = wx.CheckBox(self, label=lbl_modo)
        self.chk_modo_editor.SetValue(ProgressManager.get_editor_mode() == "editor")
        settingsSizer.Add(self.chk_modo_editor, flag=wx.ALL, border=6)

        # 3. Sonidos y Linter
        lbl_snd = "Sound confirmation effects and events" if is_en else "Efectos sonoros de confirmación y eventos"
        self.chk_sonidos = wx.CheckBox(self, label=lbl_snd)
        self.chk_sonidos.SetValue(prog.get("sound_enabled", True))
        settingsSizer.Add(self.chk_sonidos, flag=wx.ALL, border=6)

        lbl_linter = "Auditory indentation and structure cues (PEP 8)" if is_en else "Avisos sonoros de sangría y estructura (PEP 8)"
        self.chk_linter = wx.CheckBox(self, label=lbl_linter)
        self.chk_linter.SetValue(prog.get("linter_enabled", True))
        settingsSizer.Add(self.chk_linter, flag=wx.ALL, border=6)

        # 4. Modo de la tecla F1 (Local offline vs Asistente de IA)
        lbl_f1_mode = "F1 Key Explanation Mode:" if is_en else "Modo de explicación para la tecla F1:"
        settingsSizer.Add(wx.StaticText(self, label=lbl_f1_mode), flag=wx.LEFT | wx.TOP, border=6)

        f1_choices = [
            "Local offline explanation (100% private, instant, no API required)" if is_en else "Explicación sintáctica local (100% privada, instantánea, sin API)",
            "Ask AI Assistant (requires Google Gemini API Key)" if is_en else "Consultar al Asistente de IA (requiere clave API de Google Gemini)"
        ]
        self.choice_f1 = wx.Choice(self, choices=f1_choices)
        current_f1_mode = ProgressManager.get_setting("f1_mode", "local")
        self.choice_f1.SetSelection(1 if current_f1_mode == "ai" else 0)
        settingsSizer.Add(self.choice_f1, flag=wx.ALL, border=6)

        # 5. Clave API de Google Gemini (opcional)
        lbl_key = "Google Gemini API Key (optional, for AI assistant & Ctrl+Shift+I):" if is_en else "Clave de API de Google Gemini (opcional, para asistente y Ctrl+Shift+I):"
        settingsSizer.Add(wx.StaticText(self, label=lbl_key), flag=wx.LEFT | wx.TOP, border=6)
        self.txt_api_key = wx.TextCtrl(self, value=cfg_ia.get("api_key", ""), style=wx.TE_PASSWORD)
        settingsSizer.Add(self.txt_api_key, flag=wx.ALL | wx.EXPAND, border=6)

        lbl_nota_ia = (
            "Note: F1 is local and private by default. You can also press Ctrl+Shift+I anytime for AI."
            if is_en else
            "Nota: Por defecto, F1 funciona 100% local y privado. Siempre puedes pulsar Ctrl+Shift+I para consultar a la IA."
        )
        settingsSizer.Add(wx.StaticText(self, label=lbl_nota_ia), flag=wx.LEFT | wx.BOTTOM, border=6)

        # 6. Botones de soporte y donaciones
        btn_box = wx.BoxSizer(wx.HORIZONTAL)
        lbl_soporte = "Send support email" if is_en else "Enviar mensaje de soporte"
        lbl_donar = "Support project (Donate)" if is_en else "Realizar donación voluntaria"
        btn_soporte = wx.Button(self, label=lbl_soporte)
        btn_donar = wx.Button(self, label=lbl_donar)
        btn_box.Add(btn_soporte, flag=wx.RIGHT, border=8)
        btn_box.Add(btn_donar)
        settingsSizer.Add(btn_box, flag=wx.ALL, border=6)

        btn_soporte.Bind(wx.EVT_BUTTON, lambda e: webbrowser.open("mailto:kevinvelasquezvargas@gmail.com?subject=Soporte%20-%20Python%20Tutor"))
        btn_donar.Bind(wx.EVT_BUTTON, lambda e: webbrowser.open("https://paypal.me/kevinvelasquezvargas"))

    def onSave(self):
        sel_idx = self.choice_lang.GetSelection()
        if sel_idx == 1:
            establecer_idioma("es")
            ProgressManager.set_setting("language", "es")
        elif sel_idx == 2:
            establecer_idioma("en")
            ProgressManager.set_setting("language", "en")
        else:
            ProgressManager.set_setting("language", "auto")
            detectar_idioma_preferido()

        ProgressManager.set_editor_mode("editor" if self.chk_modo_editor.GetValue() else "learning")
        ProgressManager.set_setting("sound_enabled", self.chk_sonidos.GetValue())
        ProgressManager.set_setting("linter_enabled", self.chk_linter.GetValue())

        # Guardar modo de F1
        f1_mode = "ai" if self.choice_f1.GetSelection() == 1 else "local"
        ProgressManager.set_setting("f1_mode", f1_mode)

        # Guardar configuración de IA
        key = self.txt_api_key.GetValue().strip()
        activa = (f1_mode == "ai" or bool(key))
        guardar_config_ia({"api_key": key, "provider": "gemini", "activa": activa})

        # Actualizar títulos de forma reactiva
        panel_title = "Learning Python with NVDA" if obtener_idioma_actual() == "en" else "Aprendizaje de Python con NVDA"
        PythonTutorSettingsPanel.title = panel_title
        GlobalPlugin.scriptCategory = panel_title


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

            is_en = (obtener_idioma_actual() == "en")
            sub_label = "Learning Python with NVDA..." if is_en else "Aprendizaje de Python con NVDA..."
            sub_help = "Opens the interactive Python learning environment" if is_en else "Abre el entorno interactivo de aprendizaje"
            item_abrir = self._sub_menu.Append(wx.ID_ANY, sub_label, sub_help)

            lbl_donar = "Support project (Donate)..." if is_en else "Realizar una donación..."
            item_donacion = self._sub_menu.Append(wx.ID_ANY, lbl_donar, "Support development" if is_en else "Apoyar el desarrollo libre del complemento")

            lbl_soporte = "Support & contact..." if is_en else "Soporte y contacto..."
            item_soporte = self._sub_menu.Append(wx.ID_ANY, lbl_soporte, "Contact support" if is_en else "Abrir canal de soporte por correo o incidencias")

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

            menu_title = "&Learning Python with NVDA" if is_en else "&Aprendizaje de Python con NVDA"
            self._menu_item_sub = self._tools_menu.AppendSubMenu(self._sub_menu, menu_title)
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
