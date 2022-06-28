from .repositories import *
from .unit_repositories import *
from .presenters import *
from api.interactors.choosed_offer import *
from api.interactors.client_info import *
from api.interactors.make_offer import *
from api.interactors.make_order import *
from api.interactors.manage_groups import *
from api.interactors.manage_offers import *
from api.interactors.manage_permissions import *
from api.interactors.manage_users import *
from api.interactors.see_my_order import *
from api.interactors.see_orders import *
from api.interactors.update_order_state import *


class BaseOfferDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return BaseOfferDatabaseRepo()

class AddedDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return AddedDatabaseRepo()


class BaseOfferRepoFactory(object):

    @staticmethod
    def get():
        db_repo = BaseOfferDatabaseRepoFactory.get()
        return BaseOfferRepo(db_repo)

class AddedRepoFactory(object):
    
    @staticmethod
    def get():
        db_repo = AddedDatabaseRepoFactory.get()
        return AddedRepo(db_repo)

class ManageOffersInteractorFactory(object):
    
    @staticmethod
    def get():
        base_offer_repo = BaseOfferRepoFactory.get()
        added_repo = AddedRepoFactory.get()
        return ManageOffersInteractor(base_offer_repo, added_repo)

class BaseOfferViewFactory(object):

    @staticmethod
    def create():
        manage_offers_interactor = ManageOffersInteractorFactory.get()
        return BaseOfferView(manage_offers_interactor)
        
class AddedViewFactory(object):

    @staticmethod
    def create():
        manage_offers_interactor = ManageOffersInteractorFactory.get()
        return AddedView(manage_offers_interactor)
    
    
# class GetBaseOfferInteractorFactory(object):

#     @staticmethod
#     def get():
#         base_offer_repo = BaseOfferRepoFactory.get()
#         return GetBaseOffersInteractor(base_offer_repo)


# class BaseOfferViewFactory(object):

#     @staticmethod
#     def create():
#         get_base_offer_interactor = GetBaseOfferInteractorFactory.get()
#         return BaseOfferView(get_base_offer_interactor)


# class OfferDatabaseRepoFactory(object):

#     @staticmethod
#     def get():
#         return OfferDatabaseRepo()


# class OfferRepoFactory(object):

#     @staticmethod
#     def get():
#         db_repo = OfferDatabaseRepoFactory.get()
#         return OfferRepo(db_repo)


# class GetAllOffersInteractorFactory(object):

#     @staticmethod
#     def get():
#         offer_repo = OfferRepoFactory.get()
#         return GetAllOffersInteractor(offer_repo)


# class AllOffersViewFactory(object):

#     @staticmethod
#     def create():
#         get_all_offers_interactor = GetAllOffersInteractorFactory.get()
#         post_offer_interactor = PostOfferInteractorFactory().get()
#         return AllOffersView(get_all_offers_interactor, post_offer_interactor)


# class PostOfferInteractorFactory(object):

#     @staticmethod
#     def get():
#         offer_repo = OfferRepoFactory().get()
#         return CreateOfferInteractor(offer_repo)
