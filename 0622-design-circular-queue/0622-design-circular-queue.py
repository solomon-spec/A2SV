class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [0]*k
        self.front = -1
        self.rear = -1
        self.leng = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.rear += 1
                self.front += 1
                self.arr[self.rear % self.leng] = value
            else:
                self.rear += 1
                self.arr[self.rear % self.leng] = value
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.arr[self.front % self.leng]
        return -1
        

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.arr[self.rear % self.leng]
        return -1

    def isEmpty(self) -> bool:
        if self.front == self.rear == -1:
            return True
        return False

    def isFull(self) -> bool:
        if not self.isEmpty() and self.rear - self.front + 1 == self.leng:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()