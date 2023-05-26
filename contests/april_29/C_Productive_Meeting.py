import heapq
for _ in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))
    arr = [[-i,j] for j,i in enumerate(ar)]
    heapq.heapify(arr)
    z = min(sum(ar)//2,sum(ar)-max(ar))
    print(z)
    while z > 0:
        x = heapq.heappop(arr)
        y = heapq.heappop(arr)
        x[0] += 1
        y[0] += 1
        print(x[1]+1,y[1]+1)
        heapq.heappush(arr,x)
        heapq.heappush(arr,y)
        z -= 1
