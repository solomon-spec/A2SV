from itertools import combinations
from collections import defaultdict
n,m = map(int,input().split())
names = []
dic = defaultdict(set)
for _ in range(n):
    names.append(input())
for _ in range(m):
    x,y =input().split()
    dic[x].add(y)
    dic[y].add(x)
def check_true(arr):
    for i in arr:
        for j in arr:
            if j in dic[i]: return False
    return True
for i in range(n,0,-1):
    x  = list(combinations(names,i))
    done = False
    for comb in x:
        if check_true(comb):
            ans = comb
            done = True
            break
    if done: break
ans = sorted(list(ans))
print(len(ans))
for i in ans: print(i)


    

