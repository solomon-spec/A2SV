class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        for i in range(26):parent[chr(97+i)] = chr(97+i)
        def find(child):
            if child != parent[child]: 
                parent[child] = find(parent[child])
            return parent[child]
        def union(ver1,ver2):
            parent[find(ver1)] = find(ver2)
        for i in equations:
            if i[1] == "=":union(i[0],i[3])
        for i in equations:
            if i[1] == "!" and find(i[0]) == find(i[3]): return False
        return True
            