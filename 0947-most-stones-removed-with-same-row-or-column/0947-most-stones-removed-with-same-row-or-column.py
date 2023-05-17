class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {(r,c):(r,c) for r,c in stones}
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        def union(ver1,ver2):
            parent[find(ver1)] = find(ver2)
        for r,c in stones:
            for i,j in stones:
                if (i == r or c==j) and not(i==r and c==j):
                    union((r,c),(i,j))
        ans = set()
        for r,c in stones:
            ans.add(find((r,c)))
        return len(stones) - len(ans)