class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = defaultdict(int)
        nums.sort()
        
        for i in range(len(nums)-1):
            pt2 = len(nums)-1
            pt1 = i+1
            while pt1<pt2:
                if nums[i] + nums[pt1] + nums[pt2] == 0:
                    answer[tuple([nums[i],nums[pt1],nums[pt2]])]+=1
                    pt1+=1
                elif nums[i] + nums[pt1] + nums[pt2] < 0:
                    pt1+=1
                else:
                    pt2-=1

        return list(answer.keys())