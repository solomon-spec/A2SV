import sys
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
 
def solve():
    n,m = get_ints()
    dic = defaultdict(int)
    x = minn = min(n,m)
    maxx  = max(n,m)
    i = 2
    while i*i <= x:
        if minn % i == 0 and maxx % i == 0:
            dic[i] += 1
            minn //= i
            maxx //= i
        else:
            i += 1
    if minn != 1 and maxx % minn == 0:
        dic[minn] += 1
    new = []
    for i in dic:
        new += [i]*dic[i]
    num = 2**len(new) - 1
    ans = set()
    while num >= 0:
        cur = 1
        for i in range(len(new)):
            if num & (1<<i) != 0: cur *= new[i]
        ans.add(cur)
        num -= 1
    ans = sorted(list(ans))
    for _ in range(get_int()):
        x,y = get_ints()
        ind = bisect_right(ans,y)
        if ans[ind-1] >= x: print(ans[ind-1])
        else: print(-1)



    
    
    
    
 
 
 
if __name__ == "__main__":
    solve()