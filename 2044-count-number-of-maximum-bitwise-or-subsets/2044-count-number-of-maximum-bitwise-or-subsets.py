class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        num = 2**len(nums) - 1
        ans = 0
        maxx = 0
        while num > 0:
            cur = []
            for i in range(len(nums)):
                if num & (1<<i) != 0: 
                    cur.append(nums[i])
            if not cur: continue
            xor = 0
            for i in range(len(cur)): xor |= cur[i]
            if xor == maxx: ans += 1
            elif xor > maxx: 
                ans += 1
                maxx = xor
            num -= 1

        return ans