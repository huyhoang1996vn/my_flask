# from app import app
# from queue import ch
# import threading

# print '========================= in file run ', __name__

# def fun_app():
# 	app.run('localhost', 5000, True, use_reloader=False)


# if __name__ == '__main__':
# 	# app.run('localhost', 7002, True)
# 	# ch.start_consuming()
#     threading.Thread(target=ch.start_consuming).start()
#     threading.Thread(target=fun_app).start()


# from flask import Flask, request
# from flask_restful import Resource, Api, fields, marshal_with

# app = Flask(__name__)
# api = Api(app)
# todos = {}


# resource_fields = {
#     'task':   fields.String,
#     # 'uri':    fields.Url('todo_ep')
# }

# class TodoDao(object):
#     def __init__(self, todo_id, task):
#         self.todo_id = todo_id
#         self.task = task

#         # This field will not be sent in the response
#         self.status = 'active'

# class HelloWorld(Resource):
#     @marshal_with(resource_fields)
#     def get(self, todo_id=None):
#     	if todo_id:
#         	return {'hello': todo_id}
#         return TodoDao(todo_id='my_todo', task='Remember the milk')

#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}

# # api.add_resource(HelloWorld, '/')
# api.add_resource(HelloWorld, '/', '/<string:todo_id>')


# if __name__ == '__main__':
#     app.run(debug=True)

# https://pika.readthedocs.io/en/stable/examples.html
import pika
import time
import pika, sys, os
from services import subcriber
def main():
    sleepTime = 10
    print(' [*] Sleeping for ', sleepTime, ' seconds.')
    # time.sleep(30)

    print(' [*] Connecting to server ...')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    channel = connection.channel()
    channel.queue_declare(queue='queue7', durable=True)
    channel.queue_declare(queue='queue8', durable=True)

    print(' [*] Waiting for messages.')



    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='queue7', on_message_callback=subcriber.callback2)
    channel.basic_consume(queue='queue8', on_message_callback=subcriber.callback)
    channel.start_consuming()

  # app.run('localhost', 7002, True)
  # ch.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)






