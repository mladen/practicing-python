# Comprehentions are a way to create lists, dictionaries, and sets in a more concise way

x = [
    x for x in range(5)
]  # 'x' is the value that we want to add to the list; 'for x in range(5)' is the loop
print("x =", x)  # [0, 1, 2, 3, 4]

# We can also add an if statement to the comprehension
x = [x for x in range(10) if x % 2 == 0]
print("x (with if statement) =", x)  # [0, 2, 4, 6, 8]

print("========================================")

# We can also use nested loops
x = [
    (x, y) for x in range(5) for y in range(5)
]  # range is 0-indexed; range(5) is [0, 1, 2, 3, 4]
print("x (with nested loops) =", x)
# [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
#  (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
#  (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
#  (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
#  (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

print("========================================")

# We can also use nested loops with if statements
x = [(x, y) for x in range(5) for y in range(5) if x != y]
print("x (with nested loops and if statements) =", x)
# [(0, 1), (0, 2), (0, 3), (0, 4),
#  (1, 0), (1, 2), (1, 3), (1, 4),
#  (2, 0), (2, 1), (2, 3), (2, 4),
#  (3, 0), (3, 1), (3, 2), (3, 4),
#  (4, 0), (4, 1), (4, 2), (4, 3)]

print("========================================")

# We can also use nested loops with if statements and if-else statements
x = [(x, y) if x != y else "same" for x in range(5) for y in range(5)]
print("x (with nested loops and if statements and if-else statements) =", x)
# ['same', (0, 1), (0, 2), (0, 3), (0, 4),
#  (1, 0), 'same', (1, 2), (1, 3), (1, 4),
#  (2, 0), (2, 1), 'same', (2, 3), (2, 4),
#  (3, 0), (3, 1), (3, 2), 'same', (3, 4),
#  (4, 0), (4, 1), (4, 2), (4, 3), 'same']

print("========================================")

# We can also use nested loops with if statements and if-else statements and if-elif-else statements
x = [
    (x, y) if x != y else "same" if x == 0 else "different" if x == 1 else "other"
    for x in range(5)
    for y in range(5)
]
print(
    "x (with nested loops and if statements and if-else statements and if-elif-else statements) =",
    x,
)
# ['same', (0, 1), (0, 2), (0, 3), (0, 4),
#  (1, 0), 'different', (1, 2), (1, 3), (1, 4),
#  (2, 0), (2, 1), 'same', (2, 3), (2, 4),
#  (3, 0), (3, 1), (3, 2), 'same', (3, 4),
#  (4, 0), (4, 1), (4, 2), (4, 3), 'same']

print("========================================")

x = [
    [x for x in range(5)] for y in range(5)
]  # [x for x in range(5)] gives us [0, 1, 2, 3, 4]; we do this 5 times, so we get [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], ...]
print("x (with nested comprehentions) =", x)
# [[0, 1, 2, 3, 4],
#  [0, 1, 2, 3, 4],
#  [0, 1, 2, 3, 4],
#  [0, 1, 2, 3, 4],
#  [0, 1, 2, 3, 4]]

print("========================================")

# Notice: All of this works for dictionaries and sets as well
# For dictionaries:
x = {i: 0 for i in range(5)}
print("x (with dictionaries) =", x)  # {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

# For sets:
x = {i for i in range(5)}
print("x (with sets) =", x)  # {0, 1, 2, 3, 4}

# For tuples:
x = tuple(i for i in range(5))
print("x (with tuples) =", x)  # (0, 1, 2, 3, 4)

# For strings:
x = "".join([str(i) for i in range(5)])
print("x (with strings) =", x)  # 01234

# For lists (this is the same as the first examples; done using []):
x = [i for i in range(5)]
print("x (with lists) =", x)  # [0, 1, 2, 3, 4]
