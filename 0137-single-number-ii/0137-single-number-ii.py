class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = [0]*(32)
        neg = 0
        for i in nums:
            if i < 0: neg += 1
            for j in range(32):
                if  abs(i) &(1<<j) != 0:
                        arr[j] += 1
        ans = 0
        for i in range(32):
            if arr[i] % 3 != 0 : ans += pow(2,i)
        if neg % 3 != 0: ans = -ans
        return ans