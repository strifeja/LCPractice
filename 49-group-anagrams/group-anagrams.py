class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        n = len(strs)

        for i in range(n):
            s = strs[i]
            word = ''.join(sorted(s))

            if word in d:
                d[word].append(s)
            else:
                d[word] = [s]
        
        return d.values()

        