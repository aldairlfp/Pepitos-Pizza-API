from .repositories import *

class BaseOfferRepo(object):
    def __init__(self, db_repo:BaseOfferDatabaseRepo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        base_offers = self.__db_repo.get_all()
        return base_offers

    def get_element(self, id:int):
        return self.__db_repo.get_element(id)

    def create(self, name:str, price:int, addeds:list):
        return self.__db_repo.create(name, price, addeds)

    def update(self, by_id:int, id:int, name:str, available:bool, price:int, addeds:list):
        return self.__db_repo.update(by_id, id, name, available, price, addeds)

    def delete(self, by_id:int):
        return self.__db_repo.delete(by_id)


class AddedRepo(object):
    def __init__(self, db_repo:AddedDatabaseRepo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        addeds = self.__db_repo.get_all()
        return addeds

    def get_element(self, id:int):
        return self.__db_repo.get_element(id)

    def create(self, name:str, price:int):
        return self.__db_repo.create(name, price)

    def update(self, by_id:int, id:int, name:str, available:bool, price:int):
        return self.__db_repo.update(by_id, id, name, available, price)

    def delete(self, by_id:int):
        return self.__db_repo.delete(by_id)


class RequestedOfferRepo(object):
    def __init__(self, db_repo:RequestedOfferDatabaseRepo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        return self.__db_repo.get_all()

    def get_element(self, id:int):
        return self.__db_repo.get_element(id)

    def create(self, base_offer:BaseOffer, addeds:list):
        return self.__db_repo.create(base_offer, addeds)

    def update(self, by_id:int, base_offer:BaseOffer, addeds:list):
        return self.__db_repo.create(by_id, base_offer, addeds)

    def delete(self, by_id:int):
        self.__db_repo.delete(by_id)


class OrderRepo(object):
    def __init__(self, db_repo:OrderDatabaseRepo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        return self.__db_repo.get_all()

    def get_element(self, id:int):
        return self.__db_repo.get_element(id)

    def create(self, requested_offer:RequestedOffer, amount:int, order_list:Order_List):
        return self.__db_repo.create(requested_offer, amount, order_list)

    def update(self, by_id:int, id:int, requested_offer:RequestedOffer, amount:int, order_list:OrderList):
        return self.__db_repo.update(by_id, id, requested_offer, amount, order_list)

    def delete(self, by_id:int):
        self.__db_repo.delete(by_id)


class ClientRepo(object):
    def __init__(self, db_repo:ClientDatabaseRepo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        return self.__db_repo.get_all()

    def get_element(self, id:int):
        return self.__db_repo.get_element(id)

    def create(self, id:str, name:str, address:str):
        return self.__db_repo.create(id, name, address)

    def update(self, by_id:str, id:str, name:str, address:str):
        return self.__db_repo.update(by_id, id, name, address)

    def delete(self, by_id:str):
        self.__db_repo.delete(by_id)


class OrderListRepo(object):
    def __init__(self, db_repo:OrderListDatabaseRepo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        return self.__db_repo.get_all()

    def get_element(self, id:str):
        return self.__db_repo.get_element(id)

    def create(self, id:str, client:str, date:str):
        return self.__db_repo.create(id, client, date)

    def update(self, by_id:str, id:str, client:str, date:str):
        return self.__db_repo.update(by_id, id, client, date)
    
    def update_state(self, by_id:str, state:str):
        return self.__db_repo.update_state(by_id, state)

    def delete(self, by_id:str):
        self.__db_repo.delete(by_id)
        
# TODO Type all the classes

class ComplaintRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        complaint = self.__db_repo.get_all()
        return complaint

    def get_element(self, id):
        return self.__db_repo.get_element(id)

    def create(self, text, client):
        return self.__db_repo.create(text, client)

    def update(self, by_id, id, text, client):
        return self.__db_repo.update(by_id, id, text, client)

    def delete(self, by_id):
        return self.__db_repo.delete(by_id)

class GroupRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        complaint = self.__db_repo.get_all()
        return complaint

    def get_element(self, id):
        return self.__db_repo.get_element(id)

    def create(self, name, users, permissions):
        return self.__db_repo.create(name, users, permissions)

    def update(self, by_id, id, name, users, permissions):
        return self.__db_repo.update(by_id, id, name, users, permissions)

    def delete(self, by_id):
        return self.__db_repo.delete(by_id)

class PermisionRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        complaint = self.__db_repo.get_all()
        return complaint

    def get_element(self, id):
        return self.__db_repo.get_element(id)

    def create(self, code, name):
        return self.__db_repo.create(code, name)

    def update(self, by_id, id, code, name):
        return self.__db_repo.update(by_id, id, code, name)

    def delete(self, by_id):
        return self.__db_repo.delete(by_id)

class ProductRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        complaint = self.__db_repo.get_all()
        return complaint

    def get_element(self, id):
        return self.__db_repo.get_element(id)

    def create(self, name, amount):
        return self.__db_repo.create(name, amount)

    def update(self, by_id, id, name, amount):
        return self.__db_repo.update(by_id, id, name, amount)

    def delete(self, by_id):
        return self.__db_repo.delete(by_id)

class UpgradeStoreRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        complaint = self.__db_repo.get_all()
        return complaint

    def get_element(self, id):
        return self.__db_repo.get_element(id)

    def create(self, date, products):
        return self.__db_repo.create(date, products)

    def update(self, by_id, id, date, products):
        return self.__db_repo.update(by_id, id, date, products)

    def delete(self, by_id):
        return self.__db_repo.delete(by_id)

class UserRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        complaint = self.__db_repo.get_all()
        return complaint

    def get_element(self, id):
        return self.__db_repo.get_element(id)

    def create(self, username, password, is_admin):
        return self.__db_repo.create(username, password, is_admin)

    def update(self, by_id, id, username, password, is_admin):
        return self.__db_repo.update(by_id, id, username, password, is_admin)

    def delete(self, by_id):
        return self.__db_repo.delete(by_id)
