class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        pre_req = [0]*numCourses
        for i,j in prerequisites:
            dic[j].append(i)
            pre_req[i] += 1
        ans = []
        queue = deque()
        for i in range(numCourses):
            if pre_req[i] == 0: queue.append(i)
        visited = set([i for i in queue])
        while queue:
            x = queue.popleft()
            ans.append(x)
            for course in dic[x]:
                pre_req[course] -= 1
                if pre_req[course] == 0: queue.append(course)
        if len(ans) == numCourses:
            return ans
        else: return []