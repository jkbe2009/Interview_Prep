
"""

Reverse only the first k characters in string for every 2k characters in place

"""

class Solution(object):

    def my_reverse(self, res, l, r):
        if r > len(res)-1:
            r = len(res)-1

        while l < r:
            res[l], res[r] = res[r], res[l]
            l = l+1
            r = r-1
        return

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        if  s == None:
            raise ValueError("invalid Input!!!")

        if s == "" or len(s) == 0:
            return ""

        res = list(s)

        st = 0
        end = st+k-1

        if end >= len(s):
            self.my_reverse(res, 0, len(s)-1)
            return "".join(res)

        while st < len(s):
            self.my_reverse(res, st, end)
            st = st+(2*k)
            end = st+k-1

        return "".join(res)


