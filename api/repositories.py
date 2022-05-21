from .models import BaseOffer as BaseOfferORM
from .models import Offer as OfferORM
from .entities import *
from .utils import *


class BaseOfferDatabaseRepo(object):
    def get_base_offers(self):
        orm_base_offers = BaseOfferORM.objects.all()
        return self._decode_orm_base_offers(orm_base_offers)

    def _decode_orm_base_offers(self, orm_base_offers_query_set):
        base_offers_list = []
        for element in orm_base_offers_query_set:
            base_offer = BaseOffer(
                element.id, element.name, element.base_price, element.available)
            base_offers_list.append(base_offer)
        return base_offers_list


class OfferDatabaseRepo(object):
    def get_all_offers(self):
        orm_offers = OfferORM.objects.all().order_by('base_offer__name')
        return decode_orm_offers(orm_offers)
    
    def create_offer(self, id, base_offer, amount_added, price):
        orm_offer = Offer.objects.create(id=id, base_offer=base_offer, amount_added=amount_added, price=price)
        return decode_orm_offer(orm_offer)
