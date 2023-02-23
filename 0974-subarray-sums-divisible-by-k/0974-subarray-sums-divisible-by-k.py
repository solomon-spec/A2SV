class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        summ = 0
        answer = 0
        dic =  defaultdict(int)
        dic[0] = 1
        
        for i in nums:
            summ += i
            num = summ%k
            dic[num % k] += 1
            answer += dic[num % k] -1
        return answer