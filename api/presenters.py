from multiprocessing.connection import wait
from telnetlib import STATUS

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
    def __init__(self, get_all_offers_interactor):
        self.get_all_offers_interactor = get_all_offers_interactor

    def get(self):
        offers = self.get_all_offers_interactor.execute()
        body = []
        for element in offers:
            body.append(OfferSerializer.serialize(element))
        status = 200

        import logging
        logger = logging.getLogger("mylogger")
        logger.info(body)

        return body, status