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
    n = get_int()
    div = defaultdict(int)
    i = 2
    x = n
    while i*i <= x:
        if n % i == 0:
            n //=i
            div[i] += 1
        else:
            i += 1
    if n != 1: div[n] += 1
    arr = sorted([pow(i,div[i]) for i in div.keys()])
    print(arr)
    a = 1
    b = 1
    num = 2**len(arr) - 1
    ans = set()
    pd = []
    while num >= 0:
        cur = 1
        for i in range(len(arr)):
            if num & (1<<i) != 0: cur *= arr[i]
        ans.add(cur)
        num -= 1
    ans = sorted(list(ans))
    new = []
    for i in ans:
        new.append(max(i,x//i))
    ret = min(new)
    
    return ret,x//ret

    
    
    
    
 
 
 
if __name__ == "__main__":
    print(*solve())