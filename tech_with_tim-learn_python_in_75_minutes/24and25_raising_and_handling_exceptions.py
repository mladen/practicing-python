try:
    x = 7 / 0
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero, you silly goose!")
finally:
    print(
        "This will always execute."
    )  # This will always execute, whether or not an exception was raised
