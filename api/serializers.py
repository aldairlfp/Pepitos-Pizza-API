from .entities import BaseOffer

class BaseOfferSerializer(object):

    @staticmethod
    def serialize(base_offer: BaseOffer):
        return {
            'id': base_offer.id,
            'name': base_offer.name,
            'base_price': base_offer.base_price
        }