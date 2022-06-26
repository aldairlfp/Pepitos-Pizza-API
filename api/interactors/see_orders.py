class SeeOrdersInteractor(object):
    def __init__(self, _order_list_repo) -> None:
        self._order_list_repo = _order_list_repo
        
    def execute(self):
        self._order_list_repo.get_all()