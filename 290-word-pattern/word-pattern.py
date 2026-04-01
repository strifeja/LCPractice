class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        n = len(pattern)

        if (len(words) != n):
            return False

        pmap = {}
        wmap = {}
        for i in range(n):
            c, w = pattern[i], words[i]

            if c in pmap:
                if pmap[c] != w:
                    return False

            if w in wmap:
                if wmap[w] != c:
                    return False
            
            pmap[c] = w
            wmap[w] = c
        
        return True
        