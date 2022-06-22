class OrderList(object):
    def __init__(self, id: int, date: str, address: str, state: str, orders: list) -> None:
        self._id = id
        self._date = date
        self._address = address
        self._state = state
        self._orders = orders

    @property
    def id(self):
        return self._id

    @property
    def date(self):
        return self._date

    @property
    def address(self):
        return self.address

    @property
    def state(self):
        return self._state

    @property
    def orders(self):
        return self._orders