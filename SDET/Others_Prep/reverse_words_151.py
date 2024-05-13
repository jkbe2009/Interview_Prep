"""

Reverse words in a string with one space in between each words

"""

class Solution(object):

    def reverse(self, portion):
       return portion[::-1]

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ""
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
            reversed_word = self.reverse(s[start:end])

            # Append the reversed word with a space before except for the first word
            res = res + reversed_word
            res = res + " "

        return strip(self.reverse(res))
