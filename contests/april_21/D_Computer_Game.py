t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(map(int,list(input())))
    arr2 = list(map(int,list(input())))
    yes = True
    for i in range(n):
        if arr1[i] == arr2[i] == 1:
            yes = False
            break
    if yes: print("YES")
    else: print("NO")
