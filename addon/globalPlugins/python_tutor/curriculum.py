# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/curriculum.py
# Propósito: Enrutador dinámico de contenidos curriculares según el idioma de NVDA.
# Autor: Kevin Andrés Velasquez Vargas
# Internacionalización y enrutador (i18n): MisterK-Dev (desarrollado con Google Antigravity 2.0)
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================
# NOTA PARA KEVIN VELÁSQUEZ Y FUTUROS DESARROLLADORES / MAINTAINERS:
#
# 1. ¿POR QUÉ ESTE ARCHIVO ES AHORA UN ENRUTADOR (ROUTER)?
#    Originalmente, este archivo contenía directamente los 32 capítulos y el
#    glosario en español (~1.500 líneas). Para permitir la internacionalización
#    requerida por la tienda oficial de complementos de NVDA (Add-on Store)
#    sin duplicar código ni romper la compatibilidad, el contenido se modularizó:
#    - curricula/es.py : Contiene el temario y glosario original de Kevin intacto.
#    - curricula/en.py : Contiene la versión traducida al inglés.
#    - curriculum.py   : Este archivo actúa como pasarela dinámica que entrega
#                        el temario en el idioma del usuario de NVDA.
#
# 2. ¿POR QUÉ LA CARPETA SE LLAMA 'curricula/'?
#    - "Curricula" es el plural gramatical formal de la palabra latina "curriculum".
#    - En Python, si la carpeta se llamara "curriculum/", colisionaría con el
#      archivo "curriculum.py" en las importaciones relativas (name shadowing).
#      El nombre "curricula/" evita este conflicto técnico por completo.
#
# 3. ¿CÓMO AÑADIR UN NUEVO IDIOMA (FRANCÉS, PORTUGUÉS, ALEMÁN, ETC.)?
#    Cualquier traductor de la comunidad puede agregar un nuevo idioma sin tocar
#    este archivo:
#    a) Crear el archivo: addon/globalPlugins/python_tutor/curricula/<codigo>.py
#       (Por ejemplo: curricula/fr.py para francés o curricula/pt.py para portugués).
#    b) Definir las estructuras CURRICULUM (32 capítulos) y GLOSARIO en ese archivo.
#    c) ¡Listo! El método get_available_languages() detecta automáticamente
#       el nuevo archivo y lo servirá cuando NVDA esté en ese idioma.
#
# 4. COMPATIBILIDAD TOTAL:
#    Al final de este archivo se exportan las constantes CURRICULUM y GLOSARIO,
#    por lo que módulos existentes (gui_frame.py, progress.py, tests/test_tutor.py)
#    siguen funcionando exactamente igual:
#    from python_tutor.curriculum import CURRICULUM, GLOSARIO
# ============================================================================

import importlib
import os

# Detección del idioma activo en el entorno de NVDA:
# - En ejecución dentro de NVDA: languageHandler.getLanguage() devuelve el código
#   del idioma configurado (ej: 'es_ES', 'es_CO', 'en', 'fr').
# - En ejecución externa (ej: pytest, unittest en CI o terminal): languageHandler
#   no existe; capturamos la excepción y usamos 'es' por defecto para garantizar
#   que las pruebas unitarias originales de Kevin pasen al 100% sin dependencias.
try:
    import languageHandler
    _nvda_lang = languageHandler.getLanguage() or "en"
except Exception:
    _nvda_lang = "es"

# Ruta física al subpaquete de contenidos localizados
_curricula_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "curricula")


def get_available_languages():
    """
    Escanea la carpeta 'curricula/' y retorna una lista ordenada con los códigos
    de idioma que tienen un archivo curricular disponible (ej: ['en', 'es']).

    Permite auto-descubrimiento para que nuevos traductores solo necesiten
    colocar su archivo '<codigo>.py' sin modificar código del complemento.
    """
    if not os.path.isdir(_curricula_dir):
        return ["es", "en"]
    return sorted([
        os.path.splitext(f)[0]
        for f in os.listdir(_curricula_dir)
        if f.endswith(".py") and f != "__init__.py"
    ])


def get_curriculum(lang=None):
    """
    Carga y retorna dinámicamente la lista CURRICULUM para el idioma solicitado.

    Parámetros:
        lang (str, opcional): Código de idioma forzado (ej: 'es', 'en'). Si es None,
                              utiliza el idioma detectado en NVDA (_nvda_lang).

    Estrategia de resolución jerárquica:
        1. Español: Si el idioma inicia con 'es' (es, es_ES, es_CO, etc.), carga curricula.es.
        2. Idiomas comunitarios: Si existe curricula/<codigo>.py (ej. 'fr', 'pt'), se importa dinámicamente.
        3. Predeterminado: Carga inglés (curricula.en). Si ocurre cualquier error,
           retrocede de forma segura al español original (curricula.es).
    """
    target = (lang or _nvda_lang).lower()

    # 1. Si el idioma de NVDA es español, cargar versión original en español
    if target.startswith("es"):
        try:
            from .curricula.es import CURRICULUM
            return CURRICULUM
        except Exception:
            pass

    # 2. Comprobar idiomas adicionales existentes (ej. fr, pt, de)
    code = target.split("_")[0]
    avail = get_available_languages()
    if code in avail and code not in ("es", "en"):
        try:
            mod = importlib.import_module(f".curricula.{code}", package=__package__)
            return mod.CURRICULUM
        except Exception:
            pass

    # 3. Idioma predeterminado: inglés (con respaldo de seguridad en español)
    try:
        from .curricula.en import CURRICULUM
        return CURRICULUM
    except Exception:
        from .curricula.es import CURRICULUM
        return CURRICULUM


def get_glosario(lang=None):
    """
    Carga y retorna dinámicamente el diccionario GLOSARIO para el idioma solicitado.

    Parámetros:
        lang (str, opcional): Código de idioma forzado (ej: 'es', 'en'). Si es None,
                              utiliza el idioma detectado en NVDA (_nvda_lang).

    Sigue exactamente la misma jerarquía de resolución que get_curriculum().
    """
    target = (lang or _nvda_lang).lower()

    # 1. Si el idioma de NVDA es español, cargar glosario original en español
    if target.startswith("es"):
        try:
            from .curricula.es import GLOSARIO
            return GLOSARIO
        except Exception:
            pass

    # 2. Comprobar idiomas adicionales existentes (ej. fr, pt, de)
    code = target.split("_")[0]
    avail = get_available_languages()
    if code in avail and code not in ("es", "en"):
        try:
            mod = importlib.import_module(f".curricula.{code}", package=__package__)
            return mod.GLOSARIO
        except Exception:
            pass

    # 3. Idioma predeterminado: inglés (con respaldo de seguridad en español)
    try:
        from .curricula.en import GLOSARIO
        return GLOSARIO
    except Exception:
        from .curricula.es import GLOSARIO
        return GLOSARIO


# ============================================================================
# EXPORTACIONES CANÓNICAS PARA RETROCOMPATIBILIDAD:
# Permite que 'from python_tutor.curriculum import CURRICULUM, GLOSARIO'
# funcione sin modificar una sola línea de código en los módulos que lo consumen.
# ============================================================================
CURRICULUM = get_curriculum()
GLOSARIO = get_glosario()
