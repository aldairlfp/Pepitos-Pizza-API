class UpgradeStore(object):
    def __init__(self, id: int, date: str, products: list) -> None:
        self._id = id
        self._date = date
        self._products = products

    @property
    def id(self):
        return self._id

    @property
    def date(self):
        return self._date

    @property
    def products(self):
        return self._products