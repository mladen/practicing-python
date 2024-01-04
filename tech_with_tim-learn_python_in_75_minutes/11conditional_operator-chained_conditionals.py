# We can use "and", "or" and "not" to combine multiple conditions

# Examples with "and"
result1 = 3 != 3
result2 = 3 < 5
result3 = (
    result1 and result2
)  # "and" is used to compare two boolean values; if both of them are true, the result is true
# print("result1:", result1, end="\n\n")  # The result is false because 3 is equal to 3
# print("result2:", result2, end="\n\n")  # The result is true because 3 is less than 5
print("result3:", result3, end="\n\n")  # The result is false because result1 is false

result4 = (
    result1 or not result2 or result3  # "not" is used to reverse the boolean value
)  # "or" is used to compare two boolean values; if one of them is true, the result is true
print("result4:", result4, end="\n\n")

# Example with "not"
print(
    not (False or True)  # We can use parentheses to change the order of evaluation
)  # The result is false because the parentheses are evaluated first ("False or True" gives True)

# IMPORTANT: Order of operations is "not", "and", "or"
