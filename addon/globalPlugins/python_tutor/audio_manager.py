# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/audio_manager.py
# Propósito: Reproducción de señales acústicas accesibles mediante nvwave y winsound.
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import os
import wave
import struct
import math

try:
    import winsound
except ImportError:
    winsound = None

try:
    import nvwave
except ImportError:
    nvwave = None

try:
    from .progress import ProgressManager
except ImportError:
    ProgressManager = None


class SoundManager:
    """
    Gestor de audio accesible y confiable para NVDA.
    Utiliza el motor nativo nvwave de NVDA con respaldo en winsound.
    Carga las formas de onda desde el subdirectorio empaquetado 'waves/'.
    """
    _base_dir = os.path.dirname(os.path.abspath(__file__))
    _waves_dir = os.path.join(_base_dir, "waves")
    _paths = {}
    _initialized = False
    _sample_rate = 22050

    @classmethod
    def initialize(cls):
        """Inicializa las rutas a los archivos WAV y genera los faltantes si fuera necesario."""
        if cls._initialized and os.path.exists(cls._paths.get('inicio', '')):
            return

        os.makedirs(cls._waves_dir, exist_ok=True)
        cls._paths = {
            'inicio': os.path.join(cls._waves_dir, 'inicio.wav'),
            'exito': os.path.join(cls._waves_dir, 'exito.wav'),
            'error': os.path.join(cls._waves_dir, 'error.wav'),
            'pista': os.path.join(cls._waves_dir, 'pista.wav'),
            'paso': os.path.join(cls._waves_dir, 'paso.wav'),
            'indent0': os.path.join(cls._waves_dir, 'indent0.wav'),
            'indent4': os.path.join(cls._waves_dir, 'indent4.wav'),
            'indent8': os.path.join(cls._waves_dir, 'indent8.wav'),
            'indent12': os.path.join(cls._waves_dir, 'indent12.wav'),
            'bloque': os.path.join(cls._waves_dir, 'bloque.wav'),
            'sintaxis_aviso': os.path.join(cls._waves_dir, 'sintaxis_aviso.wav'),
            'modo_editor': os.path.join(cls._waves_dir, 'modo_editor.wav'),
            'modo_aprendizaje': os.path.join(cls._waves_dir, 'modo_aprendizaje.wav')
        }

        # Generar únicamente los archivos que no existan en disco
        cls._generate_missing_waves()
        cls._initialized = True

    @classmethod
    def _generate_missing_waves(cls):
        try:
            if not os.path.exists(cls._paths['inicio']):
                cls._write_arpeggio(cls._paths['inicio'], [261.63, 329.63, 392.00, 523.25, 659.25], 0.05, 0.22)
            if not os.path.exists(cls._paths['exito']):
                cls._write_arpeggio(cls._paths['exito'], [523.25, 659.25, 783.99, 1046.50], 0.05, 0.20)
            if not os.path.exists(cls._paths['error']):
                cls._write_soft_pulse(cls._paths['error'], 160, 80, 0.25)
            if not os.path.exists(cls._paths['pista']):
                cls._write_fm_bell(cls._paths['pista'], 659.25, 0.28, 2.0, 1.0)
            if not os.path.exists(cls._paths['paso']):
                cls._write_sweep(cls._paths['paso'], 440, 880, 0.10)
            if not os.path.exists(cls._paths['indent0']):
                cls._write_click(cls._paths['indent0'])
            if not os.path.exists(cls._paths['indent4']):
                cls._write_fm_bell(cls._paths['indent4'], 880, 0.18)
            if not os.path.exists(cls._paths['indent8']):
                cls._write_fm_bell(cls._paths['indent8'], 1100, 0.18)
            if not os.path.exists(cls._paths['indent12']):
                cls._write_fm_bell(cls._paths['indent12'], 1320, 0.18)
            if not os.path.exists(cls._paths['bloque']):
                cls._write_sweep(cls._paths['bloque'], 340, 1200, 0.14)
            if not os.path.exists(cls._paths['sintaxis_aviso']):
                cls._write_descending_tone(cls._paths['sintaxis_aviso'], 550, 280, 0.16)
            if not os.path.exists(cls._paths['modo_editor']):
                cls._write_arpeggio(cls._paths['modo_editor'], [587.33, 440.0], 0.06, 0.12)
            if not os.path.exists(cls._paths['modo_aprendizaje']):
                cls._write_arpeggio(cls._paths['modo_aprendizaje'], [440.0, 554.37, 659.25], 0.05, 0.14)
        except Exception:
            pass

    @classmethod
    def _write_wav(cls, path, samples):
        sr = cls._sample_rate
        raw = bytearray()
        for s in samples:
            val = max(-32767, min(32767, int(s * 32767)))
            raw.extend(struct.pack('<h', val))
        with wave.open(path, 'wb') as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(sr)
            f.writeframesraw(raw)

    @classmethod
    def _write_click(cls, path):
        sr = cls._sample_rate
        n = int(sr * 0.02)
        samples = [math.sin(2 * math.pi * 120 * (i / sr)) * math.exp(-120 * (i / sr)) * 0.35 for i in range(n)]
        cls._write_wav(path, samples)

    @classmethod
    def _write_fm_bell(cls, path, freq, duration, mod_coeff=2.0, mod_idx=1.0):
        sr = cls._sample_rate
        n = int(sr * duration)
        samples = []
        for i in range(n):
            t = i / float(sr)
            modulator = math.sin(2 * math.pi * freq * mod_coeff * t) * math.exp(-20 * t)
            val = math.sin(2 * math.pi * freq * t + mod_idx * modulator) * math.exp(-8 * t) * 0.32
            samples.append(val)
        cls._write_wav(path, samples)

    @classmethod
    def _write_sweep(cls, path, start_f, end_f, duration):
        sr = cls._sample_rate
        n = int(sr * duration)
        samples = []
        for i in range(n):
            t = i / float(sr)
            ratio = t / duration
            curr_f = start_f * ((end_f / float(start_f)) ** ratio)
            val = math.sin(2 * math.pi * curr_f * t) * (1.0 - ratio) * 0.28
            samples.append(val)
        cls._write_wav(path, samples)

    @classmethod
    def _write_descending_tone(cls, path, start_f, end_f, duration):
        sr = cls._sample_rate
        n = int(sr * duration)
        samples = []
        for i in range(n):
            t = i / float(sr)
            ratio = t / duration
            curr_f = start_f - (start_f - end_f) * ratio
            val = math.sin(2 * math.pi * curr_f * t) * math.exp(-7 * t) * 0.32
            samples.append(val)
        cls._write_wav(path, samples)

    @classmethod
    def _write_soft_pulse(cls, path, start_f, end_f, duration):
        sr = cls._sample_rate
        n = int(sr * duration)
        samples = []
        for i in range(n):
            t = i / float(sr)
            ratio = t / duration
            curr_f = start_f - (start_f - end_f) * ratio
            val = (math.sin(2 * math.pi * curr_f * t) * 0.65 +
                   math.sin(2 * math.pi * curr_f * 2.0 * t) * 0.35) * math.exp(-6 * t) * 0.38
            samples.append(val)
        cls._write_wav(path, samples)

    @classmethod
    def _write_arpeggio(cls, path, notes, time_step, note_dur):
        sr = cls._sample_rate
        total_duration = time_step * len(notes) + note_dur
        n = int(sr * total_duration)
        data = [0.0] * n

        for idx, freq in enumerate(notes):
            start_s = int(idx * time_step * sr)
            note_len = int(note_dur * sr)
            for i in range(note_len):
                target_idx = start_s + i
                if target_idx < n:
                    t = i / float(sr)
                    modulator = math.sin(2 * math.pi * freq * 2.0 * t) * math.exp(-20 * t)
                    val = math.sin(2 * math.pi * freq * t + 1.0 * modulator) * math.exp(-7 * t) * 0.28
                    data[target_idx] += val

        max_val = max(abs(x) for x in data) if data else 1.0
        if max_val > 0.9:
            data = [x / max_val * 0.9 for x in data]

        cls._write_wav(path, data)

    @classmethod
    def play(cls, name):
        """Reproduce la señal acústica solicitada de forma no bloqueante y 100% segura."""
        if ProgressManager:
            try:
                prog = ProgressManager.load_progress()
                if not prog.get("sound_enabled", True):
                    return
            except Exception:
                pass

        if not cls._initialized or name not in cls._paths or not os.path.exists(cls._paths.get(name, '')):
            cls.initialize()

        wave_file = cls._paths.get(name)
        if wave_file and os.path.exists(wave_file):
            # 1. Prioridad: nvwave de NVDA (canal no bloqueante dedicado)
            if nvwave and hasattr(nvwave, 'playWaveFile'):
                try:
                    nvwave.playWaveFile(wave_file)
                    return
                except Exception:
                    pass

            # 2. Respaldo: winsound de Windows
            if winsound:
                try:
                    winsound.PlaySound(
                        wave_file,
                        winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT
                    )
                    return
                except Exception:
                    pass

        # 3. Respaldo acústico mínimo del sistema si el archivo no responde
        if winsound:
            try:
                winsound.MessageBeep(winsound.MB_OK)
            except Exception:
                pass

    @classmethod
    def cleanup(cls):
        """No elimina los archivos empaquetados en waves/ para mantener el rendimiento."""
        pass
