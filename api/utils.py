from .entities import *


class EntityDoesNotExist(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


@staticmethod
def decode_orm_offers(orm_offers_query_set):
    offers_list = []
    for element in orm_offers_query_set:
        offers_list.append(decode_orm_offer(element))
    return offers_list


@staticmethod
def decode_orm_base_offer(orm_base_offer):
    return BaseOffer(orm_base_offer.id, orm_base_offer.name, orm_base_offer.available)


@staticmethod
def decode_orm_added(orm_added):
    return Added(orm_added.id, orm_added.name)


@staticmethod
def decode_orm_amount(orm_amount):
    return Amount(orm_amount.id, orm_amount.amount)


@staticmethod
def decode_orm_amount_added(orm_amount_added):
    added = decode_orm_added(orm_amount_added.added)
    amount = decode_orm_amount(orm_amount_added.amount)
    return AmountAdded(orm_amount_added.id, added, amount, orm_amount_added.price, orm_amount_added.available)


@staticmethod
def decode_orm_offer(orm_offer):
    base_offer = decode_orm_base_offer(orm_offer.base_offer)
    amount_added = decode_orm_amount_added(orm_offer.amount_added)
    offer = Offer(orm_offer.id, base_offer, amount_added, orm_offer.price)
    return offer
