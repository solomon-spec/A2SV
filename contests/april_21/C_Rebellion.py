for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr2 = sorted(arr)
    tot = 0
    for i in range(n):
        tot += arr[i]^arr2[i]
    print(tot//2)
