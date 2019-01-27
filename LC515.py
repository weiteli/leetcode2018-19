# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        queue = [(root, 1)]
        #BFS
        prev_height = 1
        tmp_max = float('-inf')
        while len(queue) != 0:
            q, cur_height = queue.pop(0)
            if q.left != None:
                queue.append((q.left, cur_height+1))
            if q.right != None:
                queue.append((q.right,cur_height+1))
            
            if cur_height > prev_height:
                # Change height
                res.append(tmp_max)
                tmp_max = q.val
                prev_height = cur_height
            else:
                if q.val > tmp_max:
                    tmp_max = q.val
        res.append(tmp_max)        
        return res
    
    
    def largestValues(self, root):
        self.ans = []
        self.DFS(root, 0)
        return self.ans
    
    def DFS(self, root, level):
        if root == None:
            return
        if len(self.ans) == level:
            # First time visit
            self.ans.append(root.val)
        else:
            self.ans[level] = max(self.ans[level], root.val)
        
        self.DFS(root.left, level+1)
        self.DFS(root.right, level+1)
        
        
        
        
        
