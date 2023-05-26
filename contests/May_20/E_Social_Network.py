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
    parent = [i for i in range(n)]
    ma = defaultdict(int)
    ma[1] = n
    maxi = [1 for i in range(n)]
    def find(child):
        stack = []
        while child != parent[child]: 
            child = parent[child]
            stack.append(child)
        for i in stack: parent[i] = parent[child]
        return parent[child]
    def union(ver1,ver2): 
        x = find(ver1)
        y = find(ver2)
        if x==y: return 1
        ma[maxi[x]] -= 1
        if ma[maxi[x]] == 0:
            del ma[maxi[x]]
        ma[maxi[y]] -= 1
        if ma[maxi[y]] == 0:
            del ma[maxi[y]]
        ma[maxi[x] + maxi[y] ] += 1
        if x> y:
            parent[y] = parent[x]
            maxi[x] += maxi[y]
        else:
            parent[x] = parent[y]
            maxi[y] += maxi[x]
        
        return 0
    
    ans = 1
    conn = []
    for _ in range(m):
        x,y = get_ints()
        conn.append((x-1,y-1))
    
    for _ in range(m):
        maxx = 0
        x,y = conn[_]
        ans += union(x,y)
        tot = 0
        i = 0
        arr = sorted(ma.keys(),reverse = True)
        while tot < ans:
            if ans - tot >= ma[arr[i]]:
                tot += ma[arr[i]]
                maxx += ma[arr[i]]*arr[i]
                i += 1
            else:
                maxx += (ans - tot)*arr[i]
                tot = ans
        print(maxx-1)

       
                
 
    
 
if __name__ == "__main__":
    solve()