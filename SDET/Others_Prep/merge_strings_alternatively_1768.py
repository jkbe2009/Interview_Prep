
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j = 0, 0
        m, n = len(word1), len(word2)
        res  = ""

        while i < m and j < n:
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
        
        while i < m:
            res += word1[i]
            i += 1

        while j < n:
            res += word2[j]
            j += 1
        
        return res
        