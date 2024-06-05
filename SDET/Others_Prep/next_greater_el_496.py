
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = {}
        st = []

        for i in range(len(nums2)-1, -1, -1):
            while(st and st[-1] <= nums2[i]):
                st.pop()
            map[nums2[i]] = -1 if not st else st[-1]
            st.append(nums2[i])
            
        return [map[i] for i in nums1]
