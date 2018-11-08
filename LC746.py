class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 1 or len(cost)==0:
            return 0
        
        a = cost[0]
        b = cost[1]
        for i in range(2, len(cost)):
            total = min(a, b) + cost[i]
            a = b
            b=total
        return min(a,b)
