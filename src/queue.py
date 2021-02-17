
from rabbitmq.fpika import Pika
from app import app

fpika = Pika(app)

ch = fpika.channel();
ch.queue_declare(queue='queue5')
ch.queue_declare(queue='queue6')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

ch.basic_consume(queue='queue5', on_message_callback=callback, auto_ack=True)
ch.basic_consume(queue='queue6', on_message_callback=callback, auto_ack=True)
