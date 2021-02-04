import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('172.16.24.104'))
channel = connection.channel()
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print(' [*] Waiting for messages. To exit press CTRL+C')
channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)




channel.start_consuming()
# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)