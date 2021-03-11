# https://pika.readthedocs.io/en/stable/examples.html
import pika
import time
import pika, sys, os
from services import subcriber

HOST_RABBIT = '127.0.0.1'

def main():
    sleepTime = 10
    print(' [*] Sleeping for ', sleepTime, ' seconds.')

    print(' [*] Connecting to server ...')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST_RABBIT))
    channel = connection.channel()
    channel.queue_declare(queue='queue7', durable=True)
    channel.queue_declare(queue='queue8', durable=True)

    print(' [*] Waiting for messages.')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='queue7', on_message_callback=subcriber.callback2)
    channel.basic_consume(queue='queue8', on_message_callback=subcriber.callback)
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)






