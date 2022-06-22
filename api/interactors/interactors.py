class GetBaseOffersInteractor(object):
    def __init__(self, base_offer_repo):
        self.base_offer_repo = base_offer_repo

    def execute(self):
        return self.base_offer_repo.get_base_offers()

class OfferInteractor(object):
    def __init__(self, offer_repo) -> None:
        self._offer_repo = offer_repo


class GetAllOffersInteractor(OfferInteractor):
    def execute(self):
        return self._offer_repo.get_all_offers()


class CreateOfferInteractor(OfferInteractor):
    def set_params(self, id, base_offer_id, amount_added_id, price):
        self._id = id
        self._base_offer_id = base_offer_id
        self._amount_added_id = amount_added_id
        self._price = price

    def validate(self):
        if self._id < 1 or self._base_offer_id < 0 or self._amount_added_id < 0 or self._price < 0:
            raise ValidationError('The offer to create is not valid.')

    def execute(self):
        return self._offer_repo.create_offer(self._id, self._base_offer_id, self._amount_added_id, self._price)


class UpdateOfferInteractor(object):
    def __init__(self, offer_repo) -> None:
        self._offer_repo = offer_repo

    def set_params(self, offer_id_update, id, base_offer_id, amount_added_id, price):
        self._offer_id_update = offer_id_update
        self._id = id
        self._base_offer_id = base_offer_id
        self._amount_added_id = amount_added_id
        self._price = price

    def validate(self):
        if self._offer_id_update < 0:
            raise ValidationError('The offer to update is not valid.')
        if self._id < 1 or self._base_offer_id < 0 or self._amount_added_id < 0 or self._price < 0:
            raise ValidationError('The new offer is not valid.')

    def execute(self):
        return self._offer_repo.delete_by_id(self._offer)

class DeleteOfferInteractor(object):
    def __init__(self, offer_repo) -> None:
        self._offer_repo = offer_repo

    def set_params(self, offer_id_update, id, base_offer_id, amount_added_id, price):
        self._offer_id_update = offer_id_update
        self._id = id
        self._base_offer_id = base_offer_id
        self._amount_added_id = amount_added_id
        self._price = price

    def validate(self):
        if self._offer_id_update < 0:
            raise ValidationError('The offer to update is not valid.')
        if self._id < 1 or self._base_offer_id < 0 or self._amount_added_id < 0 or self._price < 0:
            raise ValidationError('The new offer is not valid.')

    def execute(self):
        return self._offer_repo.delete_by_id(self._offer)
