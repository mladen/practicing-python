someList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func(x):
    return x**x  # 1na1, 2na2, 3na3, 4na4, ... , 10na10


# Klasican pristup bi bio
# newList = []
# for x in someList:
#     newList.append(func(x))

# print(newList)

# Prethodne 4 linije mozemo da skratimo u samo
# jednu, koristeci map funkciju
# Napomene:
# - map() uzima 2 argumenta: funkciju i listu
# - map() ce primijeniti zadatu funkciju na svaki clan liste
print(list(map(func, someList)))

# Takodje, mozemo iskoristiti i list comprehention
# Dakle, uzimamo func(x) i izvrsicemo to
# za svaku vrijednost x-a iz liste someList
print([func(x) for x in someList])

# U list comprehention mozemo dodati i uslov
# Npr. ako zelimo da se list compr. izvrsi samo za x
# koji je djeljiv (bez ostatka) sa 2
# (dakle, za 2, 4, 6, 8 i 10)
print([func(x) for x in someList if x % 2 == 0])
