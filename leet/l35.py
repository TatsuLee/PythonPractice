class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == [] or nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)
        l, r = 0, len(nums)-1
        while l < r-1:
            m = (l+r)/2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m
            else:
                r = m
        return r
