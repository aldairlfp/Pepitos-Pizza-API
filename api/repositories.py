from django.forms import ValidationError

from .models import BaseOffer as BaseOfferORM
from .models import RequestedOffer as OfferORM
from .models import Added as AddedORM
from api.entities.added import *
from api.entities.client import *
from api.entities.complaint import *
from api.entities.group import *
from api.entities.requested_offer import *
from api.entities.order_list import *
from api.entities.order import *
from api.entities.permission import *
from api.entities.product import *
from api.entities.upgrade_store import *
from api.entities.user import *
from api.entities.base_offer import *
from .exception import *
from .utils import *


class BaseOfferDatabaseRepo(object):
    def get_all(self):
        orm_base_offers = BaseOfferORM.objects.filter(available=True)
        return BaseOfferDatabaseRepo.decode_orm_base_offers(orm_base_offers)

    def get_element(self, id):
        orm_base_offer = BaseOfferORM.objects.get(pk=id)
        return BaseOfferDatabaseRepo.decode_orm_base_offer(orm_base_offer)

    def create(self, id, name, available, price, addeds):
        orm_base_offer = BaseOfferORM(
            id=id, name=name, price=price, available=available, addeds=addeds)
        orm_base_offer.save()
        return BaseOfferDatabaseRepo.decode_orm_base_offer(orm_base_offer)
        
    def update(self, by_id, id, name, available, price, addeds):
        orm_base_offer = BaseOfferORM.objects.get(pk=by_id)
        orm_base_offer.id = id
        orm_base_offer.name = name
        orm_base_offer.price = price
        orm_base_offer.available = available
        orm_base_offer.addeds = addeds
        orm_base_offer.save()
        return BaseOfferDatabaseRepo.decode_orm_base_offer(orm_base_offer)
        
    def delete(self, id):
        orm_base_offer = BaseOfferORM.objects.get(pk=id)
        orm_base_offer.delete()
        return BaseOfferDatabaseRepo.decode_orm_base_offer(orm_base_offer)

    @staticmethod
    def decode_orm_base_offers(orm_base_offers):
        base_offers_list = []
        for element in orm_base_offers:
            base_offer = BaseOfferDatabaseRepo.decode_orm_base_offer(element)
            base_offers_list.append(base_offer)
        return base_offers_list

    @staticmethod
    def decode_orm_base_offer(orm_base_offer):
        addeds = AddedDatabaseRepo.decode_orm_addeds(
            orm_base_offer.addeds.all())
        return BaseOffer(orm_base_offer.id, orm_base_offer.name, orm_base_offer.available, orm_base_offer.price, addeds)


class AddedDatabaseRepo(object):
    @staticmethod
    def decode_orm_addeds(orm_addeds):
        addeds_list = []
        for element in orm_addeds:
            added = AddedDatabaseRepo.decode_orm_added(element)
            addeds_list.append(added)
        return addeds_list

    @staticmethod
    def decode_orm_added(orm_added):
        return Added(orm_added.id, orm_added.name, orm_added.available, orm_added.price)
