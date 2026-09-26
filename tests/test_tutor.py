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
    "scriptHandler", "ui", "speech", "addonHandler", "nvwave", "config", "core"
]:
    if mod not in sys.modules:
        sys.modules[mod] = MockModule()

# Agregar la raíz del proyecto para importar módulos de prueba
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "globalPlugins"))


class TestCurriculumIntegrity(unittest.TestCase):
    """Pruebas de integridad para el temario de 32 capítulos y 128 lecciones."""

    @classmethod
    def setUpClass(cls):
        from python_tutor.curriculum import CURRICULUM, GLOSARIO
        cls.curriculum = CURRICULUM
        cls.glosario = GLOSARIO

    def test_total_chapters(self):
        """Verifica que existan exactamente 32 capítulos."""
        self.assertEqual(len(self.curriculum), 32)

    def test_chapter_structure_and_steps(self):
        """Verifica que cada capítulo contenga exactamente 4 pasos didácticos (128 en total)."""
        total_steps = 0
        for i, cap in enumerate(self.curriculum):
            self.assertIn("titulo", cap, f"Capítulo {i} carece de 'titulo'")
            self.assertIn("pasos", cap, f"Capítulo {i} carece de 'pasos'")
            pasos = cap["pasos"]
            self.assertEqual(len(pasos), 4, f"Capítulo {i+1} debe tener exactamente 4 pasos, tiene {len(pasos)}")
            total_steps += len(pasos)

            # Verificar tipos de pasos: observar, experimentar, desafio, quiz
            tipos = [p.get("tipo") for p in pasos]
            self.assertEqual(tipos, ["observar", "experimentar", "desafio", "quiz"],
                             f"Capítulo {i+1} no sigue el ciclo de 4 pasos estandarizado")
        self.assertEqual(total_steps, 128)

    def test_clean_challenge_code(self):
        """Verifica que todos los retos (Paso 3) tengan lienzo limpio para escribir."""
        for i, cap in enumerate(self.curriculum):
            paso3 = cap["pasos"][2]
            codigo = paso3.get("codigo", "").strip()
            self.assertTrue(
                codigo == "" or codigo.startswith("#"),
                f"El código inicial del Paso 3 en capítulo {i+1} debe estar en blanco o solo con comentario guía"
            )

    def test_quiz_options(self):
        """Verifica que las opciones de los quizes (Paso 4) sean válidas."""
        for i, cap in enumerate(self.curriculum):
            paso4 = cap["pasos"][3]
            correcta = paso4.get("correcta")
            opciones = paso4.get("opciones", [])
            self.assertIsInstance(correcta, int, f"La opción correcta del quiz {i+1} debe ser un entero")
            self.assertTrue(0 <= correcta < len(opciones), f"Índice de respuesta incorrecto en capítulo {i+1}")

    def test_glossary_terms_count(self):
        """Verifica que el glosario contenga al menos 114 conceptos técnicos definidos."""
        self.assertGreaterEqual(len(self.glosario), 114)
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


class TestAudioAssets(unittest.TestCase):
    """Pruebas de la presencia y formatos de los recursos de audio."""

    def test_audio_files_exist_and_valid(self):
        import wave
        waves_dir = os.path.join(BASE_DIR, "globalPlugins", "python_tutor", "waves")
        self.assertTrue(os.path.isdir(waves_dir))

        required_sounds = [
            "inicio.wav", "exito.wav", "error.wav",
            "modo_editor.wav", "modo_aprendizaje.wav",
            "paso.wav", "pista.wav", "indent0.wav", "indent4.wav"
        ]
        for snd in required_sounds:
            snd_path = os.path.join(waves_dir, snd)
            self.assertTrue(os.path.isfile(snd_path), f"El archivo de sonido {snd} debe existir")
            with wave.open(snd_path, 'rb') as wf:
                self.assertIn(wf.getnchannels(), (1, 2))
                self.assertEqual(wf.getsampwidth(), 2, "Debe ser formato PCM 16 bits")
                self.assertGreater(wf.getnframes(), 0)


if __name__ == "__main__":
    unittest.main()
