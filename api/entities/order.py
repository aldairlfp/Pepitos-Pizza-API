class Order(object):
    def __init__(self, offer, client, amount: int) -> None:
        self._offer = offer
        self._client = client
        self._amount = amount

    @property
    def offer(self):
        return self._offer

    @property
    def client(self):
        return self._client

    @property
    def amount(self):
        return self._amount