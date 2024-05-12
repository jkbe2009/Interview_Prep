class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pivot = 1
        i = 0
        j = 0
        k = len(nums)-1

        while j <= k:
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i = i+1
                j = j+1
            elif nums[j] > pivot:
                nums[k], nums[j] = nums[j], nums[k]
                k = k-1
            else:
                j = j+1

        return
            
