from .models import BaseOffer as BaseOfferORM
from .entities import BaseOffer, Offer


class BaseOfferDatabaseRepo(object):
    def get_base_offers(self):
        orm_base_offers = BaseOfferORM.objects.all()
        return self._decode_orm_base_offers(orm_base_offers)

    def _decode_orm_base_offers(self, orm_base_offers_query_set):
        base_offers_list = []
        for query_set in orm_base_offers_query_set:
            base_offer = BaseOffer(
                query_set.id, query_set.name, query_set.base_price)
            base_offers_list.append(base_offer)
        return base_offers_list


class OfferDatabaseRepo(object):
    def get_all_offers(self):
        orm_offers = BaseOfferORM.objects.all()
        return self._decode_orm_offers(orm_offers)

    def _decode_orm_offers(self, orm_offers_query_set):
        offers_list = []
        for query_set in orm_offers_query_set:
            base_offer = BaseOffer(
                query_set.id, query_set.name, query_set.base_price, query_set.available)
            offer = Offer(query_set.id, base_offer, query_set.amount_added)
            offers_list.append(offer)
        return offers_list
