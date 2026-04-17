def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
