x = 5
y = 'string'

print(type(x)) # Daje <class 'int'>
print(type(y)) # Daje <class 'str'>

print(y.upper()) # Metoda je funkcija koju pozivamo na(d) objektom
                 # Metode nam takodje vracaju nesto
                 # kao npr. string gdje su sva slova velika
                 # TODO: Da li sve metode vracaju nesto?

                 # Nekada i metode mogu uzeti objekte.

def testfunc(x):
    return x + 1
print(testfunc(5)) # Funkcija uzima objekat/objekte i primjenjuje neku operaciju nad njima