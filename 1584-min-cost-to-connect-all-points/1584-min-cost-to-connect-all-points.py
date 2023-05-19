class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = [i for i in range(len(points))]
        rank = [1 for i in range(len(points))]
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        
        def union(ver1,ver2): 
            x = find(ver1)
            y = find(ver2)
            if x == y: return False
            if rank[x] > rank[y]:
                parent[y] = x
                rank[x] += rank[y]
            else: 
                parent[x] = y
                rank[y] += rank[x]
            return True
        path = [] 
        
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    pt1,pt2 = points[i],points[j]
                    leng = abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])
                    path.append([leng,i,j])
        
        path.sort()
        ans = 0
        for k,i,j in path:
            if union(i,j):
                ans += k
        return ans
            
            
            
            
            
            
            
            
            
                