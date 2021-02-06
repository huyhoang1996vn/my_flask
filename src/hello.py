# coding: utf-8

from flask import Flask, request, render_template
from rq import Queue
from rq.job import Job
# from worker import conn

# q = Queue(connection=conn)
app = Flask(__name__)


def count_and_save_words(url):

    errors = []

    try:
    	print 'Get url ', url
    except:
        errors.append("Unable to add item to database.")
        return {"error": errors}


@app.route('/', methods=['GET', 'POST'])
def index():
    results = {}
    if request.method == "POST":
        # this import solves a rq bug which currently exists
        from app import count_and_save_words

        # get url that the person has entered
        url = request.form['url']
        if not url[:8].startswith(('https://', 'http://')):
            url = 'http://' + url

        print 'url ', url
        job = q.enqueue_call(
            func=count_and_save_words, args=(url,), result_ttl=5000
        )
        print(job.get_id())

    return render_template('hello.html', results=results)




@app.route('/staff')
def hello_staff():
   return 'Hello staff'

@app.route('/admin')
def hello_admin():
   return 'Hello admin'

@app.route('/user/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/<name>')
def hello_world(name):
	if name == 'staff':
		return redirect(url_for('hello_staff'))
	if name == 'admin':
		return redirect(url_for('hello_admin'))
	return 'Hello'


@app.route("/me")
def me_api():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return {
        "username": "hoang nguyen",
        "theme": "png",
        "image": "",
    }

print '====================================== __name__ ', __name__


if __name__ == '__main__':
    print '======================================'
    app.run('localhost', 7002, True)