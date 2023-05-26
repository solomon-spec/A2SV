from collections import defaultdict
def check():
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    g = defaultdict(list)
    for _ in range(m):
        x,y = map(int,input().split())
        g[x].append(y)
        g[y].append(x)
    visited = set()
    ans = 0
    for i in range(1,n+1):
        if i not in visited:
            stack = [i]
            minn = arr[i-1]
            while stack:
                root = stack.pop()
                minn = min(minn,arr[root-1])
                visited.add(root)
                for i in g[root]:
                    if i not in visited:
                        stack.append(i)
            ans += minn    

    print(ans)
check()
