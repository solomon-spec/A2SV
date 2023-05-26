for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    inc = False
    good  = True
    for i in range(1,len(arr)):
        if not inc:
            if arr[i] > arr[i-1]:inc = True
        else:
            if arr[i] < arr[i-1]: good = False
    if good: print("YES")
    else: print("NO")