
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def hash_map():
            comp = {}
            for i, num in enumerate(nums):
                diff = target-num
                if diff in comp:
                    return [comp[diff], i]
                comp[num] = i
            return [-1, -1]

        def two_pointers():
            
            for i, num in enumerate(nums):
                nums[i] = (num, i)
            nums.sort()

            l, r = 0, len(nums)-1

            while l<r:
                sum = nums[l][0] + nums[r][0]

                if sum == target:
                    return nums[l][1], nums[r][1]
                elif sum < target:
                    l += 1
                else:
                    r -= 1
            
            return [-1, -1]

        # return hash_map()
        return two_pointers()