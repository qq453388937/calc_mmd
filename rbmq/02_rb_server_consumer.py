# -*- coding:utf-8 -*-

import pika
import time

username = "faith"
pwd = "qq2921481"
user_pwd = pika.PlainCredentials(username, pwd)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.54.130', credentials=user_pwd))
channel = connection.channel()

# 声明 queue，因为不确定生产者先执行还是消费者先执行
channel.queue_declare(queue='hello', durable=True)


def callback(ch, method, properties, body):
    """ 回调函数，有点像事件驱动模型 """
    print(ch, method, properties)  # ch -》 channel
    time.sleep(10)
    print("收到消息", body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


#
channel.basic_qos(prefetch_count=1)  # 只要有一个队列在等待就不给你发了

channel.basic_consume(callback,
                      queue='hello')  # 不确认no_ack=True，默认是确认的no_ack=False，默认客户端不确认，就不删队列，保证消息被完整消费,全部挂了重启还会重新消费未消费完毕的队列

channel.start_consuming()

print("生产者等待消息中，阻塞")  # 默认是轮询机制，开启多个server 轮询接受

"""  
    rabbitmqctl stop 
    rabbitmq-server start &  
    rabbitmqctl list_queues
    rabbitmq-plugins enable rabbitmq_management  # 开启web管理界面 
    Exchange 定义的时候是有类型的，以决定到底是哪些Queue符合条件，可以接受信息
        fanout 所有bind到此exchange的queue都可以接收消息
        direct 通过routingkey 和 exchange 决定的哪个唯一的queue可以接受消息
        topic：所有符合routingkey（此时可以是一个表达式）的routeKey 所bind得queue可以接受到消息
        headers： 通过headers决定发给谁

"""
