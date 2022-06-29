class BaseOfferSerializer(object):

    @staticmethod
    def serialize(base_offer, many=False):
        if many:
            base_offer_list = []
            for element in base_offer:
                base_offer_list.append(BaseOfferSerializer.serialize(element))
            return base_offer_list
        else:
            return {
                'id': base_offer.id,
                'name': base_offer.name,
                'price': base_offer.price,
                'addeds': AddedSerializer.serialize(base_offer.addeds, many=True)
            }


class AddedSerializer(object):

    @staticmethod
    def serialize(added, many=False):
        if many:
            addeds_list = []
            for element in added:
                addeds_list.append(AddedSerializer.serialize(element))
            return addeds_list
        else:
            return {
                'id': added.id,
                'name': added.name,
                'price': added.price
            }


class RequestedOfferSerializer(object):

    @staticmethod
    def serialize(offer, many=False):
        if many:
            requested_offer_list = []
            for element in offer:
                requested_offer_list.append(RequestedOfferSerializer.serialize(element))
            return requested_offer_list
        return {
            'id': offer.id,
            'base_offer': BaseOfferSerializer.serialize(offer.base_offer),
            'addeds': AddedSerializer.serialize(offer.addeds.all(), many=True),
        }

class ClientSerializer(object):
    
    @staticmethod
    def serialize(client, many=False):
        if many:
            client_list = []
            for element in client:
                client_list.append(ClientSerializer.serialize(element))
            return client_list
        return {
            'ci': client.ci,
            'name': client.name,
            'address': client.address
        }

class OrderSerializer(object):

    @staticmethod
    def serialize(order, many=False):
        if many:
            order_list = []
            for element in order:
                order_list.append(OrderSerializer.serialize(element))
            return order_list
        else:
            return {
                'id': order.id,
                'requested_offer': RequestedOfferSerializer.serialize(order.requested_offer),
                'amount': order.amount
            }
            
class OrderListSerializer(object):

    @staticmethod
    def serialize(order_list, many=False):
        if many:
            order_list_list = []
            for element in order_list:
                order_list_list.append(OrderListSerializer.serialize(element))
            return order_list_list
        else:
            return {
                'id': order_list.id,
                'client': ClientSerializer.serialize(order_list.client),
                'orders': OrderSerializer.serialize(order_list.orders, many=True),
                'date': order_list.date.__str__(),
                'state': order_list.state
            }

class UserSerializer(object):
    
    @staticmethod
    def serialize(user, many=False):
        if many:
            user_list = []
            for element in user:
                user_list.append(UserSerializer.serialize(element))
            return user_list
        return {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'is_admin': user.is_admin
        }
        
class PermissionSerializer(object):
    
    @staticmethod
    def serialize(permission, many=False):
        if many:
            permission_list = []
            for element in permission:
                permission_list.append(PermissionSerializer.serialize(element))
            return permission_list
        return {
            'id': permission.id,
            'code': permission.code,
            'name': permission.name
        }
        
class GroupSerializer(object):
    
    @staticmethod
    def serialize(group, many=False):
        if many:
            group_list = []
            for element in group:
                group_list.append(GroupSerializer.serialize(element))
            return group_list
        return {
            'id': group.id,
            'name': group.name,
            'permissions': PermissionSerializer(group.permissions, many=True)
        }