class LockingTree:

    def __init__(self, parent: List[int]):
        self.paren = parent
        self.locks = [-1]*len(parent)
        
        graph = defaultdict(list)
        for i in range(len(parent)):
            if parent[i] != -1: graph[parent[i]].append(i)
        self.graph = graph

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] == -1:
            self.locks[num] = user
            return True
        else: return False
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] == user:
            self.locks[num] = -1
            return True
        return False
        return True
        

    def upgrade(self, num: int, user: int) -> bool:
        par = num
        while True:
            if par == -1: break
                
            if self.locks[par] != -1: return False
            par = self.paren[par]
            
        locked_des = False
        stack = [num]
        while stack:
            x = stack.pop()
            self.locks[x] = -1
            for i in self.graph[x]:
                stack.append(i)
                if self.locks[i] != -1: locked_des= True
        if locked_des: 
            self.locks[num] = user
            return True
        else: return False
        
        
# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)