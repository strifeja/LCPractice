class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j, carry = len(a)-1, len(b)-1, 0
        result = []

        while i >= 0 or j >= 0 or carry > 0:
            sumval = carry
            if (i >= 0):
                sumval += int(a[i])
                i -= 1
            if (j >= 0):
                sumval += int(b[j])
                j -= 1
            result.append(str(sumval % 2))
            carry = sumval // 2
        
        return ''.join(reversed(result))

        