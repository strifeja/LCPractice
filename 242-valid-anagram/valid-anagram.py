class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        smap = {}
        tmap = {}

        if len(s) != len(t): return False
        n = len(s)

        for i in range(n):
            c1, c2 = s[i], t[i]
            smap[c1] = smap.get(c1, 0) + 1
            tmap[c2] = tmap.get(c2, 0) + 1
        
        for key, value in smap.items():
            if key not in tmap or tmap[key] != value:
                return False
        
        return True
