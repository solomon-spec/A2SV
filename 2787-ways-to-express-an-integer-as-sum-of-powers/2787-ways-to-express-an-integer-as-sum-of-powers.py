class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dic = defaultdict(int)
        arr = []
        mod = 1_000_000_007
        for i in range(1,n+1):
            if i**x > n: break
            arr.append(i**x)
            
        arr.sort()
        for i in range(len(arr)+1):dic[(0,i)] = 1
            
        for amt in range(1,n+1):
            for i in range(len(arr)-1,-1,-1):
                if amt - arr[i] >= 0 and amt - arr[i] != arr[i]:
                    dic[(amt,i)] += (dic[(amt-arr[i],i+1)] + dic[(amt,i+1)])
                  
                else: dic[(amt,i)] += dic[(amt,i+1)]

                dic[(amt,i)] = dic[(amt,i)] % mod  
        return dic[(n,0)] % mod