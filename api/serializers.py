from email.mime import base


class BaseOfferSerializer(object):

    @staticmethod
    def serialize(base_offer):
        return {
            'id': base_offer.id,
            'name': base_offer.name,
            'available': base_offer.available,
            'price': base_offer.price,
            'addeds': AddedSerializer.serialize(base_offer.addeds, many=True)
        }


class AddedSerializer(object):

    @staticmethod
    def serialize(added, many=False):
        if many:
            addeds_list = []
            for element in added:
                addeds_list.append({'id': element.id,
                                    'name': element.name,
                                    'available': element.available,
                                    'price': element.price})
            return addeds_list
        else:
            return {
                'id': added.id,
                'name': added.name,
                'available': added.available,
                'price': added.price
            }


class OfferSerializer(object):

    @staticmethod
    def serialize(offer):
        return {
            'id': offer.id,
            'base_offer': BaseOfferSerializer.serialize(offer.base_offer),
            'addeds': AddedSerializer.serialize(offer.addeds, many=True),
        }
