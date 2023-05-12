from typing import List

from collections import defaultdict,deque
from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        self.tot_time = [0]*n  
        pre_req = [0]*n
        graph = defaultdict(list)
        for pre,post in edges: 
            graph[post-1].append(pre-1)
            pre_req[post-1] += 1
        self.visited = set()
        def dfs(root):
            self.visited.add(root)
            ans = 0
            for i in graph[root]:
                if i not in self.visited:
                    ans = max(ans,dfs(i))
                else:
                    ans = max(ans,self.tot_time[i])
            self.tot_time[root] = ans + 1
            return ans + 1
        for i in range(n):
            if i not in self.visited: dfs(i)
        answ = []
        return " ".join(list(map(str,self.tot_time)))
            


#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends