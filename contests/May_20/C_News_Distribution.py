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
    parent = [i for i in range(n)]
    def find(child):
        stack = []
        while child != parent[child]: 
            child = parent[child]
            stack.append(child)
        for i in stack: parent[i] = parent[child]
        return parent[child]
    def union(ver1,ver2): 
        x = find(ver1)
        y = find(ver2)
        if x> y:
            parent[y] = parent[x]
        else:
            parent[x] = parent[y]
    for _ in range(m):
        group = get_list()[1:]
        group = [i-1 for i in group]
        for i in range(len(group)):
            if i == 0 and i < len(group)-1:
                union(group[i],group[i+1])
            elif i == len(group)-1:
                union(group[i],group[i-1])
            else:
                union(group[i],group[i-1])
                union(group[i],group[i+1])
    counter = defaultdict(int)
    for i in range(n):
        counter[find(i)] += 1
    ans = []
    for i in range(n):
        ans.append(counter[find(i)])
    return ans

 
    
 
if __name__ == "__main__":
        print(*solve())