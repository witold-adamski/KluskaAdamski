class Rating:
    def __init__(self,
                 userId: int,
                 movieId: int,
                 rating: float,
                 timestamp: int):
        self._userId = userId
        self._movieId = movieId
        self._rating = rating
        self._timestamp = timestamp

    @property
    def userId(self) -> int:
        return self._userId

    @property
    def movieId(self) -> int:
        return self._movieId

    @property
    def rating(self) -> float:
        return self._rating

    @property
    def timestamp(self) -> int:
        return self._timestamp
