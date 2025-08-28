# Function to calculate Fibonacci sequence

def fibonacci(n):
    # Check for non-positive input
    if n <= 0:
        return []  # Return an empty list for non-positive input
    elif n == 1:
        return [0]  # Return the first Fibonacci number
    elif n == 2:
        return [0, 1]  # Return the first two Fibonacci numbers
    else:
        fib_series = [0, 1]  # Initialize the Fibonacci series with the first two numbers
        # Loop to calculate Fibonacci numbers from the third number onward
        for i in range(2, n):
            next_fib = fib_series[-1] + fib_series[-2]  # Calculate the next Fibonacci number
            fib_series.append(next_fib)  # Append the next number to the series
        return fib_series  # Return the complete Fibonacci series

# Example usage
if __name__ == '__main__':
    n = 10  # Change this value to get more Fibonacci numbers
    print(fibonacci(n))  # Print the Fibonacci series up to n