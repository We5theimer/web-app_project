import pytest
from main import divide, is_even

def test_divide_by_zero():
    """Тест на деление на ноль."""
    with pytest.raises(ValueError):
        divide(1, 0)

def test_divide():
    """Тест на обычное деление."""
    assert divide(6, 2) == 3

def test_is_even():
    """Тест на четность числа."""
    assert is_even(4) is True
    assert is_even(3) is False
