# -*- coding:utf-8 -*-
import pika
import time

username = 'faith'
pwd = "qq2921481"
user_pwd = pika.PlainCredentials(username, pwd)
connnection = pika.BlockingConnection(
    pika.ConnectionParameters(host='172.16.54.130', credentials=user_pwd)
)

channel = connnection.channel()

channel.queue_declare(queue='rpc_queue')


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n-2)


def on_request(ch, method, props, body):
    n = int(body)

    print('fib %s' % n)
    response = fib(n)  # 干很多事情，这里，，，，，
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response)
                     )
    ch.basic_ack(delivery_tag=method.delivery_tag)


# channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')
print("awaiting Rpc Requests")

channel.start_consuming()

"""10 必须先起来， 9 发消息，得到结果返回 """
