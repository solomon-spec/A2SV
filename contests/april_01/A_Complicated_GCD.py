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
    dic = defaultdict(list)
    for i in range(k):
        arr = get_list()
        for j in range(len(arr)):
            if arr[j] == 1: dic[i+1].append(j + 1)
    for i,j in sorted(dic.items()):
        print(*([len(j)] + j))





    
    
 
 
 
if __name__ == "__main__":
    solve()