
class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        max_l = 0
        freq = {}
        s = 0

        for e in range(len(nums)):
            k_e = nums[e]
            freq[k_e] = freq.get(k_e, 0) + 1

            while s <= e and freq[k_e] > k:
                k_s = nums[s]
                freq[k_s] = freq.get(k_s) - 1
                s += 1

            l = e-s+1
            max_l = max(l, max_l)

        return max_l
        