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
    new = []
    powr = 0
    for i in arr:
        num = i
        while num % 2 == 0:
            num //= 2
            powr += 1
        new.append(num)
    maxx = max(new)
    return sum(new) + maxx*(pow(2,powr)) - maxx


    
    
    
    
 
 
 
if __name__ == "__main__":
    for _ in range(get_int()):
        print(solve())