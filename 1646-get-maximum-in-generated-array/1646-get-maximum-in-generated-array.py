class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr = [0,1]
        if n == 0: return arr[0]
        for i in range(2,n+1):
            if i % 2 == 0: arr.append(arr[i//2])
            else: arr.append(arr[i//2] + arr[i//2 + 1])
        return max(arr)