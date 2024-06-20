
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        res = 0
        for i in range(len(strs[0])):
            flag = False
            for j in range(1, len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    flag = True
                    break
            if flag:
                res += 1

        return res
