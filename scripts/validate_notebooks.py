"""Validate the teaching-notebook contract without importing notebook packages."""

from __future__ import annotations

import json
from pathlib import Path
import sys


REQUIRED_MARKERS = ("Mục tiêu", "Tự luyện")
root = Path(__file__).resolve().parents[1]
errors: list[str] = []

for path in sorted(root.glob("[0-9][0-9]-*/**/*.ipynb")):
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{path.relative_to(root)}: JSON không hợp lệ ({error})")
        continue

    cells = notebook.get("cells", [])
    text = "\n".join("".join(cell.get("source", [])) for cell in cells)
    if notebook.get("nbformat") != 4:
        errors.append(f"{path.relative_to(root)}: phải dùng nbformat 4")
    if any(not cell.get("id") for cell in cells):
        errors.append(f"{path.relative_to(root)}: mỗi cell phải có id")
    if not any(cell.get("cell_type") == "code" for cell in cells):
        errors.append(f"{path.relative_to(root)}: thiếu code cell")
    if missing := [marker for marker in REQUIRED_MARKERS if marker not in text]:
        errors.append(f"{path.relative_to(root)}: thiếu phần {', '.join(missing)}")

if errors:
    print("Notebook validation failed:", *errors, sep="\n- ")
    raise SystemExit(1)

print(f"Validated {len(list(root.glob('[0-9][0-9]-*/**/*.ipynb')))} notebooks.")
