class Solution:
    def jump(self, nums: List[int]) -> int:
        
        cur_max = 0
        queue = deque([(0,0)])
        visited = set([0])
        if len(nums) == 1:
            return 0
        while queue:
            cur, cost = queue.popleft()
            
            for i in range(cur_max, cur + nums[cur] + 1):
                if i == len(nums) - 1:
                    return cost + 1
            
                
                if i not in visited:
                    queue.append([i,cost+1])
                    visited.add(i)
            cur_max = max(cur_max,cur + nums[cur] + 1)
        