# -*- coding: utf-8 -*-
"""Script to package the source repository cleanly for v2.0.0."""

import os
import zipfile

ZIP_NAME = "python_tutor-source-v2.0.0.zip"

# Exclude temporary or generated build artifacts
EXCLUDES = {
    ".git", ".sconsign.dblite", ".sconf_temp", "__pycache__",
    "python_tutor-2.0.0.nvda-addon", ZIP_NAME
}

base_dir = os.path.abspath(".")

with zipfile.ZipFile(ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in EXCLUDES and not d.startswith(".git")]

        for file in files:
            if file in EXCLUDES or file.endswith(".pyc"):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_dir)
            zipf.write(full_path, rel_path)

print(f"Archive {ZIP_NAME} created successfully.")
