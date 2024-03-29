class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = {}
        dic = defaultdict(list)
    
        for i in range(len(s)):
            parent[s[i]+str(i)] = s[i]+str(i)
            heapify(dic[s[i]+str(i)])
            
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        
        def union(ver1,ver2):
            letter1 = find(ver1)
            letter2 = find(ver2)
            if letter1 > letter2:
                parent[letter1] = letter2
            else:
                parent[letter2] = letter1
                
        for i,j in pairs:
            union(s[i]+str(i),s[j]+str(j))
            
        ans = []
        dic = defaultdict(list)
        
        for i in range(len(s)): 
            heappush(dic[find(s[i]+str(i))],s[i])
            
        for i in range(len(s)):
            ans.append(heappop(dic[find(s[i]+ str(i))]))
            
        return "".join(ans)