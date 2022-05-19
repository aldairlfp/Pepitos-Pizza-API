class BaseOffer(object):
    def __init__(self, id, name, base_price):
        self._id = id
        self._name = name
        self._base_price = base_price

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def base_price(self):
        return self._base_price