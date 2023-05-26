import heapq
for _ in range(int(input())):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))

    arr2 = map(int,input().split())
    for num in arr2:
        arr.sort()
        arr[0] = num
        
    print(sum(arr))
