
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        st = 0

        for e in range(len(nums)):
            if nums[e] != 0:
                nums[st] = nums[e]
                st += 1
        
        for i in range(st, len(nums)):
            nums[i] = 0

        return