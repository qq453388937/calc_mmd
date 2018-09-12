# -*- coding:utf-8 -*-
class BaseNode(object):
    def __init__(self, item):
        # 上一结点
        self.pre = None  # 双向链表比单向链表多 一个pre
        self.item = item
        # 下一结点
        self.next = None


class DoubleLinkList(object):
    """ 双向链表 """

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        else:  # 头不为空,开始遍历计数
            cur = self.__head
            count = 0
            while cur is not None:
                count = count + 1
                cur = cur.next
            return count

    def travel(self):
        if self.is_empty():
            print("")
        else:  # 有数据
            cur = self.__head
            while cur is not None:
                print(cur.item, end=" ")
                cur = cur.next
            print("")

    def search(self, item):
        if self.is_empty():
            return False
        else:
            cur = self.__head
            while cur is not None:
                if cur.item == item:
                    return True  # --> 表示有即可
                cur = cur.next
            return False  # --> 循环完毕

    def add(self, item):
        """ 头部增加 """
        node = BaseNode(item)
        node.next = self.__head
        self.__head = node
        # 比单链多的属性修改
        if node.next:  # --> node.next 就是原来的 self.__head , 意思就是原来的链表不为空
            node.next.pre = node  # --> 原来的结点的 pre是 None 需赋值,
        # else:
        #     node.next.pre = None  # --> 原本就是None不必写
        #

    def append(self, item):
        """ 尾部增加 """
        node = BaseNode(item)
        if self.is_empty():
            self.__head = node  # pre默认None符合需求
            # self.add(item)
        else:  # 原先链表不为空
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            # 循环结束该cur就是尾结点,修改属性
            cur.next = node
            node.pre = cur  # 比单向链表多的属性pre属性赋值

    def insert(self, pos, item):
        """ 双向链表指定位置插入 """
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:  # 中间
            node = BaseNode(item)
            cur = self.__head
            count = 0

            # while count < pos:
            #     count += 1
            #     cur = cur.next
            #
            # cur.pre.next = node
            # node.pre = cur.pre
            # cur.pre = node  # cur.pre = node一定要在node.pre = cur.pre之后!
            # node.next = cur

            # #
            while cur is not None:
                if count == pos:
                    cur.pre.next = node
                    node.pre = cur.pre
                    cur.pre = node
                    node.next = cur
                    return True  # or break 操作完毕无需继续循环
                count += 1
                cur = cur.next

    def insert2(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:  # 中间
            node = BaseNode(item)
            cur = self.__head
            count = 0
            # while count < pos:
            #     count += 1
            #     cur = cur.next
            # cur.pre.next = node
            # node.pre = cur.pre
            # cur.pre = node
            # node.next = cur
            while cur is not None:
                if count == pos:
                    cur.pre.next = node
                    node.pre = cur.pre
                    cur.pre = node
                    node.next = cur
                    return True
                count += 1
                cur = cur.next





if __name__ == '__main__':
    ll = DoubleLinkList()
    ll.add(2)
    ll.add(1)
    ll.append(333)
    ll.insert2(4, 123999)
    print(ll.is_empty())
    print(ll.length())
    ll.travel()
    pass
