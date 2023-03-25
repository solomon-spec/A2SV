class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_ = -inf
        
        def backtrack(index,ans):
            nonlocal max_
            
            max_ = max(max_,len(ans))
            if index == len(arr):
                return
            for i in range(index,len(arr)):
                if len(arr[i]) + len(ans) == len(set(list(arr[i]) + list(ans))):
                    ans2 = ans.copy()
                    for x in arr[i]: ans.add(x)
                    backtrack(i + 1,ans)
                    ans = ans2
        backtrack(0,set())
        return max_
            