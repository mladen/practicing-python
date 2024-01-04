result1 = (
    6 == 6
)  # The double equal sign is used to compare two values. Then it returns a boolean value to the variable "result"
print("result1:", result1, end="\n\n")

result2 = 6.9 >= 7
print("result2:", result2, end="\n\n")

result3 = 7 <= 7.1
print("result3:", result3, end="\n\n")

x = 5
result4 = 4 < x < 8  # You can compare multiple values at once
# result4 = 4 < x and x < 8  # This is the same as the previous line
print("result4:", result4, end="\n\n")

result5 = 4 < x + 1  # The "less than" is evaluated last
print("result5:", result5, end="\n\n")
