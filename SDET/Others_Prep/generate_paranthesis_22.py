
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res, st = [], []

        def helper(open, closed):
            if open < n:
                st.append("(")
                helper(open+1, closed)
                st.pop()

            if closed < open:
                st.append(")")
                helper(open, closed+1)
                st.pop()

            if open == closed == n:
                comb = "".join(st)
                res.append(comb)

        helper(0,0)
        return res