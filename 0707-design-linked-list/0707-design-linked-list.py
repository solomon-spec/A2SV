class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        cur = self.head
        i = 0
        while  i < index and cur:
            cur = cur.next
            i += 1
        if cur:
            return cur.val
        else:
            return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new = Node(val)
        if not self.head:
            self.head, self.tail = new, new
            
        else:
            new.next = self.head
            self.head = new

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new = Node(val)
       
        if not self.head:
            self.head = self.tail = new
            
        else:
            self.tail.next = new
            self.tail = new
            

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
        else:
            new = Node(val)
            i = 0
            cur = self.head
            while i < index - 1 and cur:
                cur = cur.next
                i += 1
            if cur:
                new.next = cur.next
                cur.next = new
                if not new.next:
                    self.tail = new


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index == 0:
            self.head = self.head.next
        
        else:
            cur = self.head
            i = 0
            while i < index - 1 and cur:
                i += 1
                cur = cur.next
            if cur and cur.next:
                cur.next = cur.next.next
                if not cur.next:
                    self.tail = cur
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)