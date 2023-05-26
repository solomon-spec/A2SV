from math import ceil
a, b, c = map(int,input().split())
x = (a + b + c)//3
ans = abs(x-a) + abs(x-b) + abs(x-c)
print(ans)