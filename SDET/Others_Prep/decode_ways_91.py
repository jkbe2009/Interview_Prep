
"""
First Attempt:

class Solution(object):
    def numDecodings(self, s):
        :type s: str
        :rtype: int

        count = []
        if len(s) == 0:
            return count

        def dfs(ind):
            # Base case:
            if ind == len(s):
                count.append(True)
                return
            if ind > len(s) or int(s[ind]) == 0:
                return
            
            # Recursive case:
            if int(s[ind:ind+1]) >= 1:
                dfs(ind+1)
            if ind+2 <= len(s) and int(s[ind:ind+2]) <= 26:
                dfs(ind+2)
            return

        dfs(0)
        return len(count)
"""

# Using DP:

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [-1] * (len(s)+1)
        dp[len(s)] = 1

        if len(s) == 0:
            return 0

        def dfs(ind):
            # Base case:
            if ind == len(s):
                return 1
            if ind > len(s) or int(s[ind]) == 0:
                return 0
            
            # Recursive case:
            if dp[ind] != -1:
                return dp[ind]
            if int(s[ind]) >= 1:
                res = dfs(ind+1)
            if ind <= len(s)-2 and int(s[ind:ind+2]) <= 26:
                res += dfs(ind+2)
            dp[ind] = res
            return res
        
        return dfs(0)