"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ids = {}
        for i,j in enumerate(employees):
            ids[j.id] = i
        total = 0
        def add(id,visited):
            nonlocal total
            visited.add(id)
            for i in employees[ids[id]].subordinates:
                if i not in visited:add(i,visited)
            total += employees[ids[id]].importance
        add(id,set())
        return total