# Nas racunar ima konacnu kolicinu memorije.
# Kada pokrenemo program, taj program se smjesti
# u memoriju. Dakle, kada manipulisemo promjenljivima
# listama itd. to se smjesta u memoriju.
# Problem je sto neki kod moze da ispuni cijelu memoriju
# i onda dobijamo gresku. Npr. sledeci kod:
#
# x = [i**2 for i in range(10000000000)]

# for el in x:
#     print(el)
#
# E sad - generatori nam daju mogucnost da pogledamo samo
# jednu vrijednost u odredjenom momentu a da ne smjestamo
# cijelu sekvencu (npr. brojeva) u memoriju, ako nam to
# vec nije potrebno.
