class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        Time complexity O(n), n = length of prices array
        Space Complexity O(1)
        """
        
        rest, sold, hold = 0, 0, float('-inf')
        for p in prices:
            rest, sold, hold = max(rest, sold), hold+p, max(hold, rest-p)
        return max(rest, sold)
