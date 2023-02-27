class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [-1,0]
        answer, i = 0, 0
        
        for i in range(len(arr)):
            while i < len(arr) and arr[stack[-1]] >= arr[i] and len(stack) > 1:
                num = ((stack[-1] - stack[-2]) * (i - stack[-1]) * arr[stack[-1]])
                answer += num
                stack.pop()
                
            stack.append(i)
            
        stack.append(len(arr))
        for i in range(1,len(stack)-1):
            answer += ((stack[i] - stack[i - 1]) * (stack[-1] - stack[i]) * arr[stack[i]])
        
        return answer % (10**9 + 7)