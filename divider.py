def divide_numbers(num1, num2):
    """
    Function to divide two numbers.
    Raises error if division by zero is attempted.
    """
    # This function takes two inputs: num1 and num2.
    # It returns the result of num1 divided by num2.
    # An error will be raised if an attempt is made to divide by zero to ensure safe calculations.
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2
