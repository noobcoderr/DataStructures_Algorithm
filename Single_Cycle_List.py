class Node(object):
    """单向循环链表节点"""
    def __init__(self,val):
        self.val = val
        self.next = None


class Sing_Cycle_List(object):
    """单向循环链表"""
    def __init__(self,node=None):
        self._head = node
        if node:
            node.next = node

    def is_empty(self):
        """判断是否为空表"""
        return self._head == None

    def length(self):
        """求链表长度"""
        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            print(cur.val,end=' ')
            cur = cur.next
        #退出循环时，遗漏了尾节点
        print(cur.val,end='')
        print('')


    def add(self,item):
        """头插法"""
        node = Node(item)
        #先遍历找到尾节点
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            #再执行插入操作
            node.next = self._head
            self._head = node
            cur.next = self._head

    def append(self,item):
        """尾插法"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            cur.next = node


    def insert(self,pos,item):
        """在任意位置插入节点"""
        if pos <= 0 :
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            cur = self._head
            pre = None
            count = 0
            node = Node(item)
            while count < pos:
                count += 1
                pre = cur
                cur = cur.next
            node.next = cur
            pre.next = node

    def search(self,item):
        """查找元素是否在链表中"""
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != self._head:
            if cur.val == item:
                return True
            else:
                cur = cur.next
        #退出循环时遗漏了最后一个节点，故要单独判断
        if cur.val == item:
            return True
        else:
            return False


    def remove(self,item):
        """删除节点,考虑空链表，删除头结点，中间节点，尾节点等情况"""
        if self.is_empty():
            return
        cur = self._head
        pre = None
        while cur.next != self._head:
            if cur.val == item:
                if cur == self._head:
                    #头结点的情况，需要寻找尾节点
                    rear = self._head
                    while rear.next != self._head:
                        rear = rear.next
                    self._head = cur.next
                    rear.next = self._head
                else:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next
            return
        #退出循环，遗漏了最后一个节点
        if cur.val == item:
            if cur == self._head:
                #链表只有一个节点
                self._head = None
            else:
                pre.next = self._head


#以下是测试
if __name__ == '__main__':
    ll = Sing_Cycle_List()
    print(ll.is_empty())
    print(ll.length())
    ll.append(10)
    print(ll.is_empty())
    print(ll.length())

    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    ll.travel()
    ll.add(1)
    ll.travel()
    ll.append(60)
    ll.travel()
    ll.insert(-10,-1)
    ll.insert(100,70)
    ll.insert(3,1000)
    ll.travel()
    print(ll.search(80))
    ll.remove(-1)
    ll.travel()
