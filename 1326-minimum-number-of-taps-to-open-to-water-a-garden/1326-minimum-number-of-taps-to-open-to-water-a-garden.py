class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        stack = []
        def to_range(i,tap):
            l = max(0,i-tap)
            r = min(n,i + tap)
            return [l,r]
            
            
        for i,tap in enumerate(ranges):
            l,r = to_range(i,tap)
            
            while stack and stack[-1][0] >= l and stack[-1][1] < r:
                stack.pop()
            while len(stack) > 1 and stack[-2][1] >= l and stack[-1][1] < r:
                stack.pop()
            if tap != 0 and (not stack or (stack[-1][1] >= l and stack[-1][1] < r)):
                stack.append([l,r]) 
                
        if stack and stack[0][0] == 0 and stack[-1][1] == n:
            return len(stack)
        else:
            return -1
                
        
            