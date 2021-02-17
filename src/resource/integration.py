from flask_restful import Resource, fields, marshal_with
from flask_restful import Api

api_integration = Api()


class TodoItem(Resource):
    def get(self):
        return {'task': 'Say "Hello, World!"'}

api_integration.add_resource(TodoItem, '/api')