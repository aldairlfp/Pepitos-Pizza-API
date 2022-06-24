from django.forms import ValidationError

from .models import BaseOffer as BaseOfferORM
from .models import Offer as OfferORM
from .models import Added as AddedORM
from api.entities.added import *
from api.entities.client import *
from api.entities.complaint import *
from api.entities.group import *
from api.entities.offer import *
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
    def get_base_offers(self):
        orm_base_offers = BaseOfferORM.objects.all()
        return self._decode_orm_base_offers(orm_base_offers)

    def get_base_offer(self, id):
        orm_base_offer = BaseOfferORM.objects.get(pk=id)
        return self._decode_orm_base_offer(orm_base_offer)

    def _decode_orm_base_offers(self, orm_base_offers):
        base_offers_list = []
        for element in orm_base_offers:
            base_offer = self._decode_orm_base_offer(element)
            base_offers_list.append(base_offer)
        return base_offers_list

    def _decode_orm_base_offer(self, orm_base_offer):
        return BaseOffer(orm_base_offer.id, orm_base_offer.name, orm_base_offer.available)


class OfferDatabaseRepo(object):
    def get_offers(self):
        orm_offers = OfferORM.objects.all().order_by('base_offer__name')
        return DecodeORM.decode_orm_offers(orm_offers)

    def create_offer(self, id, base_offer, amount_added, price):
        orm_base_offer = BaseOfferORM.objects.get(pk=base_offer)
        orm_amount_added = AddedORM.objects.get(pk=amount_added)
        try:
            orm_offer = OfferORM(
                id=id, base_offer=orm_base_offer, amount_added=orm_amount_added, price=price)
            OfferORM.validate_unique(orm_offer)
        except ValidationError:
            raise OfferAlreadyExist("The offer already exist.")
        else:
            orm_offer.save()
        return DecodeORM.decode_orm_offer(orm_offer)
