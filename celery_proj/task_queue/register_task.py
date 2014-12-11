import pika
import sys

message = ' '.join(sys.argv[1:]) or "Whats up"

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
channel.basic_publish(exchange='',
                     routing_key='hello',
                     body=message,
                     properties=pika.BasicProperties(delivery_mode=2))
print('Sended')
connection.close()