# calculator.py

def add(num1, num2):
    """Add two numbers."""
    return num1 + num2

def subtract(num1, num2):
    """Subtract num2 from num1."""
    return num1 - num2

def multiply(num1, num2):
    """Multiply two numbers."""
    return num1 * num2

def divide(num1, num2):
    """Divide num1 by num2."""
    if num2 == 0:
        raise ValueError("Division by zero is not allowed")
    return num1 / num2

# Test the implemented functions
if __name__ == "__main__":
    # Test addition
    print("Addition:", add(5, 3))  # Output: 8
    
    # Test subtraction
    print("Subtraction:", subtract(5, 3))  # Output: 2
    
    # Test multiplication
    print("Multiplication:", multiply(5, 3))  # Output: 15
    
    # Test division
    try:
        print("Division:", divide(5, 0))  # This should raise an exception
    except ValueError as e:
        print(e)
