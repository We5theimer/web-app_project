def divide(a, b):
    """Функция деления с проверкой на деление на ноль."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(number):
    """Проверяет, является ли число четным."""
    return number % 2 == 0
