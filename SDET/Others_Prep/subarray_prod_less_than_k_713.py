
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        st = 0
        res = 0
        prod = 1
        
        for e in range(len(nums)):
            prod *= nums[e]
            while st <= e and prod >= k:
                prod //= nums[st]
                st += 1 
            res += (e-st+1)
        
        return res

