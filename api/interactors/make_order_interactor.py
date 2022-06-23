class MakeOrderInteractor(object):
    def __init__(self, order_repo) -> None:
        self._order_repo = order_repo
        
    def set_params(self, id, client, offer, amount):
        self._id = id
        self._client = client
        self._offer = offer
        self._amount = amount