class RequestedOffer(object):
    def __init__(self, id: int, base_offer, addeds) -> None:
        self._id = id
        self._base_offer = base_offer
        self._addeds = addeds

    @property
    def id(self):
        return self._id

    @property
    def base_offer(self):
        return self._base_offer

    @property
    def addeds(self):
        return self._addeds