class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        for i in range(26):parent[chr(97+i)] = chr(97+i)
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        def union(ver1,ver2):
            parent[find(ver1)] = find(ver2)
        for i in range(len(s1)):
            union(s1[i],s2[i])
        ans = []
        for i in baseStr:
            cur = i
            par = find(i)
            for let in parent:
                if find(let) == par:cur = min(cur,let)
            ans.append(cur)
        return "".join(ans)
        