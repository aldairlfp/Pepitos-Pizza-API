class Offer(object):
    def __init__(self, id: int, base_offer, addeds, price: int, available:bool) -> None:
        self._id = id
        self._base_offer = base_offer
        self._addeds = addeds
        self._price = price
        self._available = available

    @property
    def id(self):
        return self._id

    @property
    def base_offer(self):
        return self._base_offer

    @property
    def addeds(self):
        return self._addeds

    @property
    def price(self):
        return self._price

    @property
    def available(self):
        return self._available