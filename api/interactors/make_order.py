class MakeOrderInteractor(object):
    def __init__(self, order_list_repo) -> None:
        self._order_list_repo = order_list_repo
        
    def set_params_order_list(self, by_id=None, id=None, client=None, orders=None, date=None, state=None):
        self._by_id = by_id
        self._id = id
        self._client = client
        self._orders = orders
        self._date = date
        self._state = state
        
    def get_all(self):
        return self._order_list_repo.get_all()
    
    def get_element(self):
        return self._order_list_repo.get_element(self._by_id)

    def create(self):
        return self._order_list_repo.create(self._id, self._client, self._orders, self._date, self._state)
        
    def update(self):
        return self._order_list_repo.update(self._by_id, self._id, self._client, self._orders, self._date, self._state)
        
    def delete(self):
        return self._order_list_repo.delete(self._by_id)
