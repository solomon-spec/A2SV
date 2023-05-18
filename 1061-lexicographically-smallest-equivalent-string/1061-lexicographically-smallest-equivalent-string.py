class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        for i in range(26):parent[chr(97+i)] = chr(97+i)
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        def union(ver1,ver2):
            letter1 = find(ver1)
            letter2 = find(ver2)
            if letter1 > letter2:
                parent[letter1] = letter2
            else:
                parent[letter2] = letter1
        for i in range(len(s1)):
            union(s1[i],s2[i])
        ans = []
        for i in baseStr:
            ans.append(find(i))
        return "".join(ans)
        