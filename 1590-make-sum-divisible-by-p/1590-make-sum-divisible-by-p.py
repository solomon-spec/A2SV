class Solution:
    def minSubarray(self, nums: List[int], k: int) -> int:
        p = sum(nums) % k
        if p == 0:
            return 0
        
        pre = 0
        dic = defaultdict(int)
        dic[0] = -1
        minn = len(nums)
        
        for i in range(len(nums)):
            #print(dic,i)
            pre += nums[i]
            if p == nums[i] % k:
                return 1
            
            if ((pre % k) - p) in dic:
                minn = min(minn,i - dic[(pre % k) - p])
                
            if ((pre % k + k) - p )  in dic:
                minn = min(minn,i - dic[(pre % k + k) - p])

            dic[(pre % k)] = i
        if minn == len(nums):
            return -1
        print(dic)
        return minn