import sys


def gener(n):
    for i in range(n):
        yield i**2


lList = [i**2 for i in range(10000)]
gGenerator = gener(10000)

print("List size: ", sys.getsizeof(lList))
print("Generator size: ", sys.getsizeof(gGenerator))
