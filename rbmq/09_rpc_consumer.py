# -*- coding:utf-8 -*-
# remote procudure call  远程调用函数
# snmp 简单网络管理协议 rpc
import pika
import uuid
import time


class FibonacciRpcClient(object):
    def __init__(self):
        self.username = 'faith'
        self.pwd = 'qq2921481'
        self.user_pwd = pika.PlainCredentials(self.username, self.pwd)

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='172.16.54.130', credentials=self.user_pwd)

        )

        self.channel = self.connection.channel()
        # 声明一个队列
        result = self.channel.queue_declare(exclusive=True)  # 随机生成一个队列
        self.callback_queue = result.method.queue
        # 声明了我要收，start才开始收呢  channel.start_consuming()
        self.channel.basic_consume(self.on_response, no_ack=False, queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:  # 服务端的correlation_id uuid 和 本机生成的 correlation_id uuid
            self.response = body

    def callback(self,ch, method, properties, body):
        print('-->', ch, method, properties)
        print('receive: %r' % body)
        ch.basic_ack(deliver_tag=method.delivery_tag)

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,   # body 以外带的
                correlation_id=self.corr_id
            ), body=str(n)
        )
        while self.response is None:
            self.connection.process_data_events()  # 非阻塞的start_consumer（）

            print('no msg！！！！！！！！')
            time.sleep(0.5)

        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()
print(' Requesting fib(30) ')
response = fibonacci_rpc.call(30)
print('response --> %r' % response)
