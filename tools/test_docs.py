# =============================================================================
# EH3D-HYDRA-BRIDGE - tools/test_docs.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""The written documents of a repository that has no code yet cannot say more than the repository holds: the register of requirements agrees with the
status page, the maturity of the manifest agrees with the presence of code, and the tables of the other pages keep their shape."""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATES = {"planned", "prototype", "implemented", "validated"}


def table_rows(path: Path) -> list[list[str]]:
    """The cells of every row of the tables of a Markdown page, without the header and the separator line."""
    rows: list[list[str]] = []
    header_seen = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            header_seen = False
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            header_seen = True
            continue
        if header_seen:
            rows.append(cells)
    return rows


class DocumentTests(unittest.TestCase):
    def test_the_register_of_requirements_agrees_with_the_status_page(self) -> None:
        rows = [r for r in table_rows(ROOT / "docs" / "REQUIREMENTS.md") if r[0].startswith("HBRI-")]
        self.assertTrue(rows, "the register has no requirement")
        ids = [r[0] for r in rows]
        self.assertEqual(len(ids), len(set(ids)), "a requirement is written twice")
        self.assertEqual(ids, [f"HBRI-{n:03d}" for n in range(1, len(ids) + 1)], "the numbers must be 001, 002, ... with no gap")
        for row in rows:
            self.assertGreaterEqual(len(row), 6, row[0])
            self.assertIn(row[2], STATES, row[0])
        status = (ROOT / "docs" / "STATUS.md").read_text(encoding="utf-8")
        counted = re.search(r"(\d+) requirements", status)
        self.assertIsNotNone(counted, "the status page does not count the requirements")
        self.assertEqual(int(counted.group(1)), len(rows))
        if "all `planned`" in status:
            self.assertEqual({r[2] for r in rows}, {"planned"})

    def test_the_maturity_of_the_manifest_agrees_with_the_presence_of_code(self) -> None:
        manifest = json.loads((ROOT / "eh3d.project.json").read_text(encoding="utf-8"))
        has_code = (ROOT / "Cargo.toml").exists() or (ROOT / "src").is_dir()
        if has_code:
            self.assertNotEqual(manifest["maturity"], "scaffolding", "there is code: say how far it is in the manifest and in the README")
        else:
            self.assertEqual(manifest["maturity"], "scaffolding", "there is no code: the maturity cannot be higher than scaffolding")
            self.assertEqual(manifest["evidence"], "none", "there is no code: nothing can have evidence")

    def test_the_tables_of_the_other_pages_keep_their_shape(self) -> None:
        for name, columns in (("THREAT_MODEL.md", 5), ("NOT_YET.md", 3)):
            rows = table_rows(ROOT / "docs" / name)
            self.assertTrue(rows, f"{name} has no row")
            for row in rows:
                self.assertEqual(len(row), columns, f"{name}: {row[0]!r}")
                self.assertTrue(all(row), f"{name}: an empty cell in {row[0]!r}")


if __name__ == "__main__":
    unittest.main()
