class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        pre_min = []
        post_max = deque()
        for i in range(len(nums)):
            if pre_min: pre_min.append(min(pre_min[-1],nums[i]))
            else: pre_min.append(nums[i])
            if post_max: post_max.appendleft(max(post_max[0],nums[-i-1]))
            else: post_max.append(nums[-1])
        for i in range(len(nums)):
            if pre_min[i] < nums[i] < post_max[i]: return True
        return False