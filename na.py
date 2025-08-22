# This code adds two numbers and prints the result

def add_numbers(num1, num2):
    return num1 + num2

# Example usage
if __name__ == '__main__':
    number1 = 5
    number2 = 7
    result = add_numbers(number1, number2)
    print(f'The sum of {number1} and {number2} is {add_numbers(number1, number2)}')