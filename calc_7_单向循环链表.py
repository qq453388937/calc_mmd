# -*- coding:utf-8 -*-
class BaseNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCircleList(object):
    """ 单向循环列表 """
    def __init__(self, node=None):
        """ 初始化头元素,从头开始查找 """
        self.__head = node

    def is_empty(self):
        """ 判空 """
        return self.__head is None

    def length(self):
        """ 求单向循环列表长度 """
        cur = self.__head
        if self.is_empty():
            return 0
        count = 1
        while cur.next is not self.__head:
            """进入循环统计元素个数"""
            count += 1
        # 循环结束少加1个前面补偿进去
        return count


if __name__ == '__main__':
    sc = SingleCircleList()
    print(sc.is_empty())
    print(sc.length())
