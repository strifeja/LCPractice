class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        i = x
        compar = 0
        while i > 0:
            curr = i % 10
            compar = (compar * 10) + curr
            i = i // 10

        return x == compar
        
