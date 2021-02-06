import os

from flask import Flask
from flask import current_app, g

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
# app.config.from_mapping(
#     SECRET_KEY='dev',
#     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
# )

# if test_config is None:
#     # load the instance config, if it exists, when not testing
#     app.config.from_pyfile('config.py', silent=True)
# else:
#     # load the test config if passed in
#     app.config.from_mapping(test_config)

# ensure the instance folder exists
# try:
#     os.makedirs(app.instance_path)
# except OSError:
#     pass

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.before_request
def before_request():
    from src import db_postgres
    g.db = db_postgres.connect_db().getconn()


# from . import db_postgres
# db_postgres.init_app(app)

from src.bp import auth, blog
app.register_blueprint(auth.bp)
app.register_blueprint(blog.bp)
    

app.add_url_rule('/', endpoint='index')

from src.rabbitmq.fpika import Pika
fpika = Pika(app)

ch = fpika.channel();
ch.queue_declare(queue='queue5')
ch.queue_declare(queue='queue6')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

ch.basic_consume(queue='queue5', on_message_callback=callback, auto_ack=True)
ch.basic_consume(queue='queue6', on_message_callback=callback, auto_ack=True)


# if __name__ == '__main__':
#   print '========================= in file app ', __name__

#     app.run()
ch.start_consuming()

# from threading import Thread
# thread = Thread(ch.start_consuming())
# thread.start()



