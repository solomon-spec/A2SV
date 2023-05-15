class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        def dfs(root,visited):
            apple = hasApple[root]
            tot = 0
            for i in graph[root]:
                if i not in visited:
                    visited.add(i)
                    x = dfs(i,visited)
                    if x[0]:
                        tot += x[1] +2
                        apple = True
            return [apple,tot]
        x = dfs(0,set([0]))
        return x[1]
        
        