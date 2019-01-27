from itertools import product

class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        
        # Convert allow to better format for access
        self.allowed_dict = {}
        for s in allowed:
            if s[:2] not in self.allowed_dict:
                self.allowed_dict[s[:2]] = []
            self.allowed_dict[s[:2]].append(s[2])
            
        return self.DFS(bottom)
        
    def DFS(self, bottom):
        if len(bottom) == 2 and bottom in self.allowed_dict:
            return True
        
        btms = []
        for i in range(len(bottom)-1):
            pre_fix = bottom[i:i+2]
            if pre_fix in self.allowed_dict:
                btms.append(self.allowed_dict[pre_fix])
            else:
                return False
            
        # create new btm strings
        for btm in itertools.product(*btms):
            if self.DFS(''.join(btm)):
                return True
        
        return False
  
        
