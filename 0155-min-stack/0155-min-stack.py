class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class MinStack:

    def __init__(self):
        self.head = None 
        self.head2  = None

    def push(self, val: int) -> None:
        cur = Node(val)
        cur.next = self.head
        self.head = cur
        if not self.head2 or val <=self.head2.val:
            minn = Node(val)
            minn.next = self.head2
            self.head2 = minn

    def pop(self) -> None:
        if self.head.val == self.head2.val:
            self.head = self.head.next
            self.head2 = self.head2.next
        else:
            self.head = self.head.next
    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head2.val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()