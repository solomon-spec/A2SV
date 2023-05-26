from collections import defaultdict
n  = int(input())
dic = defaultdict(int)
for _ in range(1,n + 1):
    x = int(input())
    if x != -1:
        dic[_] = x
def dfs(max_len,x):
    if dic[x] != 0:
        maxx = dfs(max_len + 1,dic[x])
        max_len = max(max_len,maxx)
    return max_len
ans = 0
for i in range(1,n + 1):
    ans = max(ans,dfs(1,i))
print(ans)