class Group(object):
    def __init__(self, id, name, users, permissions) -> None:
        self._id = id
        self._name = name
        self._users = users
        self._permissions = permissions

    @property
    def id(self):
        return self._id
        
    @property
    def name(self):
        return self._name

    @property
    def users(self):
        return self._users
        
    @property
    def permissions(self):
        return self._permissions