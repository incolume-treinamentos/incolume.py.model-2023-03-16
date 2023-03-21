import pytest

from incolume.py.model_2023_03_16 import void


def test_void_return():
    """Test void function return."""
    assert void.void() == {}


def test_void_return_type():
    """Test void function type return."""
    assert isinstance(void.void(), dict)
