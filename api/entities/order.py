class Order(object):
    def __init__(self, requested_offer, amount: int) -> None:
        self._requested_offer = requested_offer
        self._amount = amount

    @property
    def requested_offer(self):
        return self._requested_offer

    @property
    def amount(self):
        return self._amount