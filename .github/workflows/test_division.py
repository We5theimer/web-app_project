import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

def test_normal_division():
    assert divide(6, 3) == 2
