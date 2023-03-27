class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        max_count = 0
        
        def backtrack(inx,arr):
            nonlocal max_count
            nonlocal requests
            
            if inx == len(requests):
                new = [0]*n
                for i in range(len(requests)):
                    if arr[i] == 1:
                        new[requests[i][0]] -= 1
                        new[requests[i][1]] += 1
                
                if new.count(0) == len(new): 
                    max_count = max(max_count,sum(arr))
                    
                return
            arr2 = arr.copy()
            backtrack(inx+1,arr)
            arr2[inx] = 1
            backtrack(inx+1,arr2)
            return 
        backtrack(0,[0]*len(requests))
        return max_count
        
            
                    
            