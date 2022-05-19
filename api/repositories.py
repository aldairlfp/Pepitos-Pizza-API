from .models import BaseOfferORM
from .entities import BaseOffer

class BaseOfferRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_base_offers(self):
        base_offers = self.__db_repo.get_base_offers()
        return base_offers

class BaseOfferDatabaseRepo(object):
    def get_base_offers(self):
        orm_base_offers = BaseOfferORM.objects.all()
        return self._decode_orm_base_offers(orm_base_offers)

    def _decode_orm_base_offers(self, orm_base_offers_query_set):
        base_offers_list = []
        for query_set in orm_base_offers_query_set:
            base_offer = BaseOffer(query_set.id, query_set.name, query_set.base_price)
            base_offers_list.append(base_offer)
        return base_offers_list
