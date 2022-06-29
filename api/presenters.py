from .serializers import *
from .exception import EntityDoesNotExist, OfferAlreadyExist


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
            if len(error) > 0:
                raise Exception(error)

            self._manage_offers_interactor.set_params_base_offer(
                name=name, price=price, addeds=addeds)
            self._manage_offers_interactor.create_base_offer()
            status = 201
            return None, status
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

    def get(self, *args, **kwargs):
        self._manage_offers_interactor.set_params_base_offer(
            by_id=kwargs['id'])
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
            if request_body['id'] != None:
                id = request_body['id']
            if request_body['name'] != None:
                name = request_body['name']
            if request_body['available'] != None:
                available = request_body['available']
            if request_body['price'] != None:
                price = request_body['price']
            if request_body['addeds'] != None:
                addeds = request_body['addeds']

            self._manage_offers_interactor.set_params_base_offer(
                by_id=by_id, id=id, name=name, available=available, price=price, addeds=addeds)
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

    def get(self, *args, **kwargs):
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
            self._manage_offers_interactor.set_params_base_offer(
                name=name, available=available, price=price)
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

    def get(self, *args, **kwargs):
        self._manage_offers_interactor.set_params_added(by_id=kwargs['id'])
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
            if request_body['id'] != None:
                id = request_body['id']
            if request_body['name'] != None:
                name = request_body['name']
            if request_body['available'] != None:
                available = request_body['available']
            if request_body['price'] != None:
                price = request_body['price']
            self._manage_offers_interactor.set_params_added(
                by_id=by_id, id=id, name=name, available=available, price=price, addeds=addeds)
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
            error = {}
            if request_body['client'] != None:
                client_request = request_body['client']
            else:
                error['client'] = 'client is required'
            if request_body['orders'] != None:
                orders_request = request_body['orders']
            else:
                error['orders'] = 'orders is required'
            if request_body['date'] != None:
                date_request = request_body['date']
            else:
                error['date'] = 'date is required'
            if error != {}:
                raise Exception(error)

            error.clear()
            if client_request['ci'] != None:
                id_client = client_request['ci']
            else:
                error['client.ci'] = 'ci is required'
            if client_request['name'] != None:
                name_client = client_request['name']
            else:
                error['client.name'] = 'name is required'
            if client_request['address'] != None:
                address_client = client_request['address']
            else:
                error['client.address'] = 'address is required'

            self._client_info_interactor.set_params(
                ci=id_client, name=name_client, address=address_client)
            client = self._client_info_interactor.create()

            self._client_info_interactor.set_params(client.ci)
            client = self._client_info_interactor.get_element()
            self._make_order_interactor.set_params(
                client=client, date=date_request)
            order_list = self._make_order_interactor.create()

            orders = []

            for i, element in enumerate(orders_request):
                error.clear()
                if element['requested_offer'] != None:
                    requested_offer_order = element['requested_offer']
                else:
                    error['order[{}]'.format(
                        i)] = 'requested offer is required'
                if element['amount'] != None:
                    amount_order = element['amount']
                else:
                    error['order[{}]'.format(i)] = 'amount is required'
                if error != {}:
                    raise Exception(error)

                error.clear()
                if requested_offer_order['base_offer'] != None:
                    base_offer_requested_offer = requested_offer_order['base_offer']
                else:
                    error['order[{}].requested_offer.base_offer'.format(
                        i)] = 'base offer is required'
                if requested_offer_order['addeds'] != None:
                    addeds_requested_offer = requested_offer_order['addeds']
                else:
                    error['order[{}].requested_offer.addeds'.format(
                        i)] = 'addeds is required'
                if error != {}:
                    raise Exception(error)

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

                order = self._choosed_offer_interactor.set_params(
                    requested_offer=requested_offer, amount=amount_order, order_list=order_list)
                self._choosed_offer_interactor.create()
                # orders.append(order)

            status = 201
            return OrderListSerializer.serialize(order_list), status
        except OfferAlreadyExist as e:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = e.args
            status = 500
            return body, status


class OrderListDetailView(object):
    def __init__(self, see_my_order_interactor, update_state_interactor) -> None:
        self._see_my_order_interactor = see_my_order_interactor
        self._update_state_interactor = update_state_interactor

    def get(self, *args, **kwargs):
        self._see_my_order_interactor.set_params(kwargs['id'])
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
            if request_body['state'] != None:
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


class UserView(object):
    def __init__(self, manage_users_interactor) -> None:
        self._manage_users_interactor = manage_users_interactor

    def get(self, *args, **kwargs):
        users = self._manage_users_interactor.get_all()
        body = UserSerializer.serialize(users, many=True)
        status = 200
        return body, status

    def post(self, *args, **kwargs):
        try:
            error = {}
            request_body = args[0]
            if request_body['id'] != None:
                id = request_body['id']
            else:
                error['id'] = 'id is required'
            if request_body['username'] != None:
                username = request_body['username']
            else:
                error['username'] = 'username is required'
            if request_body['password'] != None:
                password = request_body['password']
            else:
                error['password'] = 'password is required'
            if error != {}:
                raise Exception(error)

            self._manage_users_interactor.set_params(
                username=username, password=password)
            self._manage_users_interactor.create()
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


class UserDetailView(object):
    def __init__(self, manage_users_interactor) -> None:
        self._manage_users_interactor = manage_users_interactor

    def get(self, *args, **kwargs):
        self._manage_users_interactor.set_params(by_id=kwargs['id'])
        user = self._manage_users_interactor.get_element()
        body = UserSerializer.serialize(user)
        status = 200
        return body, status

    def put(self, *args, **kwargs):
        try:
            self._manage_users_interactor.set_params(kwargs['id'])
            user = self._manage_users_interactor.get_element()
            id = user.id
            username = user.username
            password = user.password
            is_admin = user.is_admin

            request_body = args[0]
            if request_body['id'] != None:
                id = request_body['id']
            if request_body['username'] != None:
                username = request_body['username']
            if request_body['password'] != None:
                password = request_body['password']
            if request_body['is_admin'] != None:
                is_admin = request_body['is_admin']

            self._manage_users_interactor.set_params(
                kwargs['id'], id, username, password, is_admin)
            self._manage_users_interactor.update()
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

    def delete(self, *args, **kwargs):
        try:
            self._manage_users_interactor.set_params(kwargs['id'])
            self._manage_users_interactor.delete()
            return None, 204
        except EntityDoesNotExist as e:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = {'error': e.args[0]}
            status = 500
            return body, status


class GroupView(object):
    def __init__(self, manage_groups_interactor) -> None:
        self._manage_groups_interactor = manage_groups_interactor

    def get(self, *args, **kwargs):
        groups = self._manage_groups_interactor.get_all()
        body = GroupSerializer.serialize(groups, many=True)
        status = 200
        return body, status

    def post(self, *args, **kwargs):
        try:
            error = {}
            request_body = args[0]
            if request_body['id'] != None:
                id = request_body['id']
            else:
                error['id'] = 'id is required'
            if request_body['name'] != None:
                name = request_body['name']
            else:
                error['name'] = 'name is required'
            if request_body['users'] != None:
                users = request_body['users']
            else:
                error['users'] = 'users is required'
            if request_body['permissions'] != None:
                permissions = request_body['permissions']
            else:
                error['permissions'] = 'permissions is required'
            if error != {}:
                raise Exception(error)

            self._manage_groups_interactor.set_params(name, users, permissions)
            self._manage_groups_interactor.create()
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


class GroupDetailView(object):
    def __init__(self, manage_groups_interactor) -> None:
        self._manage_groups_interactor = manage_groups_interactor

    def get(self, *args, **kwargs):
        self._manage_groups_interactor.set_params(by_id=kwargs['id'])
        group = self._manage_groups_interactor.get_element()
        body = GroupSerializer.serialize(group)
        status = 200
        return body, status

    def put(self, *args, **kwargs):
        try:
            self._manage_groups_interactor.set_params(kwargs['id'])
            group = self._manage_groups_interactor.get_element()
            id = group.id
            name = group.name
            users = group.users
            permissions = group.permissions

            error = {}
            request_body = args[0]
            if request_body['id'] != None:
                id = request_body['id']
            if request_body['name'] != None:
                name = request_body['name']
            if request_body['users'] != None:
                users = request_body['users']
            if request_body['permissions'] != None:
                permissions = request_body['permissions']
            if error != {}:
                raise Exception(error)

            self._manage_groups_interactor.set_params(
                kwargs['id'], name, users, permissions)
            self._manage_groups_interactor.update()
            status = 200
            return None, status
        except OfferAlreadyExist:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = {'error': e.args[0]}
            status = 500
            return body, status

    def delete(self, *args, **kwargs):
        try:
            self._manage_groups_interactor.set_params(kwargs['id'])
            self._manage_groups_interactor.delete()
            return None, 204
        except EntityDoesNotExist as e:
            body = {'error': e.args[0]}
            status = 400
            return body, status
        except Exception as e:
            body = {'error': e.args[0]}
            status = 500
            return body, status


class PermissionView(object):
    def __init__(self, manage_permissions_interactor) -> None:
        self._manage_permissions_interactor = manage_permissions_interactor

    def get(self, *args, **kwargs):
        permissions = self._manage_permissions_interactor.get_all()
        body = PermissionSerializer.serialize(permissions, many=True)
        status = 200
        return body, status


class PermissionDetailView(object):
    def __init__(self, manage_permissions_interactor) -> None:
        self._manage_permissions_interactor = manage_permissions_interactor

    def get(self, *args, **kwargs):
        self._manage_permissions_interactor.set_params(by_id=kwargs['id'])
        permission = self._manage_permissions_interactor.get_element()
        body = PermissionSerializer.serialize(permission)
        status = 200
        return body, status
