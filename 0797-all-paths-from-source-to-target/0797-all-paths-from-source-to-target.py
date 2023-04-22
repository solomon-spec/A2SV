class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(root,path):
            nonlocal ans
            if root == len(graph) - 1:
                path.append(root)
                ans.append(path.copy())
                return
            path.append(root)
            for child in graph[root]:
                dfs(child,path.copy())
            return
        dfs(0,[])
        return ans
    
                