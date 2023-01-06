class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashtable = defaultdict(int)
        biggest  = nums[0]
        
        for number in nums:
            hashtable[number] += 1
        
        for number in hashtable:
            if hashtable[number]>hashtable[biggest]:
                biggest = number
                
        return biggest