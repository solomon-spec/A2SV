for _ in range(int(input())):
    n,m = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr1.sort(reverse = True)
    arr2.sort(reverse = True)
    if m >= n:
        ans = arr2[:n]
    else:
        ans = arr2 + arr1[:n-m]
    print(sum(ans))
    9014959271
    9178013311