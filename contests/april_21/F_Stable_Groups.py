import math
a, b,c = map(int,input().split())
arr = sorted(list(map(int,input().split())))
dif = []
for i in range(1,a):
    if arr[i] - arr[i-1] > c:
        dif.append(arr[i] - arr[i-1])
        
dif.sort(reverse = True)
i = len(dif) - 1
while b > 0 and dif:
    if dif[i]-c <= c*b:
        b -= math.ceil((dif[i]-c)/c)

        dif.pop()
        i -= 1
    else: break
print(len(dif)+1)
