class Solution:
    def nearestExit(self, mat: List[List[str]], entrance: List[int]) -> int:
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        n, m = len(mat), len(mat[0])
        def is_valid(i,j):
            if 0 <= i < n and 0 <= j <m: 
                if mat[i][j]== ".": return True 
            return False
        def is_exit(i,j):
            if i == 0 or i == n-1 or j == 0 or j == m - 1:return True
            return False
        
        queue = deque([entrance+[0]])
        visited = set([tuple(entrance)])
        while queue:
            cur = queue.popleft()
            k = cur[2]
            for i,j in dire:
                x = i + cur[0]
                y = j + cur[1]
                if is_valid(x,y) and (x,y) not in visited:
                    if is_exit(x,y) and (x,y) != tuple(entrance): return k+1
                    queue.append([x,y,k+1])
                    visited.add((x,y))
        return -1