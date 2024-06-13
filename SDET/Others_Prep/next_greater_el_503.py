
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st = []

        for i in range(len(nums)-1, -1, -1):
            st.append(nums[i])
        
        res = [-1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            while st and st[-1] <= nums[i]:
                st.pop()
            res[i] = st[-1] if st else -1
            st.append(nums[i])
        
        return res