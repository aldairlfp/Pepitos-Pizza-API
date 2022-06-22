class Group(object):
    def __init__(self, id, users, permissions) -> None:
        self._id = id
        self._users = users
        self._permissions = permissions

    @property
    def id(self):
        return self._id

    @property
    def users(self):
        return self._users