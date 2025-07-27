# ✅ Week 1: Triangle Pattern

def lower_triangle(n):
    for i in range(n):
        print("* " * (i + 1))

def upper_triangle(n):
    for i in range(n):
        print("  " * i + "* " * (n - i))

def pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))

print("Lower Triangle:")
lower_triangle(5)
print("\nUpper Triangle:")
upper_triangle(5)
print("\nPyramid:")
pyramid(5)