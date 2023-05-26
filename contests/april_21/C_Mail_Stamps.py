from collections import defaultdict
n = int(input())
dic = defaultdict(list)
for _ in range(n):
    x, y = map(int,input().split())
    dic[x].append(y)
    dic[y].append(x)
for i in dic:
    if len(dic[i]) == 1:
        start = i
        break

ans = [start]
visited = set([start])
cur = dic[start][0]
for i in range(n-1):
    ans.append(cur)
    visited.add(cur)
    if dic[cur][0] not in visited: cur = dic[cur][0]
    else: cur = dic[cur][1]
print(*(ans +[cur]))
