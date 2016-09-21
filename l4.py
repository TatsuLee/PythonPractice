class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import bisect
        for i in nums2:
            bisect.insort(nums1, i)
        mid = len(nums1)/2
        if nums1 is None:
            return 0
        if len(nums1)%2 == 0:
            return (nums1[mid-1]+nums1[mid])/2.0
        else:
            return nums1[mid]


