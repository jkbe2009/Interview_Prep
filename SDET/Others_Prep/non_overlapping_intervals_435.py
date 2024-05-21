
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        inters = sorted(intervals, key = lambda item: item[1])
        last_end = float("-inf")
        remove = 0

        for val in inter:
            if val[0] < last_end:
                remove += 1
            else:
                last_end = val[1]
        return remove
        