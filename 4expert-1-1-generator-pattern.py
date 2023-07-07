# ZAKLJUCAK: Generator koristimo kada nam ne trebaju svi podaci
# odjednom vec nam je potrebna samo trenutna vrijednost

# Napomena: Generatore mozemo zaustaviti, mozemo proci (loop)
# kroz generator nekoliko puta a onda kasnije u programu
# nastaviti da prolazim kroz njega a on ce nastaviti gdje je stao itd.


def gener(n):
    for i in range(n):
        yield i**2  # yield vraca vrijednost, a onda pauzira funkciju
        # Dakle, ne stopira/zavrsava (sto radi regularna funkcija
        # kada dodje do "return" rijeci) vec pauzira.
        # To znaci da i dalje imamo trenutno (interno) stanje funkcije.
        # Jos jedno objanjenje je: kada se dodje do "yield", vraca
        # se vrijednost (onome ko je pozvao) i generator(?) ceka
        # da bude pozvan opet. Tako ce je for petlja (na kraju ovog
        # koda) pozvati "n" puta.


g = gener(100000000)

# for petlja moze pozivati generator koliko god da smo stavili u gener()
# for i in g:
#     print(i)

# Osim for petljom, mozemo i manuelno pozivati generator
print(next(g))
print(
    next(g)
)  # Pozivamo next() funkciju u nasem generatoru i dobijamo sledecu vrijednost
print(next(g))
print(next(g))
