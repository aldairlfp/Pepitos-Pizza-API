class ClientInfoInteractor(object):
    def __init__(self, client_repo) -> None:
        self._client_repo = client_repo
        
    def set_params(self, by_id=None, ci=None, name=None, address=None):
        self._by_id = by_id
        self._ci = ci
        self._name = name
        self._address = address
        
    def get_all(self):
        return self._client_repo.get_all()
        
    def get_element(self):
        return self._client_repo.get_element(self._by_id)
        
    def create(self):
        self._client_repo.create(self._ci, self._name, self._address)
        
    def update(self):
        self._client_repo.update(self._by_id, self._ci, self._name, self._address)
        
    def delete(self):
        self._client_repo.delete(self._by_id)