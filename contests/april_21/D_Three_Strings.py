i = int(input())
for i in range(i):
    a = input()
    b = input()
    c = input()
    f = True
    for i in range(len(a)):
        if a[i] != c[i] and b[i] != c[i]:
            f = False 
            break
    if f: print("YES")
    else: print("NO")