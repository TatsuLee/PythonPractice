class Solution(object):

    # method 1: kadane's algorithm O(n)
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumArray, maxArray = 0, -2**32
        for i in xrange(len(nums)):
            sumArray += nums[i]
            maxArray = max(maxArray, sumArray)
            sumArray = max(sumArray, 0)
        return maxArray

    """ can't figure out
    # method2: Prefix sum O(n)
    def maxSubArray2(self, nums):
        sumArray, minArray, maxArray = 0, 0, -2**32
        for i in xrange(len(nums)):
            sumArray += nums[i]
            maxArray = max(maxArray, sumArray-minArray)
            sumArray = max(minArray, sumArray)
        return maxArray
    """

    # method 2: divide and conquer O(nlogn)
    def maxSubArray2(self, nums):
        return nums
