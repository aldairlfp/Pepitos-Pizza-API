from ..entities.requested_offer import RequestedOffer
from ..entities.order_list import Order_List

from ..unit_repositories import OrderRepo


class ChoosedOfferInteractor(object):
    def __init__(self, order_repo) -> None:
        self._order_repo: OrderRepo = order_repo

    def set_params(self, by_id:int=None, id:int=None, requested_offer:RequestedOffer=None, amount:int=None, order_list:Order_List=None):
        self._by_id = by_id
        self._id = id
        self._requested_offer = requested_offer
        self._amount = amount
        self._order_list = order_list

    def get_all(self):
        return self._order_repo.get_all()

    def get_element(self):
        return self._order_repo.get_element(self._by_id)

    def create(self):
        return self._order_repo.create(self._requested_offer, self._amount, self._order_list)

    def update(self):
        return self._order_repo.update(self._by_id, self._id, self._requested_offer, self._amount, self._order_list)

    def delete(self):
        return self._order_repo.delete(self, self._by_id)
