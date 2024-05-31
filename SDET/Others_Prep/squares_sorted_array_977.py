
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n

        l, r = 0, n-1
        ind = n-1

        while l<=r:
            ls = nums[l]**2
            rs = nums[r]**2

            if ls > rs:
                res[ind] = ls
                l += 1
            else:
                res[ind] = rs
                r -= 1
            ind -= 1
        return res

        