# import os

# from flask import Flask
# from flask import current_app, g

# # create and configure the app
# app = Flask(__name__, instance_relative_config=True)

# @app.route('/hello')
# def hello():
#     return 'Hello, World!'

# @app.teardown_request
# def teardown_request(exception):
#     db = getattr(g, 'db', None)
#     print '=== teardown_request'
#     if db is not None:
#     	print '=== db close'
#         db.close()

# @app.before_request
# def before_request():
#     # import db_postgres
#     # g.db = db_postgres.connect_db().getconn()
#     print '=== before_request'
#     import db_engine
#     g.db = db_engine.connect_engine().connect()


# # from . import db_postgres
# # db_postgres.init_app(app)

# from bp import blog
# # app.register_blueprint(auth.bp)
# app.register_blueprint(blog.bp)
    

# app.add_url_rule('/', endpoint='index')