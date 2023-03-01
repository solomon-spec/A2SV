class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dic = {}
        def check(start,end,player1):
            if (start,end,player1) not in dic:
                
                if start == end:
                    if player1: 
                        dic[(start,end,player1)] = [nums[start],0]
                        return [nums[start],0]
                    
                    dic[(start,end,player1)] = [0,nums[start]]
                    return [0,nums[start]]

                if player1:
                    answer1 = check(start + 1,end,not player1).copy()
                    answer1[0] += nums[start]

                    answer2 = check(start,end - 1,not player1).copy()
                    answer2[0] += nums[end]

                    if answer1[0] > answer2[0]:
                        dic[(start,end,player1)] = answer1
                        return answer1
                    
                    dic[(start,end,player1)] = answer2
                    return answer2

                answer1 = check(start + 1,end,not player1).copy()
                answer1[1] += nums[start]

                answer2 = check(start,end - 1,not player1).copy()
                answer2[1] += nums[end]

                if answer1[1] > answer2[1]: 
                    dic[(start,end,player1)] = answer1
                    return answer1
                
                dic[(start,end,player1)] = answer2
                return answer2
            
            else:
                return dic[(start,end,player1)]
        
        answer = check(0,len(nums)-1,True)
        if answer[0] >= answer[1]: return True
        return False