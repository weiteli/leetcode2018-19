# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        self.DFS(root, "")
        return self.res
    
    def DFS(self, root, s):
        if root == None:
            return
        s = s + str(root.val)
        if root.left == None and root.right == None:
            # it's a leaf node
            self.res.append(s)
        else:
            s = s + "->"
            self.DFS(root.left, s)
            self.DFS(root.right, s)
            
            
            
        
        
        
