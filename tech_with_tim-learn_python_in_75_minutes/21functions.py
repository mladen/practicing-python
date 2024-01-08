# Functions are a way to reuse code


def func(x, y):
    print("Run", x, y)
    return x * y, x + y  # returns a tuple


print("Calling a function that returns a tuple")
print(func(2, 3))  # (6, 5)

print("========================================")

# Unpacking a tuple
print("Unpacking a tuple")
a, b = func(2, 3)
print(a)  # 6
print(b)  # 5

print("========================================")


# We can also use default values for parameters
def func(x=1, y=2):
    print("Run", x, y)
    return x * y, x + y  # returns a tuple


print("Calling a function with default values for parameters")
func(2)  # Run 2 2
