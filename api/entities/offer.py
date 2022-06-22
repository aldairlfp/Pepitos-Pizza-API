class Offer(object):
    def __init__(self, id: int, base_offer: BaseOffer, amount_added: AmountAdded, price: int) -> None:
        self._id = id
        self._base_offer = base_offer
        self._amount_added = amount_added
        self._price = price

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