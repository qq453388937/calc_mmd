# -*- coding:utf-8 -*-
import gevent
from gevent import monkey
monkey.patch_all()
import time
from greenlet import greenlet  # 导入的类很关键

"""
进程是资源分配的单位   --> 切换资源大，效率低
线程是操作系统调度的单位  --> 资源一般， 效率一般
协程 --> 资源最小 ， 效率高  --->>>>>>>>  单纯的操作CPU上下文
多进程多线程根据cpu核数不一样可能是并行的也可能是并发的
、
协程是python 中另外一种实现多任务的方式，比线程更小占用和更小执行资源
协程的本质就是使用当前进程在不同的函数代码中切换执行！！！！ （可以理解为并行）
不同协程模型的实现可以是单线程，也可以是多线程

"""


def work1():
    while True:
        print("work1")
        yield
        time.sleep(0.5)


def work2():
    while True:
        print("2222")
        yield
        time.sleep(0.5)


def gre1func():
    while True:
        print("gr1")
        gr2.switch()
        time.sleep(0.5)


def gre2func():
    while True:
        print("gr2")
        gr1.switch()
        time.sleep(0.5)


def main():
    w1 = work1()  # 生成器对象
    w2 = work2()  # 生成器对象2
    while True:
        next(w1)
        next(w2)


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)  # 打印当前协程实例对象
        gevent.sleep(0.5)


if __name__ == '__main__':
    # main()  demo1  手写
    gr1 = greenlet(gre1func)  # 创建 greenlet 对象  demo2
    gr2 = greenlet(gre2func)  # 创建 greenlet 对象  demo2
    # gr2.switch()

    g1 = gevent.spawn(f, 5)  # 给f传参
    g2 = gevent.spawn(f, 6)  # 给f传参
    g3 = gevent.spawn(f, 7)  # 给f传参
    # g1.join()  # 默认情况下使用gevent不自动切换
    # g2.join()  # 默认情况下使用gevent不自动切换
    # g3.join()  # 默认情况下使用gevent不自动切换
    gevent.joinall([g1, g2, g3])
