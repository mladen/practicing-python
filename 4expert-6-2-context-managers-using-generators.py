# Contextlib nam daje dekorator koji koristimo
# na generatoru koji postaje context manager
# import contextlib
from contextlib import contextmanager


@contextmanager
def file(filename, method):
    print("Enter")
    file = open(filename, method)
    yield file
    file.close()
    print("Exit")


with file("1basic-testfile-writing.txt", "w") as f:
    print("Middle")
    f.write("Hellooooo there")
