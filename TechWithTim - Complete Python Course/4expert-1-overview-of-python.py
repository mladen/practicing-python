# Python je interpreted programming language
# Python se prvo kompajlira u bytecode prije nego sto se interpretira

# Sta je kompajler a sta je interpreter?
# KOMPAJLER uzima high-level code i prevodi ga u lower level code
# INTERPRETER uzima neki kod (tipicno bytecode) i interpretira i pokrece (runs)
# taj kod tj. cita (reads) taj kod i prevodiga na u trenutku (on the fly)
# u masinski kod koji moze da bude izvrsen od strane naseg racunara (za razliku
# od kompajlera koji to radi prije)


# Primjer 1
def make_class(x):
    class Dog:
        def __init__(self, name):
            self.name = name

        def print_value(self):
            print(x)

    return Dog


cls = make_class(10)
d = cls("Mladen")
print(d.name)
d.print_value()


# Primjer 2
# import inspect # TODO: Pogledati sta sve moze ova biblioteka
def func(x):
    if x == 1:

        def rv():
            print("X je jednako 1")

    else:

        def rv():
            print("X nije jednako 1")

    return rv


new_func = func(1)
new_func()

# Lokaciju funkcije u mamoriji dobijamo ovako
print(id(new_func))
