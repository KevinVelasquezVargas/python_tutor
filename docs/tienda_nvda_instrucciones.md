# Guía para Publicar en la Tienda Oficial de Complementos de NVDA

Este documento detalla los pasos para registrar **Aprendizaje de Python con NVDA** en la Tienda Oficial de Complementos integrada en NVDA (*NVDA Add-on Store*), gestionada por NV Access.

---

## 1. Requisitos Cumplidos

El proyecto ya cuenta con todos los requisitos técnicos y normativos exigidos por NV Access:

* **Licencia de Código Abierto:** GNU GPL v3 ([COPYING.txt](../COPYING.txt)).
* **Compatibilidad de API:** Declarada y validada desde NVDA 2022.1 hasta 2026.3.
* **Empaquetado Estándar:** Archivo binario generado mediante SCons: `python_tutor-2.0.0.nvda-addon`.
* **Alojamiento Público de Release:** Archivo alojado en [GitHub Releases v2.0.0](https://github.com/KevinVelasquezVargas/python_tutor/releases/tag/v2.0.0).
* **Integridad Criptográfica (SHA-256):** `63ec429bfe960eafd924f07eea7bb5e831c27cfd93066184a66a8e45aa728a9b`.
* **Pruebas Automatizadas:** Suite de tests unitarios ejecutados en CI en cada cambio.

---

## 2. Metadatos de la Entrega (`addon_datastore_entry.json`)

Los metadatos preparados para el registro se encuentran en [addon_datastore_entry.json](../addon_datastore_entry.json):

```json
{
  "addonId": "python_tutor",
  "version": "2.0.0",
  "displayName": "Aprendizaje de Python con NVDA",
  "summary": "Herramienta formativa accesible y editor de código para aprender Python con NVDA.",
  "description": "Herramienta formativa y editor de código adaptado para la programación en Python mediante NVDA. Proporciona una ruta de aprendizaje estructurada en 32 capítulos conceptuales y prácticos (128 lecciones), complementada con un entorno de trabajo de doble modalidad: modo tutor guiado y modo editor autónomo. Integra navegación por elementos de código como funciones y clases, señales sonoras de sangría y estructura, verificación de delimitadores y simplificación de mensajes de error.",
  "author": "Kevin Andrés Velasquez Vargas <kevinvelasquezvargas@gmail.com>",
  "homepage": "https://github.com/KevinVelasquezVargas/python_tutor",
  "sourceUrl": "https://github.com/KevinVelasquezVargas/python_tutor",
  "downloadUrl": "https://github.com/KevinVelasquezVargas/python_tutor/releases/download/v2.0.0/python_tutor-2.0.0.nvda-addon",
  "sha256": "63ec429bfe960eafd924f07eea7bb5e831c27cfd93066184a66a8e45aa728a9b",
  "fileSize": 856623,
  "minimumNVDAVersion": "2022.1.0",
  "lastTestedNVDAVersion": "2026.3.0",
  "channel": "stable",
  "license": "GPL-3.0-or-later"
}
```

---

## 3. Procedimiento de Envío a NV Access

Para que el complemento aparezca directamente en el diálogo *Herramientas > Tienda de complementos* de cualquier instalación de NVDA en el mundo:

1. **Visitar el repositorio oficial:**  
   [nvaccess/addon-datastore en GitHub](https://github.com/nvaccess/addon-datastore)
2. **Crear un Fork o abrir una Issue / Pull Request:**  
   * **Vía Issue:** Ir a *Issues > New Issue* y seleccionar la plantilla para registrar un nuevo complemento ("Add new addon"). Pegar el contenido del archivo `addon_datastore_entry.json`.
   * **Vía Pull Request:** Seguir la estructura de carpetas de `addon-datastore` creando `addons/python_tutor/releases/2.0.0.json` con los metadatos anteriores.
3. **Revisión de NV Access:**  
   El equipo de NV Access y la comunidad revisarán la conformidad técnica y la verificación del hash SHA-256. Una vez fusionado el PR, el complemento estará disponible inmediatamente para toda la comunidad hispanohablante e internacional en la tienda oficial.
