import os

from flask_restful import Resource, Api
from flask import Flask, request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from
from flask_restx import Api, Resource
from werkzeug.datastructures import FileStorage
from  person_detection import get_results

UPLOAD_FOLDER = '/uploads'
app = Flask(__name__)
api = Api(app)
app.json_encoder = LazyJSONEncoder

upload_parser = api.parser()
upload_parser.add_argument('file',
                           location='files',
                           type=FileStorage)

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
            "route": '/main',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}
swagger = Swagger(app, template=swagger_template,
                  config=swagger_config)

@swag_from("hello_world.yml", methods=['GET'])
@app.route("/main")
def hello_world():
    return "Hello World!!!"


@api.route('/upload/')
@api.expect(upload_parser)
class UploadDemo(Resource):
    def post(self):
        args = upload_parser.parse_args()
        file = args.get('file')
        file.save(os.path.join('uploads/', file.filename))
        result = get_results('uploads/'+file.filename)
        os.remove('uploads/'+file.filename)
        return result

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
    app.run(debug=False, host ="0.0.0.0", port=port)
