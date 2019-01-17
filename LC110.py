# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        return not self.DFS(root)==-1
        '''
        return abs(self.getTreeHeight(root.left) - self.getTreeHeight(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        '''
    def getTreeHeight(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.getTreeHeight(root.left), self.getTreeHeight(root.right))
        
    
    def DFS(self, root):
        if root == None:
            return 0
        
        h_left = self.DFS(root.left)
        h_right = self.DFS(root.right)
        
        if h_left == -1 or h_right == -1 or abs(h_left-h_right) > 1:
            return -1
        return 1 + max(h_left, h_right)
    
    
