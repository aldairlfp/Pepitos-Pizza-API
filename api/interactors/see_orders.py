from ..unit_repositories import OrderListRepo

class SeeOrdersInteractor(object):
    def __init__(self, order_list_repo:OrderListRepo) -> None:
        self._order_list_repo = order_list_repo
        
    def execute(self):
        return self._order_list_repo.get_all()