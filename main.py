def is_even(number):
    return number % 2 == 0

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
