class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        summ = 0
        answer = []
        for num in nums:
            if num%2==0:
                summ+=num
        for i in queries:
            if nums[i[1]]%2 == 0:
                if (nums[i[1]]+i[0])%2 ==0:
                    summ+=i[0]
                else:
                    summ-=nums[i[1]]
            else:
                if (nums[i[1]]+i[0])%2 ==0:
                    summ+= nums[i[1]]+i[0]
                else:
                    summ = summ
            nums[i[1]]+=i[0]
            
            answer.append(summ)
        return answer
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        