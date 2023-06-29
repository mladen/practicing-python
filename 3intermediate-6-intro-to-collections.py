# import collections
from collections import Counter

# Kolekcije nam omogucavaju da imamo razlicite tipove podataka (datatypes)
# kako bismo mogli da sortiramo informacije
# Containers:
# list
# set
# dict
# tuple - immutable
#
# Types
# counter <- u ovom fajlu cu o njemu
# deque
# namedTuple()
# orderDict
# defaultdict

# 1. String
c1 = Counter(
    "krivacevic"  # Stavljamo string
)  # Unutar Counter() moze da ide bilo koji tip podataka tipa kolekcija iz Containers sekcije
print(c1)

# 2. Lista
c2 = Counter(["a", "a", "a", "g", "d", "u", "r", "u", "e", "g", "g"])  # Stavljamo listu
print(c2)

# 3. Dictionary
# Dictionary uzima poslednju vrijednost za svaki kljuc.
# Npr. ako ima vise "a" kljuceva, uzece se poslednja vrijednost (prepisace prethodne)
c3 = Counter({"a": 1, "b": 3, "a": 2, "a": 16, "a": 2})  # Stavljamo dictionary
print(c3)

# 4. Keywords
c4 = Counter(
    cats=4, dogs=2
)  # Stavljamo keywords (TODO: pogledati i ovo - sta je u pitanju)
# Ustvari ovo prethodno je rezultat sledeceg koda? To je poenta valjda?
# c4 = Counter(["cat", "cat", "dog", "cat", "dog", "cat"])
print(c4)

# ##########################################################################

# 4.1 Pristupanje elementima
print(c4["cat"])
print(c4["elephant"])  # Kod liste, kada trazimo nepostojeci clan, ovo daje nulu (0)

# testDict = {"dog": 2, "cat": 1}
# print(
#     testDict["rhino"]
# )  # Kod dictionary ako trazimo nepostojeci kljuc - dobijamo gresku

# 4.2 Izlistavanje svih elemenata iz primjera pod 4.
print(list(c4.elements()))  # Sa ovim list() mi KONVERTUJEMO nesto u listu

# 4.3 Izlistavanje najcescih elemenata
print(c4.most_common(2))  # Izlistavamo dva najcesce koriscena elementa iz c4

# 4.3 Subtracting
sub = [
    "cats",
    "cats",
]  # Napomena: Ovdje mozemo da koristimo: dictionary, Counter object, set, tuple...
c4.subtract(sub)  # Dakle, od c4 se oduzimaju elementi iz sub liste
print("Subtracting: ", c4)

# 4.4 Update
upd = [
    "dogs"
]  # Napomena: Ovdje mozemo da koristimo: dictionary, Counter object, set, tuple...
c4.update(upd)
print("Updating: ", c4)

# 4.5 Clear (removes all of the counts)
c4.clear()
print("Clear: ", c4)

# 4.6 Adding and Subtracting
z = Counter(a=4, b=2, c=0, d=-2)
r = Counter(["a", "b", "b", "c"])
print("Addition: ", z + r)
print(
    "Subtraction:", z - r
)  # U rezultatu ovoga nam se nece prikazati b, c, i d jer ako je
# Count elementa manji ili jednak nuli, element nece bit prikazan u Counter-u

# 4.7 Intersection and Union
print("Intersection: ", z & r)  # Uzima minimalne elemente???
print("Union: ", z | r)  # Uzima maksimalne elemente
