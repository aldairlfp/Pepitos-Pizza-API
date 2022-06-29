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


class RequestedOfferDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return RequestedOfferDatabaseRepo()


class OrderDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return OrderDatabaseRepo()


class ClientDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return ClientDatabaseRepo()


class OrderListDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return OrderListDatabaseRepo()


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


class RequestedOfferRepoFactory(object):

    @staticmethod
    def get():
        db_repo = RequestedOfferDatabaseRepoFactory.get()
        return RequestedOfferRepo(db_repo)


class OrderRepoFactory(object):

    @staticmethod
    def get():
        db_repo = OrderDatabaseRepoFactory.get()
        return OrderRepo(db_repo)


class ClientRepoFactory(object):

    @staticmethod
    def get():
        db_repo = ClientDatabaseRepoFactory.get()
        return ClientRepo(db_repo)


class OrderListRepoFactory(object):

    @staticmethod
    def get():
        db_repo = OrderListDatabaseRepoFactory.get()
        return OrderListRepo(db_repo)


class ManageOffersInteractorFactory(object):

    @staticmethod
    def get():
        base_offer_repo = BaseOfferRepoFactory.get()
        added_repo = AddedRepoFactory.get()
        return ManageOffersInteractor(base_offer_repo, added_repo)


class MakeOfferInteractorFactory(object):

    @staticmethod
    def get():
        requested_offer_repo = RequestedOfferRepoFactory.get()
        return MakeOfferInteractor(requested_offer_repo)


class ChoosedInteractorFactory(object):

    @staticmethod
    def get():
        order_repo = OrderRepoFactory.get()
        return ChoosedOfferInteractor(order_repo)


class MakeOrderInteractorFactory(object):

    @staticmethod
    def get():
        order_list_repo = OrderListRepoFactory.get()
        return MakeOrderInteractor(order_list_repo)


class ClientInfoInteractorFactory(object):

    @staticmethod
    def get():
        client_repo = ClientRepoFactory.get()
        return ClientInfoInteractor(client_repo)


class SeeOrdersInteractorFactory(object):

    @staticmethod
    def get():
        order_list_repo = OrderListRepoFactory.get()
        return SeeOrdersInteractor(order_list_repo)


class SeeMyOrderInteractorFactory(object):

    @staticmethod
    def get():
        order_repo = OrderListRepoFactory.get()
        return SeeMyOrdersInteractor(order_repo)
        
class UpdateOrderStateInteractorFactory(object):

    @staticmethod
    def get():
        order_list_repo = OrderListRepoFactory.get()
        return UpdateOrderStateInteractor(order_list_repo)


class BaseOfferViewFactory(object):

    @staticmethod
    def create():
        manage_offers_interactor = ManageOffersInteractorFactory.get()
        return BaseOfferView(manage_offers_interactor)


class BaseOfferDetailViewFactory(object):

    @staticmethod
    def create():
        manage_offers_interactor = ManageOffersInteractorFactory.get()
        return BaseOfferDetailView(manage_offers_interactor)


class AddedViewFactory(object):

    @staticmethod
    def create():
        manage_offers_interactor = ManageOffersInteractorFactory.get()
        return AddedView(manage_offers_interactor)


class AddedDetailViewFactory(object):

    @staticmethod
    def create():
        manage_offers_interactor = ManageOffersInteractorFactory.get()
        return AddedDetailView(manage_offers_interactor)


class OrderListViewFactory(object):

    @staticmethod
    def create():
        manage_offers_interactor = ManageOffersInteractorFactory.get()
        make_offer_interactor = MakeOfferInteractorFactory.get()
        client_info_interactor = ClientInfoInteractorFactory.get()
        choosed_offer_interactor = ChoosedInteractorFactory.get()
        see_orders_interactor = SeeOrdersInteractorFactory.get()
        see_my_order_interactor = SeeMyOrderInteractorFactory.get()
        make_order_interactor = MakeOrderInteractorFactory.get()
        return OrderListView(manage_offers_interactor, make_offer_interactor, client_info_interactor, choosed_offer_interactor, 
            see_orders_interactor, see_my_order_interactor, make_order_interactor)
            
class OrderListDetailViewFactory(object):

    @staticmethod
    def create():
        see_my_order_interactor = SeeMyOrderInteractorFactory.get()
        update_state_interactor = UpdateOrderStateInteractorFactory.get()
        return OrderListDetailView(see_my_order_interactor, update_state_interactor)
        
class AvailableOffersViewFactory(object):

    @staticmethod
    def create():
        manage_offers_interactor = ManageOffersInteractorFactory.get()
        return AvailableOffersView(manage_offers_interactor)
        
