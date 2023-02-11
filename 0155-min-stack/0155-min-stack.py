class MinStack(object):

    def __init__(self):
        self.minn = []
        self.arr = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr.append(val)
        if not self.minn or val <= self.minn[-1]:
            self.minn.append(val)
            
    def pop(self):
        """
        :rtype: None
        """
        x = self.arr.pop()
        if x == self.minn[-1]:
            self.minn.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minn[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()