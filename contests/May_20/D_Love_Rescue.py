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
    parent = {chr(97+i):chr(97+i) for i in range(26)}

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
        if x==y: return 0
        if x> y:
            parent[y] = parent[x]
        else:
            parent[x] = parent[y]
        return 1
    n = get_int()
    word1 = input()
    word2 = input()
    ans = 0
    arr = []
    for i in range(n):
        if word1[i] != word2[i]:
            x = union(word1[i],word2[i])
            ans += x
            if x: arr.append([word1[i],word2[i]])
    return arr

 
    
 
if __name__ == "__main__":
    ans = solve()
    print(len(ans))
    for i in range(len(ans)): print(*ans[i])