def is_even(number):
    return number % 2 == 0

def test_even():
    assert is_even(4) is True

def test_odd():
    assert is_even(5) is False
