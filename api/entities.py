from msilib.schema import SelfReg
from xml.sax.handler import property_encoding


class BaseOffer(object):
    def __init__(self, id: int, name: str, base_price: int, available: bool):
        self._id = id
        self._name = name
        self._base_price = base_price
        self._available = available

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def base_price(self):
        return self._base_price

    @property
    def available(self):
        return self._available


class Added(object):
    def __init__(self, id: int, name: str, available: bool):
        self._id = id
        self._name = name
        self._available = available

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def available(self):
        return self._available


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


class AmountAdded(object):
    def __init__(self, id:int, added: Added, amount: Amount, price:int) -> None:
        self._id = id
        self._added = added
        self._amount = amount
        self._price = price

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
    def price(self):
        return self._price


class Offer(object):
    def __init__(self, id: int, base_offer: BaseOffer, amount_added: AmountAdded) -> None:
        self._id = id
        self._base_offer = base_offer
        self._amount_added = amount_added

    @property
    def id(self):
        return self._id

    @property
    def base_offer(self):
        return self._base_offer

    @property
    def amount_added(self):
        return self._amount_added
