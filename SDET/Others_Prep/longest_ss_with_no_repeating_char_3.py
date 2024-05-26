
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        "abcabcbb"
        if s == None or s == "":
            return 0

        st = 0
        max_l = 1
        bag = set()

        for e in range(len(s)):
            
            while st < e and s[e] in bag:
                bag.remove(s[st])
                st += 1
            bag.add(s[e])
            max_l = max(max_l, e-st+1)

        return max_l