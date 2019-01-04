class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        """
        dp = [False]*len(s)
        
        for i in range(len(s)):
            for w in wordDict:
                if s[i-len(w)+1:i+1] == w and (dp[i-len(w)] or i-len(w) == -1):
                    dp[i] = True
                    break
        
        return dp[-1]
        
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(1,n+1):
            for w in wordDict:
                if dp[i-len(w)] and s[i-len(w):i]==w:
                    dp[i]=True
        return dp[-1]
        """
        
        set_ = set()
        for word in wordDict:
            set_.add(word)
        
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in set_:
                    dp[i] = True
                    
        return dp[-1]
        
        
        
        
