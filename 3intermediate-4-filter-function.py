def isOdd(x):
    return x % 2 != 0  # Funkcija koja nesto provjerava


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Uz pomoc filter() mi filtriramo (uklanjamo; filtering
# out) elemente na bazi neke predefinisane funkcije
# Dakle, u listu 'b' ce uci samo clanovi liste 'a'
# zbog kojih isOdd(x) daje True
b = list(filter(isOdd, a))
print(b)
