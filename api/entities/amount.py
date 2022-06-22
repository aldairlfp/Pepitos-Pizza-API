class Amount(object):
    def __init__(self, id: int, amount: int) -> None:
        self._id = id
        self._amount = amount

    @property
    def id(self):
        return self.id

    @property
    def amount(self):
        return self._amount