# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None:
            return []
        
        res = []
        stack = []
        stack.append(root)
        
        while len(stack) != 0:
            res.append(stack[-1].val)
            tmp = []
            for node in stack:
                if node.left != None:
                    tmp.append(node.left)
                if node.right != None:
                    tmp.append(node.right)
            stack = tmp
        
        return res
            
                
            
            
            
            
    
    
