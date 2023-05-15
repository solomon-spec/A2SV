class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i in range(len(parent)):
            if parent[i]>-1: graph[parent[i]].append(i)
        self.max = 0
        def dfs(root):
            y = [0,0]
            for i in graph[root]:
                x = dfs(i)
                if x[0] != s[root]:
                    heappushpop(y,x[1])
            self.max = max(self.max,y[0]+y[1]+1)
            return(s[root],y[1] + 1)
        dfs(0)
        return self.max
            