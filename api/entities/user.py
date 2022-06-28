class User(object):
    def __init__(self, id: int, username: str, password: str, is_admin: bool) -> None:
        self._id = id
        self._username = username
        self._password = password
        self._is_admin = is_admin

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def is_admin(self):
        return self._is_admin
