class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        if n <= 1:
            nums.reverse()
            return None
        # find the nearest peak to right (leftPeak)
        for i in range(n-1, -1, -1):
            if nums[i] < nums[i+1]:
                break
        else:
            nums.reverse()
            return None
        # find the value next to (>) leftPeak, and swap
        for j in range(n, i, -1):
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                break
        # sort the subseq right to leftPeak
        for k in range((n-i)/2):
            nums[i+1+k], nums[n-k] = nums[n-k], nums[i+1+k]
