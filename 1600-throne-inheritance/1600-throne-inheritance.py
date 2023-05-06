class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dic = defaultdict(list)
        self.king = kingName
        self.dead = set()
    def birth(self, parentName: str, childName: str) -> None:
        self.dic[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans  = []
        stack = [self.king]
        while stack:
            x = stack.pop()
            if x not in self.dead: ans.append(x)
            for i in range(len(self.dic[x])-1,-1,-1):
                stack.append(self.dic[x][i])
        return ans


# Your ThroneInheritance object will ]be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()