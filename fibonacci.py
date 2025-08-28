# Function to calculate Fibonacci sequence

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        for i in range(2, n):
            next_fib = fib_series[-1] + fib_series[-2]
            fib_series.append(next_fib)
        return fib_series

# Example usage
if __name__ == '__main__':
    n = 10  # Change this value to get more Fibonacci numbers
    print(fibonacci(n))
