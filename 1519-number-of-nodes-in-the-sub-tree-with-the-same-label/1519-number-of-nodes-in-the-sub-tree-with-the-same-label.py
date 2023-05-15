class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = defaultdict(list)
        for i,j in edges: 
            graph[i].append(j)
            graph[j].append(i)
        self.ans = [0]*n
        def dfs(root,visited):
            dic = defaultdict(int)
            for i in graph[root]:
                if i not in visited:
                    visited.add(i)
                    x = dfs(i,visited)
                    
                    for let in x: dic[let] += x[let]
            dic[labels[root]] += 1
            self.ans[root] = dic[labels[root]]
            return dic
        dfs(0,set([0]))
        return self.ans