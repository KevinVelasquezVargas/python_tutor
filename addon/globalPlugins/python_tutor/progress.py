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

        # Almacenar en la carpeta de configuración persistente de NVDA
        if globalVars and hasattr(globalVars, 'appArgs') and hasattr(globalVars.appArgs, 'configPath') and globalVars.appArgs.configPath:
            base_dir = os.path.join(globalVars.appArgs.configPath, "python_tutor")
        else:
            base_dir = os.path.join(os.path.expanduser("~"), ".python_tutor")

        try:
            os.makedirs(base_dir, exist_ok=True)
        except Exception:
            pass

        target_path = os.path.join(base_dir, "progress.json")

        # Migración segura: si el archivo destino no existe, migrar desde ubicaciones anteriores
        if not os.path.exists(target_path):
            legacy_candidates = []
            if globalVars and hasattr(globalVars, 'appArgs') and hasattr(globalVars.appArgs, 'configPath') and globalVars.appArgs.configPath:
                legacy_candidates.append(os.path.join(globalVars.appArgs.configPath, "python_tutor_user_progress.json"))
            addon_dir = os.path.dirname(os.path.abspath(__file__))
            legacy_candidates.append(os.path.join(addon_dir, "user_data", "progress.json"))

            for candidate in legacy_candidates:
                if os.path.isfile(candidate):
                    try:
                        import shutil
                        shutil.copy2(candidate, target_path)
                        break
                    except Exception:
                        pass

        cls._file_path = target_path
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
        """Todos los capítulos están disponibles y desbloqueados para permitir navegación libre."""
        from .curriculum import CURRICULUM
        return 0 <= chapter_idx < len(CURRICULUM)

    @classmethod
    def unlock_up_to_chapter(cls, target_chapter_idx):
        """Desbloquea los capítulos previos completando sus pasos para permitir acceso directo."""
        from .curriculum import CURRICULUM
        progress = cls.load_progress()
        for idx in range(min(target_chapter_idx, len(CURRICULUM))):
            cap_key = f"cap_{idx}"
            total_pasos = len(CURRICULUM[idx].get("pasos", []))
            progress.setdefault("completed_steps", {})[cap_key] = list(range(total_pasos))
            if idx not in progress.setdefault("completed_chapters", []):
                progress["completed_chapters"].append(idx)
        cls.save_progress(progress)
        return progress

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
