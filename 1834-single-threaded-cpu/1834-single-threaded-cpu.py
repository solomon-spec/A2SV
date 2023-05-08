class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        time = 0
        task = [[i[1],j,i[0]] for j, i in enumerate(tasks)]
        task.sort(key = lambda x: x[2])
        heap = []
        i = 0
        ans = []
        while i < len(task):
            if not heap: time = max(time,task[i][2])
            while i < len(task) and task[i][2] <= time:
                    heappush(heap,task[i])
                    i += 1
            x = heappop(heap)
            time += x[0]
            ans.append(x[1])
        while heap: ans.append(heappop(heap)[1])
        return ans
                
        