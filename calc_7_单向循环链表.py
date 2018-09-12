# -*- coding:utf-8 -*-
class BaseNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCircleList(object):
    """ 单向循环列表 """
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """ 判空 """
        return self.__head is None


if __name__ == '__main__':
    sc = SingleCircleList()
    print(sc.is_empty())
