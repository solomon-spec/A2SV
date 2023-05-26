class Solution:
    def tribonacci(self, n: int) -> int:
        arr = deque([0,1,1])
        if n < 3: return arr[n]
        for i in range(2,n):
            arr.append(arr[-1]+arr[-2]+arr[-3])
            arr.popleft()
        return arr[-1]