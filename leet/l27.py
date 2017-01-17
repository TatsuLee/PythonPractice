class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        m, n = 0, len(nums)
        if n == 0:
            return 0
        for i in range(n):
            if nums[i] == val:
                continue
            else:
                nums[m] = nums[i]
                m += 1
        return m
