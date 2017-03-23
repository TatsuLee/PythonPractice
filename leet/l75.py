class Solution(object):

    def partition(self, nums, l, r):
        mid, pivot = l-1, nums[r]  # start from origin, end as pivot
        for i in range(l, r):
            if nums[i] <= pivot:
                mid += 1
                nums[mid], nums[i] = nums[i], nums[mid]
        nums[mid+1], nums[r] = nums[r], nums[mid+1]
        return mid+1, mid+1

    def quicksort(self, nums, l, r):
        if l < r:
            pl, pr = self.partition(nums, l, r)
            self.quicksort(nums, l, pl-1)
            self.quicksort(nums, pr+1, r)

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums)-1) if nums else return
