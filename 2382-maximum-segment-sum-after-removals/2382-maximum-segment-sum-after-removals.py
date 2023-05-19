class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        summ =[i for i in nums]
        arr = [0]*len(nums)
        parent = [i for i in range(len(nums))]
        
        def is_valid(x):
            if 0 <= x < len(nums) and arr[x]:return True
            return False
        
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        
        def union(ver1,ver2): 
            x = find(ver1)
            y = find(ver2)
            parent[x] = y
            summ[y] += summ[x]
        
        ans =[0]
        maximum = 0
        for i in range(len(nums)-1,0,-1):
            cur = removeQueries[i]
            arr[cur] = 1
            if is_valid(cur+1):
                union(cur+1,cur)
            if is_valid(cur-1):
                union(cur-1,cur)
            maximum = max(maximum,summ[find(cur)])
            ans.append(maximum)
        return reversed(ans)
            
                
        
        
        
        
        