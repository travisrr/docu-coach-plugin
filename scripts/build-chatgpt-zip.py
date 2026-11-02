#!/usr/bin/env python3
"""Build the ChatGPT plugin ZIP. The package contains no secrets."""

import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_FILES = (
    "plugin.json",
    "mcp.json",
    "skills/get-started/SKILL.md",
    "assets/logo.png",
    "LICENSE",
)
SHORT_FIELDS = ("displayName", "shortDescription", "developerName", "category")


def main() -> None:
    plugin = json.loads((ROOT / "plugin.json").read_text())
    interface = plugin["extensions"]["com.openai"]["interface"]
    for field in SHORT_FIELDS:
        value = interface[field]
        if not isinstance(value, str) or len(value) > 30:
            raise SystemExit(f"{field} must be a string of 30 characters or fewer")
    logo = plugin["extensions"]["com.openai"]["interface"]["logo"]
    if logo != "./assets/logo.png":
        raise SystemExit("logo must be ./assets/logo.png")
    output = ROOT / "dist" / "docu-coach-chatgpt.zip"
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative in PACKAGE_FILES:
            path = ROOT / relative
            if not path.is_file():
                raise SystemExit(f"missing {relative}")
            archive.write(path, relative)
    print(output)


if __name__ == "__main__":
    main()
