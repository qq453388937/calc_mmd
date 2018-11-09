# -*- coding:utf-8 -*-
import pika
import sys

username = 'faith'
pwd = "qq2921481"
user_pwd = pika.PlainCredentials(username, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.54.130', credentials=user_pwd))

channel = connection.channel()

channel.exchange_declare(exchange='top_logs', type='topic')
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[1:]) or 'hello world'

channel.basic_publish(
    exchange='top_logs',
    routing_key=routing_key,
    body=message
)

print("send level [%s] message [%s] " % (routing_key, message))

connection.close()
