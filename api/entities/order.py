from api.models import OrderList


class Order(object):
    def __init__(self, id, requested_offer, amount: int, order_list) -> None:
        self._id = id
        self._requested_offer = requested_offer
        self._amount = amount
        self._order_list = order_list

    @property
    def id(self):
        return self.id
        
    @property
    def requested_offer(self):
        return self._requested_offer

    @property
    def amount(self):
        return self._amount
        
    @property
    def order_list(self):
        return self._order_list