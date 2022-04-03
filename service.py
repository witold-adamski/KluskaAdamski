from Models.MovieModel import Movie
from Models.TagModel import Tag
from Models.LinkModel import Link
from Models.RatingModel import Rating


class FileService:
    @staticmethod
    def getMovies():
        movies: list[Movie.__dict__] = []
        with open("data/movies.csv", mode="r", encoding="utf-8") as movieFile:
            lines: list[str] = movieFile.readlines()[1:]
            for line in lines:
                lineSplit = line[0:-1].split(',')
                movies.append(Movie(lineSplit[0],
                                    lineSplit[1],
                                    lineSplit[2])
                              .__dict__)
        return movies

    @staticmethod
    def getTags():
        tags: list[Tag.__dict__] = []
        with open("data/tags.csv", mode="r", encoding="utf-8") as tagFile:
            lines: list[str] = tagFile.readlines()[1:]
            for line in lines:
                lineSplit = line[0:-1].split(',')
                tags.append(Tag(lineSplit[0],
                                lineSplit[1],
                                lineSplit[2],
                                lineSplit[3])
                            .__dict__)
        return tags

    @staticmethod
    def getLinks():
        links: list[Link.__dict__] = []
        with open("data/links.csv", mode="r", encoding="utf-8") as linkFile:
            lines: list[str] = linkFile.readlines()[1:]
            for line in lines:
                lineSplit = line[0:-1].split(',')
                links.append(Link(lineSplit[0],
                                  lineSplit[1],
                                  lineSplit[2])
                             .__dict__)
        return links

    @staticmethod
    def getRatings():
        ratings: list[Rating.__dict__] = []
        with open("data/ratings.csv",
                  mode="r",
                  encoding="utf-8") as ratingFile:
            lines: list[str] = ratingFile.readlines()[1:]
            for line in lines:
                lineSplit = line[0:-1].split(',')
                ratings.append(Rating(lineSplit[0],
                                      lineSplit[1],
                                      lineSplit[2],
                                      lineSplit[3])
                               .__dict__)
        return ratings
