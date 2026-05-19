# -*- coding: utf-8 -*-
# Módulo: __init__.py
import globalPluginHandler
import wx
import gui as nvda_gui
from scriptHandler import script
from .gui import TutorFrame
from .sound import SoundManager

# Importación segura de ui para mensajes hablados
try:
    import ui
except ImportError:
    ui = None

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    """Clase principal de Python Tutor."""
    scriptCategory = "Python Tutor"

    def __init__(self, *args, **kwargs):
        super(GlobalPlugin, self).__init__(*args, **kwargs)
        self.gui_frame = None
        self._add_to_tools_menu()
        # Inicializa la síntesis de sonidos asíncrona
        SoundManager.initialize()

    def terminate(self):
        self._remove_from_tools_menu()
        super().terminate()

    def _add_to_tools_menu(self):
        self._menu = wx.Menu()
        self._openItem = wx.MenuItem(self._menu, wx.ID_ANY, "Python Tutor")
        self._menu.Append(self._openItem)
        nvda_gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_openPythonTutor, self._openItem)
        nvda_gui.mainFrame.sysTrayIcon.toolsMenu.AppendSubMenu(self._menu, "Python Tutor")

    def _remove_from_tools_menu(self):
        try:
            nvda_gui.mainFrame.sysTrayIcon.toolsMenu.Remove(self._menu)
        except Exception:
            pass

    @script(
        description="Abre el entorno interactivo Python Tutor.",
        category="Python Tutor",
        gestures=["kb:NVDA+control+shift+p"]
    )
    def script_openPythonTutor(self, gesture=None):
        """Abre la interfaz de usuario de Python Tutor."""
        wx.CallAfter(self._crear_interfaz)

    def _crear_interfaz(self):
        parent_window = None
        try:
            if hasattr(nvda_gui, 'mainFrame') and nvda_gui.mainFrame:
                parent_window = nvda_gui.mainFrame
        except:
            pass
            
        if not self.gui_frame:
            try:
                self.gui_frame = TutorFrame(parent_window)
                self.gui_frame.Bind(wx.EVT_WINDOW_DESTROY, self.on_frame_destroy)
            except Exception as e:
                if ui: ui.message("Error al iniciar interfaz: " + str(e))
                return
        
        try:
            self.gui_frame.Show()
            self.gui_frame.Raise()
            self.gui_frame.lista_capitulos.SetFocus()
        except (RuntimeError, wx.PyDeadObjectError):
            self.gui_frame = TutorFrame(parent_window)
            self.gui_frame.Show()
            self.gui_frame.Raise()
            self.gui_frame.lista_capitulos.SetFocus()

    def on_frame_destroy(self, event):
        if event.GetEventObject() == self.gui_frame:
            self.gui_frame = None
        event.Skip()
