class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        dp[A[i], A[j]] --> fib sequence start with A[i] and ends with A[j]
        initial state: 2
        transition: dp[A[i]-A[j], A[j]]+1
        """
        
        dp = collections.defaultdict(int)
        s = set(A)
        res = 0
        for i in range(2, len(A)):
            for j in range(i):
                if A[i]-A[j] < A[j] and A[i]-A[j] in s:
                    dp[A[j], A[i]] = dp.get((A[i]-A[j], A[j]), 2) + 1
                    res = max(dp[A[j], A[i]], res)
        return res
    
        
        
