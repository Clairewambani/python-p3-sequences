#!/usr/bin/env python3

def print_fibonacci(length):
    """Print the Fibonacci sequence up to the specified length."""
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    fib_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers
    while len(fib_sequence) < length:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    print(fib_sequence)

# Example usage:
print_fibonacci(1)  # Print the first Fibonacci number
