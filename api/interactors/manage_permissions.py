from ..unit_repositories import PermisionRepo

class ManagePermissions(object):
    def __ini__(self, permission_repo:PermisionRepo) -> None:
        self._permission_repo:PermisionRepo = permission_repo
        
    def set_params(self, by_id:int):
        self._by_id = by_id
        
    def get_all(self):
        return self._permission_repo.get_all()
        
    def get_element(self):
        return self._permission_repo.get_element(self._by_id)