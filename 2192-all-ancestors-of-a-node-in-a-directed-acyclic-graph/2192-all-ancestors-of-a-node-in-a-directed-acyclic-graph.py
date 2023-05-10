class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        preg = defaultdict(list)
        num = [0]*n
        ans = [set() for i in range(n)]
        for i in edges:
            preg[i[0]].append(i[1])
            num[i[1]] += 1
        queue = deque()
        for i in range(n):
            if num[i] == 0: queue.append(i)
        while queue:
            x = queue.pop()
            for nums in preg[x]:
                ans[nums].add(x)
                for i in ans[x]: ans[nums].add(i)
                num[nums] -= 1
                if num[nums] == 0: queue.append(nums)
        answer = [sorted(list(i)) for i in ans]
        return answer
                