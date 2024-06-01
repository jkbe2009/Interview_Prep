
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, m_len = 0, float("inf")

        st = 0
        sum = 0

        for e in range(len(nums)):
            sum += nums[e]
            
            while st <= e and sum >= target:
                l = e-st+1
                m_len = min(m_len, l)
                sum -= nums[st]
                st += 1
        
        return 0 if m_len == float("inf") else m_len