from flask import Flask
from flask_restful import Resource, Api
from service import FileService

app = Flask(__name__)
api = Api(app)


class MoviesController(Resource):
    def get(self):
        return FileService.getMovies()


class LinksController(Resource):
    def get(self):
        return FileService.getLinks()


class RatingsController(Resource):
    def get(self):
        return FileService.getRatings()


class TagsController(Resource):
    def get(self):
        return FileService.getTags()


api.add_resource(MoviesController, '/movies')
api.add_resource(LinksController, '/links')
api.add_resource(RatingsController, '/ratings')
api.add_resource(TagsController, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
