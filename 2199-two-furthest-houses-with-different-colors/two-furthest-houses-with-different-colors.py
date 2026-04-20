class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        max_d = 0
        i, j = 0, len(colors)-1

        while i < j:
            if colors[i] != colors[j]:
                max_d = abs(i-j)
                break
            i += 1

        i, j = 0, len(colors)-1
        while i < j:
            if colors[i] != colors[j]:
                return max(max_d,abs(i-j))
            j -= 1
        

        