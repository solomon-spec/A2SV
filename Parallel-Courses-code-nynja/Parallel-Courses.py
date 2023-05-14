from collections import defaultdict,deque
def parallelCourses(n, edges):
    tot_time = [0]*n  
    pre_req = [0]*n
    graph = defaultdict(list)
    graph2 = defaultdict(list)
    for pre,post in edges: 
        graph[post-1].append(pre-1)
        pre_req[post-1] += 1
        graph2[pre-1].append(post-1)
    pre_req2 = pre_req.copy()
    visited = set()
    def dfs(root):
        nonlocal visited
        nonlocal tot_time
        visited.add(root)
        ans = 0
        for i in graph[root]:
            if i not in visited:
                ans = max(ans,dfs(i))
            else:
                ans = max(ans,tot_time[i])
        tot_time[root] = ans + 1
        return ans + 1
    for i in range(n):
        if i not in visited: dfs(i)
    queue = deque()
    for i in range(len(pre_req)):
        if pre_req2[i] == 0: queue.append(i)
    xx = []
    while queue:
        x = queue.popleft()
        xx.append(x)
        for i in graph2[x]:
             pre_req2[i] -= 1
             if pre_req2[i] == 0: queue.append(i)
    if len(xx) != len(tot_time): return(-1)
    else: return max(tot_time)
