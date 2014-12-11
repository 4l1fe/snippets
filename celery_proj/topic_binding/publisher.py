import pika
import sys


severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "Whats up"

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', type='topic')
channel.basic_publish(exchange='topic_logs',
                      routing_key=severity,
                      body=message)
print('Sended {} {}'.format(severity, message))
connection.close()