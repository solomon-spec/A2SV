from collections import defaultdict
def ans():
    dic = defaultdict(list)
    cost = defaultdict(int)
    x = int(input())
    for _ in range(x):
        n,m,k = map(int,input().split())
        dic[n].append(m)
        dic[m].append(n)
        cost[(m,n)] = k
    total = 0
    total2 = 0
    def dfs(root,visited):
        if root == 1 and visited: return
        nonlocal total
        if dic[root][0] != visited:
            total+= cost[(root,dic[root][0])]
            dfs(dic[root][0],root)
        else:
            total+= cost[(root,dic[root][1])]
            dfs(dic[root][1],root)


    def dfs2(root,visited):
        nonlocal total2
        if root == 1 and visited: return

        if dic[root][1] != visited:
            total2+= cost[(root,dic[root][1])]
            dfs2(dic[root][1],root)
        else:
            total2+= cost[(root,dic[root][0])]
            dfs2(dic[root][0],root)
    dfs(1,None)
    dfs2(1,None)
    print(min(total,total2))
ans()