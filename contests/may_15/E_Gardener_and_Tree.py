from collections import defaultdict,deque
for _ in range(int(input())):
    input()
    n,k = map(int,input().split())
    dic = defaultdict(list)
    pre_req = [0]*n
    for i in range(n-1):
        x,y = map(int,input().split())
        dic[x-1].append(y-1)
        dic[y-1].append(x-1)
        pre_req[x-1] += 1
        pre_req[y-1] += 1
    queue = deque()
    for i in range(n):
        if pre_req[i]<=1: queue.append(i)
    visited = set(queue)
    ans = 0
    for i in range(k):
        arr = []
        if ans == n: break
        while queue:
            x = queue.pop()
            ans += 1
            for i in dic[x]:
                if i not in visited:
                    pre_req[i] -= 1
                    if pre_req[i] == 1: 
                        arr.append(i)
                        visited.add(i)
        queue = deque(arr)
    print(n-ans)
    #print(n-ans)
                

    