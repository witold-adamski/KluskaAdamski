class Movie:
    def __init__(self, movieId: int, title: str, genres: str):
        self._movieId = movieId
        self._title = title
        self._genres = genres

    @property
    def movieId(self) -> int:
        return self._movieId

    @property
    def title(self) -> str:
        return self._title

    @property
    def genres(self) -> str:
        return self._genres
