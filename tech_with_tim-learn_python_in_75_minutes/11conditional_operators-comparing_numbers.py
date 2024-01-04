result = (
    6 == 6
)  # The double equal sign is used to compare two values. Then it returns a boolean value to the variable "result".
print(result, end="\n\n")

result = 6.9 >= 7
print(result, end="\n\n")

result = 7 <= 7.1
print(result, end="\n\n")

x = 5
result = 4 < x < 8  # You can compare multiple values at once.
# result = 4 < x and x < 8  # This is the same as the previous line.
print(result, end="\n\n")

result = 4 < x + 1  # The "less than" is evaluated last.
print(result, end="\n\n")
