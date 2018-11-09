# -*- coding:utf-8 -*-
import pika

"""
 Exchange 定义的时候是有类型的，以决定到底是哪些Queue符合条件，可以接受信息
        fanout 所有bind到此exchange的queue都可以接收消息
        direct 通过routingkey 和 exchange 决定的哪个唯一的queue可以接受消息
        topic：所有符合routingkey（此时可以是一个表达式）的routeKey 所bind得queue可以接受到消息
        headers： 通过headers决定发给谁
"""
username = "faith"
pwd = "qq2921481"
user_pwd = pika.PlainCredentials(username, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.54.130', credentials=user_pwd))
channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')

# 广播无需声明 queue
# channel.queue_declare(queue='hello', durable=True)

# 广播无需什么queue
channel.basic_publish(
    exchange='logs',
    routing_key='', # 这里不写routing_key
    body='Hello World',
    # properties=pika.BasicProperties(delivery_mode=2)  # 队列消息持久化
)

print("send hello world 收音机")

connection.close()
