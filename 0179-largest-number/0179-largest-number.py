class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        str_nums = [str(i) for i in nums]
        def compair (num1,num2):
            if num1 + num2 >num2+ num1:
                return -1
            else:
                return 1
        str_nums.sort(key = cmp_to_key(compair))
        
        if str_nums[0] == "0":
            return "0"
        return "".join(str_nums)