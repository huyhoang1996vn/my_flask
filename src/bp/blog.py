from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from src.bp.auth import login_required
from src.db_postgres import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    from src.rabbitmq.fpika import Pika
    fpika = Pika(g)
    ch = fpika.channel();
    ch.basic_publish(exchange='',routing_key='queue3',body='message')
    fpika.return_channel(ch);
    # posts = db.execute(
    #     '''SELECT p.id, title, body, created, author_id, username FROM post p JOIN user u ON p.author_id = u.id ORDER BY created DESC'''
    # ).fetchall()
    cursor = g.db.cursor()
    cursor.execute(
        '''SELECT p.id, title, body, created, author_id FROM post p ORDER BY created DESC'''
    )
    posts = cursor.fetchall()
    cursor.close()
    print '============== posts ', posts
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        author_id = None if g.user is None else g.user['id']

        if error is not None:
            flash(error)
        else:
            db = get_db()
            cursor = db.cursor()

            cursor.execute(
                'INSERT INTO post (title, body, author_id) VALUES (%s,%s, %s);' %('title', 'body', '1')
            )
            cursor.close()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')    