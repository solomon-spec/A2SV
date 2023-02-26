class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [0]*k
        self.front = None
        self.rear = None
        self.leng = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.rear = 0
                self.front = 0
                self.arr[self.front % self.leng] = value
            else:
                self.front -= 1
                self.arr[self.front % self.leng] = value
            #print(self.arr,self.front)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.rear = 0
                self.front = 0
                self.arr[self.rear % self.leng] = value
            else:
                self.rear += 1
                self.arr[self.rear % self.leng] = value
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front += 1
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.rear -= 1
            return True
        return False
    
    def getFront(self) -> int:
        if not self.isEmpty():
            #print(self.arr,self.front)
            return self.arr[self.front % self.leng]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.arr[self.rear % self.leng]
        return -1

    def isEmpty(self) -> bool:
        if self.front == self.rear == None:
            return True
        return False

    def isFull(self) -> bool:
        if not self.isEmpty() and self.rear - self.front + 1 == self.leng:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()