
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def using_HM():

            res = []
            s = set()

            for i in range(len(nums)-3):
                for j in range(i+1, len(nums)-2):
                    new_target = (target - nums[i]) - nums[j]
                    map = {}
                    for k in range(j+1, len(nums)):
                        diff = new_target-nums[k]
                        if diff in map:
                            s.add(tuple(sorted([nums[i], nums[j], diff, nums[k]])))
                        map[nums[k]] = k
            
            return [[a,b,c,d] for a,b,c,d in s]


        def using_two_pointers():
            nums.sort()
            res = []

            for i in range(len(nums)-3):
                if i != 0 and nums[i] == nums[i-1]:
                        continue
                for j in range(i+1, len(nums)-2):
                    if j != i+1 and nums[j] == nums[j-1]:
                        continue

                    new_target = (target - nums[i]) - nums[j]

                    l, r = j+1, len(nums)-1

                    while l <  r:
                        if l != j+1 and nums[l] == nums[l-1]:
                            l += 1
                            continue

                        sum = nums[l] + nums[r]
                        
                        if sum == new_target:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                            l += 1
                            r -= 1
                        elif sum < new_target:
                            l += 1
                        else:
                            r -= 1

            return res


        # return using_HM()
        return using_two_pointers()
            