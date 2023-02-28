class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a = Counter(jewels)
        b = Counter(stones)
        answer = 0
        for i in a:
            answer += b[i]
        return answer