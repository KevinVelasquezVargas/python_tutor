# -*- coding: utf-8 -*-
"""
Glosario técnico del complemento (catálogos JSON por idioma).

Cada catálogo ``locale/<idioma>/glossary.json`` es un mapa simple
``término -> definición``. Añadir términos nuevos (o idiomas nuevos)
es tan fácil como editar el JSON, sin tocar Python.

El español base vive en ``curriculum.py`` (GLOSARIO) y se fusiona con
``locale/es/glossary.json``; los demás idiomas se superponen encima, de
modo que un catálogo parcial muestra en español los términos que falten
(fallback término a término, igual que las lecciones).
"""

import json
import os

_IDIOMA_BASE = "es"


def _ruta_catalogos():
    # addon/globalPlugins/python_tutor -> addon/locale
    return os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "locale")
    )


def _cargar(idioma):
    ruta = os.path.join(_ruta_catalogos(), idioma, "glossary.json")
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
        if isinstance(datos, dict):
            return {str(k): str(v) for k, v in datos.items()}
    except (OSError, ValueError):
        pass
    return None


def _glosario_base():
    glosario = {}
    try:
        from .curriculum import GLOSARIO
    except ImportError:
        try:
            from curriculum import GLOSARIO
        except ImportError:
            GLOSARIO = {}
    glosario.update(GLOSARIO)
    extra = _cargar(_IDIOMA_BASE)
    if extra:
        glosario.update(extra)
    return glosario


def obtener_glosario(lang=None):
    """Devuelve el glosario en el idioma correspondiente con respaldo al español base."""
    if lang is None:
        try:
            from .i18n import obtener_idioma_actual
        except ImportError:
            try:
                from i18n import obtener_idioma_actual
            except ImportError:
                obtener_idioma_actual = None
        if obtener_idioma_actual is not None:
            lang = obtener_idioma_actual()
        else:
            lang = _IDIOMA_BASE
    lang = str(lang).strip().lower().replace("-", "_").split("_")[0] or _IDIOMA_BASE
    glosario = _glosario_base()
    if lang != _IDIOMA_BASE:
        traducciones = _cargar(lang)
        if traducciones:
            glosario.update(traducciones)
    return glosario
