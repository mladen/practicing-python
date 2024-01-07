# [start:stop:step] - these are all indexes; "stop" is not inclusive

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ["hi", "hello", "bye", "goodbye"]
s = "hello"

print("x = ", x, "\n")  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("x[0:5] =", x[0:5])  # [0, 1, 2, 3, 4]
print("x[0:4:2] =", x[0:4:2])  # [0, 2]
print("x[:4:2] =", x[:4:2])  # [0, 2]; start defaults to 0
print("x[0::2] =", x[0::2])  # [0, 2, 4, 6, 8]; stop defaults to len(x)
print(
    "x[::2] =", x[::2]
)  # [0, 2, 4, 6, 8]; start defaults to 0 and stop defaults to len(x)
print("x[2:] =", x[2:])  # [2, 3, 4, 5, 6, 7, 8, 9]; stop defaults to len(x)
print(
    "x[4:2:-1]", x[4:2:-1]
)  # [4, 3] # step is negative, so we go backwards from 4 to 2; stop (2) is not inclusive

# Reversing a list (or string)
print("Reversing a list, x[::-1] =", x[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("Reversing a string, s[::-1] =", s[::-1])  # olleh
