class Solution:
    def minDeletions(self, s: str) -> int:
        count=Counter(s)
        values=list(count.values())
        c=0
        n = len(values)
        for i in range(n):
            while values[i] in values[i+1:]:
                values[i]=values[i]-1 
                c+=1
            if values[i]:values.append(values[i])
        return c