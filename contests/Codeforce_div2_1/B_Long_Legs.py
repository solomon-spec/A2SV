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
    n, k = get_ints()
    ans = 0
    m = 1
    minn = min(n,k)
    maxx = max(n,k)
    def isPrime(x):
            if x == 1: return 1
            for i in range(ceil((n+k)**0.5),1,-1):
                if x % i == 0:
                    return (i)
            return x
    div = isPrime(gcd(n,k))
    ans += (minn// div +(div - 1))
    div2 = isPrime(maxx)
    ans += (maxx// div2 +(div2 - div))
    return ans

    
    
    
    
 
 
 
if __name__ == "__main__":
    for _ in range(get_int()):
        print(solve())