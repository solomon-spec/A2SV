from collections import defaultdict,deque
import sys
n,m = map(int,input().split())
dic = defaultdict(list)
arr = []
arr2 = [0]*n
for _ in range(m):
    a,b = map(int,input().split())
    dic[a-1].append(b-1)
    dic[b-1].append(a-1)
    arr.append((a-1,b-1))
    arr2[a-1] += 1
    arr2[b-1] += 1  
ans = [0]*n
visited = set()
cycle = False

def isBipartite(graph):
    color = {}
    for i in range(len(graph)):
        if i not in color:
            color[i] = 0
            if not dfs(i, graph, color):
                return [False]
        return (True, color)

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

x = isBipartite(dic)
if x[0]:
    print("YES")
    answer = []
    for i in range(m):
        if x[1][arr[i][0]] == 0: answer.append(1)
        else: answer.append(0)
    print("".join(list(map(str,answer))))
else:
    print("NO")





