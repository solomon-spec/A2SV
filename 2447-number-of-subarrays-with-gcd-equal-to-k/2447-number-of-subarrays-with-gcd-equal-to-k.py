class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            maxx = nums[i]
            if nums[i] == k: ans += 1
            for j in range(i+1,len(nums)):
                maxx = gcd(maxx,nums[j])
                if maxx == k: ans += 1
                elif maxx < k: break
        return ans
            
