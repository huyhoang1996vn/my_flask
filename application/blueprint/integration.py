from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# from bp.auth import login_required
from application.database import Integration
from application.db_engine import  execute_db
import pika
bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    print ('============== Integration ')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    channel = connection.channel()
    message = "info: Hello World!"
    channel.basic_publish(exchange='', routing_key='queue7', body=message)
    channel.basic_publish(exchange='', routing_key='queue8', body=message)

    print(" [x] Sent %r" % message)
    print(" [x] Sent 'Hello World!'")
    connection.close()

    # fpika.return_channel(ch);
    # execute_db(users.insert(), username='admin', password='admin@localhost')
    posts = execute_db(Integration.select())
    return render_template('index.html', posts=posts)
