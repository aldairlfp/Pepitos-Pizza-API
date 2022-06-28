from django.forms import ValidationError

from .models import BaseOffer as BaseOfferORM
from .models import RequestedOffer as OfferORM
from .models import Added as AddedORM
from .models import Client as ClientORM
from .models import Order as OrderORM
from .models import RequestedOffer as RequestedOfferORM
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
    def get_all(self):
        orm_base_offers = BaseOfferORM.objects.all()
        return BaseOfferDatabaseRepo.decode_all(orm_base_offers)

    def get_element(self, id):
        orm_base_offer = BaseOfferORM.objects.get(pk=id)
        return BaseOfferDatabaseRepo.decode_element(orm_base_offer)

    @staticmethod
    def decode_all(orm_base_offers):
        base_offers_list = []
        for element in orm_base_offers:
            base_offer = BaseOfferDatabaseRepo.decode_element(element)
            base_offers_list.append(base_offer)
        return base_offers_list

    @staticmethod
    def decode_element(orm_base_offer):
        addeds = AddedDatabaseRepo.decode_all(orm_base_offer.addeds.all())
        return BaseOffer(orm_base_offer.id, orm_base_offer.name, orm_base_offer.available, orm_base_offer.price, addeds)

class AddedDatabaseRepo(object):
    def get_all(self):
        orm_addeds = AddedORM.objects.all()
        return AddedDatabaseRepo.decode_all(orm_addeds)
        
    def get_element(self, id):
        orm_added = AddedORM.objects.get(pk=id)
        return AddedDatabaseRepo.decode_element(orm_added)
    
    @staticmethod
    def decode_all(orm_addeds):
        addeds_list = []
        for element in orm_addeds:
            added = AddedDatabaseRepo.decode_element(element)
            addeds_list.append(added)
        return addeds_list

    @staticmethod
    def decode_element(orm_added):
        return Added(orm_added.id, orm_added.name, orm_added.available, orm_added.price)

class ClientDatabaseRepo(object):
    def get_all(self):
        orm_clients = ClientORM.objects.all()
        return ClientDatabaseRepo.decode_all(orm_clients)
        
    def get_element(self, id):
        orm_client = ClientORM.objects.get(pk=id)
        return ClientDatabaseRepo.decode_element(orm_client)
    
    @staticmethod
    def decode_all(orm_clients):
        client_list = []
        for element in orm_clients:
            client = ClientDatabaseRepo.decode_element(element)
            client_list.append(client)
        return client_list
            
    
    @staticmethod
    def decode_element(orm_client):
        return Client(orm_client.ci, orm_client.name, orm_client.address)
        

class OrderDatabaseRepo(object):
    def get_all(self):
        orm_orders = OrderORM.objects.all()
        return OrderDatabaseRepo.decode_all(orm_orders)
        
    def get_element(self, id):
        orm_order = OrderORM.objects.get(pk=id)
        return OrderDatabaseRepo.decode_element(orm_order)
    
    @staticmethod
    def decode_all(orm_orders):
        order_list = []
        for element in orm_orders:
            order = OrderDatabaseRepo.decode_element(element)
            order_list.append(order)
        return order_list
            
    
    @staticmethod
    def decode_element(orm_order):
        return Order(orm_order.offer, orm_order.client, orm_order.amount)
        

class RequestedOfferDatabaseRepo(object):
    def get_all(self):
        orm_requested_offers = RequestedOfferORM.objects.all()
        return RequestedOfferDatabaseRepo.decode_all(orm_requested_offers)
        
    def get_element(self, id):
        orm_requested_offer = RequestedOfferORM.objects.get(pk=id)
        return RequestedOfferDatabaseRepo.decode_element(orm_requested_offer)
    
    @staticmethod
    def decode_all(orm_requested_offers):
        requested_offer_list = []
        for element in orm_requested_offers:
            requested_offer = RequestedOfferDatabaseRepo.decode_element(element)
            requested_offer_list.append(requested_offer)
        return requested_offer_list
            
    
    @staticmethod
    def decode_element(orm_requested_offer):
        return RequestedOffer(orm_requested_offer.id, orm_requested_offer.base_offer, orm_requested_offer.addeds)

        
        