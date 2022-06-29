from ..unit_repositories import OrderListRepo
from ..exception import ValidationError

class SeeMyOrdersInteractor(object):
    def __init__(self, order_list_repo:OrderListRepo) -> None:
        self._order_list_repo:OrderListRepo = order_list_repo
        
    def set_params(self, by_id:str):
        self._order_list_id = by_id
        
    def validate(self):
        try:
            int(self._order_list_id)
        except ValueError:
            raise ValidationError('The order list id is not valid.')
            
    def execute(self):
        return self._order_list_repo.get_element(self._order_list_id)