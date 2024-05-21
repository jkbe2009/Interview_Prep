
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(ind, curr, sum):
            if sum == target:
                res.append(curr[:])
                return
            
            if ind >= len(candidates) or sum > target:
                return
            
            curr.append(candidates[ind])
            helper(ind, curr, sum+candidates[ind])
            curr.pop()
            helper(ind+1, curr, sum)
            return

        helper(0, [], 0)

        return res