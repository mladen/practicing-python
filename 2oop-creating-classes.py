class User(object):
    # Klasa ima metode i atribute
    def __init__(self, name, age): # __init__ je konstruktor(ska) metoda(!); ona mora biti u vecini klasa
                                   # Konstruktor stavljamo u klasu ako zelimo da se nesto
                                   # izvrsi cim se napravi klasa (valjda objekat?)
        self.name = name # Da bismo napravili atribut, moramo da koristimo "self."
                         # "self" se odnosi na instancu koju pozivamo
        self.age = age
        # pass

    def speak(self):
        print('Hi! I am ', self.name, 'and I am', self.age, 'years old')
        # pass

tim = User('Tim', 46) # Tim je instanca klase User
fred = User('Fred', 52) # Fred je instanca klase User

tim.speak()
fred.speak()