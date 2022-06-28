class BaseOffer(object):
    def __init__(self, id: int, name: str, avaidable, price: int, addeds):
        self._id = id
        self._name = name
        self._avaidable = avaidable
        self._price = price
        self._addeds = []
        for add in addeds:
            if add.avaidable:
                self._addeds.append(add)

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
        
    @property
    def addeds(self):
        return self._addeds