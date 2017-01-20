class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def fullpermute(a, l, r):
            if l == r:
                res.append(list(a))
                # have to use list to create another obj, ram trouble?
            else:
                for i in range(l, r+1):
                    a[l], a[i] = a[i], a[l]
                    fullpermute(a, l+1, r)
                    a[l], a[i] = a[i], a[l]  # backtrack
        res = []
        n = len(nums)
        if n <= 1:
            res.append(nums)
            return res
        fullpermute(nums, 0, n-1)
        return res
