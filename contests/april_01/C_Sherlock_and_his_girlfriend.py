
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
def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
            
 
def solve():
    n = get_int()
    ans = []
    for i in range(n):
        if isPrime(i+2): ans.append(1)
        else: ans.append(2)
    if n < 3: print(1)
    else: print(2)
    return ans



    
    
    
    
 
 
 
if __name__ == "__main__":
    print(*solve())