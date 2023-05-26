import heapq
for _ in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))
    x = min(sum(ar)//2,sum(ar)-max(ar))
    arr = [ [j,i] for i, j in enumerate(ar)]
    arr2 = [ [-j,i] for i, j in enumerate(ar)]
    heapq.heapify(arr)
    heapq.heapify(arr2)
    print(x)
    
    while x > 0:
        #print(arr,arr2)
        if arr[0][1] != arr2[0][1]:
            if arr[0][0] == 0: heapq.heappop(arr)
            if arr2[0][0] == 0: heapq.heappop(arr)
            print(arr[0][1]+1,arr2[0][1]+1)
            y = heapq.heappop(arr)
            y[0] -= 1
            heapq.heappush(arr,y)
            z = heapq.heappop(arr2)
            z[0] += 1
            heapq.heappush(arr2,z)

            x -= 1
        else:
            heapq.heappop(arr)

