# Nas racunar ima konacnu kolicinu memorije.
# Kada pokrenemo program, taj program se smjesti
# u memoriju. Dakle, kada manipulisemo promjenljivima
# listama itd. to se smjesta u memoriju.
# Problem je sto neki kod moze da ispuni cijelu memoriju
# i onda dobijamo gresku. Npr. sledeci kod (bi POKUSAO da
# smjesti 10000000000 brojeva u memoriju ali bismo dobili
# gresku):
#
# x = [i**2 for i in range(10000000000)] # smesta ovo u memoriju
# for el in x:
#     print(el)
#
# E sad - generatori nam daju mogucnost da pogledamo samo
# jednu vrijednost u odredjenom momentu a da ne smjestamo
# cijelu sekvencu (npr. brojeva) u memoriju, ako nam to
# vec nije potrebno.


# Primjer kako generator radi "u pozadini" (koristeci
# klasu u Dunder metode)
class Gen:
    def __init__(self, n):
        self.n = n
        self.last = (
            0  # Ovdje cuvamo (interno) stanje sledeceg broja
            # koji trebamo da generisemo. Dakle, ne trebaju nam ostali.
        )

    def __next__(self):
        return self.next()  # self() cemo definisati ispod

    def next(self):
        if self.last == self.n:
            raise StopIteration()

        rv = self.last**2
        self.last += 1
        return rv


g = Gen(100000000000000000000000000000000000)

while True:
    try:
        print(next(g))  # __next__() omogucava da pozovemo next() na "g" generator
    except StopIteration:
        break
