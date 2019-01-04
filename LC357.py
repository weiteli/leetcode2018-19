class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        
        result = 0
        for i in range(1, n+1):
            result += self.calculateCount(i)
        return result
    
    def calculateCount(self, n):
        
        if n == 1:
            return 10

        count = 9
        for i in range(0, n-1):
            count *= (9-i)
        return count
