
class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        st, max_l = 0, 0
        count = {}

        for e in range(n):
            count[s[e]] = count.get(s[e], 0) + 1

            while (st <= e and count[s[e]] > 2):
                count[s[st]] = count[s[st]] - 1
                st += 1

            max_l = max(max_l, e-st+1)
        
        return max_l
