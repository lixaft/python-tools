from __future__ import annotations

import sys


def forget(name: str, full: bool = True) -> set[str]:
    """Remove a module from `sys.modules`.

    Arguments:
        name: The name of the module/package that should be removed.
        full: Remove every sub-modules of the given name.

    Returns:
        The list of the forgotten modules.
    """
    forgetten = set()
    for module in reversed(list(sys.modules)):
        if module == name or (full and module.startswith(name + ".")):
            forgetten.add(module)
            del sys.modules[module]
    return forgetten
