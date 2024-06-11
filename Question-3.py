def fibonacci_sequence(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
number = 50
generation = fibonacci_sequence(number)
fibonacci_list = list(generation)
print(fibonacci_list)

#OUTPUT:-[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]