operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    # Avoid division by zero
    '/': lambda a, b: a / b if b != 0 else float('inf'),
    '^': lambda a, b: a ** b  # Exponentiation operator
}


a= operators['+'](1, 2)
print(a)
b = lambda a, b: a + b
print(b(2,3))
