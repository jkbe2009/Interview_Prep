
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 1 2 3 4 5
        # 4 5 1 2 3
        # 2 3 4 5 1
        # 3 4 5 1 2

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r)//2

            if nums[m] == target:
                return m
            else:
                # If left side is sorted
                if nums[l] <= nums[m]:
                    # If element present in this side
                    if target >= nums[l] and target <= nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
                    # Else move right
                else:
                # Else right side is sorted
                    # If element present in this side
                    if target >= nums[m] and target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                    # Else move left
        return -1