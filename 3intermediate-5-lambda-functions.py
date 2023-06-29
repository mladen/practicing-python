# 1. Regularna funkcija
def funcRegular(x):
    return x + 5  # Za ovako jednostavnu funkciju je bolje da napisemo lambda funkciju


print(funcRegular(9))

# 2. Lambda funkcija
# Napomena: Lambda funkcije su ustvari anonimne funkcije
funcLambda = lambda x: x + 5  # Prvo 'x' je parametar; 'x+5' je ono sto se vraca
print(funcLambda(2))


# 3. Koriscenje lambda funkcije unutar druge funkcije
def funcInnerLambda(x):
    funcL = lambda x: x + 5
    return funcL(x)


print(funcInnerLambda(5))

# 4. Primjer funkcije sa vise parametara
# Napomena: Mozemo i opcionalne parametre da zadamo tipa 'lambda x, y = 4: x + y'
funcMultiParam = lambda x, y: x + y
print(funcMultiParam(3, 3))

# 5. Lambda f. sa filter()
# Napomena: Dakle, ovdje ne moramo da pravimo novu funkciju,
# vec odmah stavimo lambda funkciju unutar filter()
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lambdaWithMap = list(filter(lambda x: x % 2 == 0, a))
print(lambdaWithMap)
