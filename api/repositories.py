from http import client
from django.contrib.auth.models import User, Group, Permission

from django.contrib.auth.models import User, Group, Permission
from .models import BaseOffer as BaseOfferORM
from .models import OrderList as OrderListORM
from .models import Added as AddedORM
from .models import Client as ClientORM
from .models import Order as OrderORM
from .models import RequestedOffer as RequestedOfferORM
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
        orm_base_offers = BaseOfferORM.objects.all()
        return BaseOfferDatabaseRepo.decode_orm_all(orm_base_offers)

    def get_element(self, id):
        orm_base_offer = BaseOfferORM.objects.get(pk=id)
        return BaseOfferDatabaseRepo.decode_orm_element(orm_base_offer)

    def create(self, id, name, price, addeds):
        orm_base_offer = BaseOfferORM(
            id=id, name=name, price=price, addeds=addeds)
        orm_base_offer.save()
        return BaseOfferDatabaseRepo.decode_orm_element(orm_base_offer)
        
    def update(self, by_id, id, name, avaidable, price, addeds):
        orm_base_offer = BaseOfferORM.objects.get(pk=by_id)
        orm_base_offer.id = id
        orm_base_offer.name = name
        orm_base_offer.price = price
        orm_base_offer.avaidable = avaidable
        orm_base_offer.addeds = addeds
        orm_base_offer.save()
        return BaseOfferDatabaseRepo.decode_orm_element(orm_base_offer)
        
    def delete(self, id):
        orm_base_offer = BaseOfferORM.objects.get(pk=id)
        orm_base_offer.delete()
        return BaseOfferDatabaseRepo.decode_orm_element(orm_base_offer)

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
    def decode_orm_all(orm_base_offers):
        base_offers_list = []
        for element in orm_base_offers:
            base_offer = BaseOfferDatabaseRepo.decode_orm_element(element)
            base_offers_list.append(base_offer)
        return base_offers_list

    @staticmethod
    def decode_orm_element(orm_base_offer):
        addeds = AddedDatabaseRepo.decode_orm_all(
            orm_base_offer.addeds.all())
        return BaseOffer(orm_base_offer.id, orm_base_offer.name, orm_base_offer.avaidable, orm_base_offer.price, addeds)


class AddedDatabaseRepo(object):
    def get_all(self):
        orm_addeds = AddedORM.objects.all()
        return AddedDatabaseRepo.decode_orm_all(orm_addeds)

    def get_element(self, id):
        orm_added = AddedORM.objects.get(pk=id)
        return AddedDatabaseRepo.decode_orm_element(orm_added)

    def create(self, id, name, avaidable, price):
        orm_added = AddedORM(id, name, avaidable, price)
        return AddedDatabaseRepo.decode_orm_element(orm_added)
        
    def update(self, by_id, id, name, avaidable, price):
        orm_added = AddedORM.objects.get(pk=by_id)
        orm_added.id = id
        orm_added.name = name
        orm_added.price = price
        orm_added.avaidable = avaidable
        orm_added.save()
        return AddedDatabaseRepo.decode_orm_element(orm_added)
        
    def delete(self, id):
        orm_added = AddedORM.objects.get(pk=id)
        orm_added.delete()
        return AddedDatabaseRepo.decode_orm_element(orm_added)

    @staticmethod
    def decode_orm_all(orm_addeds):
        addeds_list = []
        for element in orm_addeds:
            added = AddedDatabaseRepo.decode_orm_element(element)
            addeds_list.append(added)
        return addeds_list

    @staticmethod
    def decode_orm_element(orm_added):
        addeds = AddedDatabaseRepo.decode_orm_all(
            orm_added.addeds.all())
        return Added(orm_added.id, orm_added.name, orm_added.avaidable, orm_added.price, addeds)

class ClientDatabaseRepo(object):
    def get_all(self):
        orm_clients = ClientORM.objects.all()
        return ClientDatabaseRepo.decode_all(orm_clients)
        
    def get_element(self, id):
        orm_client = ClientORM.objects.get(pk=id)
        return ClientDatabaseRepo.decode_element(orm_client)
    
    def create(self, id, name, price, addeds):
        orm_client = ClientORM(
            id=id, name=name, price=price, addeds=addeds)
        orm_client.save()
        return ClientDatabaseRepo.decode_orm_element(orm_client)
        
    def update(self, by_id, ci, name, address):
        orm_client = ClientORM.objects.get(pk=by_id)
        orm_client.ci = ci
        orm_client.name = name
        orm_client.address = address
        orm_client.save()
        return ClientDatabaseRepo.decode_orm_element(orm_client)
        
    def delete(self, id):
        orm_client = ClientORM.objects.get(pk=id)
        orm_client.delete()
        return ClientDatabaseRepo.decode_orm_element(orm_client)

    @staticmethod
    def decode_orm_all(orm_clients):
        clients_list = []
        for element in orm_clients:
            client = ClientDatabaseRepo.decode_orm_element(element)
            clients_list.append(client)
        return clients_list

    @staticmethod
    def decode_orm_element(orm_client):
        client = Client(orm_client.ci, orm_client.name, orm_client.address).save()
        return client    

class OrderDatabaseRepo(object):
    def get_all(self):
        orm_orders = OrderORM.objects.all()
        return OrderDatabaseRepo.decode_all(orm_orders)
        
    def get_element(self, id):
        orm_order = OrderORM.objects.get(pk=id)
        return OrderDatabaseRepo.decode_element(orm_order)
    
    
    def create(self, offer, client, amount, order_list):
        orm_client = ClientORM(
            client, offer, amount, order_list)
        orm_client.save()
        return OrderDatabaseRepo.decode_orm_element(orm_client)
    
    def update(self, by_id, offer, client, amount, order_list):
        orm_order = ClientORM.objects.get(pk=by_id)
        orm_order.offer = offer
        orm_order.client = client
        orm_order.amount = amount
        orm_order.order_list = order_list
        orm_order.save()
        return OrderDatabaseRepo.decode_orm_element(orm_order)
    
    @staticmethod
    def decode_orm_all(orm_orders):
        orders_list = []
        for element in orm_orders:
            order = ClientDatabaseRepo.decode_orm_element(element)
            orders_list.append(order)
        return orders_list

    @staticmethod
    def decode_orm_element(orm_order):
        client = ClientDatabaseRepo.decode_orm_all(orm_order.client.all())
        order_list = OrderListDatabaseRepo.decode_orm_all(orm_order.order_list.all())
        order = Order(client, orm_order.offer, orm_order.amount, order_list).save()
        return order    
    
class RequestedOfferDatabaseRepo(object):
    def get_all(self):
        orm_requested_offers = RequestedOfferORM.objects.all()
        return RequestedOfferDatabaseRepo.decode_orm_all(orm_requested_offers)

    def get_element(self, id):
        orm_requested_offer = RequestedOfferORM.objects.get(pk=id)
        return RequestedOfferDatabaseRepo.decode_orm_element(orm_requested_offer)

    def create(self, id, base_offer, addeds):
        orm_requested_offer = RequestedOfferORM(
            id, base_offer, addeds=addeds)
        orm_requested_offer.save()
        return RequestedOfferDatabaseRepo.decode_orm_element(orm_requested_offer)
        
    def update(self, by_id, id, base_offer, addeds):
        orm_requested_offer = RequestedOfferORM.objects.get(pk=by_id)
        orm_requested_offer.id = id
        orm_requested_offer.base_offer - base_offer
        orm_requested_offer.addeds = addeds
        orm_requested_offer.save()
        return RequestedOfferDatabaseRepo.decode_orm_element(orm_requested_offer)
        
    def delete(self, id):
        orm_requested_offer = RequestedOfferORM.objects.get(pk=id)
        orm_requested_offer.delete()
        return RequestedOfferDatabaseRepo.decode_orm_element(orm_requested_offer)

    @staticmethod
    def decode_orm_all(orm_requested_offers):
        requested_offers_list = []
        for element in orm_requested_offers:
            requested_offer = RequestedOfferDatabaseRepo.decode_orm_element(element)
            requested_offers_list.append(requested_offer)
        return requested_offers_list

    @staticmethod
    def decode_orm_element(orm_requested_offer):
        base_offer = BaseOfferDatabaseRepo.decode_orm_all(
            orm_requested_offer.base_offers.all())
        return RequestedOffer(orm_requested_offer.id, base_offer)

        
class OrderListDatabaseRepo(object):
    def get_all(self):
        orm_order_lists = OrderListORM.objects.all()
        return OrderListDatabaseRepo.decode_orm_all(orm_order_lists)

    def get_element(self, id):
        orm_order_list = OrderListORM.objects.get(pk=id)
        return OrderListDatabaseRepo.decode_orm_element(orm_order_list)

    def create(self, id, date, address, state_order):
        orm_order_list = OrderListORM(
            id, date, address, state_order)
        orm_order_list.save()
        return OrderListDatabaseRepo.decode_orm_element(orm_order_list)
        
    def update(self, by_id, id, date, address, state_order):
        orm_order_list = OrderListORM.objects.get(pk=by_id)
        orm_order_list.id = id
        orm_order_list.date = date
        orm_order_list.address = address
        orm_order_list.state_order = state_order
        orm_order_list.save()
        return OrderListDatabaseRepo.decode_orm_element(orm_order_list)
        
    def delete(self, id):
        orm_order_list = OrderListORM.objects.get(pk=id)
        orm_order_list.delete()
        return OrderListDatabaseRepo.decode_orm_element(orm_order_list)

    @staticmethod
    def decode_orm_all(orm_order_lists):
        order_lists_list = []
        for element in orm_order_lists:
            order_list = OrderListDatabaseRepo.decode_orm_element(element)
            order_lists_list.append(order_list)
        return order_lists_list

    @staticmethod
    def decode_orm_element(orm_order_list):
        return OrderList(orm_order_list.id, orm_order_list.date, orm_order_list.address, orm_order_list.state_order)
