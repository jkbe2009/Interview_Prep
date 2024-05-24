
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # edge case:
        if len(strs) == 0:
            return ""

        prefix = strs[0]

        for i, char in enumerate(prefix):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or char != strs[j][i]:
                    return prefix[:i]
                    
        return prefix