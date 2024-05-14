"""

First unique character in a string

"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        duplicates = set()

        for char in s:
            if char in seen:
                duplicates.add(char)
            seen.add(char)

        for i, char in enumerate(s):
            if char not in duplicates:
                return i
        
        return -1