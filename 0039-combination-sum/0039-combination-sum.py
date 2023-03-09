class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtrack(arr,comb):
            summ = sum(comb)
            if summ > target:
                return
            elif summ == target:
                answer.append(comb.copy())
                return
            
            for i in range(len(arr)):
                comb.append(arr[i])
                backtrack(arr[i:],comb)
                comb.pop()  
            return 
        
        backtrack(candidates,[])
        return answer