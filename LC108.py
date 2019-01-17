# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        return self.DFS(nums, 0, len(nums)-1)
    
    def DFS(self, nums, start, end):
        if start > end:
            return None
        
        mid = int((start + end) / 2)
        tmp = TreeNode(nums[mid])
        tmp.left = self.DFS(nums, start, mid-1)
        tmp.right = self.DFS(nums, mid+1, end)
        return tmp
    
        
    
        
