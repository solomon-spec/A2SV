class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i,j in adjacentPairs:
            dic[i].append(j)
            dic[j].append(i)
        ans = []
        for i in dic:
            if len(dic[i])==1:
                ans.append(i)
                break
        visited = set(ans)
        print(dic)
        while len(ans) <= len(adjacentPairs):
            x = ans[-1]
            for i in dic[x]:
                if i not in visited: 
                    ans.append(i)
                    visited.add(i)
        
        return ans
            
            