
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        visited = set()

        def helper(curr):
            # Base case:
            if len(nums) == len(curr):
                res.append(curr[:])
                return
            
            # Recursive case:
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                curr.append(nums[i])
                helper(curr)
                visited.remove(nums[i])
                curr.remove(nums[i])
                # curr.pop()
            
            return

        helper([])
        return res
