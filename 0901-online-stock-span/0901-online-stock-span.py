class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        tot = 1
        while self.stack and price >= self.stack[-1][0]:
            num = self.stack.pop()
            tot += num[1]
        self.stack.append((price,tot))
        return tot


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)