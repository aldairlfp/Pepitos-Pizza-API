from .repositories import BaseOfferDatabaseRepo, OfferDatabaseRepo
from .unit_repositories import BaseOfferRepo, OfferRepo
from .interactors import GetBaseOffersInteractor, GetAllOffersInteractor
from .presenters import BaseOfferView, AllOffersView

class BaseOfferDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return BaseOfferDatabaseRepo()

class BaseOfferRepoFactory(object):

    @staticmethod
    def get():
        db_repo = BaseOfferDatabaseRepoFactory.get()
        return BaseOfferRepo(db_repo)

class GetBaseOfferInteractorFactory(object):

    @staticmethod
    def get():
        base_offer_repo = BaseOfferRepoFactory.get()
        return GetBaseOffersInteractor(base_offer_repo)

class BaseOfferViewFactory(object):

    @staticmethod
    def create():
        get_base_offer_interactor = GetBaseOfferInteractorFactory.get()
        return BaseOfferView(get_base_offer_interactor)


class OfferDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return OfferDatabaseRepo()

class OfferRepoFactory(object):

    @staticmethod
    def get():
        db_repo = OfferDatabaseRepoFactory.get()
        return OfferRepo(db_repo)

class GetAllOffersInteractorFactory(object):

    @staticmethod
    def get():
        offer_repo = OfferRepoFactory.get()
        return GetAllOffersInteractor(offer_repo)

class AllOffersViewFactory(object):

    @staticmethod
    def create():
        get_all_offers_interactor = GetAllOffersInteractorFactory.get()
        return AllOffersView(get_all_offers_interactor)
