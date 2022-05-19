class GetBaseOffersInteractor(object):
    def __init__(self, base_offer_repo):
        self.base_offer_repo = base_offer_repo

    def execute(self):
        return self.base_offer_repo.get_base_offers()
