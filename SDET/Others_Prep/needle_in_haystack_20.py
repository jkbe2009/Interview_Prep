
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Edge case
        if not needle or not haystack:
            return -1
        if len(needle) > len(haystack):
            return -1
        if len(needle) == 0:
            return 0
        
        for i in range(len(haystack)):
            ind = 0
            while (i+ind < len(haystack) and needle[ind] == haystack[i+ind]):
                ind += 1
                if ind == len(needle):
                    return i
        return -1

        