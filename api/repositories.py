from .models import BaseOffer as BaseOfferORM
from .models import Offer as OfferORM
from .entities import *


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
        return self._decode_orm_offers(orm_offers)

    def _decode_orm_offers(self, orm_offers_query_set):
        offers_list = []
        for element in orm_offers_query_set:
            offers_list.append(self._decode_orm_offer(element))
        return offers_list

    def _decode_orm_base_offer(self, orm_base_offer):
        return BaseOffer(orm_base_offer.id, orm_base_offer.name, orm_base_offer.base_price, orm_base_offer.available)

    def _decode_orm_added(self, orm_added):
        return Added(orm_added.id, orm_added.name, orm_added.available)

    def _decode_orm_amount(self, orm_amount):
        return Amount(orm_amount.id, orm_amount.amount)

    def _decode_orm_amount_added(self, orm_amount_added):
        added = self._decode_orm_added(orm_amount_added.added)
        amount = self._decode_orm_amount(orm_amount_added.amount)
        return AmountAdded(orm_amount_added.id, added, amount, orm_amount_added.price)

    def _decode_orm_offer(self, orm_offer):
        base_offer = self._decode_orm_base_offer(orm_offer.base_offer)
        amount_added = self._decode_orm_amount_added(orm_offer.amount_added)
        offer = Offer(orm_offer.id, base_offer, amount_added)
        return offer
