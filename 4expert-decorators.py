# Dekoratori nam omogucavaju da promijenimo posananje funkciji
# bez mijenjanja samog koda te funkcije
# Ovo je korisno jer nekada zelimo da dodamo i uklonimo
# dekoratore dok debagujemo funkciju ili zelimo da
# izmijenimo ponasanje svih nasih funkcija bez mijenjanja koda
# U tom slucaju bismo napravili dekorator, i sa jednom
# linijom koda bismo izmijenili ponasanje svih funkcija


def func(string):
    def wrapper():
        print("Started")
        print(string)
        print("Ended")

    return wrapper


x = func("hello")
print(x)  # Ovo ustvari stampa adresu funkcije koju je vratila funkcija func()
# To je moguce jer je i funkcija objekat, a objekte mozemo cuvati, predavati itd.

x()  # Tek ovdje izvrsavamo/pozivamo funkciju
