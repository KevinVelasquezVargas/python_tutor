# -*- coding: utf-8 -*-
"""
Genera el catálogo base del glosario en español (locale/es/glossary.json)
a partir del glosario embutido en curriculum.py (GLOSARIO).

Las traducciones (en, pt...) ya viven en sus propios catálogos
locale/<idioma>/glossary.json y se mantienen directamente en JSON;
también pueden añadirse términos nuevos editando esos archivos.

Uso (desde la raíz del repositorio):
    uv run python tools/extract_glossary.py
"""
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN_DIR = os.path.join(REPO_ROOT, "addon", "globalPlugins", "python_tutor")
LOCALE_DIR = os.path.join(REPO_ROOT, "addon", "locale")


def main():
    if PLUGIN_DIR not in sys.path:
        sys.path.insert(0, PLUGIN_DIR)
    curriculum = __import__("curriculum")

    dir_es = os.path.join(LOCALE_DIR, "es")
    os.makedirs(dir_es, exist_ok=True)
    ruta = os.path.join(dir_es, "glossary.json")
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        json.dump(curriculum.GLOSARIO, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    print(f"Generado {ruta}: {len(curriculum.GLOSARIO)} terminos")


if __name__ == "__main__":
    main()
