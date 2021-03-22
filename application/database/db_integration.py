
from application.db_engine import  execute_db
from application.database import IntegrationAuth



def create(data):
	execute_db(IntegrationAuth.insert(), name='admin', token='admin@localhost')