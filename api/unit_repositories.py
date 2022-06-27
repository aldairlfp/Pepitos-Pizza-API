class BaseOfferRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        base_offers = self.__db_repo.get_all()
        return base_offers

    def get_element(self, id):
        return self.__db_repo.get_element(id)

    def create(self, id, name, available, price, addeds):
        return self.__db_repo.create(id, name, available, price, addeds)

    def update(self, by_id, id, name, available, price, addeds):
        return self.__db_repo.update(by_id, id, name, available, price, addeds)

    def delete(self, by_id):
        return self.__db_repo.delete(by_id)


class AddedRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        addeds = self.__db_repo.get_all()
        return addeds

    def get_element(self, id):
        return self.__db_repo.get_element(id)

    def create(self, id, name, available, price):
        return self.__db_repo.create(id, name, available, price)

    def update(self, by_id, id, name, available, price):
        return self.__db_repo.update(by_id, id, name, available, price)

    def delete(self, by_id):
        return self.__db_repo.delete(by_id)


class RequestedOfferRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        return self.__db_repo.get_all()

    def get_element(self, id):
        return self.__db_repo.get_element(id)

    def create(self, id, base_offer, addeds):
        return self.__db_repo.create(id, base_offer, addeds)

    def update(self, by_id, id, base_offer, addeds):
        return self.__db_repo.create(by_id, id, base_offer, addeds)

    def delete(self, by_id):
        self.__db_repo.delete(by_id)


class OrderRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        return self.__db_repo.get_all()

    def get_element(self, id):
        return self.__db_repo.get_element(id)

    def create(self, id, requested_offer, amount):
        return self.__db_repo.create(id, requested_offer, amount)

    def update(self, by_id, id, requested_offer, amount):
        return self.__db_repo.update(by_id, id, requested_offer, amount)

    def delete(self, by_id):
        self.__db_repo.delete(by_id)


class ClientRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        return self.__db_repo.get_all()

    def get_element(self, id):
        return self.__db_repo.get_element(id)

    def create(self, id, name, address):
        return self.__db_repo.create(id, name, address)

    def update(self, by_id, id, name, address):
        return self.__db_repo.update(by_id, id, name, address)

    def delete(self, by_id):
        self.__db_repo.delete(by_id)


class OrderListRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        return self.__db_repo.get_all()

    def get_element(self, id):
        return self.__db_repo.get_element(id)

    def create(self, id, client, orders, date, state):
        return self.__db_repo.create(id, client, date, state)

    def update(self, by_id, id, client, orders, date, state):
        return self.__db_repo.update(by_id, id, client, date, state)

    def delete(self, by_id):
        self.__db_repo.delete(by_id)

class ComplaintRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all(self):
        complaint = self.__db_repo.get_all()
        return complaint

    def get_element(self, id):
        return self.__db_repo.get_element(id)

    def create(self, id, text, client):
        return self.__db_repo.create(id, text, client)

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

    def create(self, id, name, users, permissions):
        return self.__db_repo.create(id, name, users, permissions)

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

    def create(self, id, code, name):
        return self.__db_repo.create(id, code, name)

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

    def create(self, id, name, amount):
        return self.__db_repo.create(id, name, amount)

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

    def create(self, id, date, products):
        return self.__db_repo.create(id, date, products)

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

    def create(self, id, username, password, is_admin):
        return self.__db_repo.create(id, username, password, is_admin)

    def update(self, by_id, id, username, password, is_admin):
        return self.__db_repo.update(by_id, id, username, password, is_admin)

    def delete(self, by_id):
        return self.__db_repo.delete(by_id)
