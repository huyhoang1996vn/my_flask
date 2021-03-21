from .integration import TodoItem, IntegrationAuthAPI

def initialize_routes(api):
	api.add_resource(TodoItem, '/api')
	api.add_resource(IntegrationAuthAPI, '/api/integration/auth')
