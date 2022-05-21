class BaseOffer(object):
    def __init__(self, id: int, name: str, base_price: int, available: bool):
        self._id = id
        self._name = name
        self._base_price = base_price
        self._available = available

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def base_price(self):
        return self._base_price

    @property
    def available(self):
        return self._available


class Added(object):
    def __init__(self, id: int, name: str, available: bool):
        self._id = id
        self._name = name
        self._available = available

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def available(self):
        return self._available


class Amount(object):
    def __init__(self, id: int, amount: int) -> None:
        self._id = id
        self._amount = amount

    @property
    def id(self):
        return self.id

    @property
    def amount(self):
        return self._amount


class AmountAdded(object):
    def __init__(self, id: int, added: Added, amount: Amount, price: int) -> None:
        self._id = id
        self._added = added
        self._amount = amount
        self._price = price

    @property
    def id(self):
        return self._id

    @property
    def added(self):
        return self._added

    @property
    def amount(self):
        return self._amount.amount

    @property
    def price(self):
        return self._price


class Offer(object):
    def __init__(self, id: int, base_offer: BaseOffer, amount_added: AmountAdded) -> None:
        self._id = id
        self._base_offer = base_offer
        self._amount_added = amount_added

    @property
    def id(self):
        return self._id

    @property
    def base_offer(self):
        return self._base_offer

    @property
    def amount_added(self):
        return self._amount_added


class Client(object):
    def __init__(self, ci: int, name: str, address: str) -> None:
        self._ci = ci
        self._name = name
        self._address = address

    @property
    def ci(self):
        return self._ci

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address


class Order(object):
    def __init__(self, offer: Offer, client: Client, amount: int) -> None:
        self._offer = offer
        self._client = client
        self._amount = amount

    @property
    def offer(self):
        return self._offer

    @property
    def client(self):
        return self._client

    @property
    def amount(self):
        return self._amount


class OrderList(object):
    def __init__(self, id: int, date: str, address: str, state: str, orders: list) -> None:
        self._id = id
        self._date = date
        self._address = address
        self._state = state
        self._orders = orders

    @property
    def id(self):
        return self._id

    @property
    def date(self):
        return self._date

    @property
    def address(self):
        return self.address

    @property
    def state(self):
        return self._state

    @property
    def orders(self):
        return self._orders


class Complaint(object):
    def __init__(self, id: int, text: str, client: Client) -> None:
        self._id = id
        self._text = text
        self._client = client


class Product(object):
    def __init__(self, id: int, name: str, amount: int) -> None:
        self._id = id
        self._name = name
        self._amount = amount

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def amount(self):
        return self._amount


class UpgradeStore(object):
    def __init__(self, id: int, date: str, products: list) -> None:
        self._id = id
        self._date = date
        self._products = products

    @property
    def id(self):
        return self._id

    @property
    def date(self):
        return self._date

    @property
    def products(self):
        return self._products

class User(object):
    def __init__(self, id:int, username:str, password:str, token:str, email:str=None) -> None:
        self._id = id
        self._username = username
        self._password = password
        self._token = token
        self._email = email
    
    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def token(self):
        return self._token

    @property
    def email(self):
        return self._email