# -*- coding: utf-8 -*-
# Módulo: sound.py
import os
import threading
import winsound
import wave
import struct
import math
import tempfile

class SoundManager:
    _paths = {}
    _initialized = False

    @classmethod
    def initialize(cls):
        if cls._initialized:
            return
        t = threading.Thread(target=cls._generate_all_waves)
        t.daemon = True
        t.start()
        cls._initialized = True

    @classmethod
    def _generate_all_waves(cls):
        temp_dir = tempfile.gettempdir()
        cls._paths = {
            'inicio': os.path.join(temp_dir, 'pytutor_inicio.wav'),
            'exito': os.path.join(temp_dir, 'pytutor_exito.wav'),
            'error': os.path.join(temp_dir, 'pytutor_error.wav'),
            'indent0': os.path.join(temp_dir, 'pytutor_indent0.wav'),
            'indent4': os.path.join(temp_dir, 'pytutor_indent4.wav'),
            'indent8': os.path.join(temp_dir, 'pytutor_indent8.wav'),
            'indent12': os.path.join(temp_dir, 'pytutor_indent12.wav'),
            'fin_bloque': os.path.join(temp_dir, 'pytutor_fin_bloque.wav'),
            'glosario': os.path.join(temp_dir, 'pytutor_glosario.wav')
        }

        try:
            cls._write_click(cls._paths['indent0'])
            cls._write_fm_bell(cls._paths['indent4'], 880, 0.35)
            cls._write_fm_bell(cls._paths['indent8'], 1100, 0.35)
            cls._write_fm_bell(cls._paths['indent12'], 1320, 0.35)
            cls._write_sweep(cls._paths['fin_bloque'], 320, 1400, 0.25)
            cls._write_fm_bell(cls._paths['glosario'], 587.33, 0.5, 3.0, 1.5)
            cls._write_deep_pulse(cls._paths['error'], 150, 80, 0.4)
            cls._write_arpeggio(cls._paths['exito'], [523.25, 659.25, 783.99, 1046.50], 0.08, 0.35)
            cls._write_arpeggio(cls._paths['inicio'], [130.81, 261.63, 392.00, 523.25, 659.25, 987.77], 0.12, 0.45)
        except Exception:
            pass 

    @classmethod
    def _write_wav_file(cls, path, data, sample_rate=44100):
        with wave.open(path, 'wb') as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(sample_rate)
            for val in data:
                val_int = max(-32767, min(32767, int(val * 32767)))
                f.writeframesraw(struct.pack('<h', val_int))

    @classmethod
    def _write_click(cls, path):
        sr = 44100
        dur = 0.04
        num_s = int(sr * dur)
        data = []
        for i in range(num_s):
            t = i / float(sr)
            val = math.sin(2 * math.pi * 110 * t) * math.exp(-120 * t) * 0.4
            data.append(val)
        cls._write_wav_file(path, data)

    @classmethod
    def _write_fm_bell(cls, path, freq, duration, mod_coeff=2.0, mod_idx=1.3):
        sr = 44100
        num_s = int(sr * duration)
        data = []
        for i in range(num_s):
            t = i / float(sr)
            modulator = math.sin(2 * math.pi * freq * mod_coeff * t) * math.exp(-25 * t)
            val = math.sin(2 * math.pi * freq * t + mod_idx * modulator) * math.exp(-8 * t) * 0.3
            data.append(val)
        cls._write_wav_file(path, data)

    @classmethod
    def _write_sweep(cls, path, start_f, end_f, duration):
        sr = 44100
        num_s = int(sr * duration)
        data = []
        for i in range(num_s):
            t = i / float(sr)
            ratio = t / duration
            curr_f = start_f * ((end_f / float(start_f)) ** ratio)
            val = math.sin(2 * math.pi * curr_f * t) * (1.0 - ratio) * 0.2
            data.append(val)
        cls._write_wav_file(path, data)

    @classmethod
    def _write_deep_pulse(cls, path, start_f, end_f, duration):
        sr = 44100
        num_s = int(sr * duration)
        data = []
        for i in range(num_s):
            t = i / float(sr)
            ratio = t / duration
            curr_f = start_f - (start_f - end_f) * ratio
            val = (math.sin(2 * math.pi * curr_f * t) * 0.5 + 
                   math.sin(2 * math.pi * curr_f * 2.0 * t) * 0.3 + 
                   math.sin(2 * math.pi * curr_f * 3.0 * t) * 0.15) * math.exp(-6 * t) * 0.4
            data.append(val)
        cls._write_wav_file(path, data)

    @classmethod
    def _write_arpeggio(cls, path, notes, time_step, note_dur):
        sr = 44100
        total_duration = time_step * len(notes) + note_dur
        num_s = int(sr * total_duration)
        data = [0.0] * num_s

        for idx, freq in enumerate(notes):
            start_s = int(idx * time_step * sr)
            note_len = int(note_dur * sr)
            for i in range(note_len):
                target_idx = start_s + i
                if target_idx < num_s:
                    t = i / float(sr)
                    modulator = math.sin(2 * math.pi * freq * 2.01 * t) * math.exp(-25 * t)
                    val = math.sin(2 * math.pi * freq * t + 1.2 * modulator) * math.exp(-8 * t) * 0.25
                    data[target_idx] += val

        max_val = max(abs(x) for x in data) if data else 1.0
        if max_val > 0.9:
            data = [x / max_val * 0.9 for x in data]

        cls._write_wav_file(path, data)

    @classmethod
    def play(cls, name):
        if name in cls._paths and os.path.exists(cls._paths[name]):
            try:
                winsound.PlaySound(cls._paths[name], winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception:
                pass
