class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(index,ans):
            nonlocal res
            visited = set()
            if len(ans) > 1:
                res.append(ans.copy())
                
            if index == len(nums):return
            i = index
            while i < len(nums):
                
                if nums[i] not in visited and (not ans or nums[i] >= ans[-1]):
                    ans.append(nums[i])
                    backtrack(i + 1,ans)
                    x = ans.pop()
                    """"while i < len(nums)-1 and x == nums[i + 1]:
                        i +=1"""
                visited.add(nums[i])
                i += 1
            return 
        backtrack(0,[])
        return res
        