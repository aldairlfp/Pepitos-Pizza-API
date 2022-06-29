from ..entities.client import Client

from ..unit_repositories import OrderListRepo

class MakeOrderInteractor(object):
    def __init__(self, order_list_repo:OrderListRepo) -> None:
        self._order_list_repo:OrderListRepo = order_list_repo
        
    def set_params(self, by_id:str=None, id:str=None, client:Client=None, date:str=None):
        self._by_id = by_id
        self._id = id
        self._client = client
        self._date = date

    def create(self):
        return self._order_list_repo.create(self._id, self._client, self._date)
        
    def update(self):
        return self._order_list_repo.update(self._by_id, self._id, self._client, self._orders, self._date)
        
    def delete(self):
        return self._order_list_repo.delete(self._by_id)
