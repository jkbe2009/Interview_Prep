
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def two_pointer():
            # Will not work for negative numbers:
            lsum, rsum = 0, 0
            l, r = -1, len(nums)

            while l < r:
                if lsum == rsum:
                    l += 1
                    r -= 1
                    lsum += nums[l]
                    rsum += nums[r]
                elif lsum < rsum:
                    l += 1
                    lsum += nums[l]
                else:
                    r -= 1
                    rsum += nums[r]
            
            return l if l == r and lsum == rsum else -1
        
        rsum = 0
        lsum = 0
        for num in nums:
            rsum += num
        
        for i, num in enumerate(nums):
            rsum -= num
            if lsum == rsum:
                return i
            lsum += num
            
        return -1
