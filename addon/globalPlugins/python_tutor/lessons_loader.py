# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/lessons_loader.py
# Propósito: Catálogos de lecciones por idioma (JSON externos) y fusión con el
#            currículo base. Añadir un idioma nuevo es tan simple como añadir
#            un archivo lessons/<idioma>.json y recompilar el complemento.
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================
"""
Sistema de catálogos de lecciones en JSON.

Cada archivo ``lessons/<idioma>.json`` contiene los campos traducibles del
currículo (títulos, instrucciones, pistas, preguntas, código de ejemplo...).
La lógica pedagógica (validadores, tipos de paso, respuestas correctas)
permanece en ``curriculum.py`` y nunca se traduce.

El idioma base del complemento es español: el contenido de ``curriculum.py``
se usa como respaldo parcial, de modo que un catálogo puede estar traducido
solo parcialmente (capítulo a capítulo, campo a campo) sin romper nada.

Para añadir un idioma nuevo:
1. Copia ``lessons/es.json`` a ``lessons/<idioma>.json`` (p. ej. ``pt.json``).
2. Traduce los valores (las claves permanecen en español).
   Importante: en los desafíos de código, mantén las cadenas de salida que
   exigen los validadores (estos aceptan español e inglés).
3. Recompila el complemento (``scons``): el idioma aparecerá automáticamente
   en el selector de idioma y en la detección automática del idioma de NVDA.
"""

import json
import os

_CAMPOS_CAPITULO = ("titulo", "resumen")
_CAMPOS_PASO = (
    "titulo", "instruccion", "pistas", "codigo",
    "pregunta", "opciones", "explicacion", "salida_esperada",
)

_IDIOMA_BASE = "es"


def _ruta_lecciones():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "lessons")


def idiomas_disponibles():
    """Devuelve los códigos de idioma con catálogo JSON (orden alfabético).

    El idioma base ('es') siempre se incluye porque vive en curriculum.py.
    """
    idiomas = {_IDIOMA_BASE}
    try:
        for nombre in os.listdir(_ruta_lecciones()):
            if nombre.endswith(".json"):
                idiomas.add(os.path.splitext(nombre)[0])
    except OSError:
        pass
    return sorted(idiomas)


def normalizar_idioma(lang):
    """Mapea un código de NVDA ('pt_PT', 'pt-BR', 'en_US') al catálogo disponible.

    Devuelve None si no existe catálogo adecuado.
    """
    if not lang:
        return None
    disponibles = idiomas_disponibles()
    codigo = str(lang).strip().lower().replace("-", "_")
    if codigo in disponibles:
        return codigo
    prefijo = codigo.split("_")[0]
    if prefijo in disponibles:
        return prefijo
    return None


def cargar_catalogo(idioma):
    """Carga el catálogo JSON de un idioma. Devuelve None si no existe."""
    if idioma == _IDIOMA_BASE:
        return None
    ruta = os.path.join(_ruta_lecciones(), f"{idioma}.json")
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def aplicar_traducciones(curriculum):
    """Fusiona todos los catálogos disponibles en el currículo en memoria.

    Para cada idioma (distinto del base) inyecta los campos con sufijo
    '_<idioma>' (titulo_en, titulo_pt, ...) en cada capítulo y paso, igual
    que hacía el antiguo sistema con las claves '_en'.
    """
    for idioma in idiomas_disponibles():
        if idioma == _IDIOMA_BASE:
            continue
        catalogo = cargar_catalogo(idioma)
        if not catalogo:
            continue
        for cap in curriculum:
            datos_cap = catalogo.get(str(cap.get("id")))
            if not isinstance(datos_cap, dict):
                continue
            for campo in _CAMPOS_CAPITULO:
                if campo in datos_cap:
                    cap[f"{campo}_{idioma}"] = datos_cap[campo]
            pasos_datos = datos_cap.get("pasos", [])
            pasos = cap.get("pasos", [])
            for i, datos_paso in enumerate(pasos_datos):
                if i >= len(pasos) or not isinstance(datos_paso, dict):
                    continue
                paso = pasos[i]
                for campo in _CAMPOS_PASO:
                    if campo in datos_paso:
                        paso[f"{campo}_{idioma}"] = datos_paso[campo]


def leer_texto(obj, campo, lang=None, default=None):
    """Lee un campo traducible en el idioma activo con respaldo al español base.

    Reproduce el comportamiento histórico: obj['campo_en'] si existe y el
    idioma es 'en', si no obj['campo'].
    """
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
    if lang and lang != _IDIOMA_BASE:
        clave = f"{campo}_{lang}"
        if clave in obj:
            return obj[clave]
    return obj.get(campo, default)
