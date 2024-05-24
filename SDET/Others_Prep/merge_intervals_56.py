
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_inp = sorted(intervals)
        res = []

        for inp in sorted_inp:
            if res == [] or inp[0] > res[-1][1]:
                res.append(inp)
            else:
                res[-1][1] = max(inp[1], res[-1][1])

        return res