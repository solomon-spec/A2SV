from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    color = {}
        for i in range(v):
            if i not in color:
                color[i] = -1
                stack = [(i,-1)]
                while stack:
                    x = stack.pop()
                    for j in adj[x[0]]:
                        if j != x[1]:
                            if j in color: 
                                return True
                            else:
                                stack.append((j,x[0]))
                                color[j] = x[0]
        return False
		                    
		                
		    


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends