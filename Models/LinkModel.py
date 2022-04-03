class Link:
    def __init__(self, movieId: int, imdbId: int, tmdbId: int):
        self._movieId = movieId
        self._imdbId = imdbId
        self._tmdbId = tmdbId

    @property
    def movieId(self) -> int:
        return self._movieId

    @property
    def imdbId(self) -> int:
        return self._imdbId

    @property
    def tmdbId(self) -> int:
        return self._tmdbId
