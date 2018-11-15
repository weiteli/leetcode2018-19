class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        
        #Sort pair
        pairs.sort()
        # dp[i]: max length of change at i location
        dp = [1] * len(pairs)
        
        for i in range(1, len(pairs)):
            for j in range(i):            
                if (pairs[j][1] < pairs[i][0]):
                    dp[i] = max(dp[i], dp[j]+1)
                    #dp[i] =  dp[j]+1
            
        return max(dp)
        
        '''
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key = operator.itemgetter(1)):
            if cur < x:
                cur = y
                ans += 1
        return ans
        '''
