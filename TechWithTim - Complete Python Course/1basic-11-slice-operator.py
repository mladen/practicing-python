# 1.
fruits = ["apple", "pear", "strawberry"]

# print(text[start:stop:step])
print(
    fruits[0:2]
)  # daje ['apple', 'pear'], dakle UZIMA element sa indeksom 0 i ide DO elementa sa indeksom 2 (ali ga izuzima)

text = "Hi there, I like Python"
print(text[0:4])  # daje 'Hi t'
print(
    text[3:]
)  # Pocinje od elementa na indeksu 3 i ide do kraja. Dakle daje 'there, I like Python'

# 2. Step feature
print(
    text[2:10:2]
)  # Uzima svaki drugi element, ali pocinje od elementa sa indeksom 2 i ide DO elementa sa indeksom 10 (ali ga izuzima)
print(text[::3])  # Uzima svaki treci element, ide od pocetka do kraja "Htr leyo"

# 3. Insert function (with slice operator)
# Kada zelimo nesto da dodamo u listu, radili smo fruits.append('blueberries') ali ako zelimo da unesemo neku stavku
# ne na kraj niza, vec negdje drugo, onda radimo slice operator da bismo to uradili
index = 2
fruits[index:index] = [
    "blueberry"
]  # Dobijamo ['apple', 'pear', 'blueberry', 'strawberry']
print(fruits)

# 3.1 Interesantan slucaj
index = 2
fruits[
    index:index
] = "blueberry"  # Dobijamo ['apple', 'pear', 'b', 'l', 'u', 'e', 'b', 'e', 'r', 'r', 'y', 'blueberry', 'strawberry']
print(fruits)

# 4. Last element
print(
    fruits[:-1]
)  # uzima sve OSIM zadnjeg elementa (bilo da radimo sa listama ili stringovima)
print(
    text[:-5]
)  # Dobijamo "Hi there, I like P"; dakle, uklonjeno je tacno 5 zadnjih karaktera
