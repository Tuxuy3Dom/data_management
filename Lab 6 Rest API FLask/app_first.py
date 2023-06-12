# pip install Flask
from flask import Flask

from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class SimpleExample(Resource):
    def get(self):
        return {'message': 'Flask Rest API first APP'}

api.add_resource(SimpleExample, '/')

if __name__ == '__main__':
    app.run(debug=True)
    


