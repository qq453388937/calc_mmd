# -*- coding:utf-8 -*-

# timeit python 性能测试模块 (很重要,很简单)
import timeit


def func1():
    li = []
    for i in range(1000):
        li.append(i)


def func2():
    li = []
    for i in range(1000):
        li = li + [i]


def func3():
    li = [i for i in range(1000)]


def func4():
    li = list(range(1000))


if __name__ == '__main__':
    time_model = timeit.Timer("func1()", "from __main__ import func1")
    used_time = time_model.timeit(1000)
    print("func1 used time:%f" % used_time)
    time_model = timeit.Timer("func2()", "from __main__ import func2")
    used_time = time_model.timeit(1000)
    print("func2 used time:%f" % used_time)
    time_model = timeit.Timer("func3()", "from __main__ import func3")
    used_time = time_model.timeit(1000)
    print("func3 used time:%f" % used_time)
    time_model = timeit.Timer("func4()", "from __main__ import func4")
    used_time = time_model.timeit(1000)
    print("func4 used time:%f" % used_time)
    print(list(range(100)))
