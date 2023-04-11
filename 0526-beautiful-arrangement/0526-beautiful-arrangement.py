class Solution:
    def countArrangement(self, n: int) -> int:
        res  = 0
        numm = 0
        nums = [i+1 for i in range(n)]
        def backtrack(num):
            nonlocal numm
            nonlocal res
            if len(num) == len(nums):
                res += 1
                return
            for i in range(len(nums)):
                if numm & (1<<i) == 0 and ((len(num)+1) % nums[i] == 0 or nums[i] % (len(num)+1) == 0):
                    num.append(nums[i])
                    numm |= (1<<i)
                    backtrack(num)
                    num.pop()
                    numm &= ~(1<<i)
        backtrack([])
        return res