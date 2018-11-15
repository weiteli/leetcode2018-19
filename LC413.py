class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a, total = 0, 0
        for i in range(2, len(A)):
            if (A[i]-A[i-1]) == (A[i-1]-A[i-2]):
                a += 1
                total += a
            else:
                a = 0
        return total
