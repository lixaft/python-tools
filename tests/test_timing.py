from __future__ import annotations

import time

import pytest

from pythonlib.timing import timing


@pytest.mark.parametrize(
    ("value", "expected"),
    (
        (0.1, "ms"),
        (0.0001, "μs"),
    ),
)
def test_timing_units(capsys, value, expected):
    with timing():
        time.sleep(value)

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err.split()[-1] == expected
