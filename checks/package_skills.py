#!/usr/bin/env python3
"""Build independent skill ZIPs without credentials or checkout-specific paths."""

from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from validate import NAMES, ROOT, validate


def main() -> int:
    errors = validate()
    if errors:
        raise SystemExit("Package validation failed:\n" + "\n".join(errors))
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    for name in sorted(NAMES):
        folder = ROOT / "skills" / name
        archive = output / f"{name}.zip"
        # Only explicit public instruction resources, never hidden files or cache/state.
        files = sorted(path for path in folder.rglob("*.md") if path.is_file())
        with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
            for path in files:
                bundle.write(path, Path(name) / path.relative_to(folder))
            bundle.write(ROOT / "LICENSE", Path(name) / "LICENSE")
        print(f"Built {archive.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
