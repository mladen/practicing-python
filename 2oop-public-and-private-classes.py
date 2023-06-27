class _Private:  # Mogu da se koriste unutar fajla/opsega (scope-a)
    name = ""

    def __init__(self, name) -> None:
        self.name = name


class NotPrivate:  # Moze da im svako pristupi
    def __init__(self, name) -> None:
        self.name = name
        self.priv = _Private(name)

    def _display(self):
        print("Hello")

    def display(self):
        print("Hi")
