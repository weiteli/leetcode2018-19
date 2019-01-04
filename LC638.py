class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        
        result = 0
        n = len(needs)
        # if no discount
        for i in range(n):
            result += price[i]*needs[i]
        
        for offer in special:
            valid = True
          
            for i in range(n):
                if needs[i]-offer[i] < 0:
                    valid = False
                needs[i] -= offer[i]
                
            if valid:
                result = min(result, self.shoppingOffers(price, special, needs) + offer[-1])
            
            for i in range(n):
                needs[i] += offer[i]
               
        return result
        
            
        
        
