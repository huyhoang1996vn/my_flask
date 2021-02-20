from .integration import TodoItem

def initialize_routes(api):
	api.add_resource(TodoItem, '/api')