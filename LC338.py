class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        if num == 0:
            return [0]
        
        arr = [0] * (num + 1)
        arr[0] = 0
        for i in range(num+1):
            if i%2 == 0:
                #even number
                arr[i] = arr[i/2]
            else:
                arr[i] = arr[i-1] + 1
        return arr
