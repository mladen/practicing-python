# First example
def func(x=2):
    return x**2


print(func())  # Ovo daje 4
print(func(3))  # Ovo daje 9


# Second example
def func(word, freq=1):
    print(word * freq)


call = func("mladen", 4)
call = func("mladen")
