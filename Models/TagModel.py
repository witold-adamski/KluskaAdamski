class Tag:
    def __init__(self, userId: int, movieId: int, tag: str, timestamp: int):
        self._userId = userId
        self._movieId = movieId
        self._tag = tag
        self._timestamp = timestamp

    @property
    def userId(self) -> int:
        return self._userId

    @property
    def movieId(self) -> int:
        return self._movieId

    @property
    def tag(self) -> str:
        return self._tag

    @property
    def timestamp(self) -> int:
        return self._timestamp
