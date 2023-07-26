from collections import deque

# Zasto bismo koristili deque (cita se "dek") umjesto tipicne liste?
# Deque izgleda skoro isto kao lista. Ipak, on je brzi pri dodavanju
# (TODO: i uklanjanju???) stavki na pocetku i kraju.
# Ipak, ako zelimo da pristupamo stavkama na sredini strukture podataka
# onda mozemo da koristimo listu umjesto deka.

# 1. Pravljenje deka
d = deque("hello")
print(d)  # deque(['h', 'e', 'l', 'l', 'o']) Ovo lici na listu ali je ustvari dek

# 2. Dodavanje elemenata u dek
d.append("4")
d.appendleft(5)
d.append(6)
print("dek nakon appendleft() i append()", d)

# 3. Uklanjanje elemenata iz deka
d.pop()
d.popleft()
print("dek nakon pop() i popleft(): ", d)

# 4. Ako zelimo da dodamo cijelu listu ili sl. (bilo koji iterable) u dek
# umjesto da radimo for petlju, mozemo uraditi
d.extend("456")
d.extend([1, 2, 3])
print("d nakon extend(): ", d)
d.extendleft("hey")  # Ovdje se prvo dodaje 'h', pa 'e', pa 'y
print("d nakon extendleft(): ", d)  # zato dobijemo deque(['y', 'e', 'h', ...])

# 5. Rotiranje deka
d.rotate(-1)
print("Dek nakon rotacije -1: ", d)  # Rotiramo tj. pomjeramo sve za 1 lijevo...

# 6. Ogranicavanje duzine deka
e = deque("hello", maxlen=5)
e.append(
    3
)  # Ovaj element ce biti dodat na kraj deka ali ce prvi clan ovog deka biti uklonjen
print(
    "Kada stavimo maxlen na dek, dobijamo: ", e
)  # deque(['e', 'l', 'l', 'o', 3], maxlen=5)
