
class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        res = []

        def helper(ind, curr):
            # Base case:
            if ind == len(s):
                res.append(curr)
                return
            
            # Recursive Case:
            c = s[ind]
            if c.isnumeric():
                helper(ind+1, curr+c)
            else:
                helper(ind+1, curr+c.lower())
                helper(ind+1, curr+c.upper())

            return
        
        helper(0, "")
        return res