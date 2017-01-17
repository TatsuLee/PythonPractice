class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m, n = 0, len(nums)
        if n <= 1:
            return n
        for i in range(n):
            if nums[i-1] == nums[i]:
                continue
            else:
                nums[m] = nums[i]
                m += 1
        return m
