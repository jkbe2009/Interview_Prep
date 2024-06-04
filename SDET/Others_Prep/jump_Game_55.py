
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = [False] * len(nums)

        def helper_recursive(ind):
            # if ind == len(nums)-1:
            #     return True

            if ind == len(nums)-1 and nums[ind] == 0:
                return True

            if ind >= len(nums):
                return True
            
            if visited[ind]:
                return False

            visited[ind] = True

            for i in range(nums[ind], 0, -1): 
                if helper_recursive(ind+i):
                    return True

            return False
        

        can_jump = [False] * len(nums)

        def next_jump(i):
            for ind in range(nums[i], 0, -1):
                if can_jump[i+ind]:
                    return True
            return False

        def helper_dp():
            for i in range(len(nums)-1, -1, -1):
                if i+nums[i] >= len(nums)-1 or next_jump(i):
                    can_jump[i] = True
            return can_jump[0]

        def helper_dp_optimised():
            target = len(nums)-1
            for i in range(len(nums)-1, -1, -1):
                if i+nums[i] >= target:
                    target = i
            return True if target == 0 else False

        # return helper_recursive(0)
        # return helper_dp()
        return helper_dp_optimised()