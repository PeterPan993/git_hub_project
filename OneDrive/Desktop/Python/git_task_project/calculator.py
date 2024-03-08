import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    return base ** exponent

def sqrt(number):
    if number < 0:
        raise ValueError("Square root of negative number is undefined")
    return math.sqrt(number)

# Test the implemented functions
if __name__ == "__main__":
    # Test addition
    assert add(2, 3) == 5
    
    # Test subtraction
    assert subtract(5, 3) == 2
    
    # Test multiplication
    assert multiply(2, 3) == 6
    
    # Test division
    assert divide(6, 3) == 2
    try:
        divide(6, 0)  # This should raise an exception
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    
    # Test exponentiation
    assert power(2, 3) == 8
    
    # Test square root
    assert sqrt(9) == 3
    try:
        sqrt(-9)  # This should raise an exception
    except ValueError as e:
        assert str(e) == "Square root of negative number is undefined"
