# https://docs.sqlalchemy.org/en/13/
from sqlalchemy import create_engine, text
from flask import current_app, g
import click
from flask.cli import with_appcontext

engine = create_engine('postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/flask')

def connect_engine(DATABASE_URI):
	return create_engine(DATABASE_URI, echo=True, pool_size=20, max_overflow=0)

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
        file = open("application/migration/init.sql")
        query = text(file.read())
        try:
            con.execute(query)
        except Exception as e:
            print("Exception: ",e)

@click.command('migratedb')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')    

def init_app(app):
    print ('==== init app')
    # app.db = connect_engine().connect()
    # app.config['postgreSQL_pool'] = connect_db()
    # app.teardown_appcontext()
    app.cli.add_command(init_db_command)    

