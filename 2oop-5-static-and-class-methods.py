class User:
    users = [] # svojstvo/a klase tj. class properties (a ne
    xc = 5     # objekta/instance koju pravimo uz pomoc ove klase)

    def __init__(self, name):
        self.name = name
        self.users.append(self)

    @classmethod # metoda klase (a ne objekta/instance...)
    def num_users(cls):
        return len(cls.users)

    @staticmethod
    def speak(n):
        """Speaks n times"""
        for _ in range(n):
            print('Hello')

    def __str__(self) -> str: # Bez ovako overload-ovane __str__ funkcije
        return self.name      # samo bismo dobili adrese u memoriji

marko = User("Marko")
marko.speak(1)

nikola = User("Nikola")

# print(User.users) # Ovako samo dobijamo adresu tipa
                  # [<__main__.User object at 0x7f703efcf9d0>, <__main__.User object at 0x7f703efcf940>]
for user in User.users:
    print(user) # Kao sto sam u liniji 19 i 27 vec rekao - kada
                # se pozove print(), cilj je da se istampa
                # string, ali da bismo istampali string, a ne
                # adresu u memoriji - moramo da overloadujemo
                # __str__ funkciju tako da ona ne daje memorijsku
                # adresu, vec string