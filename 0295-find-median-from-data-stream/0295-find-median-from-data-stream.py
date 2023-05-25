class MedianFinder:

    def __init__(self):
        self.min = []
        self.max = []
    def addNum(self, num: int) -> None:
        heappush(self.min,-num)
        if len(self.min) > len(self.max) + 1 or (self.max and -self.min[0] > self.max[0]):
            x = -heappop(self.min)
            heappush(self.max,x)
        if len(self.min) + 1 < len(self.max):
            x = -heappop(self.max)
            heappush(self.min,x)
        
        

    def findMedian(self) -> float:
        if len(self.min) > len(self.max): return -self.min[0]
        elif len(self.max) > len(self.min): return self.max[0]
        return (-self.min[0] + self.max[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()