n,m  = map(int,input().split())
arr = list(map(int,input().split()))
ai = 1
while ai < m:
    ai += arr[ai-1]
if ai ==m: print("YES")
else: print("NO")