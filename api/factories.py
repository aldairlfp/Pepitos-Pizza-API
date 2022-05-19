from .repositories import BaseOfferDatabaseRepo, BaseOfferRepo
from .interactors import GetBaseOffersInteractor
from .display import BaseOfferView

class BaseOfferDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return BaseOfferDatabaseRepo()

class BaseOfferFactory(object):

    @staticmethod
    def get():
        db_repo = BaseOfferDatabaseRepoFactory.get()
        return BaseOfferRepo(db_repo)

class GetBaseOfferInteractorFactory(object):

    @staticmethod
    def get():
        base_offer_repo = BaseOfferFactory.get()
        return GetBaseOffersInteractor(base_offer_repo)

class BaseOfferViewFactory(object):

    @staticmethod
    def create():
        get_base_offer_interactor = GetBaseOfferInteractorFactory.get()
        return BaseOfferView(get_base_offer_interactor)