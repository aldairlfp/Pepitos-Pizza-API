from ..exception import ValidationError

class SeeMyOrdersInteractor(object):
    def __init__(self, order_list_repo) -> None:
        self._order_list_repo = order_list_repo
        
    def set_params(self, order_list_id):
        self._order_list_id = order_list_id
        
    def validate(self):
        try:
            int(self._order_list_id)
        except ValueError:
            raise ValidationError('The order list id is not valid.')
            
    def execute(self):
        return self._order_list_repo.get_element(self._order_list_id)