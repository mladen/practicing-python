# *args and **kwargs are used to pass a variable number of arguments to a function
# *args is used to pass a variable number of positional arguments; positional arguments are arguments that don't have a name
# **kwargs is used to pass a variable number of keyword(!) arguments; keyword arguments are arguments that have a name
def func(*args, **kwargs):
    print(args)  # args is a tuple
    print(kwargs)  # kwargs is a dictionary


func(1, 2, 3, 4, 5, 6, name="Tim", age=19)

# Unpacking
x = [2, 31, 4, 21, 54, 16, 7]
print(
    *x
)  # This unpacks the list which means it prints 2, 31, 4, 21, 54, 16, 7 instead of [2, 31, 4, 21, 54, 16, 7]


# Using the unpack operator to pass arguments to a function
def func(x, y):
    print(x, y)


func(*[1, 2])  # This unpacks the list and passes the values to the function


# Using the unpack operator to pass keyword arguments to a function
def func(x, y):
    print(x, y)


func(
    **{"x": 1, "y": 2}  # keys must match the parameter names!
)  # This unpacks the dictionary and passes the values to the function
