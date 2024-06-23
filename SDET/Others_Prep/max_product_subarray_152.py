
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_prod = 1
        right_prod = 1
        max_prod = float("-inf")
        n = len(nums)

        """
        First attempt:
        for i in range(n):
            left_prod *= nums[i]
            max_prod = max(max_prod, left_prod)
            
            # Reset to beginning of the problem:
            if left_prod == 0:
                left_prod = 1
        
        for i in range(n-1, -1, -1):
            right_prod *= nums[i]
            max_prod = max(max_prod, right_prod)

            # Reset to beginning of the problem:
            if right_prod == 0:
                right_prod = 1
        """

        for i in range(n):
            left_prod *= nums[i]
            right_prod *= nums[n-1-i]
            max_prod = max(max_prod, left_prod, right_prod)

            # Reset to beginning of the problem if any prod is zero:
            if left_prod == 0: 
                left_prod = 1 
            if right_prod == 0:
                right_prod = 1 

        return max_prod