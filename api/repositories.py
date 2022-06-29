import datetime

from django.contrib.auth.models import User as UserORM, Group as GroupORM, Permission as PermissionORM

from django.contrib.auth.models import User, Group, Permission
from .models import BaseOffer as BaseOfferORM, OrderList
from .models import OrderList as OrderListORM
from .models import Added as AddedORM
from .models import Client as ClientORM
from .models import Order as OrderORM
from .models import RequestedOffer as RequestedOfferORM
from api.entities.added import Added
from api.entities.client import Client
from api.entities.complaint import Complaint
from api.entities.group import Group
from api.entities.requested_offer import RequestedOffer
from api.entities.order_list import Order_List
from api.entities.order import Order
from api.entities.permission import Permission
from api.entities.product import Product
from api.entities.upgrade_store import UpgradeStore
from api.entities.user import User
from api.entities.base_offer import BaseOffer
from .exception import *
from .utils import *


class BaseOfferDatabaseRepo(object):
    def get_all(self):
        orm_base_offers = BaseOfferORM.objects.all()
        return BaseOfferDatabaseRepo.decode_orm_all(orm_base_offers)

    def get_element(self, id:int):
        orm_base_offer = BaseOfferORM.objects.get(pk=id)
        return BaseOfferDatabaseRepo.decode_orm_element(orm_base_offer)

    def create(self, name:str, price:str, addeds:list):
        orm_base_offer = BaseOfferORM(name=name, price=price)
        if len(BaseOfferORM.objects.filter(name=orm_base_offer.name, price=orm_base_offer.price)) == 0:
            orm_base_offer.save()
            for element in addeds:
                added = AddedORM.objects.get(pk=element)
                orm_base_offer.addeds.add(added)
            orm_base_offer.save()
        else:
            orm_base_offer = BaseOfferORM.objects.filter(name=orm_base_offer.name, price=orm_base_offer.price)[0]
        return BaseOfferDatabaseRepo.decode_orm_element(orm_base_offer)

    def update(self, by_id:int, id:int, name:str, available:bool, price:str, addeds:list):
        orm_base_offer = BaseOfferORM.objects.get(pk=by_id)
        orm_base_offer.id = id
        orm_base_offer.name = name
        orm_base_offer.price = price
        orm_base_offer.available = available
        for element in addeds:
            added = AddedORM.objects.get(pk=element)
            orm_base_offer.addeds.add(added)
        orm_base_offer.save()
        return BaseOfferDatabaseRepo.decode_orm_element(orm_base_offer)

    def delete(self, id:int):
        orm_base_offer = BaseOfferORM.objects.get(pk=id)
        orm_base_offer.delete()
        return BaseOfferDatabaseRepo.decode_orm_element(orm_base_offer)

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
        return BaseOffer(orm_base_offer.id, orm_base_offer.name, orm_base_offer.available, orm_base_offer.price, addeds)


class AddedDatabaseRepo(object):
    def get_all(self):
        orm_addeds = AddedORM.objects.all()
        return AddedDatabaseRepo.decode_orm_all(orm_addeds)

    def get_element(self, id:int):
        orm_added = AddedORM.objects.get(pk=id)
        return AddedDatabaseRepo.decode_orm_element(orm_added)

    def create(self, name:str, price:int):
        orm_added = AddedORM(name=name, price=price)
        orm_added.save()
        return AddedDatabaseRepo.decode_orm_element(orm_added)

    def update(self, by_id:int, id:int, name:int, available:bool, price:int):
        orm_added = AddedORM.objects.get(pk=by_id)
        orm_added.id = id
        orm_added.name = name
        orm_added.price = price
        orm_added.available = available
        orm_added.save()
        return AddedDatabaseRepo.decode_orm_element(orm_added)

    def delete(self, id:int):
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
        return Added(orm_added.id, orm_added.name, orm_added.available, orm_added.price)


class RequestedOfferDatabaseRepo(object):
    def get_all(self):
        orm_requested_offers = RequestedOfferORM.objects.all()
        return RequestedOfferDatabaseRepo.decode_orm_all(orm_requested_offers)

    def get_element(self, id:int):
        orm_requested_offer = RequestedOfferORM.objects.get(pk=id)
        return RequestedOfferDatabaseRepo.decode_orm_element(orm_requested_offer)

    def create(self, base_offer:BaseOffer, addeds:list):
        base_offer_orm = BaseOfferORM.objects.get(pk=base_offer.id)
        orm_requested_offer = RequestedOfferORM(base_offer=base_offer_orm)
        orm_requested_offer.save()
        for element in addeds:
            added = AddedORM.objects.get(pk=element.id)
            orm_requested_offer.addeds.add(added)
        orm_requested_offer.save()
        return RequestedOfferDatabaseRepo.decode_orm_element(orm_requested_offer)

    def update(self, by_id:int, id:int, base_offer:BaseOffer, addeds:list):
        orm_requested_offer = RequestedOfferORM.objects.get(pk=by_id)
        orm_requested_offer.id = id
        orm_requested_offer.base_offer = base_offer
        orm_requested_offer.addeds = addeds
        orm_requested_offer.save()
        return RequestedOfferDatabaseRepo.decode_orm_element(orm_requested_offer)

    def delete(self, id:int):
        orm_requested_offer = RequestedOfferORM.objects.get(pk=id)
        orm_requested_offer.delete()
        return RequestedOfferDatabaseRepo.decode_orm_element(orm_requested_offer)

    @staticmethod
    def decode_orm_all(orm_requested_offers):
        requested_offers_list = []
        for element in orm_requested_offers:
            requested_offer = RequestedOfferDatabaseRepo.decode_orm_element(
                element)
            requested_offers_list.append(requested_offer)
        return requested_offers_list

    @staticmethod
    def decode_orm_element(orm_requested_offer):
        base_offer = BaseOfferDatabaseRepo.decode_orm_element(
            orm_requested_offer.base_offer)
        addeds = AddedDatabaseRepo.decode_orm_all(
            orm_requested_offer.addeds.all())
        return RequestedOffer(orm_requested_offer.id, base_offer, addeds)


class OrderDatabaseRepo(object):
    def get_all(self):
        orm_orders = OrderORM.objects.all()
        return OrderDatabaseRepo.decode_all(orm_orders)

    def get_element(self, id:int):
        orm_order = OrderORM.objects.get(pk=id)
        return OrderDatabaseRepo.decode_element(orm_order)

    def create(self, requested_offer:RequestedOffer, amount:int, order_list:OrderList):
        orm_requested_offer = RequestedOfferORM.objects.get(pk=requested_offer.id)
        orm_order_list = OrderListORM.objects.get(pk=order_list.id)
        orm_order = OrderORM(requested_offer=orm_requested_offer,
                          amount=amount, order_list=orm_order_list)
        orm_order.save()
        return OrderDatabaseRepo.decode_orm_element(orm_order)

    def update(self, by_id:int, id:int, requested_offer:RequestedOffer, amount:int, order_list:Order_List):
        orm_order = OrderORM.objects.get(pk=by_id)
        orm_order.id = id
        orm_order.requested_offer = requested_offer
        orm_order.amount = amount
        orm_order.order_list = order_list
        orm_order.save()
        return OrderDatabaseRepo.decode_orm_element(orm_order)
        
    def delete(self, id:int):
        orm_order = OrderORM.objects.get(pk=id)
        orm_order.delete()
        return OrderDatabaseRepo.decode_orm_element(orm_order)

    @staticmethod
    def decode_orm_all(orm_orders):
        orders_list = []
        for element in orm_orders:
            order = OrderDatabaseRepo.decode_orm_element(element)
            orders_list.append(order)
        return orders_list

    @staticmethod
    def decode_orm_element(orm_order):
        requested_offer = RequestedOfferDatabaseRepo.decode_orm_element(
            orm_order.requested_offer)
        order = Order(orm_order.id, requested_offer=requested_offer,
                      amount=orm_order.amount)
        return order


class ClientDatabaseRepo(object):
    def get_all(self):
        orm_clients = ClientORM.objects.all()
        return ClientDatabaseRepo.decode_all(orm_clients)

    def get_element(self, id:int):
        orm_client = ClientORM.objects.get(pk=id)
        return ClientDatabaseRepo.decode_orm_element(orm_client)

    def create(self, ci:str, name:str, address:str):
        orm_client = ClientORM(
            ci=ci, name=name, address=address)
        if orm_client.DoesNotExist:
            orm_client.save()
        return ClientDatabaseRepo.decode_orm_element(orm_client)

    def update(self, by_id:str, ci:str, name:str, address:str):
        orm_client = ClientORM.objects.get(pk=by_id)
        orm_client.ci = ci
        orm_client.name = name
        orm_client.address = address
        orm_client.save()
        return ClientDatabaseRepo.decode_orm_element(orm_client)

    def delete(self, id:str):
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
        client = Client(orm_client.ci, orm_client.name, orm_client.address)
        return client


class OrderListDatabaseRepo(object):
    def get_all(self):
        orm_order_lists = OrderListORM.objects.all()
        return OrderListDatabaseRepo.decode_orm_all(orm_order_lists)

    def get_element(self, id:str):
        orm_order_list = OrderListORM.objects.get(pk=id)
        return OrderListDatabaseRepo.decode_orm_element(orm_order_list)

    def create(self, id:str, client:Client, date:str=None):
        client_orm = ClientORM.objects.get(pk=client.ci)
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") 
        orm_order_list = OrderListORM(id=id, date=date, client=client_orm)
        orm_order_list.save()
        return OrderListDatabaseRepo.decode_orm_element(orm_order_list)

    def update(self, by_id:str, id:str, client:Client, date:str):
        orm_order_list = OrderListORM.objects.get(pk=by_id)
        orm_order_list.id = id
        orm_order_list.client = client
        orm_order_list.date = date
        orm_order_list.save()
        return OrderListDatabaseRepo.decode_orm_element(orm_order_list)
        
    def update_state(self, by_id:str, state:str):
        orm_order_list = OrderListORM.objects.get(pk=by_id)
        orm_order_list.state_order = state
        orm_order_list.save()
        return OrderListDatabaseRepo.decode_orm_element(orm_order_list)
        
    def delete(self, id:str):
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
        client = ClientDatabaseRepo.decode_orm_element(orm_order_list.client)
        orders = OrderDatabaseRepo.decode_orm_all(orm_order_list.order_set.all())
        date = orm_order_list.date
        return Order_List(orm_order_list.id, client, orders, date, orm_order_list.state_order)
        
class UserDatabaseRepo(object):
    def get_all(self):
        orm_users = UserORM.objects.all()
        return UserDatabaseRepo.decode_orm_all(orm_users)

    def get_element(self, id:int):
        orm_user = UserORM.objects.get(pk=id)
        return UserDatabaseRepo.decode_orm_element(orm_user)

    def create(self, username:str, password:str, is_admin:bool):
        orm_user = UserORM(username=username, password=password, is_admin=is_admin)
        orm_user.save()
        return UserDatabaseRepo.decode_orm_element(orm_user)

    def update(self, by_id:int, id:int, username:str, password:str, is_admin:bool):
        orm_user = UserORM.objects.get(pk=by_id)
        orm_user.id = id 
        orm_user.username = username
        orm_user.password = password
        orm_user.is_admin = is_admin
        orm_user.save()
        return UserDatabaseRepo.decode_orm_element(orm_user)

    def delete(self, id:int):
        orm_user = UserORM.objects.get(pk=id)
        orm_user.delete()
        return UserDatabaseRepo.decode_orm_element(orm_user)

    @staticmethod
    def decode_orm_all(orm_users):
        users_list = []
        for element in orm_users:
            user = UserDatabaseRepo.decode_orm_element(element)
            users_list.append(user)
        return users_list

    @staticmethod
    def decode_orm_element(orm_user):
        user = User(orm_user.username, orm_user.password)
        return user
        
class GroupDatabaseRepo(object):
    def get_all(self):
        orm_groups = GroupORM.objects.all()
        return GroupDatabaseRepo.decode_orm_all(orm_groups)

    def get_element(self, id:int):
        orm_group = GroupORM.objects.get(pk=id)
        return GroupDatabaseRepo.decode_orm_element(orm_group)

    def create(self, id:int, name:str):
        orm_group = GroupORM(id=id, name=name)
        orm_group.save()
        return GroupDatabaseRepo.decode_orm_element(orm_group)

    def update(self, by_id:int, id:int, name:str):
        orm_group = GroupORM.objects.get(pk=by_id)
        orm_group.id = id
        orm_group.name = name
        orm_group.save()
        return GroupDatabaseRepo.decode_orm_element(orm_group)

    def delete(self, id:int):
        orm_group = GroupORM.objects.get(pk=id)
        orm_group.delete()
        return GroupDatabaseRepo.decode_orm_element(orm_group)

    @staticmethod
    def decode_orm_all(orm_groups):
        groups_list = []
        for element in orm_groups:
            group = GroupDatabaseRepo.decode_orm_element(element)
            groups_list.append(group)
        return groups_list

    @staticmethod
    def decode_orm_element(orm_group):
        group = Group(orm_group.id, orm_group.name)
        return group