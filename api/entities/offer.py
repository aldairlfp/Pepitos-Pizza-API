class Offer(object):
    def __init__(self, id: int, base_offer, amount_added, price: int, available:bool) -> None:
        self._id = id
        self._base_offer = base_offer
        self._amount_added = amount_added
        self._price = price
        self._available = available

    @property
    def id(self):
        return self._id

    @property
    def base_offer(self):
        return self._base_offer

    @property
    def amount_added(self):
        return self._amount_added

    @property
    def price(self):
        return self._price

    @property
    def available(self):
        return self._available