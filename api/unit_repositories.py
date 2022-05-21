class BaseOfferRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_base_offers(self):
        base_offers = self.__db_repo.get_base_offers()
        return base_offers

class OfferRepo(object):
    def __init__(self, db_repo) -> None:
        self.__db_repo = db_repo

    def get_all_offers(self):
        return self.__db_repo.get_all_offers()