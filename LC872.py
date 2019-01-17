# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leafs1, leafs2 = [], []
        self.DFS(root1, leafs1)
        self.DFS(root2, leafs2)
        return leafs1 == leafs2
    
    def DFS(self, root, leafs):
        if root == None:
            return
        if root.left == None and root.right == None:
            leafs.append(root.val)
            return 
        else:
            self.DFS(root.left, leafs)
            self.DFS(root.right, leafs)
