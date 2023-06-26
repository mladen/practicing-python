class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Hi! I am ', self.name, 'and I am', self.age, 'years old.')

    def user_type(self):
        print(self.name, 'is a regular user.')

class Scientist(User):  # User je 'parent'
    def __init__(self, name, age, area): # Posto dodajemo 'area' moramo da imamo ovu liniju
        super().__init__(name, age) # Ovako pozivamo konstruktor iz 'parent'-a
        self.area = area

    def user_type(self): # Ovdje OVERLOAD-ujemo tj preklopimo funkciju user_type() koju smo dobili iz User klase
        print(self.name, 'is a scientist. His field of study is', self.area + '.')

# Kreiranje objekta (instanciranje) koristeci klasu User
marko = User('Marko', 40)
marko.speak()
marko.user_type()

# Kreiranje objekta (instanciranje) koristeci klasu Scientist
mladen = Scientist('Mladen', 40, 'mathematics')
mladen.speak()
mladen.user_type()
