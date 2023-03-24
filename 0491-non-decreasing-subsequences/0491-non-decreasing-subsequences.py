class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(index,ans):
            nonlocal res
            visited = set()
            if len(ans) > 1:
                res.append(ans.copy())
                
            if index == len(nums):return
            for i in range(index,len(nums)):
                if nums[i] not in visited and (not ans or nums[i] >= ans[-1]):
                    ans.append(nums[i])
                    backtrack(i + 1,ans)
                    x = ans.pop()
                visited.add(nums[i])
            return 
        backtrack(0,[])
        return res
        