from sqlalchemy import create_engine, text
from flask import current_app, g
import click
from flask.cli import with_appcontext

engine = create_engine('postgresql+psycopg2://postgres:postgres@127.0.0.1:5444/flask')

def connect_engine():
	return create_engine('postgresql+psycopg2://postgres:postgres@127.0.0.1:5444/flask', echo=True)

def connect_db():
	g.db = db_engine.connect_engine().connect()

def execute_db(*args, **kwargs):
    return g.db.execute(*args, **kwargs)

def execute_string(command):
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
    print '==== init app'
    #     print '==== init app'
#     app.db = connect_engine().connect()
    # app.config['postgreSQL_pool'] = connect_db()
    # app.teardown_appcontext()
    app.cli.add_command(init_db_command)    