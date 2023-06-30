# Ovo je dio collections module klase/datatype
# U proslom primjeru smo radili sa Couter() a danas cemo ovaj datatype/klasu
# Named tuples nam daju mogucnost da pristupamo poljima koristeci
# nazive/imena (names) umjesto koristeci indekse
from collections import namedtuple

# Point = namedtuple("Point", "x y z")  # Tretiracemo Point kao klasu
Point = namedtuple(
    "Point", ["x", "y", "z"]
)  # Takodje, bilo koji 'iterable' ce raditi (isto)

newP = Point(3, 4, 5)  # newP je ustvari Point(x=3, y=4, z=5)
print(newP)
print(newP.x, newP.y, newP.z)

# Mozemo koristiti operacije koje koristimo na osnovnim tuple-ovima
print(newP[0])  # Pristupanje preko indeksa
print(newP._asdict())  # Stampamo u formi dictionary-ja
print(newP._fields)  # Stampamo nazive polja (field names)
# i za kraj (za sada)
print(newP._replace(x=6))  # Replace metoda (koja ne mijenja originalni
# newP, ali moze ako uradimo newP = newP.replace(x=6))

# Ajde jos jedna
p2 = Point._make(["a", "b", "c"])  # Ova metoda uzima vrijednosti i
# dodjeljuje ih Point stavkama
print(p2)
