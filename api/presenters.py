from api.models import BaseOffer
from .serializers import *
from .exception import EntityAlreadyExist, OfferAlreadyExist


class BaseOfferView(object):
    def __init__(self, manage_offers_interactor) -> None:
        self._manage_offers_interactor = manage_offers_interactor

    def get(self, *args, **kwargs):
        base_offers = self._manage_offers_interactor.get_all_base_offers()
        body = BaseOfferSerializer.serialize(base_offers, many=True)
        status = 200
        return body, status

    def post(self, req):
        try:
            error = []
            if 'name' in req:
                name = req['name']
            else:
                error.append('name is required')
            if 'price' in req:
                price = req['price']
            else:
                error.append('price is required')
            if 'addeds' in req:
                addeds = req['addeds']
            else:
                error.append('addeds is required')
            if 'url' in req:
                url = req['url']
            else:
                error.append('url is required')
            if len(error) > 0:
                raise Exception(error)

            self._manage_offers_interactor.set_params_base_offer(
                name=name, price=price, addeds=addeds, url=url)
            base_offer = self._manage_offers_interactor.create_base_offer()
            body = BaseOfferSerializer.serialize(base_offer)
            status = 201
            return body, status
        except OfferAlreadyExist as e:
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

    def get(self, id):
        self._manage_offers_interactor.set_params_base_offer(id)
        base_offer = self._manage_offers_interactor.get_element_base_offer()
        body = BaseOfferSerializer.serialize(base_offer)
        status = 200
        return body, status

    def put(self, req, by_id):
        try:
            self._manage_offers_interactor.set_params_base_offer(by_id)
            base_offer = self._manage_offers_interactor.get_element_base_offer()
            id = base_offer.id
            name = base_offer.name
            available = base_offer.available
            price = base_offer.price
            addeds = base_offer.addeds
            url = base_offer.url
            
            if ('id' in req and req[id] == base_offer.id) or ('name' in req and req['name'] == base_offer.name):
                raise EntityAlreadyExist('Base offer already exist')
            
            if 'id' in req:
                id = req['id']
            if 'name' in req:
                name = req['name']
            if 'available' in req:
                available = req['available']
            if 'price' in req:
                price = req['price']
            if 'addeds' in req:
                addeds = req['addeds']
            if 'url' in req:
                url = req['url']

            self._manage_offers_interactor.set_params_base_offer(
                by_id=by_id, id=id, name=name, available=available, price=price, addeds=addeds, url=url)
            base_offer = self._manage_offers_interactor.update_base_offer()
            body = BaseOfferSerializer.serialize(base_offer)
            status = 200
            return body, status
        except EntityAlreadyExist as e:
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
            base_offer = self._manage_offers_interactor.delete_base_offer()
            body = BaseOfferSerializer.serialize(base_offer)
            return body, 204
        except EntityAlreadyExist as e:
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

    def get(self, *args, **kwargs):
        addeds = self._manage_offers_interactor.get_all_addeds()
        body = AddedSerializer.serialize(addeds, many=True)
        status = 200
        return body, status

    def post(self, request_body):
        try:
            error = []
            if 'name' in request_body:
                name = request_body['name']
            else:
                error.append('name is required')
            if 'price' in request_body:
                price = request_body['price']
            else:
                error.append('price is required')
            if len(error) > 0:
                raise Exception(error)
            self._manage_offers_interactor.set_params_added(name=name,price=price)
            added = self._manage_offers_interactor.create_added()
            body = AddedSerializer.serialize(added)
            status = 201
            return body, status
        except OfferAlreadyExist as e:
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

    def get(self, id):
        self._manage_offers_interactor.set_params_added(id)
        added = self._manage_offers_interactor.get_element_added()
        body = AddedSerializer.serialize(added)
        status = 200
        return body, status

    def put(self, request_body, by_id):
        try:
            self._manage_offers_interactor.set_params_added(by_id)
            added = self._manage_offers_interactor.get_element_added()
            
            id = added.id
            name = added.name
            available = added.available
            price = added.price
            
            if ('id' in request_body and request_body[id] == added.id) or ('name' in request_body and request_body['name'] == added.name):
                raise EntityAlreadyExist('Added already exist')
            
            if 'id' in request_body:
                id = request_body['id']
            if 'name' in request_body:
                name = request_body['name']
            if 'available' in request_body:
                available = request_body['available']
            if 'price' in request_body:
                price = request_body['price']
                
            self._manage_offers_interactor.set_params_added(
                by_id=by_id, id=id, name=name, available=available, price=price)
            added = self._manage_offers_interactor.update_added()
            body = AddedSerializer.serialize(added)
            status = 200
            return body, status
        except EntityAlreadyExist as e:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = {'error': e.args[0]}
            status = 500
            return body, status

    def delete(self, id):
        try:
            self._manage_offers_interactor.set_params_added(by_id=id)
            self._manage_offers_interactor.delete_added()
            return None, 204
        except EntityAlreadyExist as e:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = {'error': e.args[0]}
            status = 500
            return body, status


class OrderListView(object):
    def __init__(self, manage_offers_interactor, make_offer_interactor, client_info_interactor, choosed_offer_interactor, see_orders_interactor, see_my_order_interactor, make_order_interactor) -> None:
        self._manage_offers_interactor = manage_offers_interactor
        self._make_offer_interactor = make_offer_interactor
        self._client_info_interactor = client_info_interactor
        self._choosed_offer_interactor = choosed_offer_interactor
        self._see_orders_interactor = see_orders_interactor
        self._see_my_order_interactor = see_my_order_interactor
        self._make_order_interactor = make_order_interactor

    def get(self, *args, **kwargs):
        orders = self._see_orders_interactor.execute()
        body = OrderListSerializer.serialize(orders, many=True)
        status = 200
        return body, status

    def post(self, request_body):
        try:
            error = []
            if 'id' in request_body:
                id = request_body['id']
            else:
                error.append('id is required')
            if 'client' in request_body:
                client = request_body['client']
            else:
                error.append('client is required')
            if 'orders'in request_body and len(request_body['orders']) > 0:
                orders = request_body['orders']
            else:
                error.append('orders is required')
            if 'date' in request_body:
                date = request_body['date']
            else:
                date = None
            if len(error):
                raise Exception(error)

            error.clear()
            if 'ci' in client:
                ci_client = client['ci']
            else:
                error.append('client.ci is required')
            if 'name' in client:
                name_client = client['name']
            else:
                error.append('client.name is required')
            if 'address' in client:
                address_client = client['address']
            else:
                error.append('client.address is required')

            for i, element in enumerate(orders):
                error.clear()
                if 'requested_offer' in element:
                    requested_offer_order = element['requested_offer']
                else:
                    error.append('order[{}].requested offer is required'.format(i))
                if 'amount' in element:
                    amount_order = element['amount']
                else:
                    error.append('order[{}].amount is required'.format(i))
                if len(error):
                    raise Exception(error)

                error.clear()
                if 'base_offer'in requested_offer_order:
                    base_offer_requested_offer = requested_offer_order['base_offer']
                else:
                    error.append('order[{}].requested_offer.base_offer is required'.format(i))
                if 'addeds' in requested_offer_order:
                    addeds_requested_offer = requested_offer_order['addeds']
                else:
                    error.append('order[{}].requested_offer.addeds is required'.format(i))
                if len(error) > 0:
                    raise Exception(error)
                    
                self._client_info_interactor.set_params(
                ci=ci_client, name=name_client, address=address_client)
                client = self._client_info_interactor.create()

            
                self._make_order_interactor.set_params(
                    client=client, date=date)
                order_list = self._make_order_interactor.create()

                self._manage_offers_interactor.set_params_base_offer(
                    by_id=base_offer_requested_offer)
                base_offer = self._manage_offers_interactor.get_element_base_offer()
                addeds = []
                for j in addeds_requested_offer:
                    self._manage_offers_interactor.set_params_added(by_id=j)
                    addeds.append(
                        self._manage_offers_interactor.get_element_added())

                self._make_offer_interactor.set_params(
                    base_offer=base_offer, addeds=addeds)
                requested_offer = self._make_offer_interactor.create()

                self._choosed_offer_interactor.set_params(
                    requested_offer=requested_offer, amount=amount_order, order_list=order_list)
                self._choosed_offer_interactor.create()

            status = 201
            return None, status
        except OfferAlreadyExist as e:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = e.args[0]
            status = 500
            return body, status


class OrderListDetailView(object):
    def __init__(self, see_my_order_interactor, update_state_interactor) -> None:
        self._see_my_order_interactor = see_my_order_interactor
        self._update_state_interactor = update_state_interactor

    def get(self, id):
        self._see_my_order_interactor.set_params(id)
        order_list = self._see_my_order_interactor.execute()
        body = OrderListSerializer.serialize(order_list)
        status = 200
        return body, status

    def put(self, request_body, pk):
        try:
            self._see_my_order_interactor.set_params(by_id=pk)
            order_list = self._see_my_order_interactor.execute()
            state = order_list.state
            
            error=[]
            if 'state' in request_body:
                state = request_body['state']
            else:
                error.append('state is required')
            if len(error) > 0:
                raise Exception(error)
                
            self._update_state_interactor.set_params(pk, state)
            order_list = self._update_state_interactor.execute()
            
            body = OrderListSerializer.serialize(order_list)
            status = 200
            return body, status
        except EntityAlreadyExist as e:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = {'error': e.args[0]}
            status = 500
            return body, status