string = "hello there"
# string = input('Enter some string')

# Ako hocemo da vidimo da li postoji neki simbol/karakter u odredjenom stringu
print(
    string.find("l")
)  # PRVI karakter 'l' (na koji nailazi funkcija .find()) se nalazi na indeksu 2 pa je 2 rezultat
# Npr. ako zelimo da provjerimo da li neka lozinka sadrzi nedozvoljeni simbol/karakter itd.

# Ako hocemo da prebrojimo trazene karaktere ili da vidimo da li postoji karakter itd.
print(string.count("e"))
