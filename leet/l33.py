class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n, i = len(nums), 0
        if n == 0:
            return -1
        while i < n:
            if nums[i] == target:
                return i
            i += 1
        return -1
