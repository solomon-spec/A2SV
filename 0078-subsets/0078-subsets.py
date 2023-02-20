class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        num = 2 ** (len(nums))
        answer = []
        for i in range(num):
            byte = bin(i)[2:]
            if len(byte) < len(nums):
                byte = "0"*(len(nums) - len(byte)) + byte
            temp = []
            for j in range(len(byte)):
                if byte[j] =="1":
                    temp.append(nums[j])
            answer.append(temp)
        return answer
                    
                
            