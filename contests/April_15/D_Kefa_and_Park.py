import sys
import threading
import math
import bisect
import heapq
import itertools
from itertools import accumulate
from sys import stdin,stdout
from math import gcd,floor,sqrt,log, ceil
from collections import defaultdict, Counter, deque
from bisect import bisect_left,bisect_right, insort_left, insort_right
mod=1000000007
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_list_strings(): return list(map(str, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10**5 + 1)
n, m = get_ints()
threading.stack_size(10**5)
arr = get_list()
dic = defaultdict(list)
for _ in range(n - 1):
    x, y = get_ints()
    dic[x].append(y)
    dic[y].append(x)
 
def dfs(root,pre,visited):
    ans  = 0
    visited.add(root)
    if root != 1 and len(dic[root]) == 1:
        if pre + arr[root - 1] <= m:
            return 1
        else: return 0
    if (pre + arr[root - 1])*arr[root - 1] <= m:
        for i in dic[root]:
            if i not in visited:
                ans += dfs(i,(pre + arr[root - 1])*arr[root - 1],visited)
    return ans
tot = 0
tot += dfs(1,0,set())
print(tot)
threading.Thread(target=main).start()