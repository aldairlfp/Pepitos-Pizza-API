from .requested_offer import RequestedOffer
from .order_list import Order_List
class Order(object):
    def __init__(self, id:int, requested_offer: RequestedOffer, amount: int) -> None:
        self._id = id
        self._requested_offer = requested_offer
        self._amount = amount

    @property
    def id(self):
        return self._id
        
    @property
    def requested_offer(self):
        return self._requested_offer

    @property
    def amount(self):
        return self._amount