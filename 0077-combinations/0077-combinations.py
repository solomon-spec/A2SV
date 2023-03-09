class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def backtrack(i,comb):
            if i >  n + 1:
                return
            if len(comb) == k:
                answer.append(comb.copy())
                return
            
         
            comb.append(i)
            backtrack(i + 1,comb)
            comb.pop()
            backtrack(i+1,comb)
            return 
        backtrack(1,[])
        return answer
           