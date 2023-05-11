class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        child = [0]*n
        
        for i,j in edges:
            dic[i].append(j)
            dic[j].append(i)
            child[i] += 1
            child[j] += 1
            
        queue = deque()
        for i in dic:
            if len(dic[i]) == 1: queue.append(i)
        ans = [0]*n
        e = n-1
        visited = set(queue)
        while e > 1:
            x = queue.popleft()
            e -= 1
            for i in dic[x]:
                child[i] -= 1
                if i not in visited:
                    ans[i] = max(ans[i],ans[x]+1)
                if child[i] == 1: 
                    queue.append(i)
                    visited.add(i)
        maxx = max(ans)
        answer = []
        for i in range(len(ans)):
            if ans[i] == maxx: answer.append(i)
        return answer
            
        