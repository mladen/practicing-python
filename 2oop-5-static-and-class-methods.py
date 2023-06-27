class User:
    users = []  # promjenljive KLASE tj. class variable (a ne
    xc = 5  # objekta/instance koju pravimo uz pomoc ove klase)

    def __init__(self, name):
        self.name = name
        self.users.append(self)

    @classmethod  # metoda KLASE (a ne objekta/instance...); DEKORATOR
    def num_users(cls):  # Sa "cls" mi predajemo klasu tako da mozemo (unutar ove
        return len(cls.users)  # metode) da koristimo promjenljive i metode same klase
        # Npr. ako unutar num_users() hocemo da koristimo users[]
        # ili staticnu metodu ili ako hocemo da pozovemo
        # inicijalizaciju ili generalno da radimo oko User klase.

    @staticmethod  # STATICNA metoda; DEKORATOR TJ. "SPECIJALNI TIP METODE"
    def speak(n):
        """Speaks n times"""
        for _ in range(n):
            print("Hello")

    def __str__(self) -> str:  # Bez ovako overload-ovane __str__ funkcije
        return self.name  # samo bismo dobili adrese u memoriji


# OVDJE RADIM MALO SA SVOJSTVIMA KLASE
marko = User("Marko")
marko.speak(1)

nikola = User("Nikola")

# print(User.users) # Ovako samo dobijamo adresu tipa
# [<__main__.User object at 0x7f703efcf9d0>,
# <__main__.User object at 0x7f703efcf940>]
for user in User.users:
    print(user)  # Kao sto sam u liniji 19 i 27 vec rekao - kada
    # se pozove print(), cilj je da se istampa
    # string, ali da bismo istampali string, a ne
    # adresu u memoriji - moramo da overloadujemo
    # __str__ funkciju tako da ona ne daje memorijsku
    # adresu, vec string

# OVDJE RADIM SA METODAMA KLASE (dekorator @classmethod)
# NE TREBA NAM INSTANCA/OBJEKAT da bismo pozvali ovaj tip metoda.
# Pozivamo ih uz pomoc klase.
print(User.num_users())  # Dakle, pozivamo num_users() nad User klasom
# Maadaa, mozemo tu metodu pozvati i uz pomoc
# instanci, ali bolje da se drzimo pozivanja
# uz pomoc klase.

# OVDJE RADIM SA STATICNIM METODAMA (dekorator @staticmethod)
# Staticnim metodama NE TREBA KLASA da bismo tu metodu pozvali
# Ne predajemo joj klasu (sa "cls", kao sto to radimo sa metodom
# klase), pa cak ni "self" vec samo ono sto nam treba, ako treba ista.
User.speak(3)
