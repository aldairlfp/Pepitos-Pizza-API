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

