# -*- coding: utf-8 -*-
"""
Genera los catálogos JSON de lecciones (locale/es/lessons.json y
locale/en/lessons.json) a partir de los diccionarios Python del complemento
(curriculum.py y curriculum_translations.py).

Uso (desde la raíz del repositorio):
    uv run python tools/extract_lessons.py

Los catálogos contienen únicamente los campos traducibles. La lógica
(validadores, tipos de paso, índices de respuesta correcta) permanece en
curriculum.py y nunca se traduce.

Formato de cada catálogo locale/<idioma>/lessons.json:
{
  "<id_capitulo>": {
    "titulo": "...",
    "resumen": "...",
    "pasos": [
      {
        "titulo": "...",
        "instruccion": "...",
        "pistas": ["..."],
        "codigo": "...",
        "pregunta": "...",
        "opciones": ["..."],
        "explicacion": "...",
        "salida_esperada": "..."
      }
    ]
  }
}

Para añadir un nuevo idioma: copia locale/es/lessons.json, traduce los
valores (mantén las claves en español) y guárdalo como
locale/<idioma>/lessons.json.
"""
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN_DIR = os.path.join(REPO_ROOT, "addon", "globalPlugins", "python_tutor")
LOCALE_DIR = os.path.join(REPO_ROOT, "addon", "locale")

CAMPOS_CAPITULO = ("titulo", "resumen")
CAMPOS_PASO = (
    "titulo", "instruccion", "pistas", "codigo",
    "pregunta", "opciones", "explicacion", "salida_esperada",
)


def importar_modulo(nombre):
    if PLUGIN_DIR not in sys.path:
        sys.path.insert(0, PLUGIN_DIR)
    return __import__(nombre)


def extraer_es(curriculum):
    catalogo = {}
    for cap in curriculum:
        datos_cap = {c: cap[c] for c in CAMPOS_CAPITULO if c in cap}
        pasos = []
        for paso in cap.get("pasos", []):
            pasos.append({c: paso[c] for c in CAMPOS_PASO if c in paso})
        datos_cap["pasos"] = pasos
        catalogo[str(cap["id"])] = datos_cap
    return catalogo


def extraer_en(curriculum, translations):
    catalogo = {}
    for cap in curriculum:
        cid = cap["id"]
        tr = translations.CHAPTER_TRANSLATIONS.get(cid)
        if not tr:
            continue
        datos_cap = {}
        if "titulo_en" in tr:
            datos_cap["titulo"] = tr["titulo_en"]
        if "resumen_en" in tr:
            datos_cap["resumen"] = tr["resumen_en"]
        pasos_tr = tr.get("pasos", [])
        pasos = []
        for i, paso in enumerate(cap.get("pasos", [])):
            ptr = pasos_tr[i] if i < len(pasos_tr) else {}
            datos_paso = {}
            for campo in CAMPOS_PASO:
                campo_en = f"{campo}_en"
                if campo_en in ptr:
                    datos_paso[campo] = ptr[campo_en]
                elif campo == "codigo" and cid in translations.CODIGO_EN_MAP and i in translations.CODIGO_EN_MAP[cid]:
                    datos_paso["codigo"] = translations.CODIGO_EN_MAP[cid][i]
            if datos_paso:
                pasos.append(datos_paso)
        datos_cap["pasos"] = pasos
        catalogo[str(cid)] = datos_cap
    return catalogo


def guardar(catalogo, idioma):
    dir_idioma = os.path.join(LOCALE_DIR, idioma)
    os.makedirs(dir_idioma, exist_ok=True)
    ruta = os.path.join(dir_idioma, "lessons.json")
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        json.dump(catalogo, f, ensure_ascii=False, indent=2)
        f.write("\n")
    num_pasos = sum(len(c.get("pasos", [])) for c in catalogo.values())
    print(f"Generado {ruta}: {len(catalogo)} capítulos, {num_pasos} pasos")


def main():
    curriculum_mod = importar_modulo("curriculum")
    translations = importar_modulo("curriculum_translations")

    guardar(extraer_es(curriculum_mod.CURRICULUM), "es")
    guardar(extraer_en(curriculum_mod.CURRICULUM, translations), "en")


if __name__ == "__main__":
    main()
