class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        dic = defaultdict(set)
        for i in range(len(accounts)):
            dic[(i,accounts[i][0])] = set(accounts[i][1:])
          
        parent = {(i,j):(i,j) for i,j in dic}
        
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        
        def union(ver1,ver2):
            x = find(ver1)
            y = find(ver2)
            if x[0] < y[0]:parent[x] = y
            else: parent[y] = x
                
        
        for per1 in dic:
            for per2 in dic:
                if per1 != per2 and per1[1] == per2[1]:
                    for i in dic[per1]:
                        if i in dic[per2]: union(per1,per2)
        ans = []
        for par in parent:
            x = find(par)
            dic[x].update(dic[par])
        for i in parent:
            if parent[i] == i:
                arr = [i[1]] + list(sorted(list(dic[i])))
                ans.append(arr)
        return ans
        
            