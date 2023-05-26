class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dic = defaultdict(list)
        for j in range(len(routes)):
            for i in routes[j]:
                dic[i].append(j)
        if source == target: return 0
        queue = deque([(source,0)])
        visited = set()
        while queue:
            x = queue.popleft()
            for j in dic[x[0]]:
                if j not in visited:
                    for i in routes[j]:
                        if i == target: return x[1]+ 1
                        queue.append((i,x[1]+1))
                    visited.add(j)
        return -1
                    