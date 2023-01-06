class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        hashtable = {0:0,1:0,2:0}
        for num in nums:
            hashtable[num] += 1
        
        nums[:hashtable[0]] = [0 for i in range(hashtable[0])]
        nums[hashtable[0]:hashtable[0]+hashtable[1]] = [1 for i in range(hashtable[1])]
        nums[hashtable[0]+hashtable[1]:] = [2 for i in range(hashtable[2])]
        print(hashtable)