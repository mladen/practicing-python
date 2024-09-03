import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

for _ in range(100):
    my_turtle.forward(10 + _ / 4)
    my_turtle.right(10)

# Close the turtle graphics window
turtle.done()
