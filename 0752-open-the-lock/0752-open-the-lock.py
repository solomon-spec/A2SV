class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set([tuple(map(int,a)) for a in deadends])
        first = [0,0,0,0]
        target = list(map(int,list(target)))
        if tuple(first) not in dead:
            queue = deque([[first,0]])
            visited = set([tuple(first)])
        else: return -1
        if target == [0,0,0,0]:return 0
        found = False
        
        while queue:
            x = queue.popleft()
            for i in range(8):
                num = x[0].copy()
                if i//4 == 0:num[i%4] =(num[i%4] - 1) % 10
                else: num[i%4] = (num[i%4] + 1) % 10
                if tuple(num) not in visited and tuple(num) not in dead:
                    #print(num)
                    queue.append([num,x[1]+1])
                    visited.add(tuple(num))
                    if target == num:
                        print(x,num)
                        found = True
                        break
            if found: break
        if found: return x[1]+1
        else: return -1
                    
                    
                    
                