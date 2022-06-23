class AmountAdded(object):
    def __init__(self, id, added, amount, available) -> None:
        self._id = id
        self._added = added
        self._amount = amount
        self._available = available

    @property
    def id(self):
        return self._id

    @property
    def added(self):
        return self._added

    @property
    def amount(self):
        return self._amount.amount
        
    @property
    def available(self):
        return self._available