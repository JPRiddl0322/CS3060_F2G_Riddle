import time

# Recursive Factorial
def factorial(n):
    if n < 0:
        raise ValueError("Negative number!")
    elif n == 0: # Base case: factorial of 0 is 1
        return 1
    else: # Recursive case: n! = n * (n-1)
        return n * factorial(n - 1)
# Iterative Factorial
def littleFact(n):
    if n < 0:
        raise ValueError("Negative number!")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result
# Iterative Fibonacci
def littleFib(n):
    if n <= 1:
        return n
    a,b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
# Recursive Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n -2)



n = 18
start = time.perf_counter()
factorial(n)
end = time.perf_counter()
print(f"Recurisve took {(end - start) * 1e6:.2f} us")

start = time.perf_counter()
littleFact(n)
end = time.perf_counter()
print(f"Iterative took {(end - start) * 1e6:.2f} us")

start = time.perf_counter()
littleFib(n)
end = time.perf_counter()
print(f"Iterative took {(end - start) * 1e6:.2f} us")

start = time.perf_counter()
fibonacci(n)
end = time.perf_counter()
print(f"Recursive took {(end - start) * 1e6:.2f} us")

