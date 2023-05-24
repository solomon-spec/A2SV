class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        dic = {}
        x = 0
        for i,j in costs:
            arr.append((i-j,x))
            dic[(arr[-1][0],x)] = [i,j]
            x += 1
        n = len(costs)
        arr.sort()
   
        l = ans = 0
        r = n-1
        while r > l:
            ans += dic[arr[l]][0]
            ans += dic[arr[r]][1]
            r -= 1
            l += 1
        return ans
        
            