
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def iterative_soln(a):
            rob1, rob2 = 0, 0
            for i in range(len(a)-1, -1, -1):
                rob = max(a[i]+rob2, rob1)
                rob2 = rob1
                rob1 = rob
            return rob
                

        def recursive_soln(a, ind, sum):
            # Base case:
            if ind >= len(a):
                return sum
            
            # Recursive case:
            return max(
                recursive_soln(a, ind+2, sum+a[ind]), recursive_soln(a, ind+1, sum)
            )


        # Edge case:
        if len(nums) == 1:
            return nums[0]

        """
        # Recursive solution
        return max(
                recursive_soln(nums[1:], 0, 0),
                recursive_soln(nums[:-1], 0, 0)
        )
        """

        # Iterative solution
        return max(
            iterative_soln(nums[1:]),
            iterative_soln(nums[:-1])
        )
