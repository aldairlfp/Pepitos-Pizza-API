from matplotlib.style import available
from .serializers import *
from .exception import EntityDoesNotExist, OfferAlreadyExist


class BaseOfferView(object):
    def __init__(self, manage_offers_interactor) -> None:
        self._manage_offers_interactor = manage_offers_interactor

    def get(self):
        base_offers = self._manage_offers_interactor.get_all_base_offers()
        body = BaseOfferSerializer.serialize(base_offers, many=True)
        status = 200
        return body, status

    def post(self, request_body):
        try:
            id = request_body['id']
            name = request_body['name']
            available = request_body['available']
            price = request_body['price']
            addeds = request_body['addeds']
            self._manage_offers_interactor.set_params_base_offer(id=id, name=name, available=available, price=price, addeds=addeds)
            self._manage_offers_interactor.create_base_offer()
            status = 201
            return None, status
        except OfferAlreadyExist:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = {'error': e.args[0]}
            status = 500
            return body, status
            
class BaseOfferDetailView(object):
    def __init__(self, manage_offers_interactor) -> None:
        self._manage_offers_interactor = manage_offers_interactor

    def get(self, by_id):
        self._manage_offers_interactor.set_params_base_offer(by_id=by_id)
        base_offer = self._manage_offers_interactor.get_element_base_offer()
        body = BaseOfferSerializer.serialize(base_offer)
        status = 200
        return body, status

    def put(self, by_id, request_body):
        try:
            self._manage_offers_interactor.set_params_base_offer(by_id)
            base_offer = self._manage_offers_interactor.get_element_base_offer()
            id = base_offer.id
            name = base_offer.name
            available = base_offer.available
            price = base_offer.price
            addeds = base_offer.addeds
            if request_body.key('id') != None:
                id = request_body['id']
            if request_body.key('name') != None:
                name = request_body['name']
            if request_body.key('available') != None:
                available = request_body['available']
            if request_body.key('price') != None:
                price = request_body['price']
            if request_body.key('addeds') != None:
                addeds = request_body['addeds']
            self._manage_offers_interactor.set_params_base_offer(by_id=by_id, id=id, name=name, available=available, price=price, addeds=addeds)
            self._manage_offers_interactor.update_base_offer()
            status = 200
            return None, status
        except EntityDoesNotExist:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = {'error': e.args[0]}
            status = 500
            return body, status
            
    def delete(self, by_id):
        try:
            self._manage_offers_interactor.set_params_base_offer(by_id=by_id)
            self._manage_offers_interactor.delete_base_offer()
            return None, 204
        except EntityDoesNotExist as e:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = {'error': e.args[0]}
            status = 500
            return body, status
        
class AddedView(object):
    def __init__(self, manage_offers_interactor) -> None:
        self._manage_offers_interactor = manage_offers_interactor

    def get(self):
        addeds = self._manage_offers_interactor.get_all_addeds()
        body = BaseOfferSerializer.serialize(addeds, many=True)
        status = 200
        return body, status

    def post(self, request_body):
        try:
            id = request_body['id']
            name = request_body['name']
            available = request_body['available']
            price = request_body['price']
            self._manage_offers_interactor.set_params_base_offer(id=id, name=name, available=available, price=price)
            self._manage_offers_interactor.create_base_offer()
            status = 201
            return None, status
        except OfferAlreadyExist:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = {'error': e.args[0]}
            status = 500
            return body, status
            
class AddedDetailView(object):
    def __init__(self, manage_offers_interactor) -> None:
        self._manage_offers_interactor = manage_offers_interactor

    def get(self, by_id):
        self._manage_offers_interactor.set_params_added(by_id=by_id)
        added = self._manage_offers_interactor.get_element_added()
        body = AddedSerializer.serialize(added)
        status = 200
        return body, status

    def put(self, by_id, request_body):
        try:
            self._manage_offers_interactor.set_params_added(by_id)
            added = self._manage_offers_interactor.get_element_added()
            id = added.id
            name = added.name
            available = added.available
            price = added.price
            addeds = added.addeds
            if request_body.key('id') != None:
                id = request_body['id']
            if request_body.key('name') != None:
                name = request_body['name']
            if request_body.key('available') != None:
                available = request_body['available']
            if request_body.key('price') != None:
                price = request_body['price']
            self._manage_offers_interactor.set_params_added(by_id=by_id, id=id, name=name, available=available, price=price, addeds=addeds)
            self._manage_offers_interactor.update_added()
            status = 200
            return None, status
        except EntityDoesNotExist:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = {'error': e.args[0]}
            status = 500
            return body, status
            
    def delete(self, by_id):
        try:
            self._manage_offers_interactor.set_params_added(by_id=by_id)
            self._manage_offers_interactor.delete_added()
            return None, 204
        except EntityDoesNotExist as e:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = {'error': e.args[0]}
            status = 500
            return body, status

class RequestedOfferView(object):
    def __init__(self, manage_offers_interactor) -> None:
        self._manage_offers_interactor = manage_offers_interactor

    def get(self):
        requested_offers = self._manage_offers_interactor.get_all_requested_offers()
        body = RequestedOfferSerializer.serialize(requested_offers, many=True)
        status = 200
        return body, status

#TODO implement
    # def post(self, request_body):
    #     try:
    #         id = request_body['id']
    #         base_offer = request_body['base_offer']
    #         addeds = request_body['addeds']
    #         self._manage_offers_interactor.set_params_requested_offer(id=id, name=name, available=available, price=price)
    #         self._manage_offers_interactor.create_requested_offer()
    #         status = 201
    #         return None, status
    #     except OfferAlreadyExist:
    #         body = {'error': e.args[0]}
    #         status = 400
    #         return body, status
    #     except Exception as e:
    #         body = {'error': e.args[0]}
    #         status = 500
    #         return body, status