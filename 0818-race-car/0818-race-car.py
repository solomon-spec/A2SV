class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1,0)])
        visited = set()
        while queue:
            
            pos,speed,cost = queue.popleft()
            if pos == target: return cost
            if (pos,speed) in visited: continue
            visited.add((pos,speed))
            queue.append((pos+speed,speed*2,cost+1))
            
            if (pos+speed - target)*speed > 0:
                speed = -1 if speed > 0 else 1
                queue.append((pos,speed,cost+1))
                
                