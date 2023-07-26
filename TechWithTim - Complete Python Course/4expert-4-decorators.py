# Dekoratori nam omogucavaju da promijenimo ponasanje funkciji
# bez mijenjanja samog koda te funkcije
# Ovo je korisno jer nekada zelimo da dodamo i uklonimo
# dekoratore dok debagujemo funkciju ili zelimo da
# izmijenimo ponasanje svih nasih funkcija bez mijenjanja koda
# U tom slucaju bismo napravili dekorator, i sa jednom
# linijom koda bismo izmijenili ponasanje svih funkcija


# 1. Uvod
def func(string):  # Od ove funkcije cemo, kasnije, napraviti dekorator
    def wrapper():
        print("Started")
        print(string)
        print("Ended")

    return wrapper


x = func("1st example")
print(x)  # Ovo ustvari stampa adresu funkcije koju je vratila funkcija func()
# To je moguce jer je i funkcija objekat, a objekte mozemo cuvati, predavati itd.

x()  # Tek ovdje izvrsavamo/pozivamo funkciju

print("--------------------------------------------------------")


##################################################################################
# 2. Rad sa konkretnim Python dekoratorima!
def dekor(fija):
    def wrapper(
        *args, **kwargs
    ):  # *args - positional arguments; **kwargs - keyword arguments
        print("Started")
        rv = fija(*args, **kwargs)
        print("Ended")
        return rv

    return wrapper  # Dakle, ovdje ne vracamo wrapper() vec wrapper


def func2():
    print("Im func 2")


# 2.1
# Kako bismo bez "@<naziv dekoratora>" koristili gorenavedeni dekorator
func2 = dekor(func2)
func2()  # Sada, ovo mozemo da pozovemo iz bilo kojeg dijela naseg programa

print("------------------")


# 2.2
# Koristeci dekorator (bolja verzija)!
# Mozemo koristiti i vise dekoratora.
@dekor
def func3():
    print("Im func 3 - using decorator")


func3()

print("------------------")


# 2.3
# Ako dekorator koristimo sa funkcijom kojoj se predaju argumenti
# onda u dekoratoru moramo to rijesiti sa args i kwargs
@dekor
# def func4(x, y):
def func4(x):  # Ovdje se moze dodati koliko god nam treba parametara
    print("Im func 4. Printing the passed argumend: ", x)


# func4(4, 6)
func4(3)
print("---")
func4(x=None)

print("---")


# 2.4
# Ako zelimo da sa dekoratorom prosirimo
# funkciju koja vraca neku vrijednost
@dekor
def func5(j, k):
    print(j)
    return k  # Dakle, func5() ovdje vraca neku vrijednost


j = func5(3, 8)
print(j)
