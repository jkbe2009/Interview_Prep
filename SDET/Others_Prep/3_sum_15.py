
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def using_HM():
            res = set()

            for i in range(len(nums)-2):
                target = 0 - nums[i]
                map = {}
                for j in range(i+1, len(nums)):
                    diff = target - nums[j]
                    if diff in map:
                        res.add(tuple(sorted([nums[i], diff, nums[j]])))
                    map[nums[j]] = j
            
            return [[a,b,c] for a,b,c in res]
        

        def using_2_pointers():
            if nums == None or len(nums) < 3:
                raise ValueError("Invalid Input!!")
            nums.sort()
            final_target = 0
            res = []
            
            for i in range(len(nums)-2):
                target =  final_target - nums[i]

                if i != 0 and nums[i] == nums[i-1]:
                    continue

                l, r = i+1, len(nums)-1

                while l < r:
                    if l != i+1 and nums[l] == nums[l-1]:
                        l += 1
                        continue
                    
                    sum = nums[l] + nums[r]

                    if sum == target:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif sum < target:
                        l += 1
                    else:
                        r -= 1
            
            return res

        # return using_HM()
        return using_2_pointers()