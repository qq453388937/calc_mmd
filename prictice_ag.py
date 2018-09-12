# -*- coding:utf-8 -*-


class BaseNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head  #
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            print("空")
        else:
            cur = self.__head
            while cur is not None:
                print(cur.item, end=" ")
                cur = cur.next
            print("")

    def serach(self, item):
        if self.is_empty():
            return False
        else:
            cur = self.__head
            while cur is not None:
                if cur.item == item:
                    return True
                cur = cur.next  # 循环赋值
            return False

    def add(self, item):
        node = BaseNode(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node

    def append(self, item):
        node = BaseNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            # cur 是最后一个
            cur.next = node

    def insert(self, pos, item):
        node = BaseNode(item)
        if pos <= 0:
            self.add(node)
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 当前cur 就是 前一个
            node.next = cur.next  # 承上启下
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return False
        else:
            cur = self.__head
            pre = None  # 自己
            while cur is not None:
                if cur.item == item:
                    if cur == self.__head:
                        self.__head = cur.next
                    else:
                        pre.next = cur.next
                    return True  # 删除成功!
                pre = cur
                cur = cur.next


if __name__ == '__main__':
    # model = BaseNode(1)
    # print(model.item)
    # print(model.next)

    ll = SingleLinkList()
    ll.add(2)
    ll.add(1)
    ll.append(3)
    ll.insert(333, 666)
    ll.remove(2)
    print(ll.is_empty())
    print(ll.length())
    print(ll.serach(1))
    ll.travel()
