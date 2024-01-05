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
x.pop()  # removes the last element
print("Popped list:", x)  # [4, True, 6, 7]

# Inserting into a list
x.insert(2, "inserted")
print("Inserted list:", x)  # [4, True, 'inserted', 6, 7]

# Indexing a list
print("Indexed list:", x[2])  # Prints the 3rd element in the list, which is 'inserted'

# Counting in a list
print("Counted list:", x.count(4))  # 1

print("========================================")

# x does not store a copy of the list, it stores a reference to the list
y = x
print("Let's print x:", x)  # [4, True, 'inserted', 6, 7]
y[2] = "changed"
print(
    "We've made a reference to x; we've changed y[2] to 'changed'; let's print y:", y
)  # [4, True, 'changed', 6, 7]
print(
    "Let's print x; x should also be changed because 'y = x' doesn't create a new copy - it only creates a reference/link to x:",
    x,
)  # [4, True, 'changed', 6, 7]

# y is a copy of x
# y = x.copy()
# print("We've copied the list to y:", y)  # [4, True, 'inserted', 6, 7]
# y[2] = "changed"
# print("Changed list y:", y)  # [4, True, 'changed', 6, 7]
