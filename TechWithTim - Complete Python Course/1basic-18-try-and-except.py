# Kao try i catch u JavaScript-i i sl. jezicima
text = input("Enter a number: ")  # Ovdje npr. probamo da unesemo tekst,
# ili neki drugi simbol, da bismo dobili gresku

# Posto zelimo da korisnik unese samo broj, a ne tekst ili neki nedozvoljeni simbol,
# i posto ne zelimo da nam se program 'srusi' - koristicemo try i except
try:
    # BLOK KODA KOJI TESTIRAMO (se stavlja unutar 'try' dijela)!!!
    number = int(text)  # Ako je unesen string u formi broja onda ce konverzija biti
    # uspjesna, pa Python nece dati gresku
    print(number)
except:
    # Ovdje možemo pitati korisnika da unese traženi podatak opet ili nešto drugo itd.
    print("Invalid Username!")
