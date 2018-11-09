# -*- coding:utf-8 -*-
# py queue  典型应用 生产者消费者模型
# threading   queue 多个线程之间数据同步和交互
# multiprocessing  queue 父进程与子进程或者同一父进程下的多个子进程交互
import pika

username = "faith"
pwd = "qq2921481"
user_pwd = pika.PlainCredentials(username, pwd)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.54.130', credentials=user_pwd))
channel = connection.channel()

# 声明 queue
channel.queue_declare(queue='hello', durable=True)

channel.basic_publish(
        exchange='',  # 这里不写exchange
        routing_key='hello',
        body='Hello World',
        properties=pika.BasicProperties(delivery_mode=2)   # 队列消息持久化
        )

print("send hello world")

connection.close()
