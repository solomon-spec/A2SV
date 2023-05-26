n  = int(input())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
c1,c2 = map(int,input().split())
if (a1 - b1)*(a1 - c1) > 0 and (a2 - b2)*(a2 - c2) > 0:
    print("YES")
else:
    print("NO")