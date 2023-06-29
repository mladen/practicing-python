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
# c4 = Counter(
#     cats=4, dogs=2
# )  # Stavljamo keywords (TODO: pogledati i ovo - sta je u pitanju)
# Ustvari ovo prethodno je rezultat sledeceg koda? To je poenta valjda?
c4 = Counter(["cat", "cat", "dog", "cat", "dog", "cat"])
print(c4)
