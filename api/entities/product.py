class Product(object):
    def __init__(self, id: int, name: str, amount: int) -> None:
        self._id = id
        self._name = name
        self._amount = amount

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def amount(self):
        return self._amount
