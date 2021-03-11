# https://docs.sqlalchemy.org/en/13/
from sqlalchemy import create_engine, text
from flask import current_app, g
import click
from flask.cli import with_appcontext

engine = create_engine('postgresql+psycopg2://postgres:postgres@127.0.0.1:5444/flask')

def connect_engine(DATABASE_URI):
	return create_engine(DATABASE_URI, echo=True, pool_size=20, max_overflow=0)

# def connect_db():
# 	g.db = db_engine.connect_engine().connect()

def execute_db(*args, **kwargs):
    print ('=== execute_db')
    if "db" not in g:
        print ('=== execute_db db not in g')
        g.db = connect_engine(current_app.config['DATABASE_URI']).connect()
    return g.db.execute(*args, **kwargs)

def execute_string(command):
    print ('=== execute_string')
    if "db" not in g:
        print ('=== execute_string db not in g')
        g.db = connect_engine(current_app.config['DATABASE_URI']).connect()
    return g.db.execute(command)

def init_db():
    with engine.connect() as con:
        file = open("application/sql/init.sql")
        query = text(file.read())
        con.execute(query)

@click.command('migrate')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')    

def init_app(app):
    print ('==== init app')
    #     print '==== init app'
#     app.db = connect_engine().connect()
    # app.config['postgreSQL_pool'] = connect_db()
    # app.teardown_appcontext()
    app.cli.add_command(init_db_command)    




# class PostgresConnection(object):

#     def __init__(self):
#         self.connection = None

#     def init_app(self, app):
#         self.connection = psycopg2.connect("...")

#         @app.teardown_appcontext
#         def close_connection(response_or_exception):
#             self.connection.close()
#             return response_or_exception

#     def get_cursor(self):
#         if not self.connection:
#             raise RuntimeError('Attempt to get_cursor on uninitialized connection')
#         return self.connection.cursor()

# postgres_connection = PostgresConnection()    