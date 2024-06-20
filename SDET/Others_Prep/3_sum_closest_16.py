
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res_sum = float("-inf")

        for i in range(len(nums)-2):
            new_target = target-nums[i]
            l, r = i+1, len(nums)-1

            while l < r:
                total = nums[l]+ nums[r]

                if total == new_target:
                    return (nums[i] + nums[l] + nums[r])
                elif total < new_target:
                    curr_sum = nums[i] + nums[l] + nums[r]
                    if abs(target - res_sum) > abs(target- curr_sum):
                        res_sum = curr_sum
                    l += 1
                else:
                    curr_sum = nums[i] + nums[l] + nums[r]
                    if abs(target - res_sum) > abs(target- curr_sum):
                        res_sum = curr_sum
                    r -= 1
                     
        return  res_sum