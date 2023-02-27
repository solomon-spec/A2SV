class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.leng = k
        self.value = value
        self.true = k

    def consec(self, num: int) -> bool:
        if len(self.queue) < self.leng:
            self.queue.append(num)
        else:
            self.queue.append(num)
            self.queue.popleft()
        self.true = self.true + 1 if num == self.value else 0
        if self.true >= self.leng and len(self.queue) == self.leng:
            return True
        else:
            return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)