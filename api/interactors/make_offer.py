from ..entities.base_offer import BaseOffer

from ..unit_repositories import RequestedOfferRepo

class MakeOfferInteractor(object):
    def __init__(self, requested_offer_repo:RequestedOfferRepo) -> None:
        self._requested_offer_repo:RequestedOfferRepo = requested_offer_repo

    def set_params(self, by_id:int=None, id:int=None, base_offer:BaseOffer=None, addeds:list=None):
        self._by_id = by_id
        self._id = id
        self._base_offer = base_offer
        self._addeds = addeds

    def get_all(self):
        return self._requested_offer_repo.get_all()

    def get_element(self, by_id):
        return self._requested_offer_repo.get_element(by_id)

    def create(self):
        return self._requested_offer_repo.create(self._base_offer, self._addeds)

    def update(self):
        return self._requested_offer_repo.update(
            self._by_id, self._id, self._base_offer, self._addeds)

    def delete(self):
        return self._requested_offer_repo.delete(self._by_id)