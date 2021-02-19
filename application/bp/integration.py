from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# from bp.auth import login_required
from application.database import Integration
from application.db_engine import  execute_db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    from application.rabbitmq.fpika import Pika
    fpika = Pika(g)
    ch = fpika.channel();
    ch.basic_publish(exchange='',routing_key='queue7',body='Integration')
    fpika.return_channel(ch);
    # execute_db(users.insert(), username='admin', password='admin@localhost')
    posts = execute_db(Integration.select())
    print '============== posts ', posts
    
    return render_template('blog/index.html', posts=posts)
