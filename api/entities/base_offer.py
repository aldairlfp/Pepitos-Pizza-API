class BaseOffer(object):
    def __init__(self, id: int, name: str, available: bool, price: int, addeds: list, url:str):
        self._id = id
        self._name = name
        self._available = available
        self._price = price
        self._addeds = addeds
        self._url = url

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

    @property
    def addeds(self):
        return self._addeds
        
    @property
    def url(self):
        return self._url