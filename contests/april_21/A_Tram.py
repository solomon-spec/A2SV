from itertools import accumulate
n = int(input())
arr = [0]*n
for _ in range(n):
    x, y = map(int,input().split())
    arr[_] +=(y - x)
print(max(accumulate(arr)))
