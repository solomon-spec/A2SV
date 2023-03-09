class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        check = set()
        leng = 2**len(nums)
        nums.sort()
        def backtrack(ans,arr):
            if len(res) == leng:
                return
            if not arr:
                return
            
            ans.append(arr[0])
            backtrack(ans,arr[1:])
            if tuple(ans) not in check:
                res.append(ans.copy())
                check.add(tuple(ans))
            ans.pop()
            backtrack(ans,arr[1:])
            return
        backtrack([],nums)
        return res