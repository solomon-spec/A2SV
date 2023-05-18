class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        graph_row = defaultdict(list)
        graph_col = defaultdict(list)
        
        pre_row = {i:0 for i in range(1,k+1)}
        pre_col = {i:0 for i in range(1,k+1)}
        
        matrix = [[0]*k for i in range(k)]
        
        for i,j in rowConditions:
            graph_row[i].append(j)
            pre_row[j] += 1
        
        for i,j in colConditions:
            graph_col[i].append(j)
            pre_col[j] += 1
        
        def return_order(graph,pre):
            ans = {}
            place = 0
            queue = deque()
            for i in range(1,k+1):
                if pre[i] == 0: queue.append(i)
        
            while queue:
                x = queue.popleft()
                ans[x] = place
                place += 1
                
                for i in graph[x]:
                    pre[i] -= 1
                    if pre[i] == 0: queue.append(i)
            return ans
        
        row_order = return_order(graph_row,pre_row)
        col_order  = return_order(graph_col,pre_col)
        for i in range(1,k+1):
            if i in row_order and i in col_order:
                r = row_order[i]
                c = col_order[i]
                matrix[r][c] = i
            else: return
        
        return matrix
        
                
        
        
        