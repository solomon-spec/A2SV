class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        par = []
        for num in nums:
            found = False
            for i in range(len(par)-1,-1,-1):
                child = par[i]
                if child[-1] + 1 == num: 
                    child.append(num)
                    found = True
                    break
            if not found:par.append([num])
        for c in par:
            if len(c) < 3: return False
        return True
        
    