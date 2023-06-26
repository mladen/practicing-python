import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Move the turtle forward and turn right to create a square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Close the turtle graphics window
turtle.done()
