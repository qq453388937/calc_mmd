# -*- coding:utf-8 -*-
import sys
import pika
import time

username = "faith"
pwd = "qq2921481"
user_pwd = pika.PlainCredentials(username, pwd)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.54.130', credentials=user_pwd))
channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')

result = channel.queue_declare(exclusive=True)  # exclusive排他 不指定queue的名字,rabbit会随机分配
queue_name = result.method.queue
print(queue_name)
channel.queue_bind(exchange='logs', queue=queue_name)
print("waiting for logs. to exit press ctrl+c")


def callback(ch, method, properties, body):
    """ 回调函数，有点像事件驱动模型 """
    print(ch, method, properties)  # ch -》 channel
    time.sleep(10)
    print("收到消息", body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback,
                      queue=queue_name)
# 不确认no_ack=True，默认是确认的no_ack=False，默认客户端不确认，就不删队列，保证消息被完整消费,全部挂了重启还会重新消费未消费完毕的队列

channel.start_consuming()
