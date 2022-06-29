class Permission(object):
    def __init__(self, id:int, code:int, name:str) -> None:
        self._id = id
        self._code = code
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name