class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minn = nums[0]
        stack = []
        for i in nums:
            while stack and i >= stack[-1][0]:
                stack.pop()
            if stack and i > stack[-1][1]:
                return True
            minn = min(minn,i)
            #print(minn,i)
            stack.append([i,minn])
        #print(stack)
        return False
        