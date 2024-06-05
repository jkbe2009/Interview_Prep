
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum, msum = 0, float("-inf")

        for e in range(len(nums)):
            sum += nums[e]
            msum = max(sum, msum)
            if sum < 0:
                sum = 0
            
        return msum