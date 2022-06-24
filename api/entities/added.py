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