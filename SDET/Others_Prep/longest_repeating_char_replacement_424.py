
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        st = 0
        count = {}
        max_l = 0

        for e in range(len(s)):
            count[s[e]] = count.get(s[e], 0) + 1
            while st < e and (e-st+1)-max(count.values()) > k:
                count[s[st]] = count.get(s[st]) - 1
                st += 1
            max_l = max(max_l, e-st+1)
        return max_l
