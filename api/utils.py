from api.entities.base_offer import *
from api.entities.added import *
from api.entities.requested_offer import *


class DecodeORM(object):        
    @staticmethod
    def decode_orm_offers(orm_offers_query_set):
        offers_list = []
        for element in orm_offers_query_set:
            offers_list.append(DecodeORM.decode_orm_offer(element))
        return offers_list
    
    
    @staticmethod
    def decode_orm_base_offer(orm_base_offer):
        return BaseOffer(orm_base_offer.id, orm_base_offer.name)
    
    
    @staticmethod
    def decode_orm_added(orm_added):
        return Added(orm_added.id, orm_added.name)
    
    
    # @staticmethod
    # def decode_orm_amount(orm_amount):
    #     return Amount(orm_amount.id, orm_amount.amount)
    
    
    # @staticmethod
    # def decode_orm_amount_added(orm_amount_added):
    #     added = DecodeORM.decode_orm_added(orm_amount_added.added)
    #     amount = DecodeORM.decode_orm_amount(orm_amount_added.amount)
    #     return AmountAdded(orm_amount_added.id, added, amount)
    
    
    @staticmethod
    def decode_orm_offer(orm_offer):
        base_offer = DecodeORM.decode_orm_base_offer(orm_offer.base_offer)
        amount_added = DecodeORM.decode_orm_amount_added(orm_offer.amount_added)
        offer = RequestedOffer(orm_offer.id, base_offer, amount_added, orm_offer.price, orm_offer.available)
        return offer
    