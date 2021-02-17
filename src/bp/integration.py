from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# from bp.auth import login_required
from src.database import Integration
from src.db_engine import  execute_db


bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    from src.rabbitmq.fpika import Pika
    fpika = Pika(g)
    ch = fpika.channel();
    ch.basic_publish(exchange='',routing_key='queue3',body='message')
    fpika.return_channel(ch);
    # execute_db(users.insert(), username='admin', password='admin@localhost')
    posts = execute_db(Integration.select())
    print '============== posts ', posts
    
    return render_template('blog/index.html', posts=posts)


# api = Api()
# api.add_resource(...)
# api.init_app(app)

# @bp.route('/create', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         body = request.form['body']
#         error = None

#         if not title:
#             error = 'Title is required.'

#         author_id = None if g.user is None else g.user['id']

#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             cursor = db.cursor()

#             cursor.execute(
#                 'INSERT INTO post (title, body, author_id) VALUES (%s,%s, %s);' %('title', 'body', '1')
#             )
#             cursor.close()
#             return redirect(url_for('blog.index'))

#     return render_template('blog/create.html')    