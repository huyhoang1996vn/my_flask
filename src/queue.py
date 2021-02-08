
from rabbitmq.fpika import Pika
from app import app

fpika = Pika(app)

ch = fpika.channel();
ch.queue_declare(queue='queue1')
ch.queue_declare(queue='queue2')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

ch.basic_consume(queue='queue1', on_message_callback=callback, auto_ack=True)
ch.basic_consume(queue='queue2', on_message_callback=callback, auto_ack=True)
