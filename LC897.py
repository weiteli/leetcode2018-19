# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        vals = []
        self.DFS(root, vals)
        head = TreeNode(vals[0])
        res = head
        for i in range(1, len(vals)):
            tmp = TreeNode(vals[i])
            head.right = tmp
            head = head.right
        return res
        
    def DFS(self, root, vals):
        if root == None:
            return
        else:
            self.DFS(root.left, vals)
            vals.append(root.val)
            self.DFS(root.right, vals)
            
        
