"""

Reverse chars for each word in a string with one space in between each words, in-place

"""

class Solution(object):

    def reverse(self, li, l, r):
        while l < r:
            li[l], li[r] = li[r], li[l]
            l = l+1
            r = r-1
        return

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res = list(s)
        i, j  = 0, 0

        while i < len(s):
            # Find the starting index of the word starting from j
            i = j
            while (i < len(s) and s[i] == ' '):
                i = i+1

            # Find the end index of the word starting from i
            j = i
            while (j < len(s) and s[j] != ' '):
                j = j+1

            # Reverse the word    
            start = i
            end = j
            reversed_word = self.reverse(res, start, end-1)

        
        return "".join(res)