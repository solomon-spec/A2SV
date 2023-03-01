class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def check(start,end,player1):
            if start == end:
                if player1: return [nums[start],0]
                return [0,nums[start]]
            
            if player1:
                answer1 = check(start + 1,end,not player1)
                answer1[0] += nums[start]
                answer2 = check(start,end - 1,not player1)
                answer2[0] += nums[end]
                #print(answer1,answer2)
                if answer1[0] > answer2[0]: return answer1
                return answer2
            
            answer1 = check(start + 1,end,not player1)
            answer1[1] += nums[start]
            answer2 = check(start,end - 1,not player1)
            answer2[1] += nums[end]
            #print(answer1,answer2)
            if answer1[1] > answer2[1]: return answer1
            return answer2
        
        answer = check(0,len(nums)-1,True)
        if answer[0] >= answer[1]: return True
        return False