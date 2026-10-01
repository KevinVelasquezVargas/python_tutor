# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/repl_dialog.py
# Propósito: Laboratorio Rápido REPL interactivo accesible para pruebas inmediatas.
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import os
import sys
import io
import traceback
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
    import ui
    import speech
except ImportError:
    ui = None
    speech = None

from .audio_manager import SoundManager


class ReplDialog(wx.Dialog):
    """
    Diálogo accesible que funciona como una consola interactiva de una línea (REPL).
    Permite experimentar con sintaxis, tipos y funciones en tiempo real sin escribir
    un archivo completo.
    """
    def __init__(self, parent):
        super(ReplDialog, self).__init__(parent, title=_("Quick REPL Testing Lab"), size=(680, 520))

        self.historial_comandos = []
        self.indice_historial = -1
        self.namespace = {}

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Entrada de comando
        lbl_input = wx.StaticText(panel, label=_("Type an expression or command and press Enter to evaluate:"))
        lbl_input.SetName(_("Input instruction"))
        vbox.Add(lbl_input, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.input_ctrl = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.input_ctrl.SetName(_("Python command line. Type here and press Enter."))
        vbox.Add(self.input_ctrl, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        # Registro de resultados
        lbl_log = wx.StaticText(panel, label=_("Evaluation history:"))
        vbox.Add(lbl_log, flag=wx.LEFT | wx.TOP, border=12)

        self.log_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.log_ctrl.SetName(_("Results history. Navigate with arrow keys."))
        vbox.Add(self.log_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        # Botones
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_limpiar = wx.Button(panel, label=_("Clear History"))
        self.btn_limpiar.SetName(_("Clear History Button"))

        self.btn_cerrar = wx.Button(panel, wx.ID_CANCEL, label=_("Close Lab"))
        self.btn_cerrar.SetName(_("Close Lab Button"))

        hbox.Add(self.btn_limpiar, flag=wx.RIGHT, border=8)
        hbox.Add(self.btn_cerrar)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=12)

        panel.SetSizer(vbox)

        # Eventos
        self.input_ctrl.Bind(wx.EVT_TEXT_ENTER, self.on_evaluar)
        self.input_ctrl.Bind(wx.EVT_KEY_DOWN, self.on_key_down_input)
        self.btn_limpiar.Bind(wx.EVT_BUTTON, self.on_limpiar)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)

        self.CenterOnParent()
        self.input_ctrl.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

    def on_key_down_input(self, event):
        keycode = event.GetKeyCode()
        # Navegación en el historial con flecha arriba y abajo
        if keycode == wx.WXK_UP:
            if self.historial_comandos and self.indice_historial > 0:
                self.indice_historial -= 1
                self.input_ctrl.SetValue(self.historial_comandos[self.indice_historial])
                self.input_ctrl.SetInsertionPointEnd()
            return
        elif keycode == wx.WXK_DOWN:
            if self.historial_comandos and self.indice_historial < len(self.historial_comandos) - 1:
                self.indice_historial += 1
                self.input_ctrl.SetValue(self.historial_comandos[self.indice_historial])
                self.input_ctrl.SetInsertionPointEnd()
            elif self.indice_historial >= len(self.historial_comandos) - 1:
                self.indice_historial = len(self.historial_comandos)
                self.input_ctrl.SetValue("")
            return
        event.Skip()

    def on_evaluar(self, event):
        cmd = self.input_ctrl.GetValue().strip()
        if not cmd:
            return

        self.historial_comandos.append(cmd)
        self.indice_historial = len(self.historial_comandos)
        self.input_ctrl.SetValue("")

        buf = io.StringIO()
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = buf
        sys.stderr = buf

        exito = True
        resultado_str = ""

        try:
            # Primero intentar evaluar como expresión
            try:
                res_val = eval(cmd, {"__builtins__": __builtins__}, self.namespace)
                if res_val is not None:
                    resultado_str = repr(res_val)
            except SyntaxError:
                # Si no es expresión, ejecutar como sentencia
                exec(cmd, {"__builtins__": __builtins__}, self.namespace)
                resultado_str = buf.getvalue().strip()
                if not resultado_str:
                    resultado_str = _("Statement executed successfully (no return value).")
        except Exception as e:
            exito = False
            # Translators: Message shown when an error occurs during code execution in the REPL dialog.
            # {error_type} is the exception class name, {error_msg} is the exception message.
            resultado_str = _("Error ({error_type}): {error_msg}").format(error_type=type(e).__name__, error_msg=e)
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

        # Añadir al log
        log_entry = f">>> {cmd}\n{resultado_str}\n\n"
        self.log_ctrl.AppendText(log_entry)

        # Feedback auditivo y hablado inmediato
        if exito:
            SoundManager.play('paso')
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(resultado_str)
            if ui:
                ui.message(resultado_str)
        else:
            SoundManager.play('error')
            if ui:
                ui.message(resultado_str)

    def on_limpiar(self, event):
        self.log_ctrl.SetValue("")
        self.input_ctrl.SetFocus()
        if ui:
            ui.message(_("Lab history cleared."))
