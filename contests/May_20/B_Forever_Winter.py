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
    graph = [0]*(n+1)
    for _ in range(m):
        x,y = get_ints()
        graph[x] += 1
        graph[y] += 1
    g2= Counter(graph[1:])
    c = 1
    d = 1
    for i in g2:
        if g2[i] == 1 and i != 1:
            c = i
        elif g2[i] > 1 and i != 1:
            d = i
    if c == 1: c = d
    return [c,d-1]



 
    
 
if __name__ == "__main__":
    for i in range(get_int()):
        print(*solve())