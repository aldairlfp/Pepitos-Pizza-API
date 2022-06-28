from calendar import prcal
from cgi import print_environ


class Added(object):
    def __init__(self, id: int, name: str, avaidable: bool, price: int):
        self._id = id
        self._name = name
        self._avaidable = avaidable
        self._price = price

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
        
    @property
    def avaidable(self):
        return self._avaidable
        
    @property
    def price(self):
        return self._price