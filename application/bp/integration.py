from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# from bp.auth import login_required
from application.database import Integration
from application.db_engine import  execute_db
import pika
from flask import current_app

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    print ('============== Integration ', current_app.config["HOST_RABBIT"])
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=current_app.config["HOST_RABBIT"]))
    channel = connection.channel()
    message = "info: Hello World!"
    channel.basic_publish(exchange='', routing_key='queue7', body=message)
    channel.basic_publish(exchange='', routing_key='queue8', body=message)

    # execute_db(users.insert(), username='admin', password='admin@localhost')
    posts = execute_db(Integration.select())
    return render_template('blog/index.html', posts=posts)
