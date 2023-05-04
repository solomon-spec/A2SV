class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.k = k
        heapify(self.arr)
        while len(self.arr) > k: heappop(self.arr)

    def add(self, val: int) -> int:
        if len(self.arr) < self.k:heappush(self.arr,val)
        else: heappushpop(self.arr, val)
        return self.arr[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)