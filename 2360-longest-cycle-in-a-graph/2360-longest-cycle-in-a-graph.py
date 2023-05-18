class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        color = {}
        maxi = -1
        cycle = set()
        
        for i in range(len(edges)):
            if i not in color:
                cur_count = set()
                stack = [(i,-1)]
                cur_count.add(i)
                while stack:
                    x = stack.pop()
                    color[x[0]] = x[1]
                    j = edges[x[0]]
                    if j != -1:
                        if j in color and j not in cycle:
                            leng = 1
                            cur = x[0]
                            dest = j
                            while cur != dest:
                                cycle.add(cur)
                                cur = color[cur]
                                leng += 1
                            cycle.add(dest)
                            maxi = max(maxi,leng)
                        elif j not in color:
                            stack.append((j,x[0]))
                            cur_count.add(j)
                cycle.update(cur_count)
        return maxi
        return maxi
