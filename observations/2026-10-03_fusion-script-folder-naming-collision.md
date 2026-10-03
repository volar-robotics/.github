---
date: 2026-10-03
trigger: contradiction
target: NAMING.md
---

- **Doing:** Running `scripts/check_naming.py` on minithex.
- **Hit:** "Every `.py` and `.m` file" is snake_case, and "A directory only if
  it contains `__init__.py`" may be snake_case; Fusion requires a script folder
  to carry the name of its `.py` file, so `tools/fusion/export_cad/` cannot
  satisfy both.
- **Did:** Listed the folder in the repository's `.namingignore`, with ROS 2
  and CMake names that external tools fix.
