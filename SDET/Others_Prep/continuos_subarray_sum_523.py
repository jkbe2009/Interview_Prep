
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        psum = 0
        dmap = {0 : -1}

        for i, num in enumerate(nums):
            psum += num
            rem = psum % k
            if rem in dmap and i - dmap[rem] > 1:
                return True
            
            if rem not in dmap:
                dmap[rem] = i

        return False

