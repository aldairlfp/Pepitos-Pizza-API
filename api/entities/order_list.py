class Order_List(object):
    def __init__(self, id: int, client, orders: list, date: str, state: str) -> None:
        self._id = id
        self._date = date
        self._state = state
        self._orders = orders
        self._client = client

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
        
    @property
    def client(self):
        return self._client