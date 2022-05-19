from .entities import *


class BaseOfferSerializer(object):

    @staticmethod
    def serialize(base_offer: BaseOffer):
        return {
            'id': base_offer.id,
            'name': base_offer.name,
            'base_price': base_offer.base_price,
            'available': base_offer.available
        }


class AddedSerializer(object):

    @staticmethod
    def serialize(added: Added):
        return {
            'id': added.id,
            'name': added.name,
            'available': added.available
        }


class AmmountAddedSerializer(object):

    @staticmethod
    def serialize(amount_added: AmountAdded):
        return {
            'id': amount_added.id,
            'name': amount_added.added.name,
            'amunt': amount_added.amount.amount,
            'available': amount_added.added.available,
            'price': amount_added.price
        }


class OfferSerializer(object):

    @staticmethod
    def serialize(offer: Offer):
        return {
            'id': offer.id,
            'base_offer': BaseOfferSerializer.serialize(offer.base_offer),
            'added': AmmountAddedSerializer.serialize(offer.amount_added)
        }
