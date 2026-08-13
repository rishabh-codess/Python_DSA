import sys


# Recursive Fibonacci: O(N) Call Stack Space Frame Overhead
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Iterative Fibonacci: O(1) Auxiliary Space Complexity
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


n = 10
print(f"Fibonacci({n}) Recursive:", fib_recursive(n))
print(f"Fibonacci({n}) Iterative:", fib_iterative(n))