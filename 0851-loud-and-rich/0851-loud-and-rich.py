class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        dic = defaultdict(list)
        ansd =  defaultdict(set)
        pre_req = [0]*len(quiet)
        for i,j in richer:
            dic[i].append(j)
            pre_req[j] += 1
        ans = []
        queue = deque()
        for i in range(len(quiet)):
            if pre_req[i] == 0: queue.append(i)
        visited = set([i for i in queue])
        while queue:
            x = queue.popleft()
            for course in dic[x]:
                pre_req[course] -= 1
                for i in ansd[x]: ansd[course].add(i)
                ansd[course].add(x)
                if pre_req[course] == 0: queue.append(course)
        for i in range(len(quiet)):
            cur = None
            for ric in ansd[i]:
                if(cur == None and quiet[i] > quiet[ric] )or (quiet[i] > quiet[ric] and quiet[ric] < quiet[cur]):                    cur = ric
            if cur != None: ans.append(cur)
            else: ans.append(i)
        return ans
        