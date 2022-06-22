class Client(object):
    def __init__(self, ci: int, name: str, address: str) -> None:
        self._ci = ci
        self._name = name
        self._address = address

    @property
    def ci(self):
        return self._ci

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address