class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        total = 0
        freq = {}
        for char in ransomNote:
            freq[char] = freq.get(char, 0) + 1
        
        for char in magazine:
            if char in freq and freq[char] != 0:
                freq[char] -= 1
                total += 1
        
        return total == len(ransomNote)