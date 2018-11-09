# -*- coding:utf-8 -*-
import socket
import select

# io多路复用的好处就是监听多个

sk = socket.socket()
sk.bind(("127.0.0.1", 8888))
sk.listen(5)
inp = [sk, ]
while True:
    r, w, e = select.select(inp, [], [], 5)  # [sk,conn]  sk 链接变化一次新用户才有反应， coon 发送消息变化
    for i in r:
        if i == sk:
            coon, addr = i.accept()  # 内核态接受到用户态 select 就监听不到了 否则一直inp有
            print(coon)
            print("hello")
            inp.append(coon)
        else:
            data = i.recv(1024)
            print(data.decode("utf8"))
            res = input("回答%s号客户>>>>>>>>>>>" % inp.index(i))
            i.send_all(bytes(res, "utf8"))

    coon.recv(1024)
    print(">>>>>>>>>>>>>")
