class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file

    # __exit__ se poziva nevezano da li je bilo exception-a
    # izmedju enter i exit, i ovdje se deal-uje sa exception-om
    def __exit__(self, type, value, traceback):
        print("Exit")
        self.file.close()


with File("1basic-testfile-writing.txt", "w") as f:
    print("Middle")
    f.write("helloooo")
    raise Exception()
    # Iako smo exception/gresku, bice pozvana __exit__()
    # sto ce pravilno zatvoriti fajl
