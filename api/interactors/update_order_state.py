class UpdateOrderStateInteractor(object):
    def __init__(self, order_list_repo) -> None:
        self._order_list_repo = order_list_repo
        
    def set_params(self, by_id, state):
        self._by_id = by_id
        self._state = state
        
    def execute(self):
        return self._order_list_repo.update_state(self._by_id, self._state)
    