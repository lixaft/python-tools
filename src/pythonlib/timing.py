from __future__ import annotations

import contextlib
import sys
import time
from typing import Generator


@contextlib.contextmanager
def timing() -> Generator[None, None, None]:
    """Print the time required to execute the content."""
    before = time.monotonic()
    try:
        yield
    finally:
        after = time.monotonic()

        t = (after - before) * 1000
        unit = "ms"
        if t < 100:
            t *= 1000
            unit = "μs"

        print(f"Executed in {t} {unit}", file=sys.stderr, flush=True)
