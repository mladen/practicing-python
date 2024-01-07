x = [4, True, "hi"]  # This is a list
# lists are mutable (which means they can be changed), ordered, can contain duplicates and they can contain different data types

print(len(x))  # 3

# Appending to a list
x.append(6)  # adds 6 to the end of the list
print("Appended list:", x)  # [4, True, 'hi', 6]

# Extending a list
x.extend([7, 8])
print("Extended list:", x)  # [4, True, 'hi', 6, 7, 8]

# Removing from a list
x.remove("hi")
print("Removed list:", x)  # [4, True, 6, 7, 8]

# Popping from a list
x.pop()  # removes the last element; if you pass an index, it will remove that element
print("Popped list:", x)  # [4, True, 6, 7]

# Inserting into a list
x.insert(2, "inserted")
print("Inserted list:", x)  # [4, True, 'inserted', 6, 7]

# Accessing an element in a list; lists are 0-indexed; the first element is at index 0
print("Indexed list:", x[2])  # Prints the 3rd element in the list, which is 'inserted'

# Modifying an element in a list
x[4] = "modified"
print("Modified list:", x)  # [4, True, 'inserted', 6, 'modified']

# Counting in a list; returns the number of times an element appears in a list
print("Counted list:", x.count(4))  # 1

print("\n========================================")

# x does not store a copy of the list, it stores a reference to the list
y = x
print("First, let's print x:", x)  # [4, True, 'inserted', 6, 7]
y[2] = "changed"
print(
    "y = x means we've made a reference to x; we've changed y[2] to 'changed'; let's print y:"
)
print("y: ", y)  # [4, True, 'changed', 6, 7]

print(
    "\nLet's print x; x should also be changed because 'y = x' doesn't create a new copy - it only creates a reference/link to x:"
)
print("x: ", x)  # [4, True, 'changed', 6, 7]

# y is a copy of x
# y = x.copy()
# print("We've copied the list to y:", y)  # [4, True, 'inserted', 6, 7]
# y[2] = "changed"
# print("Changed list y:", y)  # [4, True, 'changed', 6, 7]

print("\n========================================")
print("If we want to copy a list, we can use the list() function:")
y = list(x)
print("Copied list y:", y)  # [4, True, 'inserted', 6, 7]
y[1] = "changed with list() function"
print("Changed list y:", y)  # [4, True, 'changed', 6, 7]

print("\n========================================")
print("We can also use the slicing operator to copy a list:")
y = x[:]
print("Copied list y:", y)  # [4, True, 'inserted', 6, 7]
y[1] = "changed with slicing operator"
print("Changed list y:", y)  # [4, True, 'changed', 6, 7]
