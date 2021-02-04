import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
import psycopg2
from psycopg2 import pool


def get_db():
    print ('GETTING CONN')
    if 'db' not in g:
        print ('GETTING CONN getconn')
        g.db = current_app.config['postgreSQL_pool'].getconn()
        print '============ g.db ', g.db
    return g.db


def close_conn(e):
    print('CLOSING CONN')
    db = g.pop('db', None)
    if db is not None:
        current_app.config['postgreSQL_pool'].putconn(db)

def init_db():
    db = get_db()
    cursor = db.cursor()
    import os
    from contextlib import closing

    with closing(connect_db()) as conn, conn.cursor() as cursor:
        with app.open_resource('schema.sql', mode='r') as f:
            cursor.execute(f.read())
        conn.commit()



@click.command('init-db-postgres') 
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')        

def connect_db():
    return psycopg2.pool.SimpleConnectionPool(1, 20,user = "postgres",
                                                  password = "postgres",
                                                  host = "172.16.24.104",
                                                  port = "5444",
                                                  database = "flask")

def connect_single_db():
    return psycopg2.connect(user = "postgres",
                          password = "postgres",
                          host = "172.16.24.104",
                          port = "5444",
                          database = "flask")    

def init_app(app):
    print '==== init app'
    app.config['postgreSQL_pool'] = connect_db()
    # app.db = connect_single_db()


    # app.teardown_appcontext(close_conn)
    # app.cli.add_command(init_db_command)    