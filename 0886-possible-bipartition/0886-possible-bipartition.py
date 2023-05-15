class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(pos, graph, color):
            stack = [pos]
            while stack:
                pos = stack.pop()
                for i in graph[pos]:
                    if i in color:
                        if color[i] == color[pos]:
                            return False
                    else:
                        color[i] = 1 - color[pos]
                        stack.append(i)
            return True
        graph = defaultdict(list)
        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        color = {}
        print(graph)
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i, graph, color):
                    return False
        return True

        
                    
                