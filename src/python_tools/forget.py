"""Forget a complete module at once."""
from __future__ import annotations

import sys


def forget(name, full=True):
    """Remove a module from `sys.modules`.

    Arguments:
        name: The name of the module that should be removed.
        full: Remove every sub-modules of the given name.

    Returns:
        The list of the forgotten modules.
    """
    forgetten = []
    for module in reversed(sys.modules.keys()):
        if module == name or (full and module.startswith(name + ".")):
            forgetten.append(module)
            del sys.modules[module]
    return forgetten
