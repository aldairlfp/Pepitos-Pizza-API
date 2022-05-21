class GetBaseOffersInteractor(object):
    def __init__(self, base_offer_repo):
        self.base_offer_repo = base_offer_repo

    def execute(self):
        return self.base_offer_repo.get_base_offers()

class GetAllOffersInteractor(object):
    def __init__(self, offer_repo) -> None:
        self.offer_repo = offer_repo

    def execute(self):
        return self.offer_repo.get_all_offers()

class PostOfferInteractor(object):
    def __init__(self, offer_repo) -> None:
        self._offer_repo = offer_repo
