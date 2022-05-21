from django.template import base
from api.entities import BaseOffer
from .serializers import BaseOfferSerializer, OfferSerializer
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


class AllOffersView(object):
    def __init__(self, get_all_offers_interactor, post_offer_interactor):
        self._get_all_offers_interactor = get_all_offers_interactor
        self._post_offer_interactor = post_offer_interactor

    def get(self):
        offers = self.get_all_offers_interactor.execute()
        body = []
        for element in offers:
            body.append(OfferSerializer.serialize(element))
        status = 200
        return body, status

    def post(self, id, base_offer, amount_added, price):
        self._post_offer_interactor.set_params(
            id, base_offer, amount_added, price)
        offer = self._post_offer_interactor.execute()
        body = offer
        status = 200
        return body, status
