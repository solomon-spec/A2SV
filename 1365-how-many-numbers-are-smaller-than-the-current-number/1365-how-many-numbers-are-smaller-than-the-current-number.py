class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic  = defaultdict(int)
        prefix = 0
        answer = []
        
        for number in nums:
            dic[number]+=1
        key_list = list(dic.keys())
        key_list.sort()
        
        for number in key_list:
            prefix+=dic[number]
            dic[number] = prefix-dic[number]
        
        for number in nums:
            answer.append(dic[number])
        
        return answer
            
       
            
            
        
        
        