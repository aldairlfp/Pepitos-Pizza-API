class OrderList(object):
    def __init__(self, id: int, orders: list, date: str, state: str) -> None:
        self._id = id
        self._date = date
        self._state = state
        self._orders = orders

    @property
    def id(self):
        return self._id

    @property
    def date(self):
        return self._date

    @property
    def state(self):
        return self._state

    @property
    def orders(self):
        return self._orders