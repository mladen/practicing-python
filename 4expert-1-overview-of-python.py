# Python je interpreted programming language
# Python se prvo kompajlira u bytecode prije nego sto se interpretira

# Sta je kompajler a sta je interpreter?
# KOMPAJLER uzima high-level code i prevodi ga u lower level code
# INTERPRETER uzima neki kod (tipicno bytecode) i interpretira i pokrece (runs)
# taj kod tj. cita (reads) taj kod i prevodiga na u trenutku (on the fly)
# u masinski kod koji moze da bude izvrsen od strane naseg racunara (za razliku
# od kompajlera koji to radi prije)


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
