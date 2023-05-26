n, m = map(int,input().split())
ans = []
yes = True
while m > n:
    ans.append(m)
    if m % 2 == 0:
        m //= 2
    elif (m - 1) % 10 == 0:
        m -= 1
        m //= 10
    else:
        yes = False
        break
if yes == False or n != m:
    print("NO")
if n == m:
    print("YES")
    print(len(ans)+1)
    print(*([n] +list(reversed(ans))))