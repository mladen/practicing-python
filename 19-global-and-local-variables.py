# Globalne promjenljive
# Napomena: ne zelimo da budemo zavisni od njih da bi nam radile funkcije,
#           jer ako neku od funkcija ukljucimo u Glavni program (npr. ako nam
#           je funkcija func() dio Modula pa hocemo taj Modul da ukljucimo negdje)
#           taj Glavni program nece vidjeti promjenljive koje su globalne u
#           tom Modulu
#
# Dakle, kako bismo mogli da promijenimo globalnu promjenljivu?
var = 9
loop = True
newVar = 23

def func(x):
    # newVar = 7  # lokalna varijabla (lokalna za funkciju func())
                # dakle, ne moze je vidjeti niko van ove funkcije
                # niti moze da promijeni ista van funkcije OSIM...
                # osim ako se ne pozovemo na globalnu promjenljivu
                # uz pomoc "global nazivGlobalnePromjenljive"
    global newVar # dakle, ovako KORISTIMO i MIJENjAMO globalNu varijablu
    newVar = 8
    print(newVar) # ovo ce da istampa vrijednost globalne varijable

    if x == 5:
        return newVar

func(4)
print(newVar) # OVDJE VIDIMO VRIJEDNOST KOJU JE IZMIJENILA FUNKCIJA func()

# def otherFunc():
#     newVar = 5 # ova funkcija vidi i newVar = 23, ali posto je newVar
#                # ovdje inicijalizovan(?) sa vrijednoscu 5 - uzimamo tu vrijednost
#     print(newVar)

# otherFunc()