class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        arr = [0]*len(graph)
        dic = defaultdict(list)
        for i in range(len(graph)):
            for j in graph[i]:
                dic[j].append(i)
                arr[i]+=1
        queue = deque()
        for i in range(len(arr)):
            if arr[i] == 0 : queue.append(i)
        ans = []
        print(queue)
        while queue:
            x = queue.popleft()
            ans.append(x)
            for num in dic[x]:
                arr[num] -= 1
                if arr[num] == 0: queue.append(num)
        return sorted(ans)