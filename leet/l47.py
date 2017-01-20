class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def fullpermute(l, r):
            if r == []:
                res.append(l)
            else:
                for i in range(len(r)):
                    if i > 0 and r[i] == r[i-1]:
                        continue
                    fullpermute(l+[r[i]], r[:i] + r[i+1:])
        res = []
        n = len(nums)
        if n <= 1:
            res.append(nums)
            return res
        fullpermute([], nums)
        return res
