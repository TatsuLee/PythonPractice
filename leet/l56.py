# Definition for an interval.

# class Interval(object):

#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x.start)
        res = []
        for i in intervals:
            if len(res) == 0 or res[-1].end < i.start:
                res += [i]
            else:
                res[-1].end = max(res[-1].end, i.end)
        return res
