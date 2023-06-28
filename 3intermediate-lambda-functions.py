# Regularna funkcija
def funcRegular(x):
    return x + 5  # Za ovako jednostavnu funkciju je bolje da napisemo lambda funkciju


print(funcRegular(9))

# Lambda funkcija
# Napomena: Lambda funkcije su ustvari anonimne funkcije
funcLambda = lambda x: x + 5  # Prvo 'x' je parametar; 'x+5' je ono sto se vraca
print(funcLambda(2))
