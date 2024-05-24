
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals):
        # Write your code here
        intervals.sort(key = lambda val: val.end)

        last_end = -1
        for val in intervals:
            if val.start < last_end:
                return False
            last_end = val.end
        return True

