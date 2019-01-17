# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        sum -= root.val
        if root.left == None and root.right == None:
            return sum == 0
        return  self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
    def iterative(self, root, sum):
        if root == None:
            return False
        
        stack = [(root, sum-root.val)]
        while len(stack) != 0:
            node, cur_sum = stack.pop()
            if node.left == None and node.right == None:
                if cur_sum == 0:
                    return True
            
            if node.right != None:
                stack.append((node.right, cur_sum-node.right.val))
            
            if node.left != None:
                stack.append((node.left, cur_sum-node.left.val))
        
        return False
            
            
        
