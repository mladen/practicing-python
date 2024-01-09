x = [2, 4, 65, 23, 12, 1, 3, 5, 6, 7, 8, 9, 10, 84]
print("x =", x)  # x = [2, 4, 65, 23, 12, 1, 3, 5, 6, 7, 8, 9, 10, 84]

# Map
# Map is a function that takes in a function and a list as arguments
# It applies the function to every item in the list
# It returns a list of the results
# Syntax: map(function, list)
# Example 1
results = map(
    lambda i: i + 5, x
)  # here i is the argument and i + 5 is the expression; map returns a map object so we need to convert it to a list
print(
    "results (add 5 to each element) =", list(results)
)  # results = [7, 9, 70, 28, 17, 6, 8, 10, 11, 12, 13, 14, 15, 89]


# Example 2
def multiply_by_2(i):  # functions can be even more complex than lambda functions!
    return i * 2


results = map(multiply_by_2, x)
print(
    "results (multiply each element by 2) =", list(results)
)  # results = [4, 8, 130, 46, 24, 2, 6, 10, 12, 14, 16, 18, 20, 168]

print("=========================================")

# Filter
# Filter is a function that takes in a function and a list as arguments
# It applies the function to every item in the list
# It returns a list of the items for which the function returned True
# Syntax: filter(function, list)
# Example 1
results = filter(
    lambda i: i % 2 == 0, x
)  # here i is the argument and i % 2 == 0 is the expression; filter returns a filter object so we need to convert it to a list
print(
    "results (filter out odd numbers) =", list(results)
)  # results = [2, 4, 12, 6, 8, 10, 84]

print("=========================================")

print(
    "We can use more complex functions with map and filter (not just lambda functions)."
)


def is_even(i):
    return i % 2 == 0


print("We can use multiply_by_2 and is_even functions from above.")


print(
    "results (filter out odd numbers and multiply each element by 2) =",
    list(map(multiply_by_2, filter(is_even, x))),
)
# results = [4, 8, 24, 2, 6, 10, 12, 14, 16, 18, 20, 168]
