from .serializers import BaseOfferSerializer, OfferSerializer
from .exception import EntityDoesNotExist, OfferAlreadyExist


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


class AllOffersView(object):
    def __init__(self, get_all_offers_interactor, post_offer_interactor):
        self._get_all_offers_interactor = get_all_offers_interactor
        self._post_offer_interactor = post_offer_interactor

    def get(self):
        offers = self._get_all_offers_interactor.execute()
        body = []
        for element in offers:
            body.append(OfferSerializer.serialize(element))
        status = 200
        return body, status

    def post(self, offer):
        self._post_offer_interactor.set_params(
            offer['id'], offer['base_offer'], offer['amount_added'], offer['price'])
        try:
            offer = self._post_offer_interactor.execute()
        except OfferAlreadyExist as e:
            body = {'error': e.args[0]}
            status = 400
        else:
            body = OfferSerializer.serialize(offer)
            status = 200
        return body, status