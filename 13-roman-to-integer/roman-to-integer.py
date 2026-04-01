class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        prev = ''
        for i in range(len(s)):
            if s[i] == 'I':
                result += 1
            elif s[i] == 'V':
                result += 3 if prev == 'I' else 5   
            elif s[i] == 'X':
                result += 8 if prev == 'I' else 10
            elif s[i] == 'L':
                result += 30 if prev == 'X' else 50
            elif s[i] == 'C':
                 result += 80 if prev == 'X' else 100
            elif s[i] == 'D':
                result += 300 if prev == 'C' else 500
            elif s[i] == 'M':
                result += 800 if prev == 'C' else 1000
            
            prev = s[i]
        
        return result