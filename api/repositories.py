from django.forms import ValidationError
from .models import BaseOffer as BaseOfferORM
from .models import Offer as OfferORM
from .models import AmountAdded as AmountAddedORM
from .entities.entities import *
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
        orm_base_offer = BaseOfferORM.objects.get(pk=base_offer)
        orm_amount_added = AmountAddedORM.objects.get(pk=amount_added)
        try:
            orm_offer = OfferORM(
            id=id, base_offer=orm_base_offer, amount_added=orm_amount_added, price=price)
            OfferORM.validate_unique(orm_offer)
        except ValidationError:
            raise OfferAlreadyExist("The offer already exist.")
        else:
            orm_offer.save()
        return decode_orm_offer(orm_offer)
