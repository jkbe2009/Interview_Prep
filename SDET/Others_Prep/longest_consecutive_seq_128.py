
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0

        bag = set(nums)
        l_seq = 1
        
        for num in nums:
            # Performing the check only if its a beginning of a sequence
            if num-1 not in bag:
                seq = 1
                while num+seq in bag:
                    seq += 1
                l_seq = max(l_seq, seq)
        
        return l_seq
        