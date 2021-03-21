# https://flask-restful.readthedocs.io/en/latest
from flask_restful import Api, reqparse, Resource
from.parser import integration_parser

class TodoItem(Resource):
    def get(self):
        return {'task': 'Say "Hello, World!"'}



class IntegrationAuthAPI(Resource):
    def get(self):
        return {'task': 'Say "Hello, World!"'}

    def post(self):
        args = integration_parser.parse_args()
        return {'task': 'Say "Hello, World!"'}
		