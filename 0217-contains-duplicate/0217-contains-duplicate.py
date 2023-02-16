class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic  = Counter(nums).values()
        for i in dic:
            if i > 1:
                return True 
        return False
        