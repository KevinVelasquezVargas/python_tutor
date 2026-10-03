# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: installTasks.py
# Propósito: Tareas de instalación y desinstalación limpia del complemento en NVDA.
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import os
import shutil

try:
    import globalVars
except ImportError:
    globalVars = None


def onInstall():
    """Se ejecuta tras instalar o actualizar el complemento en NVDA. Preserva el progreso del usuario."""
    pass



def onUninstall():
    """Se ejecuta al desinstalar el complemento en NVDA. Limpia datos de usuario."""
    try:
        # Limpieza de progreso externo
        if globalVars and hasattr(globalVars, 'appArgs') and hasattr(globalVars.appArgs, 'configPath') and globalVars.appArgs.configPath:
            old_json = os.path.join(globalVars.appArgs.configPath, "python_tutor_user_progress.json")
            if os.path.isfile(old_json):
                os.remove(old_json)

        # Limpieza de datos internos si la carpeta aún persiste
        addon_dir = os.path.dirname(os.path.abspath(__file__))
        user_data = os.path.join(addon_dir, "globalPlugins", "python_tutor", "user_data")
        if os.path.isdir(user_data):
            shutil.rmtree(user_data, ignore_errors=True)
    except Exception:
        pass
