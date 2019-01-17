"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return self.DFS(root)
        
    def DFS(self, root):
        if root is None:
            return 0
        elif len(root.children) == 0:
            return 1
        else:
            return max([self.DFS(node) for node in root.children]) + 1
    
    def BFS(self, root):
        stack = []
        if root is not None:
            stack.append((1, root))
        depth = 0
        
        while len(stack) != 0:
            cur_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, cur_depth)
                for child in root.children:
                    stack.append((cur_depth+1, child))
        
        return depth
    
            
            
            
            
        
