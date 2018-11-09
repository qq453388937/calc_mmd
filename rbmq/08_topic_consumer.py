# -*- coding:utf-8 -*-
import pika
import time
import sys

username = 'faith'
pwd = 'qq2921481'
user_pwd = pika.PlainCredentials(username, pwd)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='172.16.54.130', credentials=user_pwd)

)

channel = connection.channel()

channel.exchange_declare(exchange='top_logs', type='topic')

result = channel.queue_declare(exclusive=True)  # 随机队列
queue_name = result.method.queue
print(queue_name)
binding_keys = sys.argv[1:]
print(binding_keys)
if not binding_keys:
    sys.stderr.write('Usage: %s [binding_key]...\n' % sys.argv[0])
    sys.exit(1)

for key in binding_keys:
    channel.queue_bind(exchange='top_logs', queue=queue_name, routing_key=key)

print(' waiting for logs .To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(ch, method, properties)
    time.sleep(1)
    print("收到消息", body)
    # 如果没有下句 ，必须no_ack=True
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback, queue=queue_name)
channel.start_consuming()


"""
 python 08_topic_consumer.py \#
 python 08_topic_consumer.py *.info  收所有*.info 消息
 python 08_topic_consumer.py *.error mysql.*
"""
"""
 python 07_topic_producer.py   --> 默认 anonymous.info
 python 07_topic_producer.py   --> test.error
 python 07_topic_producer.py mysql.info
 
"""