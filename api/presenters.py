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

    def get(self, request, by_id):
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

class OrderView(object):
    def __init__(self, manage_offers_interactor, make_offer_interactor, client_info_interactor, choosed_offer_interactor, see_orders_interactor, see_my_order_interactor, make_order_interactor) -> None:
        self._manage_offers_interactor = manage_offers_interactor
        self._make_offer_interactor = make_offer_interactor
        self._client_info_interactor = client_info_interactor
        self._choosed_offer_interactor = choosed_offer_interactor
        self._see_orders_interactor = see_orders_interactor
        self._see_my_order_interactor = see_my_order_interactor
        self._make_order_interactor = make_order_interactor
    
    def get(self):
        orders = self._see_orders_interactor.get_all()
        body = OrderListSerializer.serialize(orders, many=True)
        status = 200
        return body, status
        
    def post(self, request_body):
        try:
            error = {}
            if request_body.key('id') != None:
                id_request = request_body['id']
            else:
                error['id'] = 'id is required'
            if request_body.key('client') != None:
                client_request = request_body['client']
            else:
                error['client'] = 'client is required'
            if request_body.key('orders') != None:
                orders_request = request_body['orders']
            else:
                error['orders'] = 'orders is required'
            if request_body.key('date') != None:
                date_request = request_body['date']
            else:
                error['date']= 'date is required'
            if request_body.key('state') != None:
                state_request = request_body['state']
            else:
                error['state'] = 'state is required'
            if error != {}:
                raise Exception(error)
                
            orders = []
            
            for element, i in enumerate(orders_request):
                error.clear()
                if element.key('id') != None:
                    id_order = element['id']
                else:
                    error['order[{}]'.format(i)] = 'id is required'
                if element.key('requested_offer') != None:
                    request_offer_order = request_body['requested_offer']
                else:
                    error['order[{}]'.format(i)] = 'requested offer is required'
                if request_body.key('amount') != None:
                    amount_order = request_body['amount']
                else:
                    error['order[{}]'.format(i)] = 'amount is required'
                if error != {}:
                    raise Exception(error)
                    
                error.clear()
                if request_offer_order.key('id') != None:
                    id_requested_offer = request_offer_order['id']
                else:
                    error['order[{}].requested_offer.id'.format(i)] = 'id is required'
                if request_offer_order.key('base_offer') != None:
                    base_offer_requested_offer = request_offer_order['base_offer']
                else:
                    error['order[{}].requested_offer.base_offer'.format(i)] = 'base offer is required'
                if request_offer_order.key('addeds') != None:
                    addeds_requested_offer = request_offer_order['addeds']
                else:
                    error['order[{}].requested_offer.addeds'.format(i)] = 'addeds is required'
                if error != {}:
                    raise Exception(error)
                    
                self._manage_offers_interactor.set_params_base_offer(by_id=base_offer_requested_offer)
                base_offer = self._manage_offers_interactor.get_element_base_offer()
                addeds = []
                for j in addeds_requested_offer:
                    self._manage_offers_interactor.set_params_addeds(by_id=j)
                    addeds.append(self._manage_offers_interactor.get_element_addeds())
                
                self._make_offer_interactor.set_params_choosed_offer(id=id_requested_offer, base_offer=base_offer, addeds=addeds)
                requested_offer = self._make_offer_interactor.create()
                
                order = self._choosed_offer_interactor.set_params_order(id=id_order, requested_offer=requested_offer, amount=amount_order)
                orders.append(order)
                
                
            error.clear()
            if client_request.key('ci') != None:
                id_client = client_request['ci']
            else:
                error['client.ci'] = 'ci is required'
            if client_request.key('name') != None:
                name_client = client_request['name']
            else:
                error['client.name'] = 'name is required'
            if client_request['address'] != None:
                address_client = client_request['address']
            else:
                error['client.address'] = 'address is required'
            
            self._client_info_interactor.set_params(id=id_client, name=name_client, address=address_client)
            client = self._client_info_interactor.create()
            
            self._make_order_interactor.set_params(id=id_request, client=client, orders=orders, date=date_request, state=state_request)
            self._make_order_interactor.create()
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
            
class OrderDetailView(object):
    def __init__(self, see_my_order_interactor, update_state_interactor) -> None:
        self._see_my_order_interactor = see_my_order_interactor
        self._update_state_interactor = update_state_interactor
        
    def get(self, request, pk):
        self._see_my_order_interactor.set_params(by_id=pk)
        order_list = self._see_my_order_interactor.execute()
        body = OrderListSerializer.serialize(order_list)
        status = 200
        return body, status
        
    def put(self, request_body, pk):
        try:
            self._see_my_order_interactor.set_params(by_id=pk)
            order_list = self._see_my_order_interactor.execute()
            
            # id = order_list.id
            # orders = order_list.orders
            # client = order_list.client
            # date = order_list.date
            state = order_list.state
            if request_body.key('state') != None:
                state = request_body['state']
            self._update_state_interactor.set_params(by_id=pk, state=state)
            order_list = self._update_state_interactor.execute()
            status = 200
            return OrderListSerializer.serialize(order_list), status
        except EntityDoesNotExist:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = {'error': e.args[0]}
            status = 500
            return body, status