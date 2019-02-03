# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.parent = {}
        self.dfs(None, root)
        
        dist = 0
        queue = [target]
        visited = {target}
        while queue:
            if dist == K:
                break
            tmp = []
            for node in queue:
                for n in [node.left, node.right, self.parent[node]]:
                    if n != None and n not in visited:
                        visited.add(n)
                        tmp.append(n)
            queue = tmp
            dist += 1
        
        res = [node.val for node in queue]
        return res
        
        
    def dfs(self, prev_node, cur_node):
        if cur_node != None:
            self.parent[cur_node] = prev_node
            self.dfs(cur_node, cur_node.left)
            self.dfs(cur_node, cur_node.right)
    
            
        
