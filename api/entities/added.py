from calendar import prcal
from cgi import print_environ


class Added(object):
    def __init__(self, id: int, name: str, available: bool, price: int):
        self._id = id
        self._name = name
        self._available = available
        self._price = price

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
        
    @property
    def available(self):
        return self._available
        
    @property
    def price(self):
        return self._price