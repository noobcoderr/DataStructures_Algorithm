class Node(object):
    def __init__(self,val):
        '''双向链表节点'''
        self.val = val
        self.pre = None
        self.next = None

class Two_way_Link_List(object):
    """双向链表"""

    def __init__(self,node=None):
        self._head = node

    #开始实现双向链表的一些功能
    #判断是否是空链表
    def is_empty(self):
        return self._head == None

    #求链表的长度
    #cur 是游标 cursor 的简写，用来跟踪链表中节点的位置
    def length(self):
        count = 0
        cur = self._head
        while cur != None:
            count += 1
            cur = cur.next
        return count

    #遍历整个链表
    def travel(self):
        if self._head == None:
            return None
        else:
            cur = self._head
            while cur != None:
                print(cur.val,end=' ')
                cur = cur.next
        print('')

    #头插法：在链表头部插入元素
    def add(self,item):
        node = Node(item)
        node.next = self._head
        self._head.pre = node
        self._head = node

    #尾插法:在链表尾部插入元素
    def append(self,item):
        node = Node(item)
        if self._head == None:
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.pre = cur

    #在指定位置插入元素
    def insert(self,pos,item):
        """pos为插入的位置
           item为插入的元素
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            cur = self._head
            count = 0
            node = Node(item)
            while count < pos:
                count += 1
                cur = cur.next
            node.next = cur
            node.pre = cur.pre
            cur.pre = node
            node.pre.next = node


    #删除节点（仅删除第一个匹配的）
    def remove(self,item):
        cur = self._head
        while cur != None:
            if cur.val == item:
                if cur == self._head:
                    self._head = cur.next
                    if cur.next:
                        #判断链表是否只有一个节点
                        cur.next.pre = None
                else:
                    cur.pre.next = cur.next
                    if cur.next:
                        #判断是否是最后一个元素
                        cur.next.pre = cur.pre
                break
            else:
                cur = cur.next


    #查找节点是否存在
    def search(self,item):
        """返回节点所在链表的位置,无则返回-1"""
        count = 0
        cur = self._head
        while cur != None:
            if cur.val == item:
                return count
            else:
                count += 1
                cur = cur.next
        return -1


#以下是测试
# if __name__ == '__main__':
#     ll = Two_way_Link_List()
#     print(ll.is_empty())
#     print(ll.length())
#
#     ll.append(100)
#     ll.append(200)
#     print(ll.is_empty())
#     print(ll.length())
#
#     ll.append(300)
#     ll.append(400)
#     ll.append(500)
#     ll.append(600)
#     # ll.travel(    )
#
#     ll.add(10)
#     ll.travel()
#     ll.search(500)
#     ll.insert(4,40)
#     ll.insert(-10,-10)
#     ll.insert(100,1)
#     ll.travel()
#     print(ll.search(4000))
#     ll.remove(1)
#     ll.travel()


