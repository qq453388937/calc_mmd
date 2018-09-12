# -*- coding:utf-8 -*-


class BaseNode(object):

    # 结点基本属性
    def __init__(self, item):
        self.item = item  # 存放数据元素
        self.next = None  # 下一个结点地址(结点对象)


class SingleLinkList(object):
    """ 单向链表 """

    # 链表基本属性,自动当前链表获取头结点信息
    def __init__(self, node=None):
        """ 链表头结点__haed可能为空 """
        self.__head = node  # 单向列表特点只知道自己的头结点

    def is_empty(self):
        """ 判断单向链表头部是否为空 """
        return self.__head is None

    def length(self):
        """ 求单向链表的长度 """
        # 当前头结点
        cur = self.__head
        # 设计计数初始值为0
        if self.is_empty():  # 链表头都没有为空
            return 0
        else:
            count = 0
            while cur is not None:  # 不能.next
                count += 1
                cur = cur.next  # 外部变量重新赋值,下一次循环 cur 就是 next 的对象
            # 返回总计数
            return count

    def travel(self):
        """ 打印展示所有链表内容 """
        cur = self.__head
        print("self.__head -->", cur)  # cur 一个BaseNode next 另一个BaseNode, item 值
        if self.is_empty():  # 等同于 self.__head is None
            print("")
        else:
            while cur is not None:  # 不能.next
                print(cur.item, end=" ")
                cur = cur.next
            print("")

    def search(self, item):
        """ 搜索 """
        cur = self.__head
        if self.is_empty():  # 等同于 self.__head is None
            return False
        else:
            while cur is not None:  # 下一项不为空没到最后一个
                if cur.item == item:
                    return True  # --> 返回找到即可
                cur = cur.next  # 切记!下一项赋值给外部变量下一次循环使用
            return False  # 循环完一个也没找到

    def add(self, item):
        """ 头部添加BaseNode """
        node = BaseNode(item)
        node.next = self.__head  # next 是头结点node对象
        self.__head = node  # 自己的头结点改为新插入的结点

    def append(self, item):
        """ 尾部追加 """
        node = BaseNode(item)  # 结点对象
        if self.is_empty():  # self.__head is None
            self.__head = node  # 空链表追加一个
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next  # 循环赋值变量相对于
            # 循环完毕到最后一个,cur.next 是空! now cur 是尾结点
            cur.next = node

    def insert(self, pos, item):
        node = BaseNode(item)  # 结点对象
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        # 中间位置
        else:
            cur = self.__head
            count = 0  # 标签: 计数器
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 属性修改
            node.next = cur.next  # 一定要在 cur.next = node 之前
            cur.next = node  # 承上启下

    def remove(self, item):

        if self.is_empty():
            return False  # 删除失败
        else:
            cur = self.__head
            pre = None  # 自己定义的上个结点,为了方便寻找
            while cur is not None:
                if cur.item == item:
                    # 头结点：
                    if cur == self.__head:
                        self.__head = cur.next  # 直接给接班人
                        # pre = None  --> 省略不写
                    # 其他位置,pre 肯定不为None
                    else:
                        # 只需把上一个元素的next 改为我的next 因为要删除自己
                        pre.next = cur.next  # 退位让贤,接班人旧人交接后来新人pre.next 是 cur.next
                    return True  # or break 删除成功
                #  异常情况
                pre = cur
                cur = cur.next  #


if __name__ == '__main__':
    # node = BaseNode(100)
    # print(node.item)
    # print(node.next)
    lian = SingleLinkList()
    lian.add(1)
    lian.add(2)
    # lian.append(3123123)
    # print(lian.is_empty())
    # print(lian.length())
    # print(lian.search(7))
    # lian.insert(666)
    lian.remove(1)
    lian.travel()
