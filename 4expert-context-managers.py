# Jedna od korisnijih stvari
# Bice korisni kada budemo pricali o:
# - shared memory
# - shared resources
# - unlocking
# - locking
#
# Pitanje: Koji problem context manager-i rjesavaju?
# file = open("file.txt", "w")
# file.write("hello")xffdsd
# file.close()
#
# Kako mozemo da dodjemo do kraja programa
# iako npr. u sredini naidjemo na problem?
#
# Odgovor: Mozemo iskoristiti try/finally
# file = open("file.txt", "w")
#    try:
# file.write("hello")xffdsd
#    finally:
# file.close()
#
# Ipak, postoji laksi i bolji nacin da ovo uradimo,
# koji omogucava vise funkcionalnosti, a to su
# context manager-i.
