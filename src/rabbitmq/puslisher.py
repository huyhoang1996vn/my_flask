import pika
# parameters = pika.URLParameters('amqp://guest:guest@rabbit-server1:5672/%2F?backpressure_detection=t')



connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.24.104'))
channel = connection.channel()

message = "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
print(" [x] Sent 'Hello World!'")
connection.close()



