# -*- coding:utf-8 -*-
import pika
import sys

username = "faith"
pwd = "qq2921481"
user_pwd = pika.PlainCredentials(username, pwd)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='172.16.54.130',
                              credentials=user_pwd)
)
channel = connection.channel()

# 这里还是不声明 queue
# channel.queue_declare(queue='hello', durable=True)

# 声明
channel.exchange_declare(exchange='direct_logs', type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'  # 默认info级别
# message = 'hello direct_logs [%s]' % sys.argv[1:]
message = ','.join(sys.argv[1:]) or 'hello world'  # 命令行没有输入消息类型就发 hello world
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,  # 命令行的形式生产什么类型的消息
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2)
                      )

print(' sent level【%s】 message ->【%s】' % (severity, message))
connection.close()

"""
(a3) catdeMacBook-Pro:rbmq cat$ python 05_direct_proceduer.py warning info  # 发送警告信息 warning info
 sent level【warning】message ->【warning,info】
(a3) catdeMacBook-Pro:rbmq cat$ python 05_direct_proceduer.py  # 发送默认info类型信息 helloworld
 sent level【info】 message ->【hello world】
 

"""
"""
    python 06_direct_consumer.py info warning   --》 接受warning类型信息
    python 06_direct_consumer.py info  --》 接受info类型信息 
"""


