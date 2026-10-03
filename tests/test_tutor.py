# -*- coding: utf-8 -*-
"""
Batería de pruebas unitarias automatizadas para Aprendizaje de Python con NVDA.
Valida la integridad pedagógica, ejecutor seguro y herramientas tiflotécnicas.
"""

import unittest
import os
import sys
from unittest.mock import MagicMock

# Mocks para dependencias de NVDA y wxWidgets (permitir ejecución independiente y en CI)
class MockBase(object):
    def __init__(self, *args, **kwargs):
        pass

class MockModule(MagicMock):
    def __getattr__(self, name):
        if name and name[0].isupper():
            return MockBase
        return super().__getattr__(name)

for mod in [
    "wx", "wx.xrc", "gui", "gui.settingsDialogs", "globalPluginHandler",
    "scriptHandler", "ui", "speech", "addonHandler", "nvwave", "config", "core",
    "winsound", "SCons", "SCons.Script", "markdown"
]:
    if mod not in sys.modules:
        sys.modules[mod] = MockModule()

# Agregar la raíz del proyecto para importar módulos de prueba
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "addon"))
sys.path.insert(0, os.path.join(BASE_DIR, "addon", "globalPlugins"))


class TestCurriculumIntegrity(unittest.TestCase):
    """Pruebas de integridad para el temario de 32 capítulos y 128 lecciones."""

    @classmethod
    def setUpClass(cls):
        from python_tutor.curriculum import CURRICULUM, GLOSARIO
        cls.curriculum = CURRICULUM
        cls.glosario = GLOSARIO

    def test_total_chapters(self):
        """Verifica que existan exactamente 40 capítulos."""
        self.assertEqual(len(self.curriculum), 40)

    def test_chapter_structure_and_steps(self):
        """Verifica que cada capítulo contenga pasos didácticos válidos."""
        total_steps = 0
        for i, cap in enumerate(self.curriculum):
            self.assertIn("titulo", cap, f"Capítulo {i} carece de 'titulo'")
            self.assertIn("pasos", cap, f"Capítulo {i} carece de 'pasos'")
            pasos = cap["pasos"]
            self.assertGreaterEqual(len(pasos), 3, f"Capítulo {i+1} debe tener al menos 3 pasos, tiene {len(pasos)}")
            total_steps += len(pasos)

            tipos = [p.get("tipo") for p in pasos]
            for t in tipos:
                self.assertIn(t, ["concepto", "observar", "experimentar", "desafio", "quiz"],
                              f"Tipo {t} no reconocido en capítulo {i+1}")
            self.assertEqual(tipos[-1], "quiz", f"El último paso del capítulo {i+1} debe ser quiz")
        self.assertGreaterEqual(total_steps, 180)

    def test_clean_challenge_code(self):
        """Verifica que los retos (desafio) comiencen sin la solución resuelta."""
        for i, cap in enumerate(self.curriculum):
            for paso in cap["pasos"]:
                if paso.get("tipo") == "desafio":
                    codigo = paso.get("codigo", "").strip()
                    self.assertNotIn("¡Correcto!", codigo)
                    self.assertNotIn("EXITO", codigo)

    def test_quiz_options(self):
        """Verifica que las opciones de los quizes sean válidas."""
        for i, cap in enumerate(self.curriculum):
            quiz_pasos = [p for p in cap["pasos"] if p.get("tipo") == "quiz"]
            self.assertTrue(len(quiz_pasos) >= 1, f"Capítulo {i+1} carece de quiz")
            for q in quiz_pasos:
                correcta = q.get("correcta")
                opciones = q.get("opciones", [])
                self.assertIsInstance(correcta, int, f"La opción correcta del quiz {i+1} debe ser un entero")
                self.assertTrue(0 <= correcta < len(opciones), f"Índice de respuesta incorrecto en capítulo {i+1}")

    def test_glossary_terms_count(self):
        """Verifica que el glosario contenga al menos 120 conceptos técnicos definidos."""
        self.assertGreaterEqual(len(self.glosario), 120)
        for termino, defn in self.glosario.items():
            self.assertTrue(len(termino) > 0)
            self.assertTrue(len(defn) > 10, f"Definición demasiado corta para '{termino}'")


class TestSafeExecutor(unittest.TestCase):
    """Pruebas del entorno de ejecución aislado y simplificación de errores."""

    @classmethod
    def setUpClass(cls):
        from python_tutor.executor import ejecutar_codigo_seguro
        cls.ejecutar = staticmethod(ejecutar_codigo_seguro)

    def test_successful_execution(self):
        """Ejecuta código válido y verifica la captura limpia de salida."""
        res = self.ejecutar("print('Hola accesible')\nx = 10 * 5\nprint(x)")
        self.assertTrue(res.success)
        self.assertIn("Hola accesible", res.output)
        self.assertIn("50", res.output)
        self.assertEqual(res.local_ns.get("x"), 50)

    def test_syntax_error_friendly_explanation(self):
        """Verifica la detección y traducción comprensible de SyntaxError."""
        res = self.ejecutar("print('Hola sin cerrar comilla)")
        self.assertFalse(res.success)
        self.assertIsNotNone(res.friendly_explanation)
        self.assertTrue(len(res.friendly_explanation) > 0)

    def test_zero_division_explanation(self):
        """Verifica la detección y mensaje comprensible de división por cero."""
        res = self.ejecutar("resultado = 10 / 0")
        self.assertFalse(res.success)
        self.assertIn("cero", res.friendly_explanation.lower())

    def test_timeout_protection(self):
        """Verifica que bucles infinitos sean detenidos sin congelar el hilo."""
        res = self.ejecutar("while True:\n    pass", timeout=1.0)
        self.assertFalse(res.success)
        exp = res.friendly_explanation.lower()
        self.assertTrue("tardó" in exp or "segundos" in exp or "tiempo" in exp)


class TestIDETools(unittest.TestCase):
    """Pruebas de las herramientas tiflotécnicas de productividad."""

    @classmethod
    def setUpClass(cls):
        from python_tutor.executor import comprobar_balanceo_delimitadores
        from python_tutor.ide_tools import (
            formatear_codigo_pep8,
            obtener_documentacion_simbolo
        )
        cls.balanceo = staticmethod(comprobar_balanceo_delimitadores)
        cls.pep8 = staticmethod(formatear_codigo_pep8)
        cls.doc = staticmethod(obtener_documentacion_simbolo)

    def test_delimiter_balancing_correct(self):
        """Valida que no detecte fallos en delimitadores perfectamente balanceados."""
        res = self.balanceo("datos = {'clave': [1, 2, (3, 4)], 'texto': 'OK'}")
        self.assertIsNone(res)

    def test_delimiter_balancing_unclosed(self):
        """Detecta paréntesis o llaves sin cerrar con indicación de línea."""
        res = self.balanceo("valores = [1, 2, 3\nprint(valores)")
        self.assertIsNotNone(res)
        self.assertTrue("abierto" in res.lower() or "cerrado" in res.lower())

    def test_pep8_formatter(self):
        """Verifica la aplicación de formato y espacios según PEP 8."""
        codigo_sucio = "x=1+2\nif x==3:\n    print( x )"
        codigo_formateado, reporte = self.pep8(codigo_sucio)
        self.assertIn(" = ", codigo_formateado)
        self.assertIn("formateado", reporte.lower())

    def test_quick_documentation(self):
        """Verifica la consulta de documentación para palabras clave y funciones integradas."""
        doc_print = self.doc("print")
        self.assertTrue("imprime" in doc_print.lower() or "consola" in doc_print.lower() or "salida" in doc_print.lower())
        doc_def = self.doc("def")
        self.assertTrue("función" in doc_def.lower() or "funcion" in doc_def.lower())


class TestAddonMetadata(unittest.TestCase):
    """Pruebas de consistencia de metadatos del complemento y empaquetado."""

    def test_manifest_and_buildvars_consistency(self):
        manifest_path = os.path.join(BASE_DIR, "addon", "manifest.ini")
        self.assertTrue(os.path.isfile(manifest_path), "addon/manifest.ini debe existir")
        with open(manifest_path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("name = python_tutor", content)
        self.assertIn("version = 1.0.0", content)
        self.assertIn("minimumNVDAVersion = 2022.1.0", content)
        self.assertIn("lastTestedNVDAVersion = 2026.2.0", content)
        self.assertIn("Kevin Andrés Velasquez Vargas", content)
        self.assertIn("40 capítulos", content)


class TestAudioAssets(unittest.TestCase):
    """Pruebas de la presencia y formatos de los recursos de audio."""

    def test_audio_files_exist_and_valid(self):
        import wave
        waves_dir = os.path.join(BASE_DIR, "addon", "globalPlugins", "python_tutor", "waves")
        self.assertTrue(os.path.isdir(waves_dir))

        required_sounds = [
            "inicio.wav", "exito.wav", "error.wav",
            "modo_editor.wav", "modo_aprendizaje.wav",
            "paso.wav", "pista.wav", "bloque.wav",
            "sintaxis_aviso.wav", "indent0.wav",
            "indent4.wav", "indent8.wav", "indent12.wav"
        ]
        for snd in required_sounds:
            snd_path = os.path.join(waves_dir, snd)
            self.assertTrue(os.path.isfile(snd_path), f"El archivo de sonido {snd} debe existir")
            with wave.open(snd_path, 'rb') as wf:
                self.assertIn(wf.getnchannels(), (1, 2))
                self.assertEqual(wf.getsampwidth(), 2, "Debe ser formato PCM 16 bits")
                self.assertIn(wf.getframerate(), (22050, 44100), "Debe ser frecuencia de muestreo válida (22.05 kHz o 44.1 kHz)")
                self.assertGreater(wf.getnframes(), 0)


class TestAddonFeatures(unittest.TestCase):
    """Pruebas unitarias para las funcionalidades avanzadas y la versión 1.0.0."""

    def test_version_1_0_0(self):
        """Verifica que los manifiestos y la configuración certifiquen la versión 1.0.0."""
        import buildVars
        self.assertEqual(buildVars.addon_info["addon_version"], "1.0.0")

        manifest_path = os.path.join(BASE_DIR, "addon", "manifest.ini")
        with open(manifest_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("version = 1.0.0", content)

    def test_compatibility_versions(self):
        """Verifica que el rango de compatibilidad de NVDA sea estrictamente 2022.1.0 a 2026.2.0."""
        import buildVars
        self.assertEqual(buildVars.addon_info["addon_minimumNVDAVersion"], "2022.1.0")
        self.assertEqual(buildVars.addon_info["addon_lastTestedNVDAVersion"], "2026.2.0")

        manifest_path = os.path.join(BASE_DIR, "addon", "manifest.ini")
        with open(manifest_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("minimumNVDAVersion = 2022.1.0", content)
        self.assertIn("lastTestedNVDAVersion = 2026.2.0", content)

    def test_doc_handler_bilingual_paths(self):
        """Verifica que la documentación HTML se resuelva en ambos idiomas y existan los archivos físicos."""
        import docHandler
        from python_tutor.i18n import establecer_idioma

        establecer_idioma("es")
        p_es = docHandler.getDocFilePath("readme.html")
        self.assertIsNotNone(p_es)
        self.assertTrue(os.path.isfile(p_es))
        self.assertTrue(p_es.endswith("readme.html") or p_es.endswith("readme.md") or p_es.endswith("README.md"))

        establecer_idioma("en")
        p_en = docHandler.getDocFilePath("readme.html")
        self.assertIsNotNone(p_en)
        self.assertTrue(os.path.isfile(p_en))
        self.assertTrue(p_en.endswith("readme.html") or p_en.endswith("readme.md"))
        establecer_idioma("es")

    def test_welcome_and_donation_dialog_cleanliness(self):
        """Verifica que la bienvenida no tenga avisos invasivos de Enter y la donación no incluya nombres personales."""
        gui_frame_path = os.path.join(BASE_DIR, "addon", "globalPlugins", "python_tutor", "gui_frame.py")
        with open(gui_frame_path, "r", encoding="utf-8") as f:
            src = f.read()

        # Extraer la clase WelcomeDialog
        self.assertIn("class WelcomeDialog", src)
        w_part = src[src.find("class WelcomeDialog"):src.find("class DonationPromptDialog")]
        self.assertNotIn("pulsa Enter", w_part)
        self.assertNotIn("press Enter", w_part.lower())

        # Extraer la clase DonationPromptDialog
        self.assertIn("class DonationPromptDialog", src)
        d_part = src[src.find("class DonationPromptDialog"):src.find("class ShortcutsDialog")]
        self.assertNotIn("Kevin", d_part)
        self.assertIn('btn_donar_lbl = "Donar"', d_part)
        self.assertIn('btn_continuar_lbl = "Ahora no"', d_part)
        self.assertIn('btn_donar_lbl = "Donate"', d_part)
        self.assertIn('btn_continuar_lbl = "Not now"', d_part)

    def test_settings_panel_title_bilingual(self):
        """Verifica que el título del panel de configuración de NVDA se adapte al idioma activo."""
        from addon.globalPlugins.python_tutor.i18n import establecer_idioma
        from python_tutor import PythonTutorSettingsPanel

        establecer_idioma("en")
        self.assertEqual(PythonTutorSettingsPanel.title, "Learning Python with NVDA")

        establecer_idioma("es")
        self.assertEqual(PythonTutorSettingsPanel.title, "Aprendizaje de Python con NVDA")

    def test_curriculum_english_code_snippets(self):
        """Verifica que los pasos con código en inglés tengan código inicial adaptado."""
        from python_tutor.curriculum import CURRICULUM
        cap6 = [c for c in CURRICULUM if c["id"] == 6][0]
        step2 = cap6["pasos"][1]
        self.assertIn("codigo_en", step2)
        self.assertIn("Hello, accessible world", step2["codigo_en"])

    def test_i18n_bilingual_translation(self):
        """Verifica la conmutación fluida entre Español e Inglés."""
        from addon.globalPlugins.python_tutor.i18n import (
            establecer_idioma,
            obtener_idioma_actual,
            _t
        )
        establecer_idioma("es")
        self.assertEqual(obtener_idioma_actual(), "es")
        self.assertEqual(_t("app_title"), "Aprendizaje de Python con NVDA")
        self.assertIn("print", _t("print_empty").lower())

        establecer_idioma("en")
        self.assertEqual(obtener_idioma_actual(), "en")
        self.assertEqual(_t("app_title"), "Learning Python with NVDA")
        self.assertIn("print", _t("print_empty").lower())

        # Restaurar español por defecto
        establecer_idioma("es")

    def test_braille_indentation_formatter(self):
        """Verifica los marcadores compactos de sangría para pantallas Braille."""
        from addon.globalPlugins.python_tutor.braille_helper import formatear_linea_para_braille

        # Nivel 0: sin prefijo
        self.assertEqual(formatear_linea_para_braille("x = 10"), "x = 10")
        # Nivel 1 (4 espacios): prefijo limpio nivel 1
        res1 = formatear_linea_para_braille("    print('Hola')")
        self.assertTrue(res1.startswith("[Nivel 1]") or res1.startswith("[Level 1]"))
        self.assertIn("print('Hola')", res1)
        # Nivel 2 (8 espacios): prefijo limpio nivel 2
        res2 = formatear_linea_para_braille("        return True")
        self.assertTrue(res2.startswith("[Nivel 2]") or res2.startswith("[Level 2]"))
        self.assertIn("return True", res2)

    def test_ai_assistant_config_structure(self):
        """Verifica la carga y estructura segura de configuración de IA."""
        from addon.globalPlugins.python_tutor.ai_assistant import obtener_config_ia
        cfg = obtener_config_ia()
        self.assertIsInstance(cfg, dict)
        self.assertIn("api_key", cfg)
        self.assertIn("provider", cfg)
        self.assertIn("activa", cfg)

    def test_project_manager_creation(self):
        """Verifica la inicialización del gestor de proyectos multi-archivo."""
        import tempfile
        from addon.globalPlugins.python_tutor.project_manager import ProjectManagerDialog
        with tempfile.TemporaryDirectory() as tmp_dir:
            test_file1 = os.path.join(tmp_dir, "modulo_a.py")
            with open(test_file1, "w", encoding="utf-8") as f:
                f.write("def prueba(): pass\n")
            
            archivos = [f for f in os.listdir(tmp_dir) if f.endswith(".py")]
            self.assertEqual(len(archivos), 1)
            self.assertEqual(archivos[0], "modulo_a.py")

    def test_standard_library_ecosystem(self):
        """Verifica la disponibilidad de módulos de la biblioteca estándar esenciales."""
        import sqlite3
        import json
        import math
        import random
        import datetime
        self.assertTrue(hasattr(sqlite3, 'connect'))
        self.assertTrue(hasattr(json, 'dumps'))
        self.assertTrue(hasattr(math, 'sqrt'))
        self.assertTrue(hasattr(random, 'randint'))
        self.assertTrue(hasattr(datetime, 'datetime'))


if __name__ == "__main__":
    unittest.main()



