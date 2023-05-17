class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dic = defaultdict(list)
        ansd =  defaultdict(set)
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
            for course in dic[x]:
                pre_req[course] -= 1
                for i in ansd[x]: ansd[course].add(i)
                ansd[course].add(x)
                if pre_req[course] == 0: queue.append(course)
        for i,j in queries: ans.append(j in ansd[i])
        return ans
        