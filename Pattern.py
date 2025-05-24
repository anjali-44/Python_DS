def lower_triangular(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n + 1):
        print("*" * i)
    print()

def upper_triangular(n):
    print("Upper Triangular Pattern:")
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)
    print()

def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    print()

lower_triangular(5)
upper_triangular(5)
pyramid(5)