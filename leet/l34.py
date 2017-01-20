class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == [] or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        # first find the left bound
        l, r = 0, len(nums)-1
        while l < r-1:
            m = (l+r)/2
            if nums[m] < target:
                l = m
            else:
                r = m
        if nums[l] == target:
            lb = l
        elif nums[r] == target:
            lb = r
        else:
            return [-1, -1]
        # then find the right bound
        l, r = lb, len(nums)-1
        while l < r-1:
            m = (l+r)/2
            if nums[m] > target:
                r = m
            else:
                l = m
        if nums[r] == target:
            rb = r
        else:
            rb = l
        return [lb, rb]
