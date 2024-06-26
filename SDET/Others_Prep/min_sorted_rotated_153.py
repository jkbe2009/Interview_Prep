

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1 2 3 4 5
        # 4 5 1 2 3
        # 2 3 4 5 1
        # 3 4 5 1 2

        l, r = 0, len(nums)-1
        
        # Edge case:
        if nums[0] < nums[len(nums)-1]:
            return nums[0]

        while l <= r:
            mid = (l + r)//2

            if (mid == 0 or nums[mid] < nums[mid-1]) and\
              (mid == len(nums)-1 or nums[mid] <  nums[mid+1]):
              # Found the min ele     
              return nums[mid]
            else:
                # If both sides are sorted go left:
                if nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                    r = mid - 1
                
                # If left side is sorted go right
                elif nums[l] <= nums[mid]:
                    l = mid + 1

                # If right side is sorted go left
                else:
                    r = mid - 1
                    
        return nums[l]