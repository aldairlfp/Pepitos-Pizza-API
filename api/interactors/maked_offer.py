class RequestedOfferInteractor(object):
    def __init__(self, requested_offer_repo) -> None:
        self._requested_offer_repo = requested_offer_repo

    def set_params_requested_offer(self, by_id=None, id=None, base_offer=None, addeds=None):
        self._by_id = by_id
        self._id = id
        self._base_offer = base_offer
        self._addeds = addeds

    def get_all(self):
        return self._requested_offer_repo.get_all()

    def get_element(self, by_id):
        return self._requested_offer_repo.get_element(by_id)

    def create(self):
        self._requested_offer_repo.create(
            self._id, self._base_offer, self._addeds)

    def update(self):
        self._requested_offer_repo.update(
            self._by_id, self._id, self._base_offer, self._addeds)

    def delete(self):
        self._requested_offer_repo.delete(self._by_id)