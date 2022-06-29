class EntityAlreadyExist(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class OfferAlreadyExist(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
class ValidationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)