class ManageOffersInteractor(object):
    def __init__(self, _base_offer_repo=None, added_repo=None) -> None:
        self._base_offer_repo = _base_offer_repo
        self._added_repo = added_repo

    def set_params_base_offer(self, by_id=None, id=None, name=None, available=None, price=None, addeds=None):
        self._by_id_base_offer = by_id
        self._id_base_offer = id
        self._name_base_offer = name
        self._available_base_offer = available
        self._price_base_offer = price
        self._addeds_base_offer = addeds

    def set_params_added(self, by_id=None, id=None, name=None, available=None, price=None):
        self._by_id_added = by_id
        self._id_added = id
        self._name_added = name
        self._available_added = available
        self._price_added = price

    def get_all_base_offers(self):
        return self._base_offer_repo.get_all()

    def get_element_base_offer(self):
        return self._base_offer_repo.get_element(self._by_id_base_offer)

    def get_all_addeds(self):
        return self._added_repo.get_all()

    def get_element_added(self):
        return self._added_repo.get_element(self._by_id_added)

    def create_base_offer(self):
        return self._base_offer_repo.create(self._id_base_offer, self._name_base_offer,
                                     self._available_base_offer, self._price_base_offer,
                                     self._addeds_base_offer)

    def create_added(self):
        return self._added_repo.create(
            self._id_added, self._name_added, self._available_added, self._price_added)

    def update_base_offer(self):
        return self._base_offer_repo.update(self._by_id_base_offer, self._id_base_offer, self._name_base_offer,
                                     self._available_base_offer, self._price_base_offer, self._addeds_base_offer)
                                     
    def update_added(self):
        return self._added_repo.update(self._by_id_added, self._id_added, self._name_added, self._available_added, self._price_added)
        
    def delete_base_offer(self):
        return self._base_offer_repo.delete(self._by_id_base_offer)
        
    def delete_added(self):
        return self._added_repo.delete(self._by_id_added)