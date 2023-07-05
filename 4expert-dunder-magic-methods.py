# Uzecemo dva objekta koji interaugju zajedno (medjusobno?)
# a onda cemo da vidimo kako mozemo da napravimo sopstvene objekte
# pa cak i kako da modifikujemo postojece Python objekte
import inspect

# print(inspect.getsource(list))
# 1. primjer
x = [1, 2, 3]
y = [4, 5]

print(type(x))


# 2. primjer
class Person:
    def __init__(self, name) -> None:  # funkcije sa "__" su Dunder iliti magic metode
        self.name = name

    def __repr__(
        self,
    ) -> (
        str
    ):  # Ovu funkciju dodajemo da nam print(p) ne bi vratilo samo adresu funkcije u memoriji
        return f"Person({self.name})"

    def __mul__(
        self, x
    ):  # Ovo ce da se izvrsi kada nad Person objektom izvrsimo "mul" metodu; x je neki integer
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")

        self.name = self.name * x


p = Person("Mladen")
p * 4
print(p)
