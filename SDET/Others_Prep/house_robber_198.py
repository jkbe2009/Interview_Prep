
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        dp = [-1] * len(nums)
        
        def recursive_soln(house, total):
            # Base case:
            if house >= len(nums):
                return total

            return max(recursive_soln(house+2, total+nums[house]), recursive_soln(house+1, total))
          

        def iterative_soln():

            """
            Using a dp array
            if len(nums) == 1:
                return nums[0]

            dp = [0] * len(nums)
            dp[-1] = nums[-1]
            dp[-2] = max(nums[-2], nums[-1])
            for i in range(len(nums)-3, -1, -1):
                dp[i] = max((nums[i]+dp[i+2]), dp[i+1])

            return dp[0]
            
            """
            a = 0
            b = 0

            for i in range(len(nums)-1, -1, -1):
                c = max((nums[i]+ a), b)
                a = b
                b = c

            return c

        # return recursive_soln(0, 0)
        return iterative_soln()