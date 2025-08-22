def divide_numbers(num1, num2):
    """
    Function to divide two numbers.
    Raises error if division by zero is attempted.
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2