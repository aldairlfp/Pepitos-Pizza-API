from .serializers import BaseOfferSerializer
from .utils import EntityDoesNotExist


class BaseOfferView(object):
    def __init__(self, get_base_offers_interactor) -> None:
        self.get_base_offers_interactor = get_base_offers_interactor

    def get(self):
        try:
            base_offers = self.get_base_offers_interactor.execute()
        except EntityDoesNotExist:
            body = {'error': 'Base Offer does not exist!'}
            status = 404
        else:
            body = []
            for element in base_offers:
                body.append(BaseOfferSerializer.serialize(element))
            status = 200
        return body, status