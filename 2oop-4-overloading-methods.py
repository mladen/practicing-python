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
        return Point(self.x * p.x, self.y * p.y)
    
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

print(p1 + p2)
print(p1 - p2)
print(p1 * p2)