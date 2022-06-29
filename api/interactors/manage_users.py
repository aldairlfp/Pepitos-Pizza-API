from ..unit_repositories import UserRepo

class ManageUsersInteractor(object):
    def __init__(self, user_repo:UserRepo) -> None:
        self._user_repo:UserRepo = user_repo

    def set_params(self, by_id:int=None, id:int=None, username:str=None, password:str=None, is_admin:bool=None):
        self._by_id = by_id
        self._id = id
        self._username = username
        self._password = password
        self._is_admin = is_admin

    def get_all(self):
        return self._user_repo.get_all()

    def get_element(self):
        return self._user_repo.get_element(self._by_id)

    def create(self):
        return self._user_repo.create(self._username,
                               self._password, self._is_admin)

    def update(self):
        return self._user_repo.update(self._by_id, self._id,
                               self._username, self._password, self._is_admin)

    def delete(self):
        return self._user_repo.delete(self._by_id)
