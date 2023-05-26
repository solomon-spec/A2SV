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
    n = get_ints()
    arr = get_list()
    for i in range(len(arr)):
        visit = set()
        x = i
        while x+1 not in visit:
            visit.add(x + 1)
            x = arr[x] - 1
        if len(visit) == 3 and x==i: 
            return "YES"
    return "NO"

    
    
    
    
 
 
 
if __name__ == "__main__":
    print(solve())