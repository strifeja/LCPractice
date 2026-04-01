class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sum_squares(n)
        return n == 1
    
    def sum_squares(self, n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n/=10
        return total
        
        