file = open('testfile-reading.txt', 'r')
f = file.readlines()
print(f) # ['Test text in a file called testfile.txt!\n', '\n', 'Third line...\n', '\n', '\n', '6th line...']

# To remove the '\n' symbols from the result
newList = []
for line in f:
    if line[-1] == '\n': # dakle, propusti samo one stringove koji na kraju imaju simbol '\n'
        newList.append(line[:-1]) # koristimo slice operator da bismo uklonili '\n'
    else:
        newList.append(line) # dodajemo poslenji element, koji smo izuzeli sa 'if' izrazom jer nije imao simbol '\n'

print(newList)

file.close() # moramo i da zatvorimo fajl na kraju