import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs', type='direct')
result = channel.queue_declare(exclusive=True)

severities = sys.argv[1:]
for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=result.method.queue,
                       routing_key=severity)

def callback(ch, method, properties, body):
    print('Received {} {}'.format(method.routing_key, body))


channel.basic_consume(callback,
                      queue=result.method.queue,
                      no_ack=True)
channel.start_consuming()