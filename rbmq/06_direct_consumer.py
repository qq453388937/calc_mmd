# -*- coding:utf-8 -*-
import sys
import time

import pika

username = 'faith'
pwd = "qq2921481"
user_pwd = pika.PlainCredentials(username, pwd)
connnection = pika.BlockingConnection(
    pika.ConnectionParameters(host='172.16.54.130', credentials=user_pwd)
)

channel = connnection.channel()

channel.exchange_declare(exchange='direct_logs', type='direct')

result = channel.queue_declare(exclusive=True)  # exclusive 排他，不指定queue的名字，rabbit会随机分配
queue_name = result.method.queue

severities = sys.argv[1:]  # 命令行的形式接受什么类型的消息
if not severities:
    sys.stderr.write('Usage: %s [info] [warning] [error] \n' % sys.argv[0])
    sys.exit(1)
print(severities)
for s in severities:  # 循环绑定
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=s,
                       )

print(' waiting for logs, to exit press ctrl+c')


def callback(ch, method, properties, body):
    print(ch, method, properties)
    time.sleep(1)
    print('收到消息', body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback, queue=queue_name)
channel.start_consuming()
