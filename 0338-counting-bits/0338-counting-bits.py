class Solution:
    def countBits(self, n: int) -> List[int]:
        answ = []
        for i in range(n + 1):
            ans = 0 
            cur = i
            while cur > 0:
                if cur % 2 == 1: ans += 1
                cur//= 2
            answ.append(ans)
        return answ
            