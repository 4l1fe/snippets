import pika
import sys
import os


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', type='topic')
result = channel.queue_declare(exclusive=True)

binding_keys = sys.argv[1:]
for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=result.method.queue,
                       routing_key=binding_key)


def callback(ch, method, properties, body):
    print('Received {} {}'.format(method.routing_key, body))


channel.basic_consume(callback,
                      queue=result.method.queue,
                      no_ack=True)
print('Current process pid is {}'.format(os.getpid()))
channel.start_consuming()