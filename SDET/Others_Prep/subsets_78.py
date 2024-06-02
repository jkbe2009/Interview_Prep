
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = [False] * len(nums)

        def helper(curr, ind):
            # Base case:
            if ind >= len(nums):
                res.append(curr[:])
                return

            # Recursive case:
            curr.append(nums[ind])
            helper(curr, ind+1)
            curr.pop()
            helper(curr, ind+1)
            return


        def helper1(curr, ind):
            res.append(curr[:])

            if ind == len(nums):
                return

            for i in range(ind, len(nums)):
                if not visited[i]:
                    visited[i] = True
                    curr.append(nums[i])
                    helper(curr, i+1)
                    curr.pop()
                    visited[i] = False
            return

        helper([], 0)
        #helper1([], 0)
        return  res
        