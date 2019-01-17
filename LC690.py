"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        self.emap = {e.id: e for e in employees}
        return self.DFS(id)
        
    def DFS(self, id):
        e = self.emap[id]
        return (e.importance + sum([self.DFS(i) for i in e.subordinates]))
