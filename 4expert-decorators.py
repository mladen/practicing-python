# Dekoratori nam omogucavaju da promijenimo posananje funkciji
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

print("------------------------------------")


# 2. Razrada i zakljucak :)
def dekor(fija):
    def wrapper():
        print("Started")
        fija()
        print("Ended")

    return wrapper  # Dakle, ovdje ne vracamo wrapper() vec wrapper


def func2():
    print("Im func 2")


def func3():
    print("Im func 3")


func2 = dekor(func2)
func2()  # Sada, ovo mozemo da pozovemo iz bilo kojeg dijela naseg programa
