
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        psum = 0
        d = {0:1}

        for val in nums:
            psum = psum + val
            rem = psum % k
        
            if rem in d:
                count += d[rem]
            
            d[rem] = d.get(rem, 0) + 1

        return count
        