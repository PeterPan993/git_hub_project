import math

def power(base, exponent):
    """Calculate exponentiation."""
    return base ** exponent

def sqrt(number):
    """Calculate square root."""
    if number < 0:
        raise ValueError("Square root of negative number is undefined")
    return math.sqrt(number)

# Test the implemented functions
if __name__ == "__main__":
    # Test exponentiation
    print("Exponentiation:")
    print(power(2, 3))  # Output: 8
    print(power(5, 2))  # Output: 25
    
    # Test square root
    print("\nSquare Root:")
    print(sqrt(9))  # Output: 3
    try:
        print(sqrt(-9))  # This should raise an exception
    except ValueError as e:
        print(e)
