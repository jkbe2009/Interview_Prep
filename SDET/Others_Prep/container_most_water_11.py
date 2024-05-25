class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        max_area = 0

        while l < r:
            lh = height[l]
            rh = height[r]
            leng = min(lh, rh)
            brea = r - l
            area = leng * brea
            max_area = max(max_area, area)

            if lh < rh:
                l += 1
            else:
                r -= 1

        return max_area
