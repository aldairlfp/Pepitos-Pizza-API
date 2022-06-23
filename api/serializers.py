class BaseOfferSerializer(object):

    @staticmethod
    def serialize(base_offer):
        return {
            'id': base_offer.id,
            'name': base_offer.name,
            'available': base_offer.available
        }


class AddedSerializer(object):

    @staticmethod
    def serialize(added):
        return {
            'id': added.id,
            'name': added.name,
        }

class AmountSerializer(object):

    @staticmethod
    def serialize(amount):
        return {
            'id': amount.id,
            'amount': amount.amount
        }

class AmmountAddedSerializer(object):

    @staticmethod
    def serialize(amount_added):
        return {
            'id': amount_added.id,
            'name': amount_added.added.name,
            'amount': amount_added.amount,
            'available': amount_added.available
        }


class OfferSerializer(object):

    @staticmethod
    def serialize(offer):
        return {
            'id': offer.id,
            'base_offer': BaseOfferSerializer.serialize(offer.base_offer),
            'added': AmmountAddedSerializer.serialize(offer.amount_added),
            'price': offer.price,
            'available': offer.available
        }
