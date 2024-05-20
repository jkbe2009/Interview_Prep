class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        i = 0
        sum = 0

        # Sliding window technique works only for +ve values

        for j in range(0, len(nums)): 
            sum = sum + nums[j]

            while i <= j and (sum >= k or j == len(nums)-1):
                if sum == k:
                    count += 1
                sum -= nums[i]
                i += 1

        # return count

        # Prefix sum technique works for both +ve and -ve values

        psum = 0
        count = 0
        seen = {}
        seen[0] = 1

        for val in nums:
            psum = psum+val
            diff = psum-k
            if diff in seen:
                count = count+seen[diff]
            
            seen[psum] = seen.get(psum, 0) + 1
        
        return count