class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def sort_group(m):
            arr2 = defaultdict(int)
            cur_dic = defaultdict(list)
            for i in (group_dic[m]):
                for j in group_dep[i]:
                    if group[i] == group[j]:
                        cur_dic[i].append(j)
                        arr2[j] += 1
            queue = deque()
            for i in (group_dic[m]):
                if arr2[i]==0: queue.append(i)
            ans = []
            while queue:
                x = queue.popleft()
                ans.append(x)
                for i in cur_dic[x]:
                    arr2[i] -= 1
                    if arr2[i] == 0: queue.append(i)
            return ans
        for i in range(len(group)):
            if group[i]== -1:
                group[i] = m
                m += 1
                
        arr = [0]*m
        dic = defaultdict(list)
        group_dic = defaultdict(list)
        group_dep = defaultdict(list)
        
        for i in range(n): group_dic[group[i]].append(i)
            
        for i in range(len(beforeItems)):
            cur = beforeItems[i]
            for x in cur:
                gr = group[x]
                if gr != group[i]:
                    dic[gr].append(group[i])
                    arr[group[i]] += 1
                else:
                     group_dep[x].append(i)
                        
        queue = deque([])    
        for i in range(len(arr)):
            if arr[i] == 0: queue.append(i)
        groups = []
        while queue:
            x = queue.popleft()
            groups.append(x)
            for i in dic[x]:
                arr[i] -= 1
                if arr[i] == 0: queue.append(i)
        ans = []
        for i in groups:
            ans.extend(sort_group(i))
        if len(ans) == n:return ans
        return []
        
        
        