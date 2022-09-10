"""Random utilities around python."""
try:
    from ._version import __version__, __version_tuple__
except ImportError:
    __version__ = "0.0.0-UNKNOWN"
    __version_tuple__ = ("0", "0", "0", "UNKNOWN")
