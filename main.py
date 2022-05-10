import os

from flask_restful import Resource, Api
from flask import Flask, request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)
api = Api(app)
app.json_encoder = LazyJSONEncoder


swagger_template = dict(
info = {
    'title': LazyString(lambda: 'My first Swagger UI document'),
    'version': LazyString(lambda: '0.1'),
    'description': LazyString(lambda: 'This document depicts a      sample Swagger UI document and implements Hello World functionality after executing GET.'),
    },
    host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'hello_world',
            "route": '/hello_world.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}
swagger = Swagger(app, template=swagger_template,
                  config=swagger_config)

@swag_from("hello_world.yml", methods=['GET'])
@app.route("/")
def hello_world():
    return "Hello World!!!"



# class MoviesController(Resource):
#     def get(self):
#         return FileService.getMovies()
#
#
# class LinksController(Resource):
#     def get(self):
#         return FileService.getLinks()
#
#
# class RatingsController(Resource):
#     def get(self):
#         return FileService.getRatings()
#
#
# class TagsController(Resource):
#     def get(self):
#         return FileService.getTags()
#
#
# api.add_resource(MoviesController, '/movies')
# api.add_resource(LinksController, '/links')
# api.add_resource(RatingsController, '/ratings')
# api.add_resource(TagsController, '/tags')

if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host ="0,0,0,0", port=port)
