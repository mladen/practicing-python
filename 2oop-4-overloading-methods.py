class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y # U matematici, mnozenje vraca skalar a ne vektor

    # Greater than, Greater or equal, Less then, Less or equal, Equal
    def length(self): # Prvo nam treba funkcija za racunanje duzine vektora
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, p):
        return self.length() < p.length()

    def __le__(self, p):
        return self.length() <= p.length()

    def __eq__(self, p):
        # return self.length() == p.length()
        return self.x == p.x and self.y == p.y # Drugi nacin, bez koriscenja length()

    def __str__(self) -> str: # Ova metoda se poziva svaki put kada Point
                              # objekat trebamo da konvertujemo u string
                              # Npr. kada treba da istampamo objekat sa print()
                              # ova funkcija biva automatski pozvana
                              # U slucaju da ova funkcija ne bude pronadjena
                              # bice nam prikazano nesto tipa <__main__.Point object at 0x7f9ace2c7d90>
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)
p5 = Point(3, 4)

print(p1 + p2)
print(p1 - p2)
print(p1 * p2)

print(p1 > p2)
print(p1 == p5)