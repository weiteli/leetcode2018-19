class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.special = special
        self.price = price
        
        return self.DFS(needs, 0)
    
    def DFS(self, needs, accumulate):
        if all(x == 0 for x in needs):
            return accumulate
            
        # no special offer price
        res = 0
        for i in range(len(needs)):
            res += needs[i]*self.price[i]
        
        # Check Special offer
        for s in self.special:
            updated_needs = []
            if s[-1] > res:
                continue
            for i in range(len(needs)):
                updated_needs.append(needs[i] - s[i])
            if min(updated_needs) >= 0:    
                res = min(res, self.DFS(updated_needs, s[-1]))
    
        return res + accumulate
    
            
        
