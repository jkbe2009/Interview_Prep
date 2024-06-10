
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        max_ss = ""

        def expand(l, r):
            if l < 0 or r >= len(s):
                # The pointers are invalid:
                return -1, -1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return l, r


        for i in range(len(s)):
            l, r = expand(i, i)
            if r-l-1 > len(max_ss):
                max_ss = s[l+1:r]

            l, r = expand(i, i+1)
            if r-l-1 > len(max_ss):
                max_ss = s[l+1:r]
        
        return max_ss