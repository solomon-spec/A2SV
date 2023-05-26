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
    k = get_int()
    ans = []
    for i in range(k):
        arr = set(get_list()[1:])
        cur_arr = []
        for i in range(1,k+1):
            if i in arr: cur_arr.append(1)
            else: cur_arr.append(0)
        ans.append(cur_arr)
    for i in ans: print(*i)
    





    
    
 
 
 
if __name__ == "__main__":
    solve()