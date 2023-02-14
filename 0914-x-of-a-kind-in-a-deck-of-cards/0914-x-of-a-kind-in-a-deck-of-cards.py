class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic =defaultdict(int)
        for i in deck:
            dic[i] += 1
        arr = sorted(list(dic.values()))
        greatest = arr[0]
        for i in arr:
            greatest = gcd(greatest,i)
            if greatest == 1:
                return False
            
        return True
        