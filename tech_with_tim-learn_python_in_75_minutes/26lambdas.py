# Lambda is a one line (anonymous) function; anonymous means that it is not defined with a name
# It is used for simple functions that are not going to be used again
# It is not defined with a def keyword
# Can take any number of arguments, but can only have one expression
# Syntax: lambda arguments: expression

# Example 1
addnumbers = lambda x: x + 5  # here x is the argument and x + 5 is the expression
print("addnumbers(2) =", addnumbers(2))  # x(2) = 7

# Example 2
mult = lambda x, y: x * y  # here x and y are the arguments and x * y is the expression
print("mult(2, 7) =", mult(2, 7))  # mult(2, 7) = 14
