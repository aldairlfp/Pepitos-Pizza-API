from ..unit_repositories import GroupRepo

class ManageGroupsInteractor(object):
    def __init__(self, group_repo: GroupRepo) -> None:
        self._group_repo:GroupRepo = group_repo

    def set_params(self, by_id:int=None, id:int=None, name:str=None, users:list=None, permissions:list=None):
        self._by_id = by_id
        self._id = id
        self._name = name
        self._users = users
        self._permissions = permissions

    def get_all(self):
        return self._group_repo.get_all()

    def get_element(self):
        return self._group_repo.get_element(self._by_id)

    def create(self):
        return self._group_repo.create(self._name,
                                self._users, self._permissions)

    def update(self):
        return self._group_repo.update(self._by_id, self._id,
                                self._name, self._users, self._permissions)

    def delete(self):
        return self._group_repo.delete(self._by_id)
