# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Find deepest then find leftest
        #return self.DFS_stack(root)
        #return self.BFS_queue(root)
        self.max_height = 0
        self.val = 0
        self.DFS(root, 1)
        return self.val
    
    def BFS_queue(self, root):
        if root == None:
            return 0
        queue = [(root, 1)]
        val, max_height = 0, 0
        
        while len(queue) != 0:
            node, height = queue.pop(0)
            if node != None:
                if height > max_height:
                    max_height = height
                    val = node.val
                queue.append((node.left, height+1))
                queue.append((node.right, height+1))
        return val
    
    def DFS_stack(self, root):
        if root == None:
            return 0
        
        stack = [(root, 1)]
        val, max_height = 0, 0
        
        while len(stack) != 0:
            node, height = stack.pop()
            
            if node != None:
                if height >= max_height:
                    max_height = height
                    val = node.val
                stack.append((node.left,height+1))
                stack.append((node.right,height+1))
        return val
        
        
    
    def DFS(self, root, height):
        # Need to use Pre-order Traversal for this problem
        # This method is the fastest
        if root == None:
            return
        if height > self.max_height:
            self.max_height = height
            self.val = root.val
        self.DFS(root.left, height+1)
        self.DFS(root.right, height+1)
        
            
        
