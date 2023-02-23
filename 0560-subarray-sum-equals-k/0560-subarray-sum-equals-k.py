class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        counter = defaultdict(int)
        counter[0] = 1
        prefix  = 0
        
        for num in nums:
            prefix += num
            answer += counter[prefix - k]
            counter[prefix] += 1
        return answer
        
        
    