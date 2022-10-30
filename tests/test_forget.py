
import sys
from unittest import mock

from python_tools.forget import forget


def test_forget_module():
    modules = {"a": None, "b": None, "b.a": None, "b.b": None}
    with mock.patch.object(sys, "modules", modules):
        result = forget("a")
        assert sys.modules == {"b": None, "b.a": None, "b.b": None}
        assert result == {"a"}


def test_forget_full_package():
    modules = {"a": None, "b": None, "b.a": None, "b.b": None}
    with mock.patch.object(sys, "modules", modules):
        result = forget("b")
        assert sys.modules == {"a": None}
        assert result == {"b", "b.a", "b.b"}


def test_forget_partial_package():
    modules = {"a": None, "b": None, "b.a": None, "b.b": None}
    with mock.patch.object(sys, "modules", modules):
        result = forget("b", full=False)
        assert sys.modules == {"a": None, "b.a": None, "b.b": None}
        assert result == {"b"}
