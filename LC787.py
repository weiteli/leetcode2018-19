class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        tmpK = K+2
        dp = [[999999] * n for _ in range(tmpK)]
        dp[0][src] = 0
        
        for k in range(1, tmpK):
            for flight in flights:
                if dp[k-1][flight[0]] != 999999:
                    dp[k][flight[1]] = min(dp[k][flight[1]], dp[k-1][flight[0]]+flight[2])
        
        res=999999
        for i in range(1, K+2):
            if dp[i][dst] < res:
                res = dp[i][dst]
        if res ==999999:
            return -1
        return res
                
