class Complaint(object):
    def __init__(self, id: int, text: str, client: Client) -> None:
        self._id = id
        self._text = text
        self._client = client