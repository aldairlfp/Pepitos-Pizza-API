from ..unit_repositories import ClientRepo


class ClientInfoInteractor(object):
    def __init__(self, client_repo: ClientRepo) -> None:
        self._client_repo: ClientRepo = client_repo

    def set_params(self, by_id:str=None, ci:str=None, name:str=None, address:str=None):
        self._by_id = by_id
        self._ci = ci
        self._name = name
        self._address = address

    def get_all(self):
        return self._client_repo.get_all()

    def get_element(self):
        return self._client_repo.get_element(self._by_id)

    def create(self):
        return self._client_repo.create(self._ci, self._name, self._address)

    def update(self):
        return self._client_repo.update(self._by_id, self._ci, self._name, self._address)

    def delete(self):
        return self._client_repo.delete(self._by_id)
