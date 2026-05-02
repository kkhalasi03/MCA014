import pytest
from app import add,subtract,multiply,divide

def test_add():
    assert add(2, 3) == 5
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(7, 5) == 2

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(2, 5) == 10

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
