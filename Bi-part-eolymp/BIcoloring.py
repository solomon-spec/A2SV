from collections import defaultdict
t = int(input())
while t != 0:
    n = int(input())
    graph = defaultdict(list)
    for i in range(n):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    def dfs(root):
        stack = [root]
        if root not in color: color[root] = 1
        while stack:
            x = stack.pop()
            for i in graph[x]:
                if i not in color:
                    stack.append(i)
                    color[i] = 1 - color[x]
                else:
                    if color[i] == color[x]:
                        return False
        return True

    color = {}
    bipart = True
    for i in range(t):
        if i not in color:
            if not dfs(i):
                print("NOT BICOLOURABLE.")
                bipart = False
                break
    if bipart:
        print("BICOLOURABLE.")
    t = int(input())
