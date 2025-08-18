class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while i < j-i:
            s[i], s[j-i] = s[j-i], s[i]
            i += 1
        return s
        