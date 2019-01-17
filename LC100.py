# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        '''
        if pnode == None and qnode == None: return True
        if pnode == None or qnode == None: return False
        
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        return left and right
        '''
        return self.BFS(p, q)
    
    def BFS(self, p, q):
        stack = [(p, q)]
        
        while len(stack) != 0:
            pnode, qnode = stack.pop()
            if pnode == None and qnode == None:
                continue
            if pnode == None or qnode == None:
                return False
            
            if pnode.val != qnode.val:
                return False
            else:
                stack.append((pnode.right, qnode.right))
                stack.append((pnode.left, qnode.left))
        return True
        
    
