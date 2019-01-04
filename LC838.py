class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        
        n = len(dominoes)
        score = [0] *n
        
        
        f = 0
        for i in range(len(dominoes)-1, -1, -1):
            if dominoes[i] == '.':
                f = max(f-1, 0)
            elif dominoes[i] == 'L':
                f = n
            elif dominoes[i] == 'R':
                f = 0
            
            score[i] -= f
            
        f = 0
        res = ['.']*n
        for i in range(len(dominoes)):
            if dominoes[i] == '.':
                f = max(f-1, 0)
            elif dominoes[i] == 'R':
                f = n    
            elif dominoes[i] == 'L':
                f = 0
            
            score[i] += f
            
            if score[i] > 0:
                res[i] = 'R'
            elif score[i] == 0:
                res[i] = '.'
            else:
                res[i] = 'L'
                
        return "".join(res)
                
        
