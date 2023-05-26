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
    row = defaultdict(int)
    col = defaultdict(int)
    n = get_int()
    for r in range(n):
        arr = get_list()
        for c in range(n):
            if arr[c] == 1: col[c] += 1
        if 1 in arr:
            row[r] = sum(arr)
    ans = []
    for i in range(n):
        if i not in row:
            ans.append(i + 1)
    

    ans2 = []
    for i in range(n):
        if i not in col: ans2.append(i + 1)
    print(*([len(ans2)] + ans2))
    print(*([len(ans)] + ans))





    
    
 
 
 
if __name__ == "__main__":
    solve()