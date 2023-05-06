class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        dic = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    x = abs(bombs[i][0] - bombs[j][0])
                    y = abs(bombs[i][1] - bombs[j][1])
                    r = bombs[i][2]
                    if x**2 + y**2 <= r**2: dic[i].append(j)
        def dfs(root,ans,visited):
            visited.add(root)
            for i in dic[root]:
                if i not in visited:
                    x = dfs(i,0,visited)
                    ans += x
            return ans +1
        maxx = 0
        for i in range(len(bombs)):
            maxx = max(maxx,dfs(i,0,set()))
        return maxx