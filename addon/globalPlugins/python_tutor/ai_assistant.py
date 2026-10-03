# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/ai_assistant.py
# Propósito: Asistente pedagógico de Inteligencia Artificial accesible para NVDA.
# Autor: Kevin Andrés Velasquez Vargas
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import json
import os
import threading
import urllib.request
import urllib.error
import wx

try:
    import ui
    import speech
except ImportError:
    ui = None
    speech = None

CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".python_tutor")
CONFIG_FILE = os.path.join(CONFIG_DIR, "ai_config.json")


def obtener_config_ia():
    """Carga la configuración de IA almacenada localmente de forma segura."""
    if not os.path.exists(CONFIG_DIR):
        try:
            os.makedirs(CONFIG_DIR)
        except Exception:
            pass

    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "api_key": "",
        "provider": "gemini",
        "model": "gemini-1.5-flash",
        "activa": False
    }


def guardar_config_ia(config):
    """Guarda la configuración de IA localmente."""
    if not os.path.exists(CONFIG_DIR):
        try:
            os.makedirs(CONFIG_DIR)
        except Exception:
            pass
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        return True
    except Exception:
        return False


def consultar_gemini_api(api_key, prompt_sistema, prompt_usuario, callback_exito, callback_error):
    """
    Realiza una consulta asíncrona a la API de Google Gemini en un hilo secundario
    para no congelar nunca el lector de pantalla NVDA.
    """
    def _worker():
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt_sistema + "\n\nConsulta del estudiante:\n" + prompt_usuario}
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.3,
                "maxOutputTokens": 600
            }
        }

        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=data,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST"
        )

        try:
            with urllib.request.urlopen(req, timeout=12) as response:
                res_json = json.loads(response.read().decode("utf-8"))
                candidatos = res_json.get("candidates", [])
                if candidatos and "content" in candidatos[0]:
                    partes = candidatos[0]["content"].get("parts", [])
                    if partes:
                        texto = partes[0].get("text", "").strip()
                        wx.CallAfter(callback_exito, texto)
                        return
                wx.CallAfter(callback_error, "No se recibió respuesta válida del servicio de IA.")
        except urllib.error.HTTPError as e:
            msg = f"Error en la API ({e.code}): Clave inválida o límite de consultas alcanzado."
            wx.CallAfter(callback_error, msg)
        except Exception as e:
            wx.CallAfter(callback_error, f"No fue posible conectar con el asistente de IA: {str(e)}")

    t = threading.Thread(target=_worker)
    t.daemon = True
    t.start()


class AIConfigDialog(wx.Dialog):
    """Diálogo accesible para configurar la clave de API del Asistente de IA."""
    def __init__(self, parent):
        super(AIConfigDialog, self).__init__(
            parent,
            title="Configuración del Asistente de Inteligencia Artificial",
            size=(520, 320)
        )
        self.config = obtener_config_ia()

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        info = wx.StaticText(
            panel,
            label="El Asistente de IA permite recibir explicaciones personalizadas y resolución de dudas sobre tu código.\n"
                  "Puedes obtener una clave de API gratuita en Google AI Studio (aistudio.google.com)."
        )
        vbox.Add(info, flag=wx.ALL, border=12)

        lbl_key = wx.StaticText(panel, label="Clave de API de Google Gemini:")
        vbox.Add(lbl_key, flag=wx.LEFT | wx.RIGHT, border=12)

        self.txt_key = wx.TextCtrl(panel, value=self.config.get("api_key", ""), style=wx.TE_PASSWORD)
        vbox.Add(self.txt_key, flag=wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, border=12)

        self.chk_activa = wx.CheckBox(panel, label="Habilitar el Asistente de IA en el Tutor y Editor (F1 con IA)")
        self.chk_activa.SetValue(self.config.get("activa", False))
        vbox.Add(self.chk_activa, flag=wx.ALL, border=12)

        btn_sizer = wx.StdDialogButtonSizer()
        btn_ok = wx.Button(panel, wx.ID_OK, label="Guardar")
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label="Cancelar")
        btn_sizer.AddButton(btn_ok)
        btn_sizer.AddButton(btn_cancel)
        btn_sizer.Realize()
        vbox.Add(btn_sizer, flag=wx.ALL | wx.ALIGN_RIGHT, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.on_guardar, id=wx.ID_OK)
        self.CentreOnParent()

    def on_guardar(self, event):
        key = self.txt_key.GetValue().strip()
        activa = self.chk_activa.IsChecked()
        self.config["api_key"] = key
        self.config["activa"] = activa and bool(key)
        guardar_config_ia(self.config)
        event.Skip()


class AIConsultDialog(wx.Dialog):
    """
    Diálogo accesible para consultar dudas de programación al Asistente de IA.
    Totalmente manejable por teclado para lectores de pantalla.
    """
    def __init__(self, parent, codigo_actual="", linea_actual="", error_reciente=""):
        super(AIConsultDialog, self).__init__(
            parent,
            title="Asistente Pedagógico de Inteligencia Artificial",
            size=(580, 480)
        )
        self.parent = parent
        self.codigo_actual = codigo_actual
        self.linea_actual = linea_actual
        self.error_reciente = error_reciente
        self.config = obtener_config_ia()

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl_pregunta = wx.StaticText(panel, label="Escribe tu consulta o duda sobre el código:")
        vbox.Add(lbl_pregunta, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_pregunta = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        vbox.Add(self.txt_pregunta, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=12)

        lbl_respuesta = wx.StaticText(panel, label="Explicación del Asistente:")
        vbox.Add(lbl_respuesta, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_respuesta = wx.TextCtrl(
            panel,
            style=wx.TE_MULTILINE | wx.TE_READONLY,
            size=(-1, 200)
        )
        vbox.Add(self.txt_respuesta, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=12)

        hbox_btns = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_consultar = wx.Button(panel, label="Preguntar al Asistente")
        self.btn_cerrar = wx.Button(panel, wx.ID_CANCEL, label="Cerrar")
        hbox_btns.Add(self.btn_consultar, flag=wx.RIGHT, border=8)
        hbox_btns.Add(self.btn_cerrar)
        vbox.Add(hbox_btns, flag=wx.ALL | wx.ALIGN_RIGHT, border=12)

        panel.SetSizer(vbox)

        self.btn_consultar.Bind(wx.EVT_BUTTON, self.on_consultar)
        self.txt_pregunta.Bind(wx.EVT_TEXT_ENTER, self.on_consultar)
        self.CentreOnParent()

        # Si había un error reciente, sugerir la consulta automáticamente
        if self.error_reciente:
            self.txt_pregunta.SetValue("¿Por qué ocurrió este error en mi código y cómo puedo solucionarlo?")

    def on_consultar(self, event=None):
        pregunta = self.txt_pregunta.GetValue().strip()
        if not pregunta:
            if ui: ui.message("Por favor escribe una consulta primero.")
            return

        api_key = self.config.get("api_key", "").strip()
        if not api_key:
            self.txt_respuesta.SetValue(
                "El Asistente de IA no tiene configurada una clave de API.\n"
                "Ve a Menú Herramientas > Configuración del Asistente de IA para ingresar tu clave gratuita de Google Gemini."
            )
            self.txt_respuesta.SetFocus()
            return

        self.txt_respuesta.SetValue("Consultando al Asistente Pedagógico... Por favor espera un momento.")
        if ui: ui.message("Consultando al Asistente...")

        prompt_sistema = (
            "Eres un tutor pedagógico de Python de alto nivel especializado en tiflotecnología y "
            "accesibilidad para personas ciegas usuarias del lector de pantalla NVDA.\n"
            "Pautas estrictas:\n"
            "1. Explica con claridad, empatía y rigor técnico.\n"
            "2. NUNCA uses referencias visuales (no digas 'como ves en la pantalla' o 'fíjate en los colores').\n"
            "3. Explica los errores dando analogías comprensibles por voz y orientadas a la estructura sonora y la sangría PEP 8.\n"
            "4. Sé conciso y directo (máximo 2 a 3 párrafos).\n\n"
            f"Contexto del código actual del estudiante:\n```python\n{self.codigo_actual}\n```\n"
            f"Línea donde se encuentra el cursor: {self.linea_actual}\n"
            f"Último error o Traceback: {self.error_reciente}\n"
        )

        consultar_gemini_api(
            api_key,
            prompt_sistema,
            pregunta,
            self._on_exito,
            self._on_error
        )

    def _on_exito(self, respuesta):
        self.txt_respuesta.SetValue(respuesta)
        self.txt_respuesta.SetFocus()
        if ui: ui.message("Respuesta recibida del Asistente.")

    def _on_error(self, error):
        self.txt_respuesta.SetValue(f"Aviso del Asistente:\n{error}")
        self.txt_respuesta.SetFocus()
        if ui: ui.message("Aviso recibido del Asistente.")
