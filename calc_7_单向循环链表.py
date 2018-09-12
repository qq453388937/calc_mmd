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
        """ 求单向循环链表长度 """
        cur = self.__head
        if self.is_empty():
            return 0
        count = 1
        while cur.next is not self.__head:
            """进入循环统计元素个数"""
            print(1)
            count += 1
            cur = cur.next  # 常规操作
        # 循环结束少加1个前面补偿进去,循环结束cur在尾结点上,or 最后循环外count+=1
        return count

    def travel(self):
        """ 输出单向循环链表 """
        if self.is_empty():
            print("空")
            return True  # 输出成功
        else:  # 单向链表不为空
            cur = self.__head
            while cur.next is not self.__head:
                print(cur.item, end=" ")
                cur = cur.next
            # 循环完毕最后一个没输出
            print(cur.item)
            print("")

    def search(self, item):
        if self.is_empty():
            return False  # 搜索失败
        else:
            cur = self.__head
            while cur.next is not self.__head:
                if cur.item == item:
                    return True  # 找到了
                cur = cur.next  # 基本操作
            if cur.item == item:  # 尾结点单独匹配
                return True  # 最后一个匹配
            return False

    def add(self, item):
        """ 增加头结点 (先找尾结点,没有内容头尾循环-->单向单结点)"""
        node = BaseNode(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head  # 单向循环链表(单节点添加->next指向自己)
        else:  # 链表不为空
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            # 循环结束cur是尾结点
            cur.next = node
            # 新的头的next 指向老的头结点
            node.next = self.__head
            # 新的__head存储
            self.__head = node

            # 循环结束cur是尾结点 写法2 同一指向
            # cur.next = self.__head

    def append(self, item):
        """ 单向循环链表尾部追加结点内容 """
        node = BaseNode(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head  # 单向循环链表(单节点添加-->next->指向自己)
            # self.add(item)         # 也可以直接调用
        else:  # 链表不为空
            cur = self.__head
            while cur.next is not self.__head:  # 找尾结点,循环完毕cur为尾结点
                cur = cur.next
            # 属性修改
            cur.next = node  # 尾部的next指向新的node
            node.next = self.__head  # 尾部node指向头

    def insert(self, pos, item):
        """ 单向循环链表指定位置增加 (和单向链表一样!) """
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:  # 中间添加
            node = BaseNode(item)
            cur = self.__head
            count = 0
            while count < (pos - 1):
                cur = cur.next
            # 当前cur为更改位置前一个元素, 修改属性
            node.next = cur.next  # 一定要在 cur.next = node 之前
            cur.next = node  # 承上启下

    def remove(self, item):
        """ 单向循环链表删除元素(最复杂情况考虑) """
        if self.is_empty():
            return False  # 元素不存在删除失败
        else:  # 单向循环链表存在
            cur = self.__head
            pre = None
            # count = 0
            while cur.next is not self.__head:
                if cur.item == item:  # 循环内匹配上删除的
                    if cur == self.__head:  # 正好是头结点,头部删除,需再次循环找到尾结点
                        tail_node = self.__head
                        while tail_node.next is not self.__head:
                            tail_node = tail_node.next
                        # 修改属性
                        self.__head = cur.next
                        tail_node.next = self.__head
                    else:  # 中间删除
                        pre.next = cur.next
                    return True
                # count += 1
                pre = cur
                cur = cur.next

            # 循环完毕 cur 为尾结点 ,尾结点一个或者多个
            if cur.item == item:
                # 链表只有一个元素
                if cur == self.__head:
                    self.__head = None
                else:
                    pre.next = self.__head
                return True
            return False


if __name__ == '__main__':
    sc = SingleCircleList()
    sc.add(1)
    sc.add(23)
    sc.append(66)
    sc.insert(1, 110)
    sc.remove(66)
    print(sc.is_empty())
    print(sc.length())
    print(sc.search(1))
    sc.travel()
