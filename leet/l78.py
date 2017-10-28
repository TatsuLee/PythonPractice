import itertools


class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        if not nums:
            return res
        for i in xrange(1, len(nums)):
            for j in itertools.combinations(nums, i):
                res.append(list(j))
        res.append(nums)
        return res
