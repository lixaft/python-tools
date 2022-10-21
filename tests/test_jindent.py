from __future__ import annotations

import os

from python_tools.jindent import main


def test_jindent(tmpdir) -> None:
    f = tmpdir.join("f.json")
    f.write('{"a": 1, "b": 2}')
    assert main([f.strpath]) == 0
    assert f.read() == ("{\n" '  "a": 1,\n' '  "b": 2\n' "}")


def test_jindent_four(tmpdir) -> None:
    f = tmpdir.join("f.json")
    f.write('{"a": 1, "b": 2}')
    assert main(["--indent", "4", f.strpath]) == 0
    assert f.read() == ("{\n" '    "a": 1,\n' '    "b": 2\n' "}")
