# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/progress.py
# Propósito: Persistencia y seguimiento del avance y configuración del alumno.
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import os
import json

try:
    import globalVars
except ImportError:
    globalVars = None


class ProgressManager:
    """
    Gestiona el almacenamiento y recuperación del progreso y configuración del estudiante
    en el perfil local del usuario, asegurando persistencia entre sesiones de NVDA.
    """
    _file_path = None

    @classmethod
    def _get_storage_path(cls):
        if cls._file_path:
            return cls._file_path

        # Limpiar archivo huérfano de versiones previas si existiera en la raíz de configuración
        if globalVars and hasattr(globalVars, 'appArgs') and hasattr(globalVars.appArgs, 'configPath') and globalVars.appArgs.configPath:
            legacy_path = os.path.join(globalVars.appArgs.configPath, "python_tutor_user_progress.json")
            if os.path.isfile(legacy_path):
                try:
                    os.remove(legacy_path)
                except Exception:
                    pass

        # Almacenar dentro del propio complemento para que al desinstalarlo se elimine por completo
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_data")
        try:
            os.makedirs(base_dir, exist_ok=True)
        except Exception:
            pass

        cls._file_path = os.path.join(base_dir, "progress.json")
        return cls._file_path

    @classmethod
    def load_progress(cls):
        """Carga el diccionario de configuración y progreso desde el archivo JSON."""
        path = cls._get_storage_path()
        default_data = {
            "current_chapter": 0,
            "current_step": 0,
            "completed_steps": {},     # Formato: {"cap_0": [0, 1, 2, 3]}
            "completed_chapters": [],  # Lista de índices de capítulos finalizados
            "hints_used": 0,
            "exercises_passed": 0,
            "sound_enabled": True,
            "linter_enabled": True,
            "show_welcome": True,
            "editor_mode": "learning"
        }
        if not os.path.exists(path):
            return default_data

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for k, v in default_data.items():
                    if k not in data:
                        data[k] = v
                return data
        except Exception:
            return default_data

    @classmethod
    def save_progress(cls, data):
        """Guarda la configuración y avances del usuario en el archivo JSON."""
        path = cls._get_storage_path()
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception:
            return False

    @classmethod
    def mark_step_completed(cls, chapter_idx, step_idx):
        """Registra un paso superado y actualiza estadísticas."""
        progress = cls.load_progress()
        cap_key = f"cap_{chapter_idx}"

        if cap_key not in progress["completed_steps"]:
            progress["completed_steps"][cap_key] = []

        if step_idx not in progress["completed_steps"][cap_key]:
            progress["completed_steps"][cap_key].append(step_idx)
            progress["exercises_passed"] += 1

        cls.save_progress(progress)
        return progress

    @classmethod
    def is_step_completed(cls, chapter_idx, step_idx):
        """Indica si un paso concreto ya fue aprobado por el estudiante."""
        progress = cls.load_progress()
        cap_key = f"cap_{chapter_idx}"
        return step_idx in progress.get("completed_steps", {}).get(cap_key, [])

    @classmethod
    def is_chapter_completed(cls, chapter_idx, total_steps_in_chapter):
        """Indica si todos los pasos de un capítulo han sido completados."""
        progress = cls.load_progress()
        cap_key = f"cap_{chapter_idx}"
        completed = progress.get("completed_steps", {}).get(cap_key, [])
        return all(s in completed for s in range(total_steps_in_chapter))

    @classmethod
    def is_chapter_unlocked(cls, chapter_idx):
        """El capítulo 0 siempre está disponible; el capítulo N requiere haber completado el N-1."""
        if chapter_idx <= 0:
            return True
        from .curriculum import CURRICULUM
        if chapter_idx >= len(CURRICULUM):
            return False
        prev_cap = CURRICULUM[chapter_idx - 1]
        return cls.is_chapter_completed(chapter_idx - 1, len(prev_cap.get("pasos", [])))

    @classmethod
    def get_setting(cls, key, default_value=True):
        """Obtiene una preferencia de configuración específica."""
        prog = cls.load_progress()
        return prog.get(key, default_value)

    @classmethod
    def set_setting(cls, key, value):
        """Establece y guarda una preferencia de configuración específica."""
        prog = cls.load_progress()
        prog[key] = value
        cls.save_progress(prog)

    @classmethod
    def get_editor_mode(cls):
        """Devuelve el modo de trabajo activo ('learning' o 'editor')."""
        return cls.get_setting("editor_mode", "learning")

    @classmethod
    def set_editor_mode(cls, mode):
        """Establece el modo de trabajo activo ('learning' o 'editor')."""
        val = mode if mode in ("learning", "editor") else "learning"
        cls.set_setting("editor_mode", val)
