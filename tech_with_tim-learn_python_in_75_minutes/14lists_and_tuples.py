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
print("Indexed list:", x[2])  # inserted

# Counting in a list
print("Counted list:", x.count(4))  # 1
