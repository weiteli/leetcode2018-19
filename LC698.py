class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def searchFunction(groups):
            if len(nums) == 0:
                return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if v + group <= target:
                    groups[i] += v
                    if searchFunction(groups):
                        return True
                    groups[i] -= v
                if group == 0: break
            nums.append(v)
            return False
        
        
        def search(groups, idx):
            if idx < 0:
                return True
            
            selected = nums[idx]
            for i, group in enumerate(groups):
                if group + selected <= target:
                    groups[i] += selected
                    if search(groups, idx-1):
                        return True
                    groups[i] -= selected
                if group == 0:
                    break
            return False
            
        
        s = sum(nums)
        if s%k != 0:
            return False
        
        target = s/k
        nums = sorted(nums)
        
        if nums[-1] > target:
            return False
        
        #return searchFunction([0]*k)    
        return search([0]*k, len(nums)-1)    
        
            
            
        
        
