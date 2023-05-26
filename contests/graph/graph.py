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
    dic = defaultdict(set)
    n = get_int()
    k = get_list()
    for _ in range(k):
        arr = get_list()
        if len(arr) == 3: 
            dic[arr[1]].add(arr[2])
            dic[arr[2]].add(arr[1])
        else:
            if dic[arr[1]]: print(*dic[arr[1]])




    
    
 
 
 
if __name__ == "__main__":
    print(solve())