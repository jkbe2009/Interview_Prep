
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        sum = 0

        for i in range(1, len(nums)+1):
            res = res ^ i
            sum += i
    
        for num in nums:
            res = res ^ num
            sum -= num 

        return sum
        return res

        