class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cur = n**2
        graph = {}
        if n % 2 == 0: dec = True
        else: 
            dec = False
            cur -= (n-1)
        for i in range(n):
            for j in range(n):
                graph[cur] = board[i][j]
                if dec: cur -= 1
                else: cur += 1
          
            if dec: cur  -= (n-1)
            else: cur -= (n+1)
            dec = not dec
        queue = deque([(1,0)])
        visited = set([1])
        while queue:
            x,y = queue.popleft()
            if x == 14: print(graph[x],y)
            if graph[x] != -1 : x = graph[x]
            if x == n**2: return y
            for i in range(1,7):
                new = x + i
                if new == n**2 or graph[new] == n**2: return y + 1
                if new < n**2 and new not in visited:
                    visited.add(new)
                    queue.append((new,y+1))
        return -1        
                